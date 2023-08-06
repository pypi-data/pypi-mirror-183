import configparser
import logging
import shlex
import subprocess
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Tuple

from pglift.models.system import PostgreSQLInstance
from pglift.settings import PgBackRestSettings


@dataclass
class CA:
    name: str
    crt: Path
    key: Path

    @classmethod
    def make(cls, path: Path, name: str) -> "CA":
        crt = path / f"{name}.crt"
        key = path / f"{name}.key"
        key.touch(mode=0o600)
        subprocess.run(
            [
                "openssl",
                "req",
                "-new",
                "-x509",
                "-nodes",
                "-out",
                crt,
                "-keyout",
                key,
                "-subj",
                f"/CN={name}",
            ],
            capture_output=True,
            check=True,
        )
        return cls(name, crt, key)


@dataclass
class Certificate:
    name: str
    key: bytes
    crt: bytes

    @classmethod
    def make(cls, ca_cert: Path, ca_key: Path, cn: str) -> "Certificate":
        with tempfile.NamedTemporaryFile(
            suffix=".key"
        ) as key, tempfile.NamedTemporaryFile(suffix=".crt") as crt:
            with subprocess.Popen(
                [
                    "openssl",
                    "req",
                    "-new",
                    "-nodes",
                    "-keyout",
                    key.name,
                    "-subj",
                    f"/CN={cn}",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            ) as req:
                subprocess.run(
                    [
                        "openssl",
                        "x509",
                        "-req",
                        "-CA",
                        ca_cert,
                        "-CAkey",
                        ca_key,
                        "-CAcreateserial",
                        "-out",
                        crt.name,
                    ],
                    stdin=req.stdout,
                    check=True,
                    capture_output=True,
                )
            if req.returncode:
                raise subprocess.CalledProcessError(req.returncode, req.args)

            return cls(cn, key.read(), crt.read())

    def install(self, where: Path) -> Tuple[Path, Path]:
        keyfile = where / f"{self.name}.key"
        keyfile.touch(mode=0o600)
        keyfile.write_bytes(self.key)
        certfile = where / f"{self.name}.crt"
        certfile.write_bytes(self.crt)
        return keyfile, certfile


@dataclass
class PgbackrestRepoHost:
    configpath: Path
    logpath: Path
    port: int
    path: Path
    client_cn: str
    server_cn: str
    ca_file: Path
    server_certfile: Path
    server_keyfile: Path

    logger: logging.Logger

    # Use low timeout values to avoid getting stuck long.
    archive_timeout: int = 1
    io_timeout: int = 1
    db_timeout: int = 1

    proc: Optional[subprocess.Popen[str]] = field(default=None, init=False)

    def __post_init__(self) -> None:
        with self.edit_config() as cp:
            cp.add_section("global")
            cp["global"] = {
                "repo1-path": str(self.path),
                "repo1-retention-full": "2",
                "start-fast": "y",
                "tls-server-address": "*",
                "tls-server-ca-file": str(self.ca_file),
                "tls-server-cert-file": str(self.server_certfile),
                "tls-server-key-file": str(self.server_keyfile),
                "tls-server-auth": f"{self.client_cn}=*",
                "tls-server-port": str(self.port),
                "archive-timeout": str(self.archive_timeout),
                "log-level-console": "off",
                "log-level-file": "detail",
                "log-level-stderr": "detail",
                "log-path": str(self.logpath),
            }

    def cmd(self, *args: str) -> list[str]:
        return ["pgbackrest", "--config", str(self.configpath)] + list(args)

    def start(self) -> None:
        assert self.proc is None, "process already started"
        self.proc = subprocess.Popen(self.cmd("server"), text=True)

    def kill(self) -> None:
        assert self.proc is not None, "process not started"
        self.proc.kill()
        self.proc = None

    def __enter__(self) -> "PgbackrestRepoHost":
        self.start()
        return self

    def __exit__(self, *args: Any) -> None:
        self.kill()

    @contextmanager
    def edit_config(self) -> Iterator[configparser.ConfigParser]:
        cp = configparser.ConfigParser(strict=True)
        if self.configpath.exists():
            with self.configpath.open() as f:
                cp.read_file(f)
        yield cp
        with self.configpath.open("w") as f:
            cp.write(f)

    def add_stanza(self, name: str, instance: PostgreSQLInstance) -> None:
        settings = instance._settings
        pgbackrest_settings = settings.pgbackrest
        assert pgbackrest_settings is not None
        host_config_path = pgbackrest_settings.configpath
        assert isinstance(
            pgbackrest_settings.repository, PgBackRestSettings.HostRepository
        )
        host_port = pgbackrest_settings.repository.port
        user = settings.postgresql.backuprole.name
        socket_path = settings.postgresql.socket_directory
        with self.edit_config() as cp:
            if not cp.has_section(name):
                cp.add_section(name)
            cp[name].update(
                {
                    "pg1-host": self.client_cn,
                    "pg1-host-port": str(host_port),
                    "pg1-host-type": "tls",
                    "pg1-host-config-path": str(host_config_path),
                    "pg1-host-ca-file": str(self.ca_file),
                    "pg1-host-cert-file": str(self.server_certfile),
                    "pg1-host-key-file": str(self.server_keyfile),
                    "pg1-path": str(instance.datadir),
                    "pg1-port": str(instance.port),
                    "pg1-user": user,
                    "pg1-socket-path": str(socket_path),
                }
            )
        self.run(
            "server-ping",
            "--io-timeout",
            str(self.io_timeout),
            "--tls-server-address",
            self.client_cn,
            "--tls-server-port",
            str(host_port),
        )
        self.run("stanza-create", "--stanza", name, "--no-online")
        self.run("verify", "--stanza", name)
        self.run("repo-ls")
        self.check(name)

    def check(self, stanza: str) -> None:
        self.run(
            "check",
            "--stanza",
            stanza,
            "--no-archive-check",
            "--io-timeout",
            str(self.io_timeout),
            "--db-timeout",
            str(self.db_timeout),
        )

    def run(self, *args: str) -> None:
        """Run a pgbackrest command on the repository."""
        cmd = self.cmd(*args)
        self.logger.debug("running: %s", shlex.join(cmd))
        with subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        ) as p:
            assert p.stderr is not None
            for errline in p.stderr:
                self.logger.debug("%s: %s", args[0], errline.rstrip())
        if p.returncode != 0:
            raise subprocess.CalledProcessError(p.returncode, p.args)
