from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Members(core.Schema):

    group_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_ip_address: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Members.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_ip_address: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()


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
class Sources(core.Schema):

    group_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        group_ip_address: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Sources.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_ip_address: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Associations(core.Schema):

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        subnet_id: Union[str, core.StringOut],
        transit_gateway_attachment_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Associations.Args(
                subnet_id=subnet_id,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_attachment_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_ec2_transit_gateway_multicast_domain", namespace="aws_transit_gateway")
class DsEc2TransitGatewayMulticastDomain(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associations: Union[List[Associations], core.ArrayOut[Associations]] = core.attr(
        Associations, computed=True, kind=core.Kind.array
    )

    auto_accept_shared_associations: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    igmpv2_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    members: Union[List[Members], core.ArrayOut[Members]] = core.attr(
        Members, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    sources: Union[List[Sources], core.ArrayOut[Sources]] = core.attr(
        Sources, computed=True, kind=core.Kind.array
    )

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    static_sources_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_multicast_domain_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transit_gateway_multicast_domain_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGatewayMulticastDomain.Args(
                filter=filter,
                tags=tags,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        transit_gateway_multicast_domain_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )
