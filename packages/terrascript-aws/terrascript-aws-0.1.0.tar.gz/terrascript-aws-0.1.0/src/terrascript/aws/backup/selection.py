from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class StringEquals(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StringEquals.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class StringLike(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StringLike.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class StringNotEquals(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StringNotEquals.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class StringNotLike(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StringNotLike.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Condition(core.Schema):

    string_equals: Optional[Union[List[StringEquals], core.ArrayOut[StringEquals]]] = core.attr(
        StringEquals, default=None, kind=core.Kind.array
    )

    string_like: Optional[Union[List[StringLike], core.ArrayOut[StringLike]]] = core.attr(
        StringLike, default=None, kind=core.Kind.array
    )

    string_not_equals: Optional[
        Union[List[StringNotEquals], core.ArrayOut[StringNotEquals]]
    ] = core.attr(StringNotEquals, default=None, kind=core.Kind.array)

    string_not_like: Optional[Union[List[StringNotLike], core.ArrayOut[StringNotLike]]] = core.attr(
        StringNotLike, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        string_equals: Optional[Union[List[StringEquals], core.ArrayOut[StringEquals]]] = None,
        string_like: Optional[Union[List[StringLike], core.ArrayOut[StringLike]]] = None,
        string_not_equals: Optional[
            Union[List[StringNotEquals], core.ArrayOut[StringNotEquals]]
        ] = None,
        string_not_like: Optional[Union[List[StringNotLike], core.ArrayOut[StringNotLike]]] = None,
    ):
        super().__init__(
            args=Condition.Args(
                string_equals=string_equals,
                string_like=string_like,
                string_not_equals=string_not_equals,
                string_not_like=string_not_like,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        string_equals: Optional[Union[List[StringEquals], core.ArrayOut[StringEquals]]] = core.arg(
            default=None
        )

        string_like: Optional[Union[List[StringLike], core.ArrayOut[StringLike]]] = core.arg(
            default=None
        )

        string_not_equals: Optional[
            Union[List[StringNotEquals], core.ArrayOut[StringNotEquals]]
        ] = core.arg(default=None)

        string_not_like: Optional[
            Union[List[StringNotLike], core.ArrayOut[StringNotLike]]
        ] = core.arg(default=None)


@core.schema
class SelectionTag(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SelectionTag.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_backup_selection", namespace="aws_backup")
class Selection(core.Resource):

    condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = core.attr(
        Condition, default=None, computed=True, kind=core.Kind.array
    )

    iam_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    plan_id: Union[str, core.StringOut] = core.attr(str)

    resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    selection_tag: Optional[Union[List[SelectionTag], core.ArrayOut[SelectionTag]]] = core.attr(
        SelectionTag, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        iam_role_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        plan_id: Union[str, core.StringOut],
        condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = None,
        not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        selection_tag: Optional[Union[List[SelectionTag], core.ArrayOut[SelectionTag]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Selection.Args(
                iam_role_arn=iam_role_arn,
                name=name,
                plan_id=plan_id,
                condition=condition,
                not_resources=not_resources,
                resources=resources,
                selection_tag=selection_tag,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = core.arg(
            default=None
        )

        iam_role_arn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        plan_id: Union[str, core.StringOut] = core.arg()

        resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        selection_tag: Optional[Union[List[SelectionTag], core.ArrayOut[SelectionTag]]] = core.arg(
            default=None
        )
