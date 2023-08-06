from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_route_table_association", namespace="aws_vpc")
class EndpointRouteTableAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route_table_id: Union[str, core.StringOut] = core.attr(str)

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route_table_id: Union[str, core.StringOut],
        vpc_endpoint_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointRouteTableAssociation.Args(
                route_table_id=route_table_id,
                vpc_endpoint_id=vpc_endpoint_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        route_table_id: Union[str, core.StringOut] = core.arg()

        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()
