from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_default_subnet", namespace="aws_vpc")
class DefaultSubnet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    assign_ipv6_address_on_creation: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_dns64: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_resource_name_dns_aaaa_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    existing_default_subnet: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_cidr_block_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_native: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: Union[str, core.StringOut],
        assign_ipv6_address_on_creation: Optional[Union[bool, core.BoolOut]] = None,
        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = None,
        enable_dns64: Optional[Union[bool, core.BoolOut]] = None,
        enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        enable_resource_name_dns_aaaa_record_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        ipv6_native: Optional[Union[bool, core.BoolOut]] = None,
        map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = None,
        private_dns_hostname_type_on_launch: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultSubnet.Args(
                availability_zone=availability_zone,
                assign_ipv6_address_on_creation=assign_ipv6_address_on_creation,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                enable_dns64=enable_dns64,
                enable_resource_name_dns_a_record_on_launch=enable_resource_name_dns_a_record_on_launch,
                enable_resource_name_dns_aaaa_record_on_launch=enable_resource_name_dns_aaaa_record_on_launch,
                force_destroy=force_destroy,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_native=ipv6_native,
                map_customer_owned_ip_on_launch=map_customer_owned_ip_on_launch,
                map_public_ip_on_launch=map_public_ip_on_launch,
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

        availability_zone: Union[str, core.StringOut] = core.arg()

        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_dns64: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_resource_name_dns_a_record_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        enable_resource_name_dns_aaaa_record_on_launch: Optional[
            Union[bool, core.BoolOut]
        ] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_native: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        map_customer_owned_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        map_public_ip_on_launch: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        private_dns_hostname_type_on_launch: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
