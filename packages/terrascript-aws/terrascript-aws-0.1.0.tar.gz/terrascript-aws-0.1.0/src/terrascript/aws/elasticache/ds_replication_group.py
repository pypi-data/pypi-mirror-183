from typing import List, Union

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


@core.data(type="aws_elasticache_replication_group", namespace="aws_elasticache")
class DsReplicationGroup(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auth_token_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    automatic_failover_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    configuration_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_delivery_configuration: Union[
        List[LogDeliveryConfiguration], core.ArrayOut[LogDeliveryConfiguration]
    ] = core.attr(LogDeliveryConfiguration, computed=True, kind=core.Kind.array)

    member_clusters: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    multi_az_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    num_cache_clusters: Union[int, core.IntOut] = core.attr(int, computed=True)

    num_node_groups: Union[int, core.IntOut] = core.attr(int, computed=True)

    number_cache_clusters: Union[int, core.IntOut] = core.attr(int, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    primary_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    reader_endpoint_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    replicas_per_node_group: Union[int, core.IntOut] = core.attr(int, computed=True)

    replication_group_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_group_id: Union[str, core.StringOut] = core.attr(str)

    snapshot_retention_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        replication_group_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsReplicationGroup.Args(
                replication_group_id=replication_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replication_group_id: Union[str, core.StringOut] = core.arg()
