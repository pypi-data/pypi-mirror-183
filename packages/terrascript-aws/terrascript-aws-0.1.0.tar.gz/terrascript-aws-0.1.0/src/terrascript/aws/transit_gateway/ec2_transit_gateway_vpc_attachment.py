from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_vpc_attachment", namespace="aws_transit_gateway")
class Ec2TransitGatewayVpcAttachment(core.Resource):

    appliance_mode_support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_default_route_table_association: Optional[
        Union[bool, core.BoolOut]
    ] = core.attr(bool, default=None)

    transit_gateway_default_route_table_propagation: Optional[
        Union[bool, core.BoolOut]
    ] = core.attr(bool, default=None)

    transit_gateway_id: Union[str, core.StringOut] = core.attr(str)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    vpc_owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        transit_gateway_id: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
        appliance_mode_support: Optional[Union[str, core.StringOut]] = None,
        dns_support: Optional[Union[str, core.StringOut]] = None,
        ipv6_support: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transit_gateway_default_route_table_association: Optional[Union[bool, core.BoolOut]] = None,
        transit_gateway_default_route_table_propagation: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayVpcAttachment.Args(
                subnet_ids=subnet_ids,
                transit_gateway_id=transit_gateway_id,
                vpc_id=vpc_id,
                appliance_mode_support=appliance_mode_support,
                dns_support=dns_support,
                ipv6_support=ipv6_support,
                tags=tags,
                tags_all=tags_all,
                transit_gateway_default_route_table_association=transit_gateway_default_route_table_association,
                transit_gateway_default_route_table_propagation=transit_gateway_default_route_table_propagation,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        appliance_mode_support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dns_support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        transit_gateway_default_route_table_association: Optional[
            Union[bool, core.BoolOut]
        ] = core.arg(default=None)

        transit_gateway_default_route_table_propagation: Optional[
            Union[bool, core.BoolOut]
        ] = core.arg(default=None)

        transit_gateway_id: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()
