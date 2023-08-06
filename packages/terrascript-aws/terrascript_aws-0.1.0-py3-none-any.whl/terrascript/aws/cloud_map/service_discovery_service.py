from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DnsRecords(core.Schema):

    ttl: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

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
        DnsRecords, kind=core.Kind.array
    )

    namespace_id: Union[str, core.StringOut] = core.attr(str)

    routing_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dns_records: Union[List[DnsRecords], core.ArrayOut[DnsRecords]],
        namespace_id: Union[str, core.StringOut],
        routing_policy: Optional[Union[str, core.StringOut]] = None,
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

        routing_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class HealthCheckConfig(core.Schema):

    failure_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    resource_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        failure_threshold: Optional[Union[int, core.IntOut]] = None,
        resource_path: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
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
        failure_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        resource_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class HealthCheckCustomConfig(core.Schema):

    failure_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        failure_threshold: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HealthCheckCustomConfig.Args(
                failure_threshold=failure_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_service_discovery_service", namespace="aws_cloud_map")
class ServiceDiscoveryService(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_config: Optional[DnsConfig] = core.attr(DnsConfig, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check_config: Optional[HealthCheckConfig] = core.attr(HealthCheckConfig, default=None)

    health_check_custom_config: Optional[HealthCheckCustomConfig] = core.attr(
        HealthCheckCustomConfig, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    namespace_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        dns_config: Optional[DnsConfig] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        health_check_config: Optional[HealthCheckConfig] = None,
        health_check_custom_config: Optional[HealthCheckCustomConfig] = None,
        namespace_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ServiceDiscoveryService.Args(
                name=name,
                description=description,
                dns_config=dns_config,
                force_destroy=force_destroy,
                health_check_config=health_check_config,
                health_check_custom_config=health_check_custom_config,
                namespace_id=namespace_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dns_config: Optional[DnsConfig] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check_config: Optional[HealthCheckConfig] = core.arg(default=None)

        health_check_custom_config: Optional[HealthCheckCustomConfig] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        namespace_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
