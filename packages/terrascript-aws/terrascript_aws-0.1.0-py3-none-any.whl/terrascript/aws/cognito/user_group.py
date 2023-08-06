from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cognito_user_group", namespace="aws_cognito")
class UserGroup(core.Resource):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    precedence: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        precedence: Optional[Union[int, core.IntOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroup.Args(
                name=name,
                user_pool_id=user_pool_id,
                description=description,
                precedence=precedence,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        precedence: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()
