from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sns_topic_policy", namespace="aws_sns")
class TopicPolicy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicPolicy.Args(
                arn=arn,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()
