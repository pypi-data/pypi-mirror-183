from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_rest_api_policy", namespace="aws_api_gateway")
class RestApiPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RestApiPolicy.Args(
                policy=policy,
                rest_api_id=rest_api_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()
