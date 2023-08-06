from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AttachedTo(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AttachedTo.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Subnet(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Subnet.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceVpc(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceVpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class PortRange(core.Schema):

    from_: Union[int, core.IntOut] = core.attr(int, computed=True, alias="from")

    to: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: Union[int, core.IntOut],
        to: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PortRange.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: Union[int, core.IntOut] = core.arg()

        to: Union[int, core.IntOut] = core.arg()


@core.schema
class AclRule(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    egress: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.attr(
        PortRange, computed=True, kind=core.Kind.array
    )

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule_action: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
        egress: Union[bool, core.BoolOut],
        port_range: Union[List[PortRange], core.ArrayOut[PortRange]],
        protocol: Union[str, core.StringOut],
        rule_action: Union[str, core.StringOut],
        rule_number: Union[int, core.IntOut],
    ):
        super().__init__(
            args=AclRule.Args(
                cidr=cidr,
                egress=egress,
                port_range=port_range,
                protocol=protocol,
                rule_action=rule_action,
                rule_number=rule_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()

        egress: Union[bool, core.BoolOut] = core.arg()

        port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        rule_action: Union[str, core.StringOut] = core.arg()

        rule_number: Union[int, core.IntOut] = core.arg()


@core.schema
class TransitGatewayRouteTableRoute(core.Schema):

    attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_origin: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment_id: Union[str, core.StringOut],
        destination_cidr: Union[str, core.StringOut],
        prefix_list_id: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        resource_type: Union[str, core.StringOut],
        route_origin: Union[str, core.StringOut],
        state: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TransitGatewayRouteTableRoute.Args(
                attachment_id=attachment_id,
                destination_cidr=destination_cidr,
                prefix_list_id=prefix_list_id,
                resource_id=resource_id,
                resource_type=resource_type,
                route_origin=route_origin,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: Union[str, core.StringOut] = core.arg()

        destination_cidr: Union[str, core.StringOut] = core.arg()

        prefix_list_id: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()

        resource_type: Union[str, core.StringOut] = core.arg()

        route_origin: Union[str, core.StringOut] = core.arg()

        state: Union[str, core.StringOut] = core.arg()


@core.schema
class RouteTableRoute(core.Schema):

    destination_cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    egress_only_internet_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    nat_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    origin: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_peering_connection_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_cidr: Union[str, core.StringOut],
        destination_prefix_list_id: Union[str, core.StringOut],
        egress_only_internet_gateway_id: Union[str, core.StringOut],
        gateway_id: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        nat_gateway_id: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        origin: Union[str, core.StringOut],
        transit_gateway_id: Union[str, core.StringOut],
        vpc_peering_connection_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RouteTableRoute.Args(
                destination_cidr=destination_cidr,
                destination_prefix_list_id=destination_prefix_list_id,
                egress_only_internet_gateway_id=egress_only_internet_gateway_id,
                gateway_id=gateway_id,
                instance_id=instance_id,
                nat_gateway_id=nat_gateway_id,
                network_interface_id=network_interface_id,
                origin=origin,
                transit_gateway_id=transit_gateway_id,
                vpc_peering_connection_id=vpc_peering_connection_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_cidr: Union[str, core.StringOut] = core.arg()

        destination_prefix_list_id: Union[str, core.StringOut] = core.arg()

        egress_only_internet_gateway_id: Union[str, core.StringOut] = core.arg()

        gateway_id: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        nat_gateway_id: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()

        origin: Union[str, core.StringOut] = core.arg()

        transit_gateway_id: Union[str, core.StringOut] = core.arg()

        vpc_peering_connection_id: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationVpc(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DestinationVpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Vpc(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Vpc.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SourcePortRanges(core.Schema):

    from_: Union[int, core.IntOut] = core.attr(int, computed=True, alias="from")

    to: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: Union[int, core.IntOut],
        to: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SourcePortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: Union[int, core.IntOut] = core.arg()

        to: Union[int, core.IntOut] = core.arg()


@core.schema
class DestinationPortRanges(core.Schema):

    from_: Union[int, core.IntOut] = core.attr(int, computed=True, alias="from")

    to: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: Union[int, core.IntOut],
        to: Union[int, core.IntOut],
    ):
        super().__init__(
            args=DestinationPortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: Union[int, core.IntOut] = core.arg()

        to: Union[int, core.IntOut] = core.arg()


@core.schema
class OutboundHeader(core.Schema):

    destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    destination_port_ranges: Union[
        List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
    ] = core.attr(DestinationPortRanges, computed=True, kind=core.Kind.array)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_port_ranges: Union[List[SourcePortRanges], core.ArrayOut[SourcePortRanges]] = core.attr(
        SourcePortRanges, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        destination_port_ranges: Union[
            List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
        ],
        protocol: Union[str, core.StringOut],
        source_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        source_port_ranges: Union[List[SourcePortRanges], core.ArrayOut[SourcePortRanges]],
    ):
        super().__init__(
            args=OutboundHeader.Args(
                destination_addresses=destination_addresses,
                destination_port_ranges=destination_port_ranges,
                protocol=protocol,
                source_addresses=source_addresses,
                source_port_ranges=source_port_ranges,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        destination_port_ranges: Union[
            List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
        ] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        source_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        source_port_ranges: Union[
            List[SourcePortRanges], core.ArrayOut[SourcePortRanges]
        ] = core.arg()


@core.schema
class Component(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Component.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class AdditionalDetails(core.Schema):

    additional_detail_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        additional_detail_type: Union[str, core.StringOut],
        component: Union[List[Component], core.ArrayOut[Component]],
    ):
        super().__init__(
            args=AdditionalDetails.Args(
                additional_detail_type=additional_detail_type,
                component=component,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_detail_type: Union[str, core.StringOut] = core.arg()

        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()


@core.schema
class SecurityGroupRule(core.Schema):

    cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    direction: Union[str, core.StringOut] = core.attr(str, computed=True)

    port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.attr(
        PortRange, computed=True, kind=core.Kind.array
    )

    prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr: Union[str, core.StringOut],
        direction: Union[str, core.StringOut],
        port_range: Union[List[PortRange], core.ArrayOut[PortRange]],
        prefix_list_id: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        security_group_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SecurityGroupRule.Args(
                cidr=cidr,
                direction=direction,
                port_range=port_range,
                prefix_list_id=prefix_list_id,
                protocol=protocol,
                security_group_id=security_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr: Union[str, core.StringOut] = core.arg()

        direction: Union[str, core.StringOut] = core.arg()

        port_range: Union[List[PortRange], core.ArrayOut[PortRange]] = core.arg()

        prefix_list_id: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        security_group_id: Union[str, core.StringOut] = core.arg()


@core.schema
class TransitGateway(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TransitGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class InboundHeader(core.Schema):

    destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    destination_port_ranges: Union[
        List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
    ] = core.attr(DestinationPortRanges, computed=True, kind=core.Kind.array)

    protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_port_ranges: Union[List[SourcePortRanges], core.ArrayOut[SourcePortRanges]] = core.attr(
        SourcePortRanges, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        destination_port_ranges: Union[
            List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
        ],
        protocol: Union[str, core.StringOut],
        source_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        source_port_ranges: Union[List[SourcePortRanges], core.ArrayOut[SourcePortRanges]],
    ):
        super().__init__(
            args=InboundHeader.Args(
                destination_addresses=destination_addresses,
                destination_port_ranges=destination_port_ranges,
                protocol=protocol,
                source_addresses=source_addresses,
                source_port_ranges=source_port_ranges,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        destination_port_ranges: Union[
            List[DestinationPortRanges], core.ArrayOut[DestinationPortRanges]
        ] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        source_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        source_port_ranges: Union[
            List[SourcePortRanges], core.ArrayOut[SourcePortRanges]
        ] = core.arg()


@core.schema
class ReturnPathComponents(core.Schema):

    acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    additional_details: Union[
        List[AdditionalDetails], core.ArrayOut[AdditionalDetails]
    ] = core.attr(AdditionalDetails, computed=True, kind=core.Kind.array)

    attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]] = core.attr(
        InboundHeader, computed=True, kind=core.Kind.array
    )

    outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]] = core.attr(
        OutboundHeader, computed=True, kind=core.Kind.array
    )

    route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group_rule: Union[
        List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
    ] = core.attr(SecurityGroupRule, computed=True, kind=core.Kind.array)

    sequence_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_route_table_route: Union[
        List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]],
        additional_details: Union[List[AdditionalDetails], core.ArrayOut[AdditionalDetails]],
        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]],
        component: Union[List[Component], core.ArrayOut[Component]],
        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]],
        inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]],
        outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]],
        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]],
        security_group_rule: Union[List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]],
        sequence_number: Union[int, core.IntOut],
        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]],
        subnet: Union[List[Subnet], core.ArrayOut[Subnet]],
        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]],
        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ],
        vpc: Union[List[Vpc], core.ArrayOut[Vpc]],
    ):
        super().__init__(
            args=ReturnPathComponents.Args(
                acl_rule=acl_rule,
                additional_details=additional_details,
                attached_to=attached_to,
                component=component,
                destination_vpc=destination_vpc,
                inbound_header=inbound_header,
                outbound_header=outbound_header,
                route_table_route=route_table_route,
                security_group_rule=security_group_rule,
                sequence_number=sequence_number,
                source_vpc=source_vpc,
                subnet=subnet,
                transit_gateway=transit_gateway,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.arg()

        additional_details: Union[
            List[AdditionalDetails], core.ArrayOut[AdditionalDetails]
        ] = core.arg()

        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.arg()

        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()

        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.arg()

        inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]] = core.arg()

        outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]] = core.arg()

        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.arg()

        security_group_rule: Union[
            List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
        ] = core.arg()

        sequence_number: Union[int, core.IntOut] = core.arg()

        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.arg()

        subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.arg()

        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.arg()

        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ] = core.arg()

        vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.arg()


