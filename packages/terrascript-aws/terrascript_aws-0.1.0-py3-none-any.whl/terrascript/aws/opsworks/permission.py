from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_opsworks_permission", namespace="aws_opsworks")
class Permission(core.Resource):

    allow_ssh: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    allow_sudo: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    stack_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    user_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        user_arn: Union[str, core.StringOut],
        allow_ssh: Optional[Union[bool, core.BoolOut]] = None,
        allow_sudo: Optional[Union[bool, core.BoolOut]] = None,
        level: Optional[Union[str, core.StringOut]] = None,
        stack_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permission.Args(
                user_arn=user_arn,
                allow_ssh=allow_ssh,
                allow_sudo=allow_sudo,
                level=level,
                stack_id=stack_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_ssh: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        allow_sudo: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stack_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_arn: Union[str, core.StringOut] = core.arg()
