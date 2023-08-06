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
class XssMatchTuple(core.Schema):

    field_to_match: FieldToMatch = core.attr(FieldToMatch)

    text_transformation: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        field_to_match: FieldToMatch,
        text_transformation: Union[str, core.StringOut],
    ):
        super().__init__(
            args=XssMatchTuple.Args(
                field_to_match=field_to_match,
                text_transformation=text_transformation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: FieldToMatch = core.arg()

        text_transformation: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafregional_xss_match_set", namespace="aws_wafregional")
class XssMatchSet(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    xss_match_tuple: Optional[Union[List[XssMatchTuple], core.ArrayOut[XssMatchTuple]]] = core.attr(
        XssMatchTuple, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        xss_match_tuple: Optional[Union[List[XssMatchTuple], core.ArrayOut[XssMatchTuple]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=XssMatchSet.Args(
                name=name,
                xss_match_tuple=xss_match_tuple,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        xss_match_tuple: Optional[
            Union[List[XssMatchTuple], core.ArrayOut[XssMatchTuple]]
        ] = core.arg(default=None)
