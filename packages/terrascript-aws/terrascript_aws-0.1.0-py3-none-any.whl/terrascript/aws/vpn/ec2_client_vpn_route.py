from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_route", namespace="aws_vpn")
class Ec2ClientVpnRoute(core.Resource):

    client_vpn_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_cidr_block: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    origin: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_vpc_subnet_id: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: Union[str, core.StringOut],
        destination_cidr_block: Union[str, core.StringOut],
        target_vpc_subnet_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnRoute.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                destination_cidr_block=destination_cidr_block,
                target_vpc_subnet_id=target_vpc_subnet_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        client_vpn_endpoint_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_cidr_block: Union[str, core.StringOut] = core.arg()

        target_vpc_subnet_id: Union[str, core.StringOut] = core.arg()
