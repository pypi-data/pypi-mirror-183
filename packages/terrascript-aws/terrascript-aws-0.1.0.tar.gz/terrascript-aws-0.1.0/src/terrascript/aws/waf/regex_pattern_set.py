from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_waf_regex_pattern_set", namespace="aws_waf")
class RegexPatternSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    regex_pattern_strings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        regex_pattern_strings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RegexPatternSet.Args(
                name=name,
                regex_pattern_strings=regex_pattern_strings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        regex_pattern_strings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
