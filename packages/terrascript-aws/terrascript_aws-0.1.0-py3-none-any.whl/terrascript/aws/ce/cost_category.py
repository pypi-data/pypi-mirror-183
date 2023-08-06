from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InheritedValue(core.Schema):

    dimension_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dimension_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        dimension_key: Optional[Union[str, core.StringOut]] = None,
        dimension_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InheritedValue.Args(
                dimension_key=dimension_key,
                dimension_name=dimension_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dimension_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CostCategoryBlk(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=CostCategoryBlk.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Dimension(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Dimension.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Tags(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Tags.Args(
                key=key,
                match_options=match_options,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        match_options: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class And(core.Schema):

    cost_category: Optional[CostCategoryBlk] = core.attr(CostCategoryBlk, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[Tags] = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategoryBlk] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[Tags] = None,
    ):
        super().__init__(
            args=And.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: Optional[CostCategoryBlk] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[Tags] = core.arg(default=None)


@core.schema
class Not(core.Schema):

    cost_category: Optional[CostCategoryBlk] = core.attr(CostCategoryBlk, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[Tags] = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategoryBlk] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[Tags] = None,
    ):
        super().__init__(
            args=Not.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: Optional[CostCategoryBlk] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[Tags] = core.arg(default=None)


@core.schema
class Or(core.Schema):

    cost_category: Optional[CostCategoryBlk] = core.attr(CostCategoryBlk, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[Tags] = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategoryBlk] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[Tags] = None,
    ):
        super().__init__(
            args=Or.Args(
                cost_category=cost_category,
                dimension=dimension,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category: Optional[CostCategoryBlk] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[Tags] = core.arg(default=None)


@core.schema
class RuleRule(core.Schema):

    and_: Optional[Union[List[And], core.ArrayOut[And]]] = core.attr(
        And, default=None, kind=core.Kind.array, alias="and"
    )

    cost_category: Optional[CostCategoryBlk] = core.attr(CostCategoryBlk, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    not_: Optional[Not] = core.attr(Not, default=None, alias="not")

    or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = core.attr(
        Or, default=None, kind=core.Kind.array, alias="or"
    )

    tags: Optional[Tags] = core.attr(Tags, default=None)

    def __init__(
        self,
        *,
        and_: Optional[Union[List[And], core.ArrayOut[And]]] = None,
        cost_category: Optional[CostCategoryBlk] = None,
        dimension: Optional[Dimension] = None,
        not_: Optional[Not] = None,
        or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = None,
        tags: Optional[Tags] = None,
    ):
        super().__init__(
            args=RuleRule.Args(
                and_=and_,
                cost_category=cost_category,
                dimension=dimension,
                not_=not_,
                or_=or_,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[Union[List[And], core.ArrayOut[And]]] = core.arg(default=None)

        cost_category: Optional[CostCategoryBlk] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        not_: Optional[Not] = core.arg(default=None)

        or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = core.arg(default=None)

        tags: Optional[Tags] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    inherited_value: Optional[InheritedValue] = core.attr(InheritedValue, default=None)

    rule: Optional[RuleRule] = core.attr(RuleRule, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        inherited_value: Optional[InheritedValue] = None,
        rule: Optional[RuleRule] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                inherited_value=inherited_value,
                rule=rule,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inherited_value: Optional[InheritedValue] = core.arg(default=None)

        rule: Optional[RuleRule] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Parameter(core.Schema):

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        type: Optional[Union[str, core.StringOut]] = None,
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Parameter.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class SplitChargeRule(core.Schema):

    method: Union[str, core.StringOut] = core.attr(str)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    source: Union[str, core.StringOut] = core.attr(str)

    targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        method: Union[str, core.StringOut],
        source: Union[str, core.StringOut],
        targets: Union[List[str], core.ArrayOut[core.StringOut]],
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
    ):
        super().__init__(
            args=SplitChargeRule.Args(
                method=method,
                source=source,
                targets=targets,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        method: Union[str, core.StringOut] = core.arg()

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        source: Union[str, core.StringOut] = core.arg()

        targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_ce_cost_category", namespace="aws_ce")
class CostCategory(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    effective_end: Union[str, core.StringOut] = core.attr(str, computed=True)

    effective_start: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    rule_version: Union[str, core.StringOut] = core.attr(str)

    split_charge_rule: Optional[
        Union[List[SplitChargeRule], core.ArrayOut[SplitChargeRule]]
    ] = core.attr(SplitChargeRule, default=None, kind=core.Kind.array)

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
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        rule_version: Union[str, core.StringOut],
        default_value: Optional[Union[str, core.StringOut]] = None,
        split_charge_rule: Optional[
            Union[List[SplitChargeRule], core.ArrayOut[SplitChargeRule]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CostCategory.Args(
                name=name,
                rule=rule,
                rule_version=rule_version,
                default_value=default_value,
                split_charge_rule=split_charge_rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()

        rule_version: Union[str, core.StringOut] = core.arg()

        split_charge_rule: Optional[
            Union[List[SplitChargeRule], core.ArrayOut[SplitChargeRule]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
