from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_default_vpc", namespace="aws_vpc")
class DefaultVpc(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    assign_generated_ipv6_cidr_block: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_network_acl_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    dhcp_options_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    enable_classiclink: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enable_classiclink_dns_support: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enable_dns_hostnames: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_dns_support: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    existing_default_vpc: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_tenancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_cidr_block_network_border_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv6_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    main_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        assign_generated_ipv6_cidr_block: Optional[Union[bool, core.BoolOut]] = None,
        enable_classiclink: Optional[Union[bool, core.BoolOut]] = None,
        enable_classiclink_dns_support: Optional[Union[bool, core.BoolOut]] = None,
        enable_dns_hostnames: Optional[Union[bool, core.BoolOut]] = None,
        enable_dns_support: Optional[Union[bool, core.BoolOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_block_network_border_group: Optional[Union[str, core.StringOut]] = None,
        ipv6_ipam_pool_id: Optional[Union[str, core.StringOut]] = None,
        ipv6_netmask_length: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultVpc.Args(
                assign_generated_ipv6_cidr_block=assign_generated_ipv6_cidr_block,
                enable_classiclink=enable_classiclink,
                enable_classiclink_dns_support=enable_classiclink_dns_support,
                enable_dns_hostnames=enable_dns_hostnames,
                enable_dns_support=enable_dns_support,
                force_destroy=force_destroy,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_cidr_block_network_border_group=ipv6_cidr_block_network_border_group,
                ipv6_ipam_pool_id=ipv6_ipam_pool_id,
                ipv6_netmask_length=ipv6_netmask_length,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assign_generated_ipv6_cidr_block: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        enable_classiclink: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_classiclink_dns_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_dns_hostnames: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_dns_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_cidr_block_network_border_group: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        ipv6_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
