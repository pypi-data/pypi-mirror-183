from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloud9_environment_membership", namespace="aws_cloud9")
class EnvironmentMembership(core.Resource):
    """
    (Required) The ID of the environment that contains the environment member you want to add.
    """

    environment_id: Union[str, core.StringOut] = core.attr(str)

    """
    The ID of the environment membership.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The type of environment member permissions you want to associate with this environment me
    mber. Allowed values are `read-only` and `read-write` .
    """
    permissions: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the environment member you want to add.
    """
    user_arn: Union[str, core.StringOut] = core.attr(str)

    """
    he user ID in AWS Identity and Access Management (AWS IAM) of the environment member.
    """
    user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        environment_id: Union[str, core.StringOut],
        permissions: Union[str, core.StringOut],
        user_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EnvironmentMembership.Args(
                environment_id=environment_id,
                permissions=permissions,
                user_arn=user_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        environment_id: Union[str, core.StringOut] = core.arg()

        permissions: Union[str, core.StringOut] = core.arg()

        user_arn: Union[str, core.StringOut] = core.arg()