@core.schema
class ForwardPathComponents(core.Schema):

    acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    additional_details: Union[
        List[AdditionalDetails], core.ArrayOut[AdditionalDetails]
    ] = core.attr(AdditionalDetails, computed=True, kind=core.Kind.array)

    attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]] = core.attr(
        InboundHeader, computed=True, kind=core.Kind.array
    )

    outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]] = core.attr(
        OutboundHeader, computed=True, kind=core.Kind.array
    )

    route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group_rule: Union[
        List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
    ] = core.attr(SecurityGroupRule, computed=True, kind=core.Kind.array)

    sequence_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_route_table_route: Union[
        List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]],
        additional_details: Union[List[AdditionalDetails], core.ArrayOut[AdditionalDetails]],
        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]],
        component: Union[List[Component], core.ArrayOut[Component]],
        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]],
        inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]],
        outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]],
        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]],
        security_group_rule: Union[List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]],
        sequence_number: Union[int, core.IntOut],
        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]],
        subnet: Union[List[Subnet], core.ArrayOut[Subnet]],
        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]],
        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ],
        vpc: Union[List[Vpc], core.ArrayOut[Vpc]],
    ):
        super().__init__(
            args=ForwardPathComponents.Args(
                acl_rule=acl_rule,
                additional_details=additional_details,
                attached_to=attached_to,
                component=component,
                destination_vpc=destination_vpc,
                inbound_header=inbound_header,
                outbound_header=outbound_header,
                route_table_route=route_table_route,
                security_group_rule=security_group_rule,
                sequence_number=sequence_number,
                source_vpc=source_vpc,
                subnet=subnet,
                transit_gateway=transit_gateway,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.arg()

        additional_details: Union[
            List[AdditionalDetails], core.ArrayOut[AdditionalDetails]
        ] = core.arg()

        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.arg()

        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()

        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.arg()

        inbound_header: Union[List[InboundHeader], core.ArrayOut[InboundHeader]] = core.arg()

        outbound_header: Union[List[OutboundHeader], core.ArrayOut[OutboundHeader]] = core.arg()

        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.arg()

        security_group_rule: Union[
            List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
        ] = core.arg()

        sequence_number: Union[int, core.IntOut] = core.arg()

        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.arg()

        subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.arg()

        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.arg()

        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ] = core.arg()

        vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.arg()


@core.schema
class PrefixList(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PrefixList.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LoadBalancerTargetGroups(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LoadBalancerTargetGroups.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class VpnGateway(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpnGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class ElasticLoadBalancerListener(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ElasticLoadBalancerListener.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SecurityGroup(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SecurityGroup.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Destination(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Destination.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkInterface(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NetworkInterface.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class NatGateway(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NatGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SecurityGroups(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SecurityGroups.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class InternetGateway(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InternetGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomerGateway(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomerGateway.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class VpcPeeringConnection(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcPeeringConnection.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class TransitGatewayAttachment(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TransitGatewayAttachment.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LoadBalancerTargetGroup(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LoadBalancerTargetGroup.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class VpnConnection(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpnConnection.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class RouteTable(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class SubnetRouteTable(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SubnetRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class PortRanges(core.Schema):

    from_: Union[int, core.IntOut] = core.attr(int, computed=True, alias="from")

    to: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        from_: Union[int, core.IntOut],
        to: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PortRanges.Args(
                from_=from_,
                to=to,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_: Union[int, core.IntOut] = core.arg()

        to: Union[int, core.IntOut] = core.arg()


@core.schema
class Acl(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Acl.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class IngressRouteTable(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IngressRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class VpcEndpoint(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcEndpoint.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class TransitGatewayRouteTable(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TransitGatewayRouteTable.Args(
                arn=arn,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class ClassicLoadBalancerListener(core.Schema):

    instance_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    load_balancer_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        instance_port: Union[int, core.IntOut],
        load_balancer_port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ClassicLoadBalancerListener.Args(
                instance_port=instance_port,
                load_balancer_port=load_balancer_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_port: Union[int, core.IntOut] = core.arg()

        load_balancer_port: Union[int, core.IntOut] = core.arg()


@core.schema
class Explanations(core.Schema):

    acl: Union[List[Acl], core.ArrayOut[Acl]] = core.attr(Acl, computed=True, kind=core.Kind.array)

    acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.attr(
        AclRule, computed=True, kind=core.Kind.array
    )

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.attr(
        AttachedTo, computed=True, kind=core.Kind.array
    )

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    classic_load_balancer_listener: Union[
        List[ClassicLoadBalancerListener], core.ArrayOut[ClassicLoadBalancerListener]
    ] = core.attr(ClassicLoadBalancerListener, computed=True, kind=core.Kind.array)

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    customer_gateway: Union[List[CustomerGateway], core.ArrayOut[CustomerGateway]] = core.attr(
        CustomerGateway, computed=True, kind=core.Kind.array
    )

    destination: Union[List[Destination], core.ArrayOut[Destination]] = core.attr(
        Destination, computed=True, kind=core.Kind.array
    )

    destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.attr(
        DestinationVpc, computed=True, kind=core.Kind.array
    )

    direction: Union[str, core.StringOut] = core.attr(str, computed=True)

    elastic_load_balancer_listener: Union[
        List[ElasticLoadBalancerListener], core.ArrayOut[ElasticLoadBalancerListener]
    ] = core.attr(ElasticLoadBalancerListener, computed=True, kind=core.Kind.array)

    explanation_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    ingress_route_table: Union[
        List[IngressRouteTable], core.ArrayOut[IngressRouteTable]
    ] = core.attr(IngressRouteTable, computed=True, kind=core.Kind.array)

    internet_gateway: Union[List[InternetGateway], core.ArrayOut[InternetGateway]] = core.attr(
        InternetGateway, computed=True, kind=core.Kind.array
    )

    load_balancer_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_listener_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    load_balancer_target_group: Union[
        List[LoadBalancerTargetGroup], core.ArrayOut[LoadBalancerTargetGroup]
    ] = core.attr(LoadBalancerTargetGroup, computed=True, kind=core.Kind.array)

    load_balancer_target_groups: Union[
        List[LoadBalancerTargetGroups], core.ArrayOut[LoadBalancerTargetGroups]
    ] = core.attr(LoadBalancerTargetGroups, computed=True, kind=core.Kind.array)

    load_balancer_target_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    missing_component: Union[str, core.StringOut] = core.attr(str, computed=True)

    nat_gateway: Union[List[NatGateway], core.ArrayOut[NatGateway]] = core.attr(
        NatGateway, computed=True, kind=core.Kind.array
    )

    network_interface: Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]] = core.attr(
        NetworkInterface, computed=True, kind=core.Kind.array
    )

    packet_field: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    port_ranges: Union[List[PortRanges], core.ArrayOut[PortRanges]] = core.attr(
        PortRanges, computed=True, kind=core.Kind.array
    )

    prefix_list: Union[List[PrefixList], core.ArrayOut[PrefixList]] = core.attr(
        PrefixList, computed=True, kind=core.Kind.array
    )

    protocols: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    route_table: Union[List[RouteTable], core.ArrayOut[RouteTable]] = core.attr(
        RouteTable, computed=True, kind=core.Kind.array
    )

    route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.attr(
        RouteTableRoute, computed=True, kind=core.Kind.array
    )

    security_group: Union[List[SecurityGroup], core.ArrayOut[SecurityGroup]] = core.attr(
        SecurityGroup, computed=True, kind=core.Kind.array
    )

    security_group_rule: Union[
        List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
    ] = core.attr(SecurityGroupRule, computed=True, kind=core.Kind.array)

    security_groups: Union[List[SecurityGroups], core.ArrayOut[SecurityGroups]] = core.attr(
        SecurityGroups, computed=True, kind=core.Kind.array
    )

    source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.attr(
        SourceVpc, computed=True, kind=core.Kind.array
    )

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.attr(
        Subnet, computed=True, kind=core.Kind.array
    )

    subnet_route_table: Union[List[SubnetRouteTable], core.ArrayOut[SubnetRouteTable]] = core.attr(
        SubnetRouteTable, computed=True, kind=core.Kind.array
    )

    transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.attr(
        TransitGateway, computed=True, kind=core.Kind.array
    )

    transit_gateway_attachment: Union[
        List[TransitGatewayAttachment], core.ArrayOut[TransitGatewayAttachment]
    ] = core.attr(TransitGatewayAttachment, computed=True, kind=core.Kind.array)

    transit_gateway_route_table: Union[
        List[TransitGatewayRouteTable], core.ArrayOut[TransitGatewayRouteTable]
    ] = core.attr(TransitGatewayRouteTable, computed=True, kind=core.Kind.array)

    transit_gateway_route_table_route: Union[
        List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
    ] = core.attr(TransitGatewayRouteTableRoute, computed=True, kind=core.Kind.array)

    vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.attr(Vpc, computed=True, kind=core.Kind.array)

    vpc_endpoint: Union[List[VpcEndpoint], core.ArrayOut[VpcEndpoint]] = core.attr(
        VpcEndpoint, computed=True, kind=core.Kind.array
    )

    vpc_peering_connection: Union[
        List[VpcPeeringConnection], core.ArrayOut[VpcPeeringConnection]
    ] = core.attr(VpcPeeringConnection, computed=True, kind=core.Kind.array)

    vpn_connection: Union[List[VpnConnection], core.ArrayOut[VpnConnection]] = core.attr(
        VpnConnection, computed=True, kind=core.Kind.array
    )

    vpn_gateway: Union[List[VpnGateway], core.ArrayOut[VpnGateway]] = core.attr(
        VpnGateway, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        acl: Union[List[Acl], core.ArrayOut[Acl]],
        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]],
        address: Union[str, core.StringOut],
        addresses: Union[List[str], core.ArrayOut[core.StringOut]],
        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]],
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        cidrs: Union[List[str], core.ArrayOut[core.StringOut]],
        classic_load_balancer_listener: Union[
            List[ClassicLoadBalancerListener], core.ArrayOut[ClassicLoadBalancerListener]
        ],
        component: Union[List[Component], core.ArrayOut[Component]],
        customer_gateway: Union[List[CustomerGateway], core.ArrayOut[CustomerGateway]],
        destination: Union[List[Destination], core.ArrayOut[Destination]],
        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]],
        direction: Union[str, core.StringOut],
        elastic_load_balancer_listener: Union[
            List[ElasticLoadBalancerListener], core.ArrayOut[ElasticLoadBalancerListener]
        ],
        explanation_code: Union[str, core.StringOut],
        ingress_route_table: Union[List[IngressRouteTable], core.ArrayOut[IngressRouteTable]],
        internet_gateway: Union[List[InternetGateway], core.ArrayOut[InternetGateway]],
        load_balancer_arn: Union[str, core.StringOut],
        load_balancer_listener_port: Union[int, core.IntOut],
        load_balancer_target_group: Union[
            List[LoadBalancerTargetGroup], core.ArrayOut[LoadBalancerTargetGroup]
        ],
        load_balancer_target_groups: Union[
            List[LoadBalancerTargetGroups], core.ArrayOut[LoadBalancerTargetGroups]
        ],
        load_balancer_target_port: Union[int, core.IntOut],
        missing_component: Union[str, core.StringOut],
        nat_gateway: Union[List[NatGateway], core.ArrayOut[NatGateway]],
        network_interface: Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]],
        packet_field: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
        port_ranges: Union[List[PortRanges], core.ArrayOut[PortRanges]],
        prefix_list: Union[List[PrefixList], core.ArrayOut[PrefixList]],
        protocols: Union[List[str], core.ArrayOut[core.StringOut]],
        route_table: Union[List[RouteTable], core.ArrayOut[RouteTable]],
        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]],
        security_group: Union[List[SecurityGroup], core.ArrayOut[SecurityGroup]],
        security_group_rule: Union[List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]],
        security_groups: Union[List[SecurityGroups], core.ArrayOut[SecurityGroups]],
        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]],
        state: Union[str, core.StringOut],
        subnet: Union[List[Subnet], core.ArrayOut[Subnet]],
        subnet_route_table: Union[List[SubnetRouteTable], core.ArrayOut[SubnetRouteTable]],
        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]],
        transit_gateway_attachment: Union[
            List[TransitGatewayAttachment], core.ArrayOut[TransitGatewayAttachment]
        ],
        transit_gateway_route_table: Union[
            List[TransitGatewayRouteTable], core.ArrayOut[TransitGatewayRouteTable]
        ],
        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ],
        vpc: Union[List[Vpc], core.ArrayOut[Vpc]],
        vpc_endpoint: Union[List[VpcEndpoint], core.ArrayOut[VpcEndpoint]],
        vpc_peering_connection: Union[
            List[VpcPeeringConnection], core.ArrayOut[VpcPeeringConnection]
        ],
        vpn_connection: Union[List[VpnConnection], core.ArrayOut[VpnConnection]],
        vpn_gateway: Union[List[VpnGateway], core.ArrayOut[VpnGateway]],
    ):
        super().__init__(
            args=Explanations.Args(
                acl=acl,
                acl_rule=acl_rule,
                address=address,
                addresses=addresses,
                attached_to=attached_to,
                availability_zones=availability_zones,
                cidrs=cidrs,
                classic_load_balancer_listener=classic_load_balancer_listener,
                component=component,
                customer_gateway=customer_gateway,
                destination=destination,
                destination_vpc=destination_vpc,
                direction=direction,
                elastic_load_balancer_listener=elastic_load_balancer_listener,
                explanation_code=explanation_code,
                ingress_route_table=ingress_route_table,
                internet_gateway=internet_gateway,
                load_balancer_arn=load_balancer_arn,
                load_balancer_listener_port=load_balancer_listener_port,
                load_balancer_target_group=load_balancer_target_group,
                load_balancer_target_groups=load_balancer_target_groups,
                load_balancer_target_port=load_balancer_target_port,
                missing_component=missing_component,
                nat_gateway=nat_gateway,
                network_interface=network_interface,
                packet_field=packet_field,
                port=port,
                port_ranges=port_ranges,
                prefix_list=prefix_list,
                protocols=protocols,
                route_table=route_table,
                route_table_route=route_table_route,
                security_group=security_group,
                security_group_rule=security_group_rule,
                security_groups=security_groups,
                source_vpc=source_vpc,
                state=state,
                subnet=subnet,
                subnet_route_table=subnet_route_table,
                transit_gateway=transit_gateway,
                transit_gateway_attachment=transit_gateway_attachment,
                transit_gateway_route_table=transit_gateway_route_table,
                transit_gateway_route_table_route=transit_gateway_route_table_route,
                vpc=vpc,
                vpc_endpoint=vpc_endpoint,
                vpc_peering_connection=vpc_peering_connection,
                vpn_connection=vpn_connection,
                vpn_gateway=vpn_gateway,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        acl: Union[List[Acl], core.ArrayOut[Acl]] = core.arg()

        acl_rule: Union[List[AclRule], core.ArrayOut[AclRule]] = core.arg()

        address: Union[str, core.StringOut] = core.arg()

        addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        attached_to: Union[List[AttachedTo], core.ArrayOut[AttachedTo]] = core.arg()

        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        classic_load_balancer_listener: Union[
            List[ClassicLoadBalancerListener], core.ArrayOut[ClassicLoadBalancerListener]
        ] = core.arg()

        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()

        customer_gateway: Union[List[CustomerGateway], core.ArrayOut[CustomerGateway]] = core.arg()

        destination: Union[List[Destination], core.ArrayOut[Destination]] = core.arg()

        destination_vpc: Union[List[DestinationVpc], core.ArrayOut[DestinationVpc]] = core.arg()

        direction: Union[str, core.StringOut] = core.arg()

        elastic_load_balancer_listener: Union[
            List[ElasticLoadBalancerListener], core.ArrayOut[ElasticLoadBalancerListener]
        ] = core.arg()

        explanation_code: Union[str, core.StringOut] = core.arg()

        ingress_route_table: Union[
            List[IngressRouteTable], core.ArrayOut[IngressRouteTable]
        ] = core.arg()

        internet_gateway: Union[List[InternetGateway], core.ArrayOut[InternetGateway]] = core.arg()

        load_balancer_arn: Union[str, core.StringOut] = core.arg()

        load_balancer_listener_port: Union[int, core.IntOut] = core.arg()

        load_balancer_target_group: Union[
            List[LoadBalancerTargetGroup], core.ArrayOut[LoadBalancerTargetGroup]
        ] = core.arg()

        load_balancer_target_groups: Union[
            List[LoadBalancerTargetGroups], core.ArrayOut[LoadBalancerTargetGroups]
        ] = core.arg()

        load_balancer_target_port: Union[int, core.IntOut] = core.arg()

        missing_component: Union[str, core.StringOut] = core.arg()

        nat_gateway: Union[List[NatGateway], core.ArrayOut[NatGateway]] = core.arg()

        network_interface: Union[
            List[NetworkInterface], core.ArrayOut[NetworkInterface]
        ] = core.arg()

        packet_field: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()

        port_ranges: Union[List[PortRanges], core.ArrayOut[PortRanges]] = core.arg()

        prefix_list: Union[List[PrefixList], core.ArrayOut[PrefixList]] = core.arg()

        protocols: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        route_table: Union[List[RouteTable], core.ArrayOut[RouteTable]] = core.arg()

        route_table_route: Union[List[RouteTableRoute], core.ArrayOut[RouteTableRoute]] = core.arg()

        security_group: Union[List[SecurityGroup], core.ArrayOut[SecurityGroup]] = core.arg()

        security_group_rule: Union[
            List[SecurityGroupRule], core.ArrayOut[SecurityGroupRule]
        ] = core.arg()

        security_groups: Union[List[SecurityGroups], core.ArrayOut[SecurityGroups]] = core.arg()

        source_vpc: Union[List[SourceVpc], core.ArrayOut[SourceVpc]] = core.arg()

        state: Union[str, core.StringOut] = core.arg()

        subnet: Union[List[Subnet], core.ArrayOut[Subnet]] = core.arg()

        subnet_route_table: Union[
            List[SubnetRouteTable], core.ArrayOut[SubnetRouteTable]
        ] = core.arg()

        transit_gateway: Union[List[TransitGateway], core.ArrayOut[TransitGateway]] = core.arg()

        transit_gateway_attachment: Union[
            List[TransitGatewayAttachment], core.ArrayOut[TransitGatewayAttachment]
        ] = core.arg()

        transit_gateway_route_table: Union[
            List[TransitGatewayRouteTable], core.ArrayOut[TransitGatewayRouteTable]
        ] = core.arg()

        transit_gateway_route_table_route: Union[
            List[TransitGatewayRouteTableRoute], core.ArrayOut[TransitGatewayRouteTableRoute]
        ] = core.arg()

        vpc: Union[List[Vpc], core.ArrayOut[Vpc]] = core.arg()

        vpc_endpoint: Union[List[VpcEndpoint], core.ArrayOut[VpcEndpoint]] = core.arg()

        vpc_peering_connection: Union[
            List[VpcPeeringConnection], core.ArrayOut[VpcPeeringConnection]
        ] = core.arg()

        vpn_connection: Union[List[VpnConnection], core.ArrayOut[VpnConnection]] = core.arg()

        vpn_gateway: Union[List[VpnGateway], core.ArrayOut[VpnGateway]] = core.arg()


@core.schema
class AlternatePathHints(core.Schema):

    component_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    component_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        component_arn: Union[str, core.StringOut],
        component_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AlternatePathHints.Args(
                component_arn=component_arn,
                component_id=component_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_arn: Union[str, core.StringOut] = core.arg()

        component_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ec2_network_insights_analysis", namespace="aws_vpc")
class Ec2NetworkInsightsAnalysis(core.Resource):

    alternate_path_hints: Union[
        List[AlternatePathHints], core.ArrayOut[AlternatePathHints]
    ] = core.attr(AlternatePathHints, computed=True, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    explanations: Union[List[Explanations], core.ArrayOut[Explanations]] = core.attr(
        Explanations, computed=True, kind=core.Kind.array
    )

    filter_in_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    forward_path_components: Union[
        List[ForwardPathComponents], core.ArrayOut[ForwardPathComponents]
    ] = core.attr(ForwardPathComponents, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_insights_path_id: Union[str, core.StringOut] = core.attr(str)

    path_found: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    return_path_components: Union[
        List[ReturnPathComponents], core.ArrayOut[ReturnPathComponents]
    ] = core.attr(ReturnPathComponents, computed=True, kind=core.Kind.array)

    start_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    wait_for_completion: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    warning_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        network_insights_path_id: Union[str, core.StringOut],
        filter_in_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        wait_for_completion: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2NetworkInsightsAnalysis.Args(
                network_insights_path_id=network_insights_path_id,
                filter_in_arns=filter_in_arns,
                tags=tags,
                tags_all=tags_all,
                wait_for_completion=wait_for_completion,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        filter_in_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        network_insights_path_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        wait_for_completion: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
