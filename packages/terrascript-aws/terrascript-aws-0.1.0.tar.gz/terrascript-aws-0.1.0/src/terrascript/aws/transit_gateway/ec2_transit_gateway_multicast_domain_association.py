from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_ec2_transit_gateway_multicast_domain_association", namespace="aws_transit_gateway"
)
class Ec2TransitGatewayMulticastDomainAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    transit_gateway_attachment_id: Union[str, core.StringOut] = core.attr(str)

    transit_gateway_multicast_domain_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_id: Union[str, core.StringOut],
        transit_gateway_attachment_id: Union[str, core.StringOut],
        transit_gateway_multicast_domain_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TransitGatewayMulticastDomainAssociation.Args(
                subnet_id=subnet_id,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                transit_gateway_multicast_domain_id=transit_gateway_multicast_domain_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        subnet_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_attachment_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_multicast_domain_id: Union[str, core.StringOut] = core.arg()
