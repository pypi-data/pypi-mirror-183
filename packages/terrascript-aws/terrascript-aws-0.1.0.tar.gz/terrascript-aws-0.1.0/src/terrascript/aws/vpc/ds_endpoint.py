from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DnsOptions(core.Schema):

    dns_record_ip_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dns_record_ip_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DnsOptions.Args(
                dns_record_ip_type=dns_record_ip_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_record_ip_type: Union[str, core.StringOut] = core.arg()


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


@core.data(type="aws_vpc_endpoint", namespace="aws_vpc")
class DsEndpoint(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_blocks: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    dns_entry: Union[List[DnsEntry], core.ArrayOut[DnsEntry]] = core.attr(
        DnsEntry, computed=True, kind=core.Kind.array
    )

    dns_options: Union[List[DnsOptions], core.ArrayOut[DnsOptions]] = core.attr(
        DnsOptions, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    ip_address_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    prefix_list_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    requester_managed: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    route_table_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        service_name: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpoint.Args(
                filter=filter,
                id=id,
                service_name=service_name,
                state=state,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
