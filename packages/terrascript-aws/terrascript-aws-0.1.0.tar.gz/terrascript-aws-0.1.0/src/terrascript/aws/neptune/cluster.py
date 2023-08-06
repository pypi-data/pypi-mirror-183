from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_neptune_cluster", namespace="aws_neptune")
class Cluster(core.Resource):

    allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    backup_retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_members: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_cloudwatch_logs_exports: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    neptune_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    preferred_backup_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    reader_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_source_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        backup_retention_period: Optional[Union[int, core.IntOut]] = None,
        cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        enable_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = None,
        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        neptune_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preferred_backup_window: Optional[Union[str, core.StringOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        replication_source_identifier: Optional[Union[str, core.StringOut]] = None,
        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        storage_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                deletion_protection=deletion_protection,
                enable_cloudwatch_logs_exports=enable_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                iam_roles=iam_roles,
                kms_key_arn=kms_key_arn,
                neptune_cluster_parameter_group_name=neptune_cluster_parameter_group_name,
                neptune_subnet_group_name=neptune_subnet_group_name,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                replication_source_identifier=replication_source_identifier,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                storage_encrypted=storage_encrypted,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        backup_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        neptune_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_source_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
