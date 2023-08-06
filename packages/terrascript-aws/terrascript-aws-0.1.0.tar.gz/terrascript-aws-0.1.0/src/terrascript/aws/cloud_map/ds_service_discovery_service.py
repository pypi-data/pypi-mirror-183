from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class HealthCheckConfig(core.Schema):

    failure_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

    resource_path: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        failure_threshold: Union[int, core.IntOut],
        resource_path: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=HealthCheckConfig.Args(
                failure_threshold=failure_threshold,
                resource_path=resource_path,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: Union[int, core.IntOut] = core.arg()

        resource_path: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class DnsRecords(core.Schema):

    ttl: Union[int, core.IntOut] = core.attr(int, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ttl: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DnsRecords.Args(
                ttl=ttl,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ttl: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class DnsConfig(core.Schema):

    dns_records: Union[List[DnsRecords], core.ArrayOut[DnsRecords]] = core.attr(
        DnsRecords, computed=True, kind=core.Kind.array
    )

    namespace_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    routing_policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_records: Union[List[DnsRecords], core.ArrayOut[DnsRecords]],
        namespace_id: Union[str, core.StringOut],
        routing_policy: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DnsConfig.Args(
                dns_records=dns_records,
                namespace_id=namespace_id,
                routing_policy=routing_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_records: Union[List[DnsRecords], core.ArrayOut[DnsRecords]] = core.arg()

        namespace_id: Union[str, core.StringOut] = core.arg()

        routing_policy: Union[str, core.StringOut] = core.arg()


@core.schema
class HealthCheckCustomConfig(core.Schema):

    failure_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        failure_threshold: Union[int, core.IntOut],
    ):
        super().__init__(
            args=HealthCheckCustomConfig.Args(
                failure_threshold=failure_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_service_discovery_service", namespace="aws_cloud_map")
class DsServiceDiscoveryService(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_config: Union[List[DnsConfig], core.ArrayOut[DnsConfig]] = core.attr(
        DnsConfig, computed=True, kind=core.Kind.array
    )

    health_check_config: Union[
        List[HealthCheckConfig], core.ArrayOut[HealthCheckConfig]
    ] = core.attr(HealthCheckConfig, computed=True, kind=core.Kind.array)

    health_check_custom_config: Union[
        List[HealthCheckCustomConfig], core.ArrayOut[HealthCheckCustomConfig]
    ] = core.attr(HealthCheckCustomConfig, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    namespace_id: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        namespace_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsServiceDiscoveryService.Args(
                name=name,
                namespace_id=namespace_id,
                tags=tags,
                tags_all=tags_all,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        namespace_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
