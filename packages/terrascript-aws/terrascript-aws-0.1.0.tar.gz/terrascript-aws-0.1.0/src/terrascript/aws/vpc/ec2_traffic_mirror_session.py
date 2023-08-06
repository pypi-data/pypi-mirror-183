from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_traffic_mirror_session", namespace="aws_vpc")
class Ec2TrafficMirrorSession(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    packet_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    session_number: Union[int, core.IntOut] = core.attr(int)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    traffic_mirror_filter_id: Union[str, core.StringOut] = core.attr(str)

    traffic_mirror_target_id: Union[str, core.StringOut] = core.attr(str)

    virtual_network_id: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        network_interface_id: Union[str, core.StringOut],
        session_number: Union[int, core.IntOut],
        traffic_mirror_filter_id: Union[str, core.StringOut],
        traffic_mirror_target_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        packet_length: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        virtual_network_id: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorSession.Args(
                network_interface_id=network_interface_id,
                session_number=session_number,
                traffic_mirror_filter_id=traffic_mirror_filter_id,
                traffic_mirror_target_id=traffic_mirror_target_id,
                description=description,
                packet_length=packet_length,
                tags=tags,
                tags_all=tags_all,
                virtual_network_id=virtual_network_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interface_id: Union[str, core.StringOut] = core.arg()

        packet_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        session_number: Union[int, core.IntOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        traffic_mirror_filter_id: Union[str, core.StringOut] = core.arg()

        traffic_mirror_target_id: Union[str, core.StringOut] = core.arg()

        virtual_network_id: Optional[Union[int, core.IntOut]] = core.arg(default=None)
