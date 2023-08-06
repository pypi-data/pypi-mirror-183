from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.data(type="aws_ec2_transit_gateway", namespace="aws_transit_gateway")
class DsEc2TransitGateway(core.Data):

    amazon_side_asn: Union[int, core.IntOut] = core.attr(int, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    association_default_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_accept_shared_attachments: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_route_table_association: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_route_table_propagation: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    multicast_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    propagation_default_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    transit_gateway_cidr_blocks: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpn_ecmp_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEc2TransitGateway.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
