from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_group_policy_attachment", namespace="aws_iam")
class GroupPolicyAttachment(core.Resource):

    group: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group: Union[str, core.StringOut],
        policy_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupPolicyAttachment.Args(
                group=group,
                policy_arn=policy_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group: Union[str, core.StringOut] = core.arg()

        policy_arn: Union[str, core.StringOut] = core.arg()
