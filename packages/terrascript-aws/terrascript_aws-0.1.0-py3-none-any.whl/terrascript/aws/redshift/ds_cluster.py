from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterNodes(core.Schema):

    node_role: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        node_role: Union[str, core.StringOut],
        private_ip_address: Union[str, core.StringOut],
        public_ip_address: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ClusterNodes.Args(
                node_role=node_role,
                private_ip_address=private_ip_address,
                public_ip_address=public_ip_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        node_role: Union[str, core.StringOut] = core.arg()

        private_ip_address: Union[str, core.StringOut] = core.arg()

        public_ip_address: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_redshift_cluster", namespace="aws_redshift")
class DsCluster(core.Data):

    allow_version_upgrade: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    aqua_configuration_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automated_snapshot_retention_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_relocation_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    bucket_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    cluster_nodes: Union[List[ClusterNodes], core.ArrayOut[ClusterNodes]] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    cluster_parameter_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_public_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_revision_number: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cluster_subnet_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_iam_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    elastic_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    enable_logging: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    enhanced_vpc_routing: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iam_roles: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_destination_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_exports: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    maintenance_track_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    manual_snapshot_retention_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    master_username: Union[str, core.StringOut] = core.attr(str, computed=True)

    node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    number_of_nodes: Union[int, core.IntOut] = core.attr(int, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    preferred_maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    publicly_accessible: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    s3_key_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
