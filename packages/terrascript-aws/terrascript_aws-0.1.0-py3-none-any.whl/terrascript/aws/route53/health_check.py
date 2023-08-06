from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_health_check", namespace="aws_route53")
class HealthCheck(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    child_health_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    child_healthchecks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cloudwatch_alarm_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloudwatch_alarm_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_sni: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    failure_threshold: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    fqdn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    insufficient_data_health_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    invert_healthcheck: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ip_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    measure_latency: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    reference_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    request_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    resource_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    routing_control_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    search_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: Union[str, core.StringOut],
        child_health_threshold: Optional[Union[int, core.IntOut]] = None,
        child_healthchecks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        cloudwatch_alarm_name: Optional[Union[str, core.StringOut]] = None,
        cloudwatch_alarm_region: Optional[Union[str, core.StringOut]] = None,
        disabled: Optional[Union[bool, core.BoolOut]] = None,
        enable_sni: Optional[Union[bool, core.BoolOut]] = None,
        failure_threshold: Optional[Union[int, core.IntOut]] = None,
        fqdn: Optional[Union[str, core.StringOut]] = None,
        insufficient_data_health_status: Optional[Union[str, core.StringOut]] = None,
        invert_healthcheck: Optional[Union[bool, core.BoolOut]] = None,
        ip_address: Optional[Union[str, core.StringOut]] = None,
        measure_latency: Optional[Union[bool, core.BoolOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        reference_name: Optional[Union[str, core.StringOut]] = None,
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        request_interval: Optional[Union[int, core.IntOut]] = None,
        resource_path: Optional[Union[str, core.StringOut]] = None,
        routing_control_arn: Optional[Union[str, core.StringOut]] = None,
        search_string: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HealthCheck.Args(
                type=type,
                child_health_threshold=child_health_threshold,
                child_healthchecks=child_healthchecks,
                cloudwatch_alarm_name=cloudwatch_alarm_name,
                cloudwatch_alarm_region=cloudwatch_alarm_region,
                disabled=disabled,
                enable_sni=enable_sni,
                failure_threshold=failure_threshold,
                fqdn=fqdn,
                insufficient_data_health_status=insufficient_data_health_status,
                invert_healthcheck=invert_healthcheck,
                ip_address=ip_address,
                measure_latency=measure_latency,
                port=port,
                reference_name=reference_name,
                regions=regions,
                request_interval=request_interval,
                resource_path=resource_path,
                routing_control_arn=routing_control_arn,
                search_string=search_string,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        child_health_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        child_healthchecks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        cloudwatch_alarm_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatch_alarm_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_sni: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        failure_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        fqdn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        insufficient_data_health_status: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        invert_healthcheck: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        measure_latency: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        reference_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        request_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        resource_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        routing_control_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        search_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
