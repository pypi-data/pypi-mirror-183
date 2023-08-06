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
class ByteMatchTuples(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    positional_constraint: Union[str, core.StringOut] = core.attr(str)

    target_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    text_transformation: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        positional_constraint: Union[str, core.StringOut],
        text_transformation: Union[str, core.StringOut],
        target_string: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ByteMatchTuples.Args(
                field_to_match=field_to_match,
                positional_constraint=positional_constraint,
                text_transformation=text_transformation,
                target_string=target_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        positional_constraint: Union[str, core.StringOut] = core.arg()

        target_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        text_transformation: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_byte_match_set", namespace="aws_wafregional")
class ByteMatchSet(core.Resource):

    byte_match_tuples: Optional[
        Union[List[ByteMatchTuples], core.ArrayOut[ByteMatchTuples]]
    ] = core.attr(ByteMatchTuples, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        byte_match_tuples: Optional[
            Union[List[ByteMatchTuples], core.ArrayOut[ByteMatchTuples]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ByteMatchSet.Args(
                name=name,
                byte_match_tuples=byte_match_tuples,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        byte_match_tuples: Optional[
            Union[List[ByteMatchTuples], core.ArrayOut[ByteMatchTuples]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
