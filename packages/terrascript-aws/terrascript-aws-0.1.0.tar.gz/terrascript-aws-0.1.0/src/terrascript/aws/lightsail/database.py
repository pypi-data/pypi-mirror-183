from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lightsail_database", namespace="aws_lightsail")
class Database(core.Resource):

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    backup_retention_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    blueprint_id: Union[str, core.StringOut] = core.attr(str)

    bundle_id: Union[str, core.StringOut] = core.attr(str)

    ca_certificate_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    cpu_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    disk_size: Union[float, core.FloatOut] = core.attr(float, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_database_name: Union[str, core.StringOut] = core.attr(str)

    master_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_endpoint_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    master_password: Union[str, core.StringOut] = core.attr(str)

    master_username: Union[str, core.StringOut] = core.attr(str)

    preferred_backup_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ram_size: Union[float, core.FloatOut] = core.attr(float, computed=True)

    relational_database_name: Union[str, core.StringOut] = core.attr(str)

    secondary_availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    support_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: Union[str, core.StringOut],
        blueprint_id: Union[str, core.StringOut],
        bundle_id: Union[str, core.StringOut],
        master_database_name: Union[str, core.StringOut],
        master_password: Union[str, core.StringOut],
        master_username: Union[str, core.StringOut],
        relational_database_name: Union[str, core.StringOut],
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        backup_retention_enabled: Optional[Union[bool, core.BoolOut]] = None,
        final_snapshot_name: Optional[Union[str, core.StringOut]] = None,
        preferred_backup_window: Optional[Union[str, core.StringOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Database.Args(
                availability_zone=availability_zone,
                blueprint_id=blueprint_id,
                bundle_id=bundle_id,
                master_database_name=master_database_name,
                master_password=master_password,
                master_username=master_username,
                relational_database_name=relational_database_name,
                apply_immediately=apply_immediately,
                backup_retention_enabled=backup_retention_enabled,
                final_snapshot_name=final_snapshot_name,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                skip_final_snapshot=skip_final_snapshot,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Union[str, core.StringOut] = core.arg()

        backup_retention_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        blueprint_id: Union[str, core.StringOut] = core.arg()

        bundle_id: Union[str, core.StringOut] = core.arg()

        final_snapshot_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_database_name: Union[str, core.StringOut] = core.arg()

        master_password: Union[str, core.StringOut] = core.arg()

        master_username: Union[str, core.StringOut] = core.arg()

        preferred_backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        relational_database_name: Union[str, core.StringOut] = core.arg()

        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
