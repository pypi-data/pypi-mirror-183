from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_traffic_mirror_target", namespace="aws_vpc")
class Ec2TrafficMirrorTarget(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    network_load_balancer_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        description: Optional[Union[str, core.StringOut]] = None,
        network_interface_id: Optional[Union[str, core.StringOut]] = None,
        network_load_balancer_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorTarget.Args(
                description=description,
                network_interface_id=network_interface_id,
                network_load_balancer_arn=network_load_balancer_arn,
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

        network_interface_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_load_balancer_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
