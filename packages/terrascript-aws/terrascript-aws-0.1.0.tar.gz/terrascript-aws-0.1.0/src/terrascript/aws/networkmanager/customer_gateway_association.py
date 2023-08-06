from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_networkmanager_customer_gateway_association", namespace="aws_networkmanager"
)
class CustomerGatewayAssociation(core.Resource):

    customer_gateway_arn: Union[str, core.StringOut] = core.attr(str)

    device_id: Union[str, core.StringOut] = core.attr(str)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    link_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        customer_gateway_arn: Union[str, core.StringOut],
        device_id: Union[str, core.StringOut],
        global_network_id: Union[str, core.StringOut],
        link_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomerGatewayAssociation.Args(
                customer_gateway_arn=customer_gateway_arn,
                device_id=device_id,
                global_network_id=global_network_id,
                link_id=link_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        customer_gateway_arn: Union[str, core.StringOut] = core.arg()

        device_id: Union[str, core.StringOut] = core.arg()

        global_network_id: Union[str, core.StringOut] = core.arg()

        link_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
