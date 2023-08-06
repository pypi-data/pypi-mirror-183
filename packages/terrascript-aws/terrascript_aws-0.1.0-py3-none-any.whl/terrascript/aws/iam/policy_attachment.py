from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iam_policy_attachment", namespace="aws_iam")
class PolicyAttachment(core.Resource):

    groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    policy_arn: Union[str, core.StringOut] = core.attr(str)

    roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        policy_arn: Union[str, core.StringOut],
        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PolicyAttachment.Args(
                name=name,
                policy_arn=policy_arn,
                groups=groups,
                roles=roles,
                users=users,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        policy_arn: Union[str, core.StringOut] = core.arg()

        roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)
