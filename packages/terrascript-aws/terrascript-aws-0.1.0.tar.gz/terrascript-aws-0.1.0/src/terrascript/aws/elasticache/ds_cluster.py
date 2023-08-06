from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LogDeliveryConfiguration(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_format: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_type: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_elasticache_cluster", namespace="aws_elasticache")
class DsCluster(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    cache_nodes: Union[List[CacheNodes], core.ArrayOut[CacheNodes]] = core.attr(
        CacheNodes, computed=True, kind=core.Kind.array
    )

    cluster_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    configuration_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_delivery_configuration: Union[
        List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]
    ] = core.attr(LogDeliveryConfiguration, computed=True, kind=core.Kind.array)

    maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    notification_topic_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    num_cache_nodes: Union[int, core.IntOut] = core.attr(int, computed=True)

    parameter_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    replication_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    snapshot_retention_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_id=cluster_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
