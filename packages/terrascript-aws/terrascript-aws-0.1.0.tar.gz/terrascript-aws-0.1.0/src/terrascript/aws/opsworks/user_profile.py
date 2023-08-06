from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_opsworks_user_profile", namespace="aws_opsworks")
class UserProfile(core.Resource):

    allow_self_management: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ssh_public_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssh_username: Union[str, core.StringOut] = core.attr(str)

    user_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ssh_username: Union[str, core.StringOut],
        user_arn: Union[str, core.StringOut],
        allow_self_management: Optional[Union[bool, core.BoolOut]] = None,
        ssh_public_key: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserProfile.Args(
                ssh_username=ssh_username,
                user_arn=user_arn,
                allow_self_management=allow_self_management,
                ssh_public_key=ssh_public_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_self_management: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ssh_public_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssh_username: Union[str, core.StringOut] = core.arg()

        user_arn: Union[str, core.StringOut] = core.arg()
