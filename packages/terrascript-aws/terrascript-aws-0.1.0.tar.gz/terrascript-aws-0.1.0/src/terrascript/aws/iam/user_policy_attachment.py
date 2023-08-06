from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_user_policy_attachment", namespace="aws_iam")
class UserPolicyAttachment(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_arn: Union[str, core.StringOut] = core.attr(str)

    user: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy_arn: Union[str, core.StringOut],
        user: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserPolicyAttachment.Args(
                policy_arn=policy_arn,
                user=user,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy_arn: Union[str, core.StringOut] = core.arg()

        user: Union[str, core.StringOut] = core.arg()
