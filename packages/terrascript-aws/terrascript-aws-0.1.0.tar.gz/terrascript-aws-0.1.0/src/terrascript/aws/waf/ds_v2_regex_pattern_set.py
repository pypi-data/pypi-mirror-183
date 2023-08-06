from typing import List, Union

import terrascript.core as core


@core.schema
class RegularExpression(core.Schema):

    regex_string: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_wafv2_regex_pattern_set", namespace="aws_waf")
class DsV2RegexPatternSet(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    regular_expression: Union[
        List[RegularExpression], core.ArrayOut[RegularExpression]
    ] = core.attr(RegularExpression, computed=True, kind=core.Kind.array)

    scope: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        scope: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsV2RegexPatternSet.Args(
                name=name,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        scope: Union[str, core.StringOut] = core.arg()
