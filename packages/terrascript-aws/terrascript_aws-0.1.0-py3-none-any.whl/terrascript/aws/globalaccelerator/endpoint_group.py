from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PortOverride(core.Schema):

    endpoint_port: Union[int, core.IntOut] = core.attr(int)

    listener_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        endpoint_port: Union[int, core.IntOut],
        listener_port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PortOverride.Args(
                endpoint_port=endpoint_port,
                listener_port=listener_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_port: Union[int, core.IntOut] = core.arg()

        listener_port: Union[int, core.IntOut] = core.arg()


@core.schema
class EndpointConfiguration(core.Schema):

    client_ip_preservation_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    weight: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        client_ip_preservation_enabled: Optional[Union[bool, core.BoolOut]] = None,
        endpoint_id: Optional[Union[str, core.StringOut]] = None,
        weight: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                client_ip_preservation_enabled=client_ip_preservation_enabled,
                endpoint_id=endpoint_id,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_ip_preservation_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        weight: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_globalaccelerator_endpoint_group", namespace="aws_globalaccelerator")
class EndpointGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_configuration: Optional[
        Union[List[EndpointConfiguration], core.ArrayOut[EndpointConfiguration]]
    ] = core.attr(EndpointConfiguration, default=None, kind=core.Kind.array)

    endpoint_group_region: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    health_check_interval_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    health_check_path: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    health_check_port: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    health_check_protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    listener_arn: Union[str, core.StringOut] = core.attr(str)

    port_override: Optional[Union[List[PortOverride], core.ArrayOut[PortOverride]]] = core.attr(
        PortOverride, default=None, kind=core.Kind.array
    )

    threshold_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    traffic_dial_percentage: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        listener_arn: Union[str, core.StringOut],
        endpoint_configuration: Optional[
            Union[List[EndpointConfiguration], core.ArrayOut[EndpointConfiguration]]
        ] = None,
        endpoint_group_region: Optional[Union[str, core.StringOut]] = None,
        health_check_interval_seconds: Optional[Union[int, core.IntOut]] = None,
        health_check_path: Optional[Union[str, core.StringOut]] = None,
        health_check_port: Optional[Union[int, core.IntOut]] = None,
        health_check_protocol: Optional[Union[str, core.StringOut]] = None,
        port_override: Optional[Union[List[PortOverride], core.ArrayOut[PortOverride]]] = None,
        threshold_count: Optional[Union[int, core.IntOut]] = None,
        traffic_dial_percentage: Optional[Union[float, core.FloatOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointGroup.Args(
                listener_arn=listener_arn,
                endpoint_configuration=endpoint_configuration,
                endpoint_group_region=endpoint_group_region,
                health_check_interval_seconds=health_check_interval_seconds,
                health_check_path=health_check_path,
                health_check_port=health_check_port,
                health_check_protocol=health_check_protocol,
                port_override=port_override,
                threshold_count=threshold_count,
                traffic_dial_percentage=traffic_dial_percentage,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint_configuration: Optional[
            Union[List[EndpointConfiguration], core.ArrayOut[EndpointConfiguration]]
        ] = core.arg(default=None)

        endpoint_group_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health_check_interval_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        health_check_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health_check_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        health_check_protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        listener_arn: Union[str, core.StringOut] = core.arg()

        port_override: Optional[Union[List[PortOverride], core.ArrayOut[PortOverride]]] = core.arg(
            default=None
        )

        threshold_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        traffic_dial_percentage: Optional[Union[float, core.FloatOut]] = core.arg(default=None)
