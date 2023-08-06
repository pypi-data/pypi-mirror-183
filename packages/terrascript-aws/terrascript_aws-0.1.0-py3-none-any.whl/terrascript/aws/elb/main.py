from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AccessLogs.Args(
                bucket=bucket,
                bucket_prefix=bucket_prefix,
                enabled=enabled,
                interval=interval,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: Union[int, core.IntOut] = core.attr(int)

    interval: Union[int, core.IntOut] = core.attr(int)

    target: Union[str, core.StringOut] = core.attr(str)

    timeout: Union[int, core.IntOut] = core.attr(int)

    unhealthy_threshold: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        healthy_threshold: Union[int, core.IntOut],
        interval: Union[int, core.IntOut],
        target: Union[str, core.StringOut],
        timeout: Union[int, core.IntOut],
        unhealthy_threshold: Union[int, core.IntOut],
    ):
        super().__init__(
            args=HealthCheck.Args(
                healthy_threshold=healthy_threshold,
                interval=interval,
                target=target,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: Union[int, core.IntOut] = core.arg()

        interval: Union[int, core.IntOut] = core.arg()

        target: Union[str, core.StringOut] = core.arg()

        timeout: Union[int, core.IntOut] = core.arg()

        unhealthy_threshold: Union[int, core.IntOut] = core.arg()


@core.schema
class Listener(core.Schema):

    instance_port: Union[int, core.IntOut] = core.attr(int)

    instance_protocol: Union[str, core.StringOut] = core.attr(str)

    lb_port: Union[int, core.IntOut] = core.attr(int)

    lb_protocol: Union[str, core.StringOut] = core.attr(str)

    ssl_certificate_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_port: Union[int, core.IntOut],
        instance_protocol: Union[str, core.StringOut],
        lb_port: Union[int, core.IntOut],
        lb_protocol: Union[str, core.StringOut],
        ssl_certificate_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Listener.Args(
                instance_port=instance_port,
                instance_protocol=instance_protocol,
                lb_port=lb_port,
                lb_protocol=lb_protocol,
                ssl_certificate_id=ssl_certificate_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_port: Union[int, core.IntOut] = core.arg()

        instance_protocol: Union[str, core.StringOut] = core.arg()

        lb_port: Union[int, core.IntOut] = core.arg()

        lb_protocol: Union[str, core.StringOut] = core.arg()

        ssl_certificate_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_elb", namespace="aws_elb")
class Main(core.Resource):

    access_logs: Optional[AccessLogs] = core.attr(AccessLogs, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    connection_draining: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    connection_draining_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    desync_mitigation_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    health_check: Optional[HealthCheck] = core.attr(HealthCheck, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    instances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    internal: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    listener: Union[List[Listener], core.ArrayOut[Listener]] = core.attr(
        Listener, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    source_security_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        listener: Union[List[Listener], core.ArrayOut[Listener]],
        access_logs: Optional[AccessLogs] = None,
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        connection_draining: Optional[Union[bool, core.BoolOut]] = None,
        connection_draining_timeout: Optional[Union[int, core.IntOut]] = None,
        cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = None,
        desync_mitigation_mode: Optional[Union[str, core.StringOut]] = None,
        health_check: Optional[HealthCheck] = None,
        idle_timeout: Optional[Union[int, core.IntOut]] = None,
        instances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        internal: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        source_security_group: Optional[Union[str, core.StringOut]] = None,
        subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                listener=listener,
                access_logs=access_logs,
                availability_zones=availability_zones,
                connection_draining=connection_draining,
                connection_draining_timeout=connection_draining_timeout,
                cross_zone_load_balancing=cross_zone_load_balancing,
                desync_mitigation_mode=desync_mitigation_mode,
                health_check=health_check,
                idle_timeout=idle_timeout,
                instances=instances,
                internal=internal,
                name=name,
                name_prefix=name_prefix,
                security_groups=security_groups,
                source_security_group=source_security_group,
                subnets=subnets,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_logs: Optional[AccessLogs] = core.arg(default=None)

        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        connection_draining: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        connection_draining_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cross_zone_load_balancing: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        desync_mitigation_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health_check: Optional[HealthCheck] = core.arg(default=None)

        idle_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        internal: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        listener: Union[List[Listener], core.ArrayOut[Listener]] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        source_security_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
