from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AccessLogs(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    interval: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        bucket_prefix: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        interval: Union[int, core.IntOut],
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

        bucket_prefix: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()

        interval: Union[int, core.IntOut] = core.arg()


@core.schema
class Listener(core.Schema):

    instance_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    instance_protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    lb_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    lb_protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssl_certificate_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        instance_port: Union[int, core.IntOut],
        instance_protocol: Union[str, core.StringOut],
        lb_port: Union[int, core.IntOut],
        lb_protocol: Union[str, core.StringOut],
        ssl_certificate_id: Union[str, core.StringOut],
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

        ssl_certificate_id: Union[str, core.StringOut] = core.arg()


@core.schema
class HealthCheck(core.Schema):

    healthy_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

    interval: Union[int, core.IntOut] = core.attr(int, computed=True)

    target: Union[str, core.StringOut] = core.attr(str, computed=True)

    timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    unhealthy_threshold: Union[int, core.IntOut] = core.attr(int, computed=True)

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


@core.data(type="aws_elb", namespace="aws_elb")
class DsMain(core.Data):

    access_logs: Union[List[AccessLogs], core.ArrayOut[AccessLogs]] = core.attr(
        AccessLogs, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connection_draining: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    connection_draining_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    cross_zone_load_balancing: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    desync_mitigation_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    health_check: Union[List[HealthCheck], core.ArrayOut[HealthCheck]] = core.attr(
        HealthCheck, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    instances: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    internal: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    listener: Union[List[Listener], core.ArrayOut[Listener]] = core.attr(
        Listener, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_security_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMain.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
