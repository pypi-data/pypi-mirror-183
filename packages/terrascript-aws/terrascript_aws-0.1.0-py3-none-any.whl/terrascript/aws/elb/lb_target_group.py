from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Stickiness(core.Schema):

    cookie_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cookie_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        cookie_duration: Optional[Union[int, core.IntOut]] = None,
        cookie_name: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Stickiness.Args(
                type=type,
                cookie_duration=cookie_duration,
                cookie_name=cookie_name,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cookie_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class HealthCheck(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    healthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    matcher: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    port: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        healthy_threshold: Optional[Union[int, core.IntOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        matcher: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[str, core.StringOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
        unhealthy_threshold: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HealthCheck.Args(
                enabled=enabled,
                healthy_threshold=healthy_threshold,
                interval=interval,
                matcher=matcher,
                path=path,
                port=port,
                protocol=protocol,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        healthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        matcher: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_lb_target_group", namespace="aws_elb")
class LbTargetGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    deregistration_delay: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    health_check: Optional[HealthCheck] = core.attr(HealthCheck, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    lambda_multi_value_headers_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    load_balancing_algorithm_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    preserve_client_ip: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    proxy_protocol_v2: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    slow_start: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    stickiness: Optional[Stickiness] = core.attr(Stickiness, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_termination: Optional[Union[bool, core.BoolOut]] = None,
        deregistration_delay: Optional[Union[str, core.StringOut]] = None,
        health_check: Optional[HealthCheck] = None,
        ip_address_type: Optional[Union[str, core.StringOut]] = None,
        lambda_multi_value_headers_enabled: Optional[Union[bool, core.BoolOut]] = None,
        load_balancing_algorithm_type: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preserve_client_ip: Optional[Union[str, core.StringOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        protocol_version: Optional[Union[str, core.StringOut]] = None,
        proxy_protocol_v2: Optional[Union[bool, core.BoolOut]] = None,
        slow_start: Optional[Union[int, core.IntOut]] = None,
        stickiness: Optional[Stickiness] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_type: Optional[Union[str, core.StringOut]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbTargetGroup.Args(
                connection_termination=connection_termination,
                deregistration_delay=deregistration_delay,
                health_check=health_check,
                ip_address_type=ip_address_type,
                lambda_multi_value_headers_enabled=lambda_multi_value_headers_enabled,
                load_balancing_algorithm_type=load_balancing_algorithm_type,
                name=name,
                name_prefix=name_prefix,
                port=port,
                preserve_client_ip=preserve_client_ip,
                protocol=protocol,
                protocol_version=protocol_version,
                proxy_protocol_v2=proxy_protocol_v2,
                slow_start=slow_start,
                stickiness=stickiness,
                tags=tags,
                tags_all=tags_all,
                target_type=target_type,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        deregistration_delay: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health_check: Optional[HealthCheck] = core.arg(default=None)

        ip_address_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_multi_value_headers_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        load_balancing_algorithm_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preserve_client_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        proxy_protocol_v2: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        slow_start: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        stickiness: Optional[Stickiness] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
