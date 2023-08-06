from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpn_connection_route", namespace="aws_vpn")
class ConnectionRoute(core.Resource):

    destination_cidr_block: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpn_connection_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: Union[str, core.StringOut],
        vpn_connection_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConnectionRoute.Args(
                destination_cidr_block=destination_cidr_block,
                vpn_connection_id=vpn_connection_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_cidr_block: Union[str, core.StringOut] = core.arg()

        vpn_connection_id: Union[str, core.StringOut] = core.arg()
