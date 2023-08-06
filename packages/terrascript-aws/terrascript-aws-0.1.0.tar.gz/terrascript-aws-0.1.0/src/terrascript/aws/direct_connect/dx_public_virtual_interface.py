from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_public_virtual_interface", namespace="aws_direct_connect")
class DxPublicVirtualInterface(core.Resource):

    address_family: Union[str, core.StringOut] = core.attr(str)

    amazon_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    amazon_side_asn: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    bgp_asn: Union[int, core.IntOut] = core.attr(int)

    bgp_auth_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    connection_id: Union[str, core.StringOut] = core.attr(str)

    customer_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    route_filter_prefixes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vlan: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: Union[str, core.StringOut],
        bgp_asn: Union[int, core.IntOut],
        connection_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        route_filter_prefixes: Union[List[str], core.ArrayOut[core.StringOut]],
        vlan: Union[int, core.IntOut],
        amazon_address: Optional[Union[str, core.StringOut]] = None,
        bgp_auth_key: Optional[Union[str, core.StringOut]] = None,
        customer_address: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxPublicVirtualInterface.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                connection_id=connection_id,
                name=name,
                route_filter_prefixes=route_filter_prefixes,
                vlan=vlan,
                amazon_address=amazon_address,
                bgp_auth_key=bgp_auth_key,
                customer_address=customer_address,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: Union[str, core.StringOut] = core.arg()

        amazon_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bgp_asn: Union[int, core.IntOut] = core.arg()

        bgp_auth_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_id: Union[str, core.StringOut] = core.arg()

        customer_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        route_filter_prefixes: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vlan: Union[int, core.IntOut] = core.arg()
