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
class RegexMatchTuple(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    regex_pattern_set_id: Union[str, core.StringOut] = core.attr(str)

    text_transformation: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        regex_pattern_set_id: Union[str, core.StringOut],
        text_transformation: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RegexMatchTuple.Args(
                field_to_match=field_to_match,
                regex_pattern_set_id=regex_pattern_set_id,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        regex_pattern_set_id: Union[str, core.StringOut] = core.arg()

        text_transformation: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_regex_match_set", namespace="aws_wafregional")
class RegexMatchSet(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    regex_match_tuple: Optional[
        Union[List[RegexMatchTuple], core.ArrayOut[RegexMatchTuple]]
    ] = core.attr(RegexMatchTuple, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        regex_match_tuple: Optional[
            Union[List[RegexMatchTuple], core.ArrayOut[RegexMatchTuple]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegexMatchSet.Args(
                name=name,
                regex_match_tuple=regex_match_tuple,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        regex_match_tuple: Optional[
            Union[List[RegexMatchTuple], core.ArrayOut[RegexMatchTuple]]
        ] = core.arg(default=None)
