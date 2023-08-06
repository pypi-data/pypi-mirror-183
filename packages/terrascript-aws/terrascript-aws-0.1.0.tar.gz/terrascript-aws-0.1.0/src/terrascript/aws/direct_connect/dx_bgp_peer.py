from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_bgp_peer", namespace="aws_direct_connect")
class DxBgpPeer(core.Resource):

    address_family: Union[str, core.StringOut] = core.attr(str)

    amazon_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    aws_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    bgp_asn: Union[int, core.IntOut] = core.attr(int)

    bgp_auth_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    bgp_peer_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    bgp_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtual_interface_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: Union[str, core.StringOut],
        bgp_asn: Union[int, core.IntOut],
        virtual_interface_id: Union[str, core.StringOut],
        amazon_address: Optional[Union[str, core.StringOut]] = None,
        bgp_auth_key: Optional[Union[str, core.StringOut]] = None,
        customer_address: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxBgpPeer.Args(
                address_family=address_family,
                bgp_asn=bgp_asn,
                virtual_interface_id=virtual_interface_id,
                amazon_address=amazon_address,
                bgp_auth_key=bgp_auth_key,
                customer_address=customer_address,
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

        customer_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        virtual_interface_id: Union[str, core.StringOut] = core.arg()
