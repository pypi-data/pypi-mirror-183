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


@core.data(type="aws_vpc_endpoint_service", namespace="aws_vpc")
class DsEndpointService(core.Data):

    acceptance_required: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    base_endpoint_dns_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    manages_vpc_endpoints: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    service: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    service_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    supported_ip_address_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_policy_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        service: Optional[Union[str, core.StringOut]] = None,
        service_name: Optional[Union[str, core.StringOut]] = None,
        service_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsEndpointService.Args(
                filter=filter,
                service=service,
                service_name=service_name,
                service_type=service_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        service: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
