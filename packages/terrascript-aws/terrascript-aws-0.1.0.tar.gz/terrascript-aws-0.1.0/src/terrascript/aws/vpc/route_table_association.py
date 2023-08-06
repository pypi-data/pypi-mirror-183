from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route_table_association", namespace="aws_vpc")
class RouteTableAssociation(core.Resource):

    gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Union[str, core.StringOut] = core.attr(str)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: Union[str, core.StringOut],
        gateway_id: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RouteTableAssociation.Args(
                route_table_id=route_table_id,
                gateway_id=gateway_id,
                subnet_id=subnet_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route_table_id: Union[str, core.StringOut] = core.arg()

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
