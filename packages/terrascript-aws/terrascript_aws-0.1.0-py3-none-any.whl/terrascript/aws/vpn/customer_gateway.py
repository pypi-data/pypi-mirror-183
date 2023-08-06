from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_customer_gateway", namespace="aws_vpn")
class CustomerGateway(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bgp_asn: Union[str, core.StringOut] = core.attr(str)

    certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bgp_asn: Union[str, core.StringOut],
        ip_address: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        certificate_arn: Optional[Union[str, core.StringOut]] = None,
        device_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomerGateway.Args(
                bgp_asn=bgp_asn,
                ip_address=ip_address,
                type=type,
                certificate_arn=certificate_arn,
                device_name=device_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bgp_asn: Union[str, core.StringOut] = core.arg()

        certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ip_address: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
