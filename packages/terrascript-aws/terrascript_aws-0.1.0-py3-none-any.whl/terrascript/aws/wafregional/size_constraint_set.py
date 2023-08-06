from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class FieldToMatch(core.Schema):

    data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        data: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                type=type,
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class SizeConstraints(core.Schema):

    comparison_operator: Union[str, core.StringOut] = core.attr(str)

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    size: Union[int, core.IntOut] = core.attr(int)

    text_transformation: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        comparison_operator: Union[str, core.StringOut],
        field_to_match: FieldToMatch,
        size: Union[int, core.IntOut],
        text_transformation: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SizeConstraints.Args(
                comparison_operator=comparison_operator,
                field_to_match=field_to_match,
                size=size,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comparison_operator: Union[str, core.StringOut] = core.arg()

        field_to_match: FieldToMatch = core.arg()

        size: Union[int, core.IntOut] = core.arg()

        text_transformation: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_size_constraint_set", namespace="aws_wafregional")
class SizeConstraintSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    size_constraints: Optional[
        Union[List[SizeConstraints], core.ArrayOut[SizeConstraints]]
    ] = core.attr(SizeConstraints, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        size_constraints: Optional[
            Union[List[SizeConstraints], core.ArrayOut[SizeConstraints]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SizeConstraintSet.Args(
                name=name,
                size_constraints=size_constraints,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        size_constraints: Optional[
            Union[List[SizeConstraints], core.ArrayOut[SizeConstraints]]
        ] = core.arg(default=None)
