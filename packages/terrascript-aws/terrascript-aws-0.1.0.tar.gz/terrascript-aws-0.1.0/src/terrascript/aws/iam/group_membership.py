from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_group_membership", namespace="aws_iam")
class GroupMembership(core.Resource):

    group: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    users: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        group: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        users: Union[List[str], core.ArrayOut[core.StringOut]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GroupMembership.Args(
                group=group,
                name=name,
                users=users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        users: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()
