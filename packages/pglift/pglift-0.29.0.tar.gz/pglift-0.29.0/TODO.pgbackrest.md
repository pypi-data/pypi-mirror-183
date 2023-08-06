# pgbackrest dedicated repository

## Design

* This seems to be needed to implement the standby feature.

* We would need a way to initialize a repository, from the declarative API.

  In this step, we'll need to provide a list of stanza names with
  corresponding `pgN-*` configuration items.

  Some `pgN-*` can probably be inferred from site settings, assuming that
  these are consistent across hosts in the distributed setup. So maybe
  something like this would be enough:

  ```yaml
  - stanzas:
    - name: demo
      instances:
        - host: pg1.example.com
          name: 15/main
        - host: pg2.example.com
          name: 15/main
  ```

  where `instances` references database host names and instances qualified
  name from which we can infer `pg-host` and `pg-path` configuration items.

  In a distributed setup, this would be an extra step independent from
  instance creation. In Ansible, this could be a `pgbackrest_repository`
  module. In general, this would be a new interface model
  `PgBackRestRepository`.

  In Ansible, it might be possible to inject information about database
  hosts in repository configuration by using return values of
  `dalibo.pglift.instance` tasks or variables.

  For each listed stanza, we'll invoke `stanza-create --no-online` on the
  repository host, the `--no-online` is to to avoid deadlocking the setup as
  the instance and repository setups would need to happen simultaneously
  otherwise.

  The `check` step seems difficult to run in a distributed context because
  it would need both the repository and the instance to be configured and so
  cannot be run as part of one of these step.

* In `Instance` model, more precisely in `pgbackrest` field, we'll need
  a way to specify the repository host(s); probably through a `repo-hosts:
  list[str]` field.

  Or is this something we want to manage through site settings? Probably yes,
  at least unless there is a need to do otherwise or the approach proves to be
  limited.

* Backup operations (`pgbackrest backup` or the systemd timer/unit) will
  need to be run from the repository host.

  We can probably install systemd timer/unit on the repository host
  unconditionally and enable them for each managed stanza.

  On database hosts, we only need to install them if the repository is local
  (i.e. if no `repo-host` option got specified at instance creation).

  Otherwise, we'll also need to disable the `instance backup` command.

  Restore operations still happens on database hosts.

* We probably want to use TLS communication rather than SSH.

## Implementation

* Create the `PgBackRestRepository` interface model and handle its state
  (through an `apply()` function) as well as create/(update/)delete operations
  from the CLI.

* Implement the Ansible module based on this.

* Define a `repository-hosts: list[str]` in site settings.

* If set, adjust pgbackrest setup for instances accordingly.

* Adjust operations as described above to support this mode (systemd
  unit/timers, CLI commands, etc.)

## Plain pgbackrest configuration and setup

On repository:

    [demo]
    pg1-host=pg-primary
    pg1-path=/var/lib/postgresql/12/demo

    [global]
    repo1-path=/var/lib/pgbackrest
    repo1-retention-full=2
    start-fast=y

On database host:

    [demo]
    pg1-path=/var/lib/postgresql/12/demo

    [global]
    log-level-file=detail
    repo1-host=repository

<!--
   vim: spelllang=en spell ft=markdown
   -->
