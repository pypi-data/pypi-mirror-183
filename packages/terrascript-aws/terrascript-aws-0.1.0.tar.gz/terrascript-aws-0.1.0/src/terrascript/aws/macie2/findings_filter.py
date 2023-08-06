from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Criterion(core.Schema):

    eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    eq_exact_match: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: Union[str, core.StringOut] = core.attr(str)

    gt: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lt: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lte: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: Union[str, core.StringOut],
        eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        eq_exact_match: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        gt: Optional[Union[str, core.StringOut]] = None,
        gte: Optional[Union[str, core.StringOut]] = None,
        lt: Optional[Union[str, core.StringOut]] = None,
        lte: Optional[Union[str, core.StringOut]] = None,
        neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Criterion.Args(
                field=field,
                eq=eq,
                eq_exact_match=eq_exact_match,
                gt=gt,
                gte=gte,
                lt=lt,
                lte=lte,
                neq=neq,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        eq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        eq_exact_match: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        field: Union[str, core.StringOut] = core.arg()

        gt: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lt: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lte: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        neq: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class FindingCriteria(core.Schema):

    criterion: Optional[Union[List[Criterion], core.ArrayOut[Criterion]]] = core.attr(
        Criterion, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criterion: Optional[Union[List[Criterion], core.ArrayOut[Criterion]]] = None,
    ):
        super().__init__(
            args=FindingCriteria.Args(
                criterion=criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        criterion: Optional[Union[List[Criterion], core.ArrayOut[Criterion]]] = core.arg(
            default=None
        )


@core.resource(type="aws_macie2_findings_filter", namespace="aws_macie2")
class FindingsFilter(core.Resource):

    action: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    finding_criteria: FindingCriteria = core.attr(FindingCriteria)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    position: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

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
        action: Union[str, core.StringOut],
        finding_criteria: FindingCriteria,
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        position: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FindingsFilter.Args(
                action=action,
                finding_criteria=finding_criteria,
                description=description,
                name=name,
                name_prefix=name_prefix,
                position=position,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        finding_criteria: FindingCriteria = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        position: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
