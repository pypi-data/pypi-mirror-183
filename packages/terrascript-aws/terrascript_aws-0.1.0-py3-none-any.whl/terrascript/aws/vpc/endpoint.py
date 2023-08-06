from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DnsEntry(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        hosted_zone_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DnsEntry.Args(
                dns_name=dns_name,
                hosted_zone_id=hosted_zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        hosted_zone_id: Union[str, core.StringOut] = core.arg()


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dns_record_ip_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_vpc_endpoint", namespace="aws_vpc")
class Endpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_accept: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cidr_blocks: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    dns_entry: Union[List[DnsEntry], core.ArrayOut[DnsEntry]] = core.attr(
        DnsEntry, computed=True, kind=core.Kind.array
    )

    dns_options: Optional[DnsOptions] = core.attr(DnsOptions, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    requester_managed: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    service_name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
        auto_accept: Optional[Union[bool, core.BoolOut]] = None,
        dns_options: Optional[DnsOptions] = None,
        ip_address_type: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        private_dns_enabled: Optional[Union[bool, core.BoolOut]] = None,
        route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_endpoint_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                service_name=service_name,
                vpc_id=vpc_id,
                auto_accept=auto_accept,
                dns_options=dns_options,
                ip_address_type=ip_address_type,
                policy=policy,
                private_dns_enabled=private_dns_enabled,
                route_table_ids=route_table_ids,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_type=vpc_endpoint_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_accept: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        dns_options: Optional[DnsOptions] = core.arg(default=None)

        ip_address_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_dns_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        service_name: Union[str, core.StringOut] = core.arg()

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_endpoint_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Union[str, core.StringOut] = core.arg()
