from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InlinePolicy(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InlinePolicy.Args(
                name=name,
                policy=policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_iam_role", namespace="aws_iam")
class Role(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    assume_role_policy: Union[str, core.StringOut] = core.attr(str)

    create_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_detach_policies: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inline_policy: Optional[Union[List[InlinePolicy], core.ArrayOut[InlinePolicy]]] = core.attr(
        InlinePolicy, default=None, computed=True, kind=core.Kind.array
    )

    managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    max_session_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    permissions_boundary: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    unique_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        assume_role_policy: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        force_detach_policies: Optional[Union[bool, core.BoolOut]] = None,
        inline_policy: Optional[Union[List[InlinePolicy], core.ArrayOut[InlinePolicy]]] = None,
        managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        max_session_duration: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
        permissions_boundary: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Role.Args(
                assume_role_policy=assume_role_policy,
                description=description,
                force_detach_policies=force_detach_policies,
                inline_policy=inline_policy,
                managed_policy_arns=managed_policy_arns,
                max_session_duration=max_session_duration,
                name=name,
                name_prefix=name_prefix,
                path=path,
                permissions_boundary=permissions_boundary,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        assume_role_policy: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_detach_policies: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        inline_policy: Optional[Union[List[InlinePolicy], core.ArrayOut[InlinePolicy]]] = core.arg(
            default=None
        )

        managed_policy_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_session_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permissions_boundary: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
