from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_route_table_attachment", namespace="aws_networkmanager"
)
class TransitGatewayRouteTableAttachment(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    attachment_policy_rule_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    attachment_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    edge_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peering_id: Union[str, core.StringOut] = core.attr(str)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    segment_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_route_table_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        peering_id: Union[str, core.StringOut],
        transit_gateway_route_table_arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayRouteTableAttachment.Args(
                peering_id=peering_id,
                transit_gateway_route_table_arn=transit_gateway_route_table_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        peering_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_gateway_route_table_arn: Union[str, core.StringOut] = core.arg()
