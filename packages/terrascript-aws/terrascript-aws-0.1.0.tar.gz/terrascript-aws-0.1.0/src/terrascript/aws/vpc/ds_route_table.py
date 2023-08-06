from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Associations(core.Schema):

    gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    main: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    route_table_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        gateway_id: Union[str, core.StringOut],
        main: Union[bool, core.BoolOut],
        route_table_association_id: Union[str, core.StringOut],
        route_table_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Associations.Args(
                gateway_id=gateway_id,
                main=main,
                route_table_association_id=route_table_association_id,
                route_table_id=route_table_id,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gateway_id: Union[str, core.StringOut] = core.arg()

        main: Union[bool, core.BoolOut] = core.arg()

        route_table_association_id: Union[str, core.StringOut] = core.arg()

        route_table_id: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Routes(core.Schema):

    carrier_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    core_network_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    egress_only_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    nat_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_peering_connection_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        carrier_gateway_id: Union[str, core.StringOut],
        cidr_block: Union[str, core.StringOut],
        core_network_arn: Union[str, core.StringOut],
        destination_prefix_list_id: Union[str, core.StringOut],
        egress_only_gateway_id: Union[str, core.StringOut],
        gateway_id: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        ipv6_cidr_block: Union[str, core.StringOut],
        local_gateway_id: Union[str, core.StringOut],
        nat_gateway_id: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        transit_gateway_id: Union[str, core.StringOut],
        vpc_endpoint_id: Union[str, core.StringOut],
        vpc_peering_connection_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Routes.Args(
                carrier_gateway_id=carrier_gateway_id,
                cidr_block=cidr_block,
                core_network_arn=core_network_arn,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_gateway_id=egress_only_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                ipv6_cidr_block=ipv6_cidr_block,
                local_gateway_id=local_gateway_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                transit_gateway_id=transit_gateway_id,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        carrier_gateway_id: Union[str, core.StringOut] = core.arg()

        cidr_block: Union[str, core.StringOut] = core.arg()

        core_network_arn: Union[str, core.StringOut] = core.arg()

        destination_prefix_list_id: Union[str, core.StringOut] = core.arg()

        egress_only_gateway_id: Union[str, core.StringOut] = core.arg()

        gateway_id: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        ipv6_cidr_block: Union[str, core.StringOut] = core.arg()

        local_gateway_id: Union[str, core.StringOut] = core.arg()

        nat_gateway_id: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_id: Union[str, core.StringOut] = core.arg()

        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()

        vpc_peering_connection_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_route_table", namespace="aws_vpc")
class DsRouteTable(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associations: Union[List[Associations], core.ArrayOut[Associations]] = core.attr(
        Associations, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    routes: Union[List[Routes], core.ArrayOut[Routes]] = core.attr(
        Routes, computed=True, kind=core.Kind.array
    )

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        gateway_id: Optional[Union[str, core.StringOut]] = None,
        route_table_id: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRouteTable.Args(
                filter=filter,
                gateway_id=gateway_id,
                route_table_id=route_table_id,
                subnet_id=subnet_id,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route_table_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
