from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_networkmanager_transit_gateway_peering", namespace="aws_networkmanager")
class TransitGatewayPeering(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_id: Union[str, core.StringOut] = core.attr(str)

    edge_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peering_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_arn: Union[str, core.StringOut] = core.attr(str)

    transit_gateway_peering_attachment_id: Union[str, core.StringOut] = core.attr(
        str, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        core_network_id: Union[str, core.StringOut],
        transit_gateway_arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayPeering.Args(
                core_network_id=core_network_id,
                transit_gateway_arn=transit_gateway_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        core_network_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_gateway_arn: Union[str, core.StringOut] = core.arg()
