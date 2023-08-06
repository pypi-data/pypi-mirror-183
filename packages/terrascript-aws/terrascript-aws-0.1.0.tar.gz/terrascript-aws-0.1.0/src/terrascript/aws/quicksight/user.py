from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_quicksight_user", namespace="aws_quicksight")
class User(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_account_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    email: Union[str, core.StringOut] = core.attr(str)

    iam_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_type: Union[str, core.StringOut] = core.attr(str)

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    session_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_role: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        email: Union[str, core.StringOut],
        identity_type: Union[str, core.StringOut],
        user_role: Union[str, core.StringOut],
        aws_account_id: Optional[Union[str, core.StringOut]] = None,
        iam_arn: Optional[Union[str, core.StringOut]] = None,
        namespace: Optional[Union[str, core.StringOut]] = None,
        session_name: Optional[Union[str, core.StringOut]] = None,
        user_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                email=email,
                identity_type=identity_type,
                user_role=user_role,
                aws_account_id=aws_account_id,
                iam_arn=iam_arn,
                namespace=namespace,
                session_name=session_name,
                user_name=user_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        email: Union[str, core.StringOut] = core.arg()

        iam_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_type: Union[str, core.StringOut] = core.arg()

        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        session_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_role: Union[str, core.StringOut] = core.arg()
