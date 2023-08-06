from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Criterion(core.Schema):

    equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: Union[str, core.StringOut] = core.attr(str)

    greater_than: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    greater_than_or_equal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    less_than: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    less_than_or_equal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: Union[str, core.StringOut],
        equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        greater_than: Optional[Union[str, core.StringOut]] = None,
        greater_than_or_equal: Optional[Union[str, core.StringOut]] = None,
        less_than: Optional[Union[str, core.StringOut]] = None,
        less_than_or_equal: Optional[Union[str, core.StringOut]] = None,
        not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Criterion.Args(
                field=field,
                equals=equals,
                greater_than=greater_than,
                greater_than_or_equal=greater_than_or_equal,
                less_than=less_than,
                less_than_or_equal=less_than_or_equal,
                not_equals=not_equals,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        field: Union[str, core.StringOut] = core.arg()

        greater_than: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        greater_than_or_equal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        less_than: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        less_than_or_equal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class FindingCriteria(core.Schema):

    criterion: Union[List[Criterion], core.ArrayOut[Criterion]] = core.attr(
        Criterion, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        criterion: Union[List[Criterion], core.ArrayOut[Criterion]],
    ):
        super().__init__(
            args=FindingCriteria.Args(
                criterion=criterion,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        criterion: Union[List[Criterion], core.ArrayOut[Criterion]] = core.arg()


@core.resource(type="aws_guardduty_filter", namespace="aws_guardduty")
class Filter(core.Resource):

    action: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    detector_id: Union[str, core.StringOut] = core.attr(str)

    finding_criteria: FindingCriteria = core.attr(FindingCriteria)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rank: Union[int, core.IntOut] = core.attr(int)

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
        detector_id: Union[str, core.StringOut],
        finding_criteria: FindingCriteria,
        name: Union[str, core.StringOut],
        rank: Union[int, core.IntOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Filter.Args(
                action=action,
                detector_id=detector_id,
                finding_criteria=finding_criteria,
                name=name,
                rank=rank,
                description=description,
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

        detector_id: Union[str, core.StringOut] = core.arg()

        finding_criteria: FindingCriteria = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        rank: Union[int, core.IntOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
