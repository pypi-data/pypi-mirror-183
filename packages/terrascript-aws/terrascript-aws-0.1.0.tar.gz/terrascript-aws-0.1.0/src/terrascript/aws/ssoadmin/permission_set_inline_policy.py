from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssoadmin_permission_set_inline_policy", namespace="aws_ssoadmin")
class PermissionSetInlinePolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inline_policy: Union[str, core.StringOut] = core.attr(str)

    instance_arn: Union[str, core.StringOut] = core.attr(str)

    permission_set_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        inline_policy: Union[str, core.StringOut],
        instance_arn: Union[str, core.StringOut],
        permission_set_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PermissionSetInlinePolicy.Args(
                inline_policy=inline_policy,
                instance_arn=instance_arn,
                permission_set_arn=permission_set_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        inline_policy: Union[str, core.StringOut] = core.arg()

        instance_arn: Union[str, core.StringOut] = core.arg()

        permission_set_arn: Union[str, core.StringOut] = core.arg()
