from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_peering_attachment_accepter", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayPeeringAttachmentAccepter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_transit_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_attachment_id: Union[str, core.StringOut] = core.attr(str)

    transit_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_attachment_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayPeeringAttachmentAccepter.Args(
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_gateway_attachment_id: Union[str, core.StringOut] = core.arg()
