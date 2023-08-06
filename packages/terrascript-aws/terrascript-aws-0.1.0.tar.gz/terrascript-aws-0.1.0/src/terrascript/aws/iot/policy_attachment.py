from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_policy_attachment", namespace="aws_iot")
class PolicyAttachment(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    target: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        target: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PolicyAttachment.Args(
                policy=policy,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: Union[str, core.StringOut] = core.arg()

        target: Union[str, core.StringOut] = core.arg()
