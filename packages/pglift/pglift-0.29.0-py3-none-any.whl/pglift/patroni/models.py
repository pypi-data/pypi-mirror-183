import functools
import json
import re
import socket
from datetime import timedelta
from typing import (
    TYPE_CHECKING,
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

import attr
import pgtoolkit.conf
import yaml
from pydantic import BaseModel, ConstrainedStr, Field, root_validator, validator
from pydantic.utils import lenient_issubclass

from .. import types

if TYPE_CHECKING:
    from ..models import interface, system
    from ..settings import Settings


class Address(ConstrainedStr):
    r"""Network address type <host or ip>:<port>.

    >>> class Cfg(BaseModel):
    ...     addr: Address
    >>> cfg = Cfg(addr="server:123")
    >>> cfg.addr
    'server:123'
    >>> cfg.addr.host, cfg.addr.port
    ('server', 123)

    >>> Cfg(addr="server")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    pydantic.error_wrappers.ValidationError: 1 validation error for Cfg
    addr
      string does not match regex "(?P<host>[^\s:?#]+):(?P<port>\d+)" (type=value_error.str.regex; pattern=...)
    >>> Cfg(addr="server:ab")  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    pydantic.error_wrappers.ValidationError: 1 validation error for Cfg
    addr
      string does not match regex "(?P<host>[^\s:?#]+):(?P<port>\d+)" (type=value_error.str.regex; pattern=...)
    """

    __slots__ = ("host", "port")

    regex = re.compile(r"(?P<host>[^\s:?#]+):(?P<port>\d+)")

    A = TypeVar("A", bound="Address")

    def __new__(cls: Type[A], value: str, *, host: str, port: int) -> A:
        return str.__new__(cls, value)

    def __init__(self, value: str, *, host: str, port: int) -> None:
        str.__init__(value)
        self.host = host
        self.port = port

    @classmethod
    def validate(cls: Type[A], value: str) -> A:
        value = super().validate(value)
        m = cls.regex.match(value)
        assert m  # True, per parent validation.
        host, port = m.group("host"), m.group("port")
        return cls(value, host=host, port=int(port))

    @classmethod
    def get(cls: Type[A], port: int) -> A:
        host = socket.gethostbyname(socket.gethostname())
        if host.startswith("127."):  # loopback addresses
            host = socket.getfqdn()
        return cls.validate(f"{host}:{port}")


class _BaseModel(BaseModel):
    class Config:
        allow_mutation = False
        extra = "allow"
        validate_always = True
        validate_assignment = True


def bootstrap(manifest: "interface.Instance", settings: "Settings") -> Dict[str, Any]:
    """Return values for the "bootstrap" section of Patroni configuration."""
    patroni_settings = settings.patroni
    assert patroni_settings
    initdb_options = manifest.initdb_options(settings.postgresql.initdb)
    initdb: List[Union[str, Dict[str, str]]] = [
        {key: value}
        for key, value in initdb_options.dict(exclude_none=True).items()
        if key != "data_checksums"
    ]
    if initdb_options.data_checksums:
        initdb.append("data-checksums")
    pg_hba = manifest.pg_hba(settings).splitlines()
    pg_ident = manifest.pg_ident(settings).splitlines()
    return dict(
        dcs={"loop_wait": patroni_settings.loop_wait},
        initdb=initdb,
        pg_hba=pg_hba,
        pg_ident=pg_ident,
    )


def postgresql(
    instance: "system.BaseInstance",
    manifest: "interface.Instance",
    configuration: pgtoolkit.conf.Configuration,
    postgresql_connect_host: Optional[str],
    **args: Any,
) -> Dict[str, Any]:
    """Return values for the "postgresql" section of Patroni configuration.

    Any values from `**args` are used over default values that would be
    inferred but values from `manifest` still take precedence.
    """
    if "authentication" not in args:
        settings = instance._settings

        def r(role: "interface.Role") -> Dict[str, str]:
            d = {"username": role.name}
            if role.password:
                d["password"] = role.password.get_secret_value()
            return d

        args["authentication"] = {
            "superuser": r(manifest.surole(settings)),
            "replication": r(manifest.replrole(settings)),
        }
        args["authentication"]["rewind"] = args["authentication"]["superuser"]

    if postgresql_connect_host is not None:
        args["connect_address"] = Address.validate(
            f"{postgresql_connect_host}:{manifest.port}"
        )
    else:
        args["connect_address"] = Address.get(manifest.port)

    def s(entry: pgtoolkit.conf.Entry) -> Union[str, bool, int, float]:
        # Serialize pgtoolkit entry without quoting; specially needed to
        # timedelta.
        if isinstance(entry.value, timedelta):
            return entry.serialize().strip("'")
        return entry.value

    parameters = args.setdefault("parameters", {})
    parameters.update({k: s(e) for k, e in sorted(configuration.entries.items())})

    listen_addresses = parameters.get("listen_addresses", "*")
    args["listen"] = Address.validate(f"{listen_addresses}:{manifest.port}")

    args.setdefault("use_unix_socket", True)
    args.setdefault("use_unix_socket_repl", True)
    args.setdefault("pgpass", None)
    args.setdefault("data_dir", instance.datadir)
    args.setdefault("bin_dir", instance.bindir)
    if "pg_hba" not in args:
        args["pg_hba"] = manifest.pg_hba(settings).splitlines()
    if "pg_ident" not in args:
        args["pg_ident"] = manifest.pg_ident(settings).splitlines()

    return args


class RESTAPI(_BaseModel):
    connect_address: Address = Field(
        default_factory=functools.partial(Address.get, port=8008),
        description="IP address (or hostname) and port, to access the Patroni's REST API.",
    )
    listen: Address = Field(
        default=None,
        description="IP address (or hostname) and port that Patroni will listen to for the REST API.",
    )

    @validator("listen", always=True, pre=True)
    def __validate_listen_(cls, value: Optional[str], values: Dict[str, Any]) -> str:
        """Set 'listen' from 'connect_address' if unspecified.

        >>> RESTAPI(connect_address="localhost:8008")
        RESTAPI(connect_address='localhost:8008', listen='localhost:8008')
        >>> RESTAPI(connect_address="localhost:8008", listen="server:123")
        RESTAPI(connect_address='localhost:8008', listen='server:123')
        """
        if not value:
            value = values["connect_address"]
            assert isinstance(value, str)
        return value


class DCS(_BaseModel):
    pass


class Etcd(DCS):
    host: Address = Field(
        default="127.0.0.1:2379",
        description="address of the etcd endpoint.",
    )


class Patroni(_BaseModel):
    """A Patroni instance."""

    class PostgreSQL(_BaseModel):
        connect_address: Address
        listen: Address
        parameters: Dict[str, Any]

    scope: str = Field(description="Cluster name.")
    name: str = Field(description="Host name.")
    restapi: RESTAPI = Field(default_factory=RESTAPI)
    etcd: Optional[Etcd]
    etcd3: Optional[Etcd]
    postgresql: PostgreSQL

    _P = TypeVar("_P", bound="Patroni")

    @classmethod
    def build(
        cls: Type[_P],
        postgresql_connect_host: Optional[str],
        instance: "system.BaseInstance",
        manifest: "interface.Instance",
        configuration: pgtoolkit.conf.Configuration,
        **args: Any,
    ) -> _P:
        if "bootstrap" not in args:
            args["bootstrap"] = bootstrap(manifest, instance._settings)
        args["postgresql"] = postgresql(
            instance,
            manifest,
            configuration,
            postgresql_connect_host,
            **args.pop("postgresql", {}),
        )
        return cls(**args)

    @root_validator
    def __validate_dcs_(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that exactly one DCS is defined.

        >>> Patroni(scope="foo", name="bar")
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 2 validation errors for Patroni
        postgresql
          field required (type=value_error.missing)
        __root__
          at least one of ['etcd', 'etcd3'] is required (type=type_error)

        >>> Patroni.parse_obj({"scope": "main", "name": "pg1", "etcd": {}, "etcd3": {"host": "server:123"}})
        Traceback (most recent call last):
            ...
        pydantic.error_wrappers.ValidationError: 2 validation errors for Patroni
        postgresql
          field required (type=value_error.missing)
        __root__
          at most one of ['etcd', 'etcd3'] is expected (type=type_error)

        """
        dcs_fields = {
            name
            for name, ftype in cls.__fields__.items()
            if lenient_issubclass(ftype.outer_type_, DCS)
        }
        dcss = {d for d in dcs_fields if values.get(d) is not None}
        if len(dcss) == 0:
            raise TypeError(f"at least one of {sorted(dcs_fields)} is required")
        elif len(dcss) > 1:
            raise TypeError(f"at most one of {sorted(dcs_fields)} is expected")
        return values

    def yaml(self) -> str:
        data = json.loads(self.json(exclude_none=True))
        return yaml.dump(data, sort_keys=True)  # type: ignore[no-any-return]


@attr.s(auto_attribs=True, frozen=True, slots=True)
class Service:
    """A Patroni service bound to a PostgreSQL instance."""

    cluster: str
    node: str


class ClusterMember(BaseModel):
    """An item of the list of members returned by Patroni API /cluster endpoint."""

    class Config:
        extra = "allow"
        frozen = True

    host: str
    name: str
    port: int
    role: str
    state: str


class ServiceManifest(types.ServiceManifest, service_name="patroni"):
    _cli_config: ClassVar[Dict[str, types.CLIConfig]] = {
        "cluster_members": {"hide": True},
    }
    _ansible_config: ClassVar[Dict[str, types.AnsibleConfig]] = {
        "cluster_members": {"hide": True},
    }

    # XXX Or simply use instance.qualname?
    cluster: str = Field(
        description="Name (scope) of the Patroni cluster.",
        readOnly=True,
    )
    node: str = Field(
        default_factory=socket.getfqdn,
        description="Name of the node (usually the host name).",
        readOnly=True,
    )
    etcd: Etcd = Field(default_factory=Etcd, description="etcd backend information")
    restapi: RESTAPI = Field(
        default_factory=RESTAPI, description="REST API configuration"
    )
    postgresql_connect_host: Optional[str] = Field(
        default=None,
        description="Host or IP address through which PostgreSQL is externally accessible.",
    )
    cluster_members: List[ClusterMember] = Field(
        default=[],
        description="Members of the Patroni this instance is member of.",
        readOnly=True,
    )
