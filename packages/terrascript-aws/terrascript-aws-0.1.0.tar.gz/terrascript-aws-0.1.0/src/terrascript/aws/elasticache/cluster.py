from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.schema
class CacheNodes(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        availability_zone: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=CacheNodes.Args(
                address=address,
                availability_zone=availability_zone,
                id=id,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        availability_zone: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_elasticache_cluster", namespace="aws_elasticache")
class Cluster(core.Resource):

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    az_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cache_nodes: Union[List[CacheNodes], core.ArrayOut[CacheNodes]] = core.attr(
        CacheNodes, computed=True, kind=core.Kind.array
    )

    cluster_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    configuration_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_delivery_configuration: Optional[
        Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
    ] = core.attr(LogDeliveryConfiguration, default=None, kind=core.Kind.array)

    maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    node_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    notification_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    num_cache_nodes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    preferred_availability_zones: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    replication_group_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

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

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        az_mode: Optional[Union[str, core.StringOut]] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        log_delivery_configuration: Optional[
            Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
        ] = None,
        maintenance_window: Optional[Union[str, core.StringOut]] = None,
        node_type: Optional[Union[str, core.StringOut]] = None,
        notification_topic_arn: Optional[Union[str, core.StringOut]] = None,
        num_cache_nodes: Optional[Union[int, core.IntOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preferred_availability_zones: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        replication_group_id: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        snapshot_name: Optional[Union[str, core.StringOut]] = None,
        snapshot_retention_limit: Optional[Union[int, core.IntOut]] = None,
        snapshot_window: Optional[Union[str, core.StringOut]] = None,
        subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                cluster_id=cluster_id,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                az_mode=az_mode,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                log_delivery_configuration=log_delivery_configuration,
                maintenance_window=maintenance_window,
                node_type=node_type,
                notification_topic_arn=notification_topic_arn,
                num_cache_nodes=num_cache_nodes,
                parameter_group_name=parameter_group_name,
                port=port,
                preferred_availability_zones=preferred_availability_zones,
                replication_group_id=replication_group_id,
                security_group_ids=security_group_ids,
                security_group_names=security_group_names,
                snapshot_arns=snapshot_arns,
                snapshot_name=snapshot_name,
                snapshot_retention_limit=snapshot_retention_limit,
                snapshot_window=snapshot_window,
                subnet_group_name=subnet_group_name,
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

        auto_minor_version_upgrade: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        az_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_id: Union[str, core.StringOut] = core.arg()

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_delivery_configuration: Optional[
            Union[List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]]
        ] = core.arg(default=None)

        maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        num_cache_nodes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_availability_zones: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        replication_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

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
