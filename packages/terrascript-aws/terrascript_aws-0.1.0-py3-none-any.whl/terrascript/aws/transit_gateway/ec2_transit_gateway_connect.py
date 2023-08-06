from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_transit_gateway_connect", namespace="aws_transit_gateway")
class Ec2TransitGatewayConnect(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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

    transport_attachment_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        transit_gateway_id: Union[str, core.StringOut],
        transport_attachment_id: Union[str, core.StringOut],
        protocol: Optional[Union[str, core.StringOut]] = None,
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
            args=Ec2TransitGatewayConnect.Args(
                transit_gateway_id=transit_gateway_id,
                transport_attachment_id=transport_attachment_id,
                protocol=protocol,
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
        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

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

        transport_attachment_id: Union[str, core.StringOut] = core.arg()
