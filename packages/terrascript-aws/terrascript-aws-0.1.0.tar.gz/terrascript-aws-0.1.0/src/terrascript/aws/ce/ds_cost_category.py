from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Dimension(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        match_options: Union[List[str], core.ArrayOut[core.StringOut]],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
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
        key: Union[str, core.StringOut] = core.arg()

        match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CostCategoryBlk(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        match_options: Union[List[str], core.ArrayOut[core.StringOut]],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
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
        key: Union[str, core.StringOut] = core.arg()

        match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Tags(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        match_options: Union[List[str], core.ArrayOut[core.StringOut]],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
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
        key: Union[str, core.StringOut] = core.arg()

        match_options: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Not(core.Schema):

    cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: Union[List[Tags], core.ArrayOut[Tags]] = core.attr(
        Tags, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]],
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
        tags: Union[List[Tags], core.ArrayOut[Tags]],
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
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.arg()

        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()

        tags: Union[List[Tags], core.ArrayOut[Tags]] = core.arg()


@core.schema
class Or(core.Schema):

    cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: Union[List[Tags], core.ArrayOut[Tags]] = core.attr(
        Tags, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]],
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
        tags: Union[List[Tags], core.ArrayOut[Tags]],
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
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.arg()

        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()

        tags: Union[List[Tags], core.ArrayOut[Tags]] = core.arg()


@core.schema
class And(core.Schema):

    cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    tags: Union[List[Tags], core.ArrayOut[Tags]] = core.attr(
        Tags, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]],
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
        tags: Union[List[Tags], core.ArrayOut[Tags]],
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
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.arg()

        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()

        tags: Union[List[Tags], core.ArrayOut[Tags]] = core.arg()


@core.schema
class RuleRule(core.Schema):

    and_: Union[List[And], core.ArrayOut[And]] = core.attr(
        And, computed=True, kind=core.Kind.array, alias="and"
    )

    cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.attr(
        CostCategoryBlk, computed=True, kind=core.Kind.array
    )

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, computed=True, kind=core.Kind.array
    )

    not_: Union[List[Not], core.ArrayOut[Not]] = core.attr(
        Not, computed=True, kind=core.Kind.array, alias="not"
    )

    or_: Union[List[Or], core.ArrayOut[Or]] = core.attr(
        Or, computed=True, kind=core.Kind.array, alias="or"
    )

    tags: Union[List[Tags], core.ArrayOut[Tags]] = core.attr(
        Tags, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        and_: Union[List[And], core.ArrayOut[And]],
        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]],
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
        not_: Union[List[Not], core.ArrayOut[Not]],
        or_: Union[List[Or], core.ArrayOut[Or]],
        tags: Union[List[Tags], core.ArrayOut[Tags]],
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
        and_: Union[List[And], core.ArrayOut[And]] = core.arg()

        cost_category: Union[List[CostCategoryBlk], core.ArrayOut[CostCategoryBlk]] = core.arg()

        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()

        not_: Union[List[Not], core.ArrayOut[Not]] = core.arg()

        or_: Union[List[Or], core.ArrayOut[Or]] = core.arg()

        tags: Union[List[Tags], core.ArrayOut[Tags]] = core.arg()


@core.schema
class InheritedValue(core.Schema):

    dimension_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    dimension_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        dimension_key: Union[str, core.StringOut],
        dimension_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InheritedValue.Args(
                dimension_key=dimension_key,
                dimension_name=dimension_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension_key: Union[str, core.StringOut] = core.arg()

        dimension_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Rule(core.Schema):

    inherited_value: Union[List[InheritedValue], core.ArrayOut[InheritedValue]] = core.attr(
        InheritedValue, computed=True, kind=core.Kind.array
    )

    rule: Union[List[RuleRule], core.ArrayOut[RuleRule]] = core.attr(
        RuleRule, computed=True, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        inherited_value: Union[List[InheritedValue], core.ArrayOut[InheritedValue]],
        rule: Union[List[RuleRule], core.ArrayOut[RuleRule]],
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
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
        inherited_value: Union[List[InheritedValue], core.ArrayOut[InheritedValue]] = core.arg()

        rule: Union[List[RuleRule], core.ArrayOut[RuleRule]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Parameter(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Parameter.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class SplitChargeRule(core.Schema):

    method: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter: Union[List[Parameter], core.ArrayOut[Parameter]] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    source: Union[str, core.StringOut] = core.attr(str, computed=True)

    targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        method: Union[str, core.StringOut],
        parameter: Union[List[Parameter], core.ArrayOut[Parameter]],
        source: Union[str, core.StringOut],
        targets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=SplitChargeRule.Args(
                method=method,
                parameter=parameter,
                source=source,
                targets=targets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        method: Union[str, core.StringOut] = core.arg()

        parameter: Union[List[Parameter], core.ArrayOut[Parameter]] = core.arg()

        source: Union[str, core.StringOut] = core.arg()

        targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_ce_cost_category", namespace="aws_ce")
class DsCostCategory(core.Data):

    cost_category_arn: Union[str, core.StringOut] = core.attr(str)

    effective_end: Union[str, core.StringOut] = core.attr(str, computed=True)

    effective_start: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(
        Rule, computed=True, kind=core.Kind.array
    )

    rule_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    split_charge_rule: Union[List[SplitChargeRule], core.ArrayOut[SplitChargeRule]] = core.attr(
        SplitChargeRule, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cost_category_arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCostCategory.Args(
                cost_category_arn=cost_category_arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cost_category_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
