from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_rds_cluster", namespace="aws_rds")
class DsCluster(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    backtrack_window: Union[int, core.IntOut] = core.attr(int, computed=True)

    backup_retention_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    cluster_members: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_cluster_parameter_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_subnet_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled_cloudwatch_logs_exports: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_database_authentication_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iam_roles: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_username: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    preferred_backup_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    reader_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_source_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_identifier=cluster_identifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
