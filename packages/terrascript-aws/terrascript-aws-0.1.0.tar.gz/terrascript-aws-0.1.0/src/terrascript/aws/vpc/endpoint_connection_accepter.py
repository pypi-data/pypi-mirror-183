from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_connection_accepter", namespace="aws_vpc")
class EndpointConnectionAccepter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    vpc_endpoint_service_id: Union[str, core.StringOut] = core.attr(str)

    vpc_endpoint_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_endpoint_id: Union[str, core.StringOut],
        vpc_endpoint_service_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConnectionAccepter.Args(
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_service_id=vpc_endpoint_service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()

        vpc_endpoint_service_id: Union[str, core.StringOut] = core.arg()
