from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_multicast_group_source", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayMulticastGroupSource(core.Resource):

    group_ip_address: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    transit_gateway_multicast_domain_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_ip_address: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        transit_gateway_multicast_domain_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastGroupSource.Args(
                group_ip_address=group_ip_address,
                network_interface_id=network_interface_id,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_ip_address: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_multicast_domain_id: Union[str, core.StringOut] = core.arg()
