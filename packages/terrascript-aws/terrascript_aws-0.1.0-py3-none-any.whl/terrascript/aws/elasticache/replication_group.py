from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClusterMode(core.Schema):

    num_node_groups: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    replicas_per_node_group: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        num_node_groups: Optional[Union[int, core.IntOut]] = None,
        replicas_per_node_group: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ClusterMode.Args(
                num_node_groups=num_node_groups,
                replicas_per_node_group=replicas_per_node_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        num_node_groups: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        replicas_per_node_group: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class LogDeliveryConfiguration(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str)

    destination_type: Union[str, core.StringOut] = core.attr(str)

    log_format: Union[str, core.StringOut] = core.attr(str)

    log_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination: Union[str, core.StringOut],
        destination_type: Union[str, core.StringOut],
        log_format: Union[str, core.StringOut],
        log_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LogDeliveryConfiguration.Args(
                destination=destination,
                destination_type=destination_type,
                log_format=log_format,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[str, core.StringOut] = core.arg()

        destination_type: Union[str, core.StringOut] = core.arg()

        log_format: Union[str, core.StringOut] = core.arg()

        log_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_elasticache_replication_group", namespace="aws_elasticache")
class ReplicationGroup(core.Resource):

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    auth_token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    automatic_failover_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cluster_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    cluster_mode: Optional[ClusterMode] = core.attr(ClusterMode, default=None, computed=True)

    configuration_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_tiering_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_replication_group_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_delivery_configuration: Optional[
        Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
    ] = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    member_clusters: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    multi_az_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    node_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    notification_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    num_cache_clusters: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    num_node_groups: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    number_cache_clusters: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    preferred_cache_cluster_azs: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    primary_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    reader_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    replicas_per_node_group: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    replication_group_description: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    replication_group_id: Union[str, core.StringOut] = core.attr(str)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    snapshot_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_retention_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    snapshot_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    user_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        replication_group_id: Union[str, core.StringOut],
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        auth_token: Optional[Union[str, core.StringOut]] = None,
        auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = None,
        automatic_failover_enabled: Optional[Union[bool, core.BoolOut]] = None,
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        cluster_mode: Optional[ClusterMode] = None,
        data_tiering_enabled: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        global_replication_group_id: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        log_delivery_configuration: Optional[
            Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
        ] = None,
        maintenance_window: Optional[Union[str, core.StringOut]] = None,
        multi_az_enabled: Optional[Union[bool, core.BoolOut]] = None,
        node_type: Optional[Union[str, core.StringOut]] = None,
        notification_topic_arn: Optional[Union[str, core.StringOut]] = None,
        num_cache_clusters: Optional[Union[int, core.IntOut]] = None,
        num_node_groups: Optional[Union[int, core.IntOut]] = None,
        number_cache_clusters: Optional[Union[int, core.IntOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preferred_cache_cluster_azs: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        replicas_per_node_group: Optional[Union[int, core.IntOut]] = None,
        replication_group_description: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_name: Optional[Union[str, core.StringOut]] = None,
        snapshot_retention_limit: Optional[Union[int, core.IntOut]] = None,
        snapshot_window: Optional[Union[str, core.StringOut]] = None,
        subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        user_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationGroup.Args(
                replication_group_id=replication_group_id,
                apply_immediately=apply_immediately,
                at_rest_encryption_enabled=at_rest_encryption_enabled,
                auth_token=auth_token,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                automatic_failover_enabled=automatic_failover_enabled,
                availability_zones=availability_zones,
                cluster_mode=cluster_mode,
                data_tiering_enabled=data_tiering_enabled,
                description=description,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                global_replication_group_id=global_replication_group_id,
                kms_key_id=kms_key_id,
                log_delivery_configuration=log_delivery_configuration,
                maintenance_window=maintenance_window,
                multi_az_enabled=multi_az_enabled,
                node_type=node_type,
                notification_topic_arn=notification_topic_arn,
                num_cache_clusters=num_cache_clusters,
                num_node_groups=num_node_groups,
                number_cache_clusters=number_cache_clusters,
                parameter_group_name=parameter_group_name,
                port=port,
                preferred_cache_cluster_azs=preferred_cache_cluster_azs,
                replicas_per_node_group=replicas_per_node_group,
                replication_group_description=replication_group_description,
                security_group_ids=security_group_ids,
                security_group_names=security_group_names,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
                tags=tags,
                tags_all=tags_all,
                transit_encryption_enabled=transit_encryption_enabled,
                user_group_ids=user_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        at_rest_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auth_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        automatic_failover_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        cluster_mode: Optional[ClusterMode] = core.arg(default=None)

        data_tiering_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_replication_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_delivery_configuration: Optional[
            Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
        ] = core.arg(default=None)

        maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_az_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        node_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        num_cache_clusters: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        num_node_groups: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        number_cache_clusters: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_cache_cluster_azs: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        replicas_per_node_group: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        replication_group_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_group_id: Union[str, core.StringOut] = core.arg()

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        snapshot_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_retention_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        snapshot_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        user_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
