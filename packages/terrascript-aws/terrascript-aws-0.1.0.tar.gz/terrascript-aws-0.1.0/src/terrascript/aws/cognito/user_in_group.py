from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cognito_user_in_group", namespace="aws_cognito")
class UserInGroup(core.Resource):

    group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserInGroup.Args(
                group_name=group_name,
                user_pool_id=user_pool_id,
                username=username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_name: Union[str, core.StringOut] = core.arg()

        user_pool_id: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()
