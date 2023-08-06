from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PrivateDnsNameConfiguration(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        state: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PrivateDnsNameConfiguration.Args(
                name=name,
                state=state,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        state: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_vpc_endpoint_service", namespace="aws_vpc")
class EndpointService(core.Resource):

    acceptance_required: Union[bool, core.BoolOut] = core.attr(bool)

    allowed_principals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    base_endpoint_dns_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    gateway_load_balancer_arns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    manages_vpc_endpoints: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    network_load_balancer_arns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    private_dns_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    private_dns_name_configuration: Union[
        List[PrivateDnsNameConfiguration], core.ArrayOut[PrivateDnsNameConfiguration]
    ] = core.attr(PrivateDnsNameConfiguration, computed=True, kind=core.Kind.array)

    service_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    supported_ip_address_types: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, computed=True, kind=core.Kind.array)

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
        acceptance_required: Union[bool, core.BoolOut],
        allowed_principals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        gateway_load_balancer_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        network_load_balancer_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        private_dns_name: Optional[Union[str, core.StringOut]] = None,
        supported_ip_address_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointService.Args(
                acceptance_required=acceptance_required,
                allowed_principals=allowed_principals,
                gateway_load_balancer_arns=gateway_load_balancer_arns,
                network_load_balancer_arns=network_load_balancer_arns,
                private_dns_name=private_dns_name,
                supported_ip_address_types=supported_ip_address_types,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acceptance_required: Union[bool, core.BoolOut] = core.arg()

        allowed_principals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        gateway_load_balancer_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        network_load_balancer_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        private_dns_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        supported_ip_address_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
