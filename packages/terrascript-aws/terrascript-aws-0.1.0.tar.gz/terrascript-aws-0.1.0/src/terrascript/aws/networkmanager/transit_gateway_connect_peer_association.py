from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_connect_peer_association",
    namespace="aws_networkmanager",
)
class TransitGatewayConnectPeerAssociation(core.Resource):

    device_id: Union[str, core.StringOut] = core.attr(str)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    link_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transit_gateway_connect_peer_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        device_id: Union[str, core.StringOut],
        global_network_id: Union[str, core.StringOut],
        transit_gateway_connect_peer_arn: Union[str, core.StringOut],
        link_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayConnectPeerAssociation.Args(
                device_id=device_id,
                global_network_id=global_network_id,
                transit_gateway_connect_peer_arn=transit_gateway_connect_peer_arn,
                link_id=link_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_id: Union[str, core.StringOut] = core.arg()

        global_network_id: Union[str, core.StringOut] = core.arg()

        link_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_gateway_connect_peer_arn: Union[str, core.StringOut] = core.arg()
