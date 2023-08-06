from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_networkmanager_transit_gateway_registration", namespace="aws_networkmanager"
)
class TransitGatewayRegistration(core.Resource):

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    transit_gateway_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        global_network_id: Union[str, core.StringOut],
        transit_gateway_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TransitGatewayRegistration.Args(
                global_network_id=global_network_id,
                transit_gateway_arn=transit_gateway_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_network_id: Union[str, core.StringOut] = core.arg()

        transit_gateway_arn: Union[str, core.StringOut] = core.arg()
