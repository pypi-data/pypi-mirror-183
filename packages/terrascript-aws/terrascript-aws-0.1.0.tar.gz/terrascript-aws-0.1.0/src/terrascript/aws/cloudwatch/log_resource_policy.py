from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_resource_policy", namespace="aws_cloudwatch")
class LogResourcePolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_document: Union[str, core.StringOut] = core.attr(str)

    policy_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy_document: Union[str, core.StringOut],
        policy_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogResourcePolicy.Args(
                policy_document=policy_document,
                policy_name=policy_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy_document: Union[str, core.StringOut] = core.arg()

        policy_name: Union[str, core.StringOut] = core.arg()
