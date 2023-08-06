from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sqs_queue_policy", namespace="aws_sqs")
class QueuePolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    queue_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        queue_url: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueuePolicy.Args(
                policy=policy,
                queue_url=queue_url,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: Union[str, core.StringOut] = core.arg()

        queue_url: Union[str, core.StringOut] = core.arg()
