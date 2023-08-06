from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_main_route_table_association", namespace="aws_vpc")
class MainRouteTableAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    original_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Union[str, core.StringOut] = core.attr(str)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MainRouteTableAssociation.Args(
                route_table_id=route_table_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        route_table_id: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()
