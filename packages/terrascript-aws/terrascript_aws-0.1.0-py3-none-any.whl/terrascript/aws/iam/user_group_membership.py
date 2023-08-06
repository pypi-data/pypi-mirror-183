from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_user_group_membership", namespace="aws_iam")
class UserGroupMembership(core.Resource):

    groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        groups: Union[List[str], core.ArrayOut[core.StringOut]],
        user: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserGroupMembership.Args(
                groups=groups,
                user=user,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        user: Union[str, core.StringOut] = core.arg()
