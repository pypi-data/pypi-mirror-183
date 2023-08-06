from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_prefix_list_reference", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayPrefixListReference(core.Resource):

    blackhole: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    prefix_list_id: Union[str, core.StringOut] = core.attr(str)

    prefix_list_owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    transit_gateway_route_table_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        prefix_list_id: Union[str, core.StringOut],
        transit_gateway_route_table_id: Union[str, core.StringOut],
        blackhole: Optional[Union[bool, core.BoolOut]] = None,
        transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayPrefixListReference.Args(
                prefix_list_id=prefix_list_id,
                transit_gateway_route_table_id=transit_gateway_route_table_id,
                blackhole=blackhole,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        blackhole: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        prefix_list_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_gateway_route_table_id: Union[str, core.StringOut] = core.arg()
