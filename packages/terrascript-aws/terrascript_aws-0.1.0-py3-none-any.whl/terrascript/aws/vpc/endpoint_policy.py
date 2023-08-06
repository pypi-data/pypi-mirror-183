from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_policy", namespace="aws_vpc")
class EndpointPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    vpc_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_endpoint_id: Union[str, core.StringOut],
        policy: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointPolicy.Args(
                vpc_endpoint_id=vpc_endpoint_id,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_endpoint_id: Union[str, core.StringOut] = core.arg()
