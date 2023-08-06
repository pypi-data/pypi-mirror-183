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


@core.data(type="aws_subnet", namespace="aws_vpc")
class DsSubnet(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    assign_ipv6_address_on_creation: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    availability_zone_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    available_ip_address_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    customer_owned_ipv4_pool: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_for_az: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enable_dns64: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_resource_name_dns_a_record_on_launch: Union[bool, core.BoolOut] = core.attr(
        bool, computed=True
    )

    enable_resource_name_dns_aaaa_record_on_launch: Union[bool, core.BoolOut] = core.attr(
        bool, computed=True
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_cidr_block_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_native: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    map_customer_owned_ip_on_launch: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    map_public_ip_on_launch: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_hostname_type_on_launch: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        availability_zone_id: Optional[Union[str, core.StringOut]] = None,
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        default_for_az: Optional[Union[bool, core.BoolOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubnet.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                cidr_block=cidr_block,
                default_for_az=default_for_az,
                filter=filter,
                id=id,
                ipv6_cidr_block=ipv6_cidr_block,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_for_az: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
