from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RegularExpression(core.Schema):

    regex_string: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        regex_string: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RegularExpression.Args(
                regex_string=regex_string,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        regex_string: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_wafv2_regex_pattern_set", namespace="aws_waf")
class V2RegexPatternSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lock_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    regular_expression: Optional[
        Union[List[RegularExpression], core.ArrayOut[RegularExpression]]
    ] = core.attr(RegularExpression, default=None, kind=core.Kind.array)

    scope: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        regular_expression: Optional[
            Union[List[RegularExpression], core.ArrayOut[RegularExpression]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=V2RegexPatternSet.Args(
                name=name,
                scope=scope,
                description=description,
                regular_expression=regular_expression,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        regular_expression: Optional[
            Union[List[RegularExpression], core.ArrayOut[RegularExpression]]
        ] = core.arg(default=None)

        scope: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
