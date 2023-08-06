from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_subnet", namespace="aws_vpc")
class Subnet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    assign_ipv6_address_on_creation: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    availability_zone_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_dns64: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_resource_name_dns_aaaa_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv6_cidr_block_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_native: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_hostname_type_on_launch: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: Union[str, core.StringOut],
        assign_ipv6_address_on_creation: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        availability_zone_id: Optional[Union[str, core.StringOut]] = None,
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = None,
        enable_dns64: Optional[Union[bool, core.BoolOut]] = None,
        enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        enable_resource_name_dns_aaaa_record_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        ipv6_native: Optional[Union[bool, core.BoolOut]] = None,
        map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        private_dns_hostname_type_on_launch: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Subnet.Args(
                vpc_id=vpc_id,
                assign_ipv6_address_on_creation=assign_ipv6_address_on_creation,
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                cidr_block=cidr_block,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                enable_dns64=enable_dns64,
                enable_resource_name_dns_a_record_on_launch=enable_resource_name_dns_a_record_on_launch,
                enable_resource_name_dns_aaaa_record_on_launch=enable_resource_name_dns_aaaa_record_on_launch,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_native=ipv6_native,
                map_customer_owned_ip_on_launch=map_customer_owned_ip_on_launch,
                map_public_ip_on_launch=map_public_ip_on_launch,
                outpost_arn=outpost_arn,
                private_dns_hostname_type_on_launch=private_dns_hostname_type_on_launch,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assign_ipv6_address_on_creation: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_dns64: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        enable_resource_name_dns_aaaa_record_on_launch: Optional[
            Union[bool, core.BoolOut]
        ] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_native: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_dns_hostname_type_on_launch: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Union[str, core.StringOut] = core.arg()
