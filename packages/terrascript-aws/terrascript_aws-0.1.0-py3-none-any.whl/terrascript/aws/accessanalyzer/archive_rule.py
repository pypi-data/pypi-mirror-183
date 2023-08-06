from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    contains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    criteria: Union[str, core.StringOut] = core.attr(str)

    eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    exists: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criteria: Union[str, core.StringOut],
        contains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        exists: Optional[Union[str, core.StringOut]] = None,
        neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                criteria=criteria,
                contains=contains,
                eq=eq,
                exists=exists,
                neq=neq,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        criteria: Union[str, core.StringOut] = core.arg()

        eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        exists: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.resource(type="aws_accessanalyzer_archive_rule", namespace="aws_accessanalyzer")
class ArchiveRule(core.Resource):

    analyzer_name: Union[str, core.StringOut] = core.attr(str)

    filter: Union[List[Filter], core.ArrayOut[Filter]] = core.attr(Filter, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        analyzer_name: Union[str, core.StringOut],
        filter: Union[List[Filter], core.ArrayOut[Filter]],
        rule_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ArchiveRule.Args(
                analyzer_name=analyzer_name,
                filter=filter,
                rule_name=rule_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        analyzer_name: Union[str, core.StringOut] = core.arg()

        filter: Union[List[Filter], core.ArrayOut[Filter]] = core.arg()

        rule_name: Union[str, core.StringOut] = core.arg()
