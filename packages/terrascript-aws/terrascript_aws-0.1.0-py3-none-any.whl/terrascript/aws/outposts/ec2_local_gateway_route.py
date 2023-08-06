from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_local_gateway_route", namespace="aws_outposts")
class Ec2LocalGatewayRoute(core.Resource):

    destination_cidr_block: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_gateway_route_table_id: Union[str, core.StringOut] = core.attr(str)

    local_gateway_virtual_interface_group_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: Union[str, core.StringOut],
        local_gateway_route_table_id: Union[str, core.StringOut],
        local_gateway_virtual_interface_group_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2LocalGatewayRoute.Args(
                destination_cidr_block=destination_cidr_block,
                local_gateway_route_table_id=local_gateway_route_table_id,
                local_gateway_virtual_interface_group_id=local_gateway_virtual_interface_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_cidr_block: Union[str, core.StringOut] = core.arg()

        local_gateway_route_table_id: Union[str, core.StringOut] = core.arg()

        local_gateway_virtual_interface_group_id: Union[str, core.StringOut] = core.arg()
