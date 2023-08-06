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
class SqlInjectionMatchTuple(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    text_transformation: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        text_transformation: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SqlInjectionMatchTuple.Args(
                field_to_match=field_to_match,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        text_transformation: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_sql_injection_match_set", namespace="aws_wafregional")
class SqlInjectionMatchSet(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    sql_injection_match_tuple: Optional[
        Union[List[SqlInjectionMatchTuple], core.ArrayOut[SqlInjectionMatchTuple]]
    ] = core.attr(SqlInjectionMatchTuple, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        sql_injection_match_tuple: Optional[
            Union[List[SqlInjectionMatchTuple], core.ArrayOut[SqlInjectionMatchTuple]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SqlInjectionMatchSet.Args(
                name=name,
                sql_injection_match_tuple=sql_injection_match_tuple,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        sql_injection_match_tuple: Optional[
            Union[List[SqlInjectionMatchTuple], core.ArrayOut[SqlInjectionMatchTuple]]
        ] = core.arg(default=None)
