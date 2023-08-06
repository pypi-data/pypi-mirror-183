from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_devicefarm_network_profile", namespace="aws_devicefarm")
class NetworkProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    downlink_bandwidth_bits: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    downlink_delay_ms: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    downlink_jitter_ms: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    downlink_loss_percent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    project_arn: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    uplink_bandwidth_bits: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    uplink_delay_ms: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    uplink_jitter_ms: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    uplink_loss_percent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        project_arn: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        downlink_bandwidth_bits: Optional[Union[int, core.IntOut]] = None,
        downlink_delay_ms: Optional[Union[int, core.IntOut]] = None,
        downlink_jitter_ms: Optional[Union[int, core.IntOut]] = None,
        downlink_loss_percent: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        uplink_bandwidth_bits: Optional[Union[int, core.IntOut]] = None,
        uplink_delay_ms: Optional[Union[int, core.IntOut]] = None,
        uplink_jitter_ms: Optional[Union[int, core.IntOut]] = None,
        uplink_loss_percent: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkProfile.Args(
                name=name,
                project_arn=project_arn,
                description=description,
                downlink_bandwidth_bits=downlink_bandwidth_bits,
                downlink_delay_ms=downlink_delay_ms,
                downlink_jitter_ms=downlink_jitter_ms,
                downlink_loss_percent=downlink_loss_percent,
                tags=tags,
                tags_all=tags_all,
                type=type,
                uplink_bandwidth_bits=uplink_bandwidth_bits,
                uplink_delay_ms=uplink_delay_ms,
                uplink_jitter_ms=uplink_jitter_ms,
                uplink_loss_percent=uplink_loss_percent,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        downlink_bandwidth_bits: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        downlink_delay_ms: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        downlink_jitter_ms: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        downlink_loss_percent: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        project_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        uplink_bandwidth_bits: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        uplink_delay_ms: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        uplink_jitter_ms: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        uplink_loss_percent: Optional[Union[int, core.IntOut]] = core.arg(default=None)
