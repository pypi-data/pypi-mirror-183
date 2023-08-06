from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_dx_hosted_private_virtual_interface_accepter", namespace="aws_direct_connect"
)
class DxHostedPrivateVirtualInterfaceAccepter(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    dx_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    virtual_interface_id: Union[str, core.StringOut] = core.attr(str)

    vpn_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        virtual_interface_id: Union[str, core.StringOut],
        dx_gateway_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpn_gateway_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedPrivateVirtualInterfaceAccepter.Args(
                virtual_interface_id=virtual_interface_id,
                dx_gateway_id=dx_gateway_id,
                tags=tags,
                tags_all=tags_all,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        dx_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        virtual_interface_id: Union[str, core.StringOut] = core.arg()

        vpn_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
