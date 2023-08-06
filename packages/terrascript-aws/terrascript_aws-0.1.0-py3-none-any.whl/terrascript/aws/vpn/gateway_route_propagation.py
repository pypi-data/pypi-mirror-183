from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpn_gateway_route_propagation", namespace="aws_vpn")
class GatewayRoutePropagation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Union[str, core.StringOut] = core.attr(str)

    vpn_gateway_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: Union[str, core.StringOut],
        vpn_gateway_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayRoutePropagation.Args(
                route_table_id=route_table_id,
                vpn_gateway_id=vpn_gateway_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        route_table_id: Union[str, core.StringOut] = core.arg()

        vpn_gateway_id: Union[str, core.StringOut] = core.arg()
