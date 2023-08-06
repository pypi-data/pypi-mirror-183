from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class HealthCheck(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    healthy_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

    interval: Union[int, core.IntOut] = core.attr(int, computed=True)

    matcher: Union[str, core.StringOut] = core.attr(str, computed=True)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    unhealthy_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        healthy_threshold: Union[int, core.IntOut],
        interval: Union[int, core.IntOut],
        matcher: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        port: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        timeout: Union[int, core.IntOut],
        unhealthy_threshold: Union[int, core.IntOut],
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
        enabled: Union[bool, core.BoolOut] = core.arg()

        healthy_threshold: Union[int, core.IntOut] = core.arg()

        interval: Union[int, core.IntOut] = core.arg()

        matcher: Union[str, core.StringOut] = core.arg()

        path: Union[str, core.StringOut] = core.arg()

        port: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        timeout: Union[int, core.IntOut] = core.arg()

        unhealthy_threshold: Union[int, core.IntOut] = core.arg()


@core.schema
class Stickiness(core.Schema):

    cookie_duration: Union[int, core.IntOut] = core.attr(int, computed=True)

    cookie_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cookie_duration: Union[int, core.IntOut],
        cookie_name: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Stickiness.Args(
                cookie_duration=cookie_duration,
                cookie_name=cookie_name,
                enabled=enabled,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cookie_duration: Union[int, core.IntOut] = core.arg()

        cookie_name: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_lb_target_group", namespace="aws_elb")
class DsLbTargetGroup(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    deregistration_delay: Union[int, core.IntOut] = core.attr(int, computed=True)

    health_check: Union[List[HealthCheck], core.ArrayOut[HealthCheck]] = core.attr(
        HealthCheck, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lambda_multi_value_headers_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    load_balancing_algorithm_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    preserve_client_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    proxy_protocol_v2: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    slow_start: Union[int, core.IntOut] = core.attr(int, computed=True)

    stickiness: Union[List[Stickiness], core.ArrayOut[Stickiness]] = core.attr(
        Stickiness, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbTargetGroup.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
