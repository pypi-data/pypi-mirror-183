from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SnapshotCopy(core.Schema):

    destination_region: Union[str, core.StringOut] = core.attr(str)

    grant_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        destination_region: Union[str, core.StringOut],
        grant_name: Optional[Union[str, core.StringOut]] = None,
        retention_period: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SnapshotCopy.Args(
                destination_region=destination_region,
                grant_name=grant_name,
                retention_period=retention_period,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_region: Union[str, core.StringOut] = core.arg()

        grant_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)


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


@core.schema
class Logging(core.Schema):

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enable: Union[bool, core.BoolOut] = core.attr(bool)

    log_destination_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        enable: Union[bool, core.BoolOut],
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        log_destination_type: Optional[Union[str, core.StringOut]] = None,
        log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Logging.Args(
                enable=enable,
                bucket_name=bucket_name,
                log_destination_type=log_destination_type,
                log_exports=log_exports,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable: Union[bool, core.BoolOut] = core.arg()

        log_destination_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_exports: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_redshift_cluster", namespace="aws_redshift")
class Cluster(core.Resource):

    allow_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    aqua_configuration_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automated_snapshot_retention_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    availability_zone_relocation_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    cluster_nodes: Union[List[ClusterNodes], core.ArrayOut[ClusterNodes]] = core.attr(
        ClusterNodes, computed=True, kind=core.Kind.array
    )

    cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_public_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_revision_number: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    cluster_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cluster_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    database_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    elastic_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    logging: Optional[Logging] = core.attr(Logging, default=None)

    maintenance_track_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    manual_snapshot_retention_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    master_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    node_type: Union[str, core.StringOut] = core.attr(str)

    number_of_nodes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    owner_account: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    snapshot_cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_copy: Optional[SnapshotCopy] = core.attr(SnapshotCopy, default=None)

    snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        cluster_identifier: Union[str, core.StringOut],
        node_type: Union[str, core.StringOut],
        allow_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        aqua_configuration_status: Optional[Union[str, core.StringOut]] = None,
        automated_snapshot_retention_period: Optional[Union[int, core.IntOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        availability_zone_relocation_enabled: Optional[Union[bool, core.BoolOut]] = None,
        cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        cluster_public_key: Optional[Union[str, core.StringOut]] = None,
        cluster_revision_number: Optional[Union[str, core.StringOut]] = None,
        cluster_security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        cluster_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        cluster_type: Optional[Union[str, core.StringOut]] = None,
        cluster_version: Optional[Union[str, core.StringOut]] = None,
        database_name: Optional[Union[str, core.StringOut]] = None,
        default_iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        elastic_ip: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        endpoint: Optional[Union[str, core.StringOut]] = None,
        enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        logging: Optional[Logging] = None,
        maintenance_track_name: Optional[Union[str, core.StringOut]] = None,
        manual_snapshot_retention_period: Optional[Union[int, core.IntOut]] = None,
        master_password: Optional[Union[str, core.StringOut]] = None,
        master_username: Optional[Union[str, core.StringOut]] = None,
        number_of_nodes: Optional[Union[int, core.IntOut]] = None,
        owner_account: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        snapshot_copy: Optional[SnapshotCopy] = None,
        snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
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
                cluster_identifier=cluster_identifier,
                node_type=node_type,
                allow_version_upgrade=allow_version_upgrade,
                apply_immediately=apply_immediately,
                aqua_configuration_status=aqua_configuration_status,
                automated_snapshot_retention_period=automated_snapshot_retention_period,
                availability_zone=availability_zone,
                availability_zone_relocation_enabled=availability_zone_relocation_enabled,
                cluster_parameter_group_name=cluster_parameter_group_name,
                cluster_public_key=cluster_public_key,
                cluster_revision_number=cluster_revision_number,
                cluster_security_groups=cluster_security_groups,
                cluster_subnet_group_name=cluster_subnet_group_name,
                cluster_type=cluster_type,
                cluster_version=cluster_version,
                database_name=database_name,
                default_iam_role_arn=default_iam_role_arn,
                elastic_ip=elastic_ip,
                encrypted=encrypted,
                endpoint=endpoint,
                enhanced_vpc_routing=enhanced_vpc_routing,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_roles=iam_roles,
                kms_key_id=kms_key_id,
                logging=logging,
                maintenance_track_name=maintenance_track_name,
                manual_snapshot_retention_period=manual_snapshot_retention_period,
                master_password=master_password,
                master_username=master_username,
                number_of_nodes=number_of_nodes,
                owner_account=owner_account,
                port=port,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_cluster_identifier=snapshot_cluster_identifier,
                snapshot_copy=snapshot_copy,
                snapshot_identifier=snapshot_identifier,
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
        allow_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        aqua_configuration_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        automated_snapshot_retention_period: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone_relocation_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_public_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_revision_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_security_groups: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        cluster_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elastic_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enhanced_vpc_routing: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logging: Optional[Logging] = core.arg(default=None)

        maintenance_track_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        manual_snapshot_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        master_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Union[str, core.StringOut] = core.arg()

        number_of_nodes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        owner_account: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_copy: Optional[SnapshotCopy] = core.arg(default=None)

        snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
