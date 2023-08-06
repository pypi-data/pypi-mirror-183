from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Route(core.Schema):

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    core_network_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_prefix_list_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    egress_only_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    nat_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    network_interface_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transit_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_peering_connection_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        core_network_arn: Optional[Union[str, core.StringOut]] = None,
        destination_prefix_list_id: Optional[Union[str, core.StringOut]] = None,
        egress_only_gateway_id: Optional[Union[str, core.StringOut]] = None,
        gateway_id: Optional[Union[str, core.StringOut]] = None,
        instance_id: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        nat_gateway_id: Optional[Union[str, core.StringOut]] = None,
        network_interface_id: Optional[Union[str, core.StringOut]] = None,
        transit_gateway_id: Optional[Union[str, core.StringOut]] = None,
        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        vpc_peering_connection_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Route.Args(
                cidr_block=cidr_block,
                core_network_arn=core_network_arn,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                ipv6_cidr_block=ipv6_cidr_block,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        core_network_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_prefix_list_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        egress_only_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nat_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interface_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_peering_connection_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_default_route_table", namespace="aws_vpc")
class DefaultRouteTable(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_route_table_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    propagating_vgws: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    route: Optional[Union[List[Route], core.ArrayOut[Route]]] = core.attr(
        Route, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_route_table_id: Union[str, core.StringOut],
        propagating_vgws: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        route: Optional[Union[List[Route], core.ArrayOut[Route]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultRouteTable.Args(
                default_route_table_id=default_route_table_id,
                propagating_vgws=propagating_vgws,
                route=route,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_route_table_id: Union[str, core.StringOut] = core.arg()

        propagating_vgws: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        route: Optional[Union[List[Route], core.ArrayOut[Route]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
