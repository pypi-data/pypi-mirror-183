from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SortBy(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sort_order: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        sort_order: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SortBy.Args(
                key=key,
                sort_order=sort_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sort_order: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TimePeriod(core.Schema):

    end: Union[str, core.StringOut] = core.attr(str)

    start: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        end: Union[str, core.StringOut],
        start: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TimePeriod.Args(
                end=end,
                start=start,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        end: Union[str, core.StringOut] = core.arg()

        start: Union[str, core.StringOut] = core.arg()


@core.schema
class TagsBlk(core.Schema):

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
            args=TagsBlk.Args(
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
class CostCategory(core.Schema):

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
            args=CostCategory.Args(
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
class And(core.Schema):

    cost_category: Optional[CostCategory] = core.attr(CostCategory, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[TagsBlk] = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategory] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[TagsBlk] = None,
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
        cost_category: Optional[CostCategory] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[TagsBlk] = core.arg(default=None)


@core.schema
class Not(core.Schema):

    cost_category: Optional[CostCategory] = core.attr(CostCategory, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[TagsBlk] = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategory] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[TagsBlk] = None,
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
        cost_category: Optional[CostCategory] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[TagsBlk] = core.arg(default=None)


@core.schema
class Or(core.Schema):

    cost_category: Optional[CostCategory] = core.attr(CostCategory, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    tags: Optional[TagsBlk] = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        cost_category: Optional[CostCategory] = None,
        dimension: Optional[Dimension] = None,
        tags: Optional[TagsBlk] = None,
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
        cost_category: Optional[CostCategory] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        tags: Optional[TagsBlk] = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    and_: Optional[Union[List[And], core.ArrayOut[And]]] = core.attr(
        And, default=None, kind=core.Kind.array, alias="and"
    )

    cost_category: Optional[CostCategory] = core.attr(CostCategory, default=None)

    dimension: Optional[Dimension] = core.attr(Dimension, default=None)

    not_: Optional[Not] = core.attr(Not, default=None, alias="not")

    or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = core.attr(
        Or, default=None, kind=core.Kind.array, alias="or"
    )

    tags: Optional[TagsBlk] = core.attr(TagsBlk, default=None)

    def __init__(
        self,
        *,
        and_: Optional[Union[List[And], core.ArrayOut[And]]] = None,
        cost_category: Optional[CostCategory] = None,
        dimension: Optional[Dimension] = None,
        not_: Optional[Not] = None,
        or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = None,
        tags: Optional[TagsBlk] = None,
    ):
        super().__init__(
            args=Filter.Args(
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

        cost_category: Optional[CostCategory] = core.arg(default=None)

        dimension: Optional[Dimension] = core.arg(default=None)

        not_: Optional[Not] = core.arg(default=None)

        or_: Optional[Union[List[Or], core.ArrayOut[Or]]] = core.arg(default=None)

        tags: Optional[TagsBlk] = core.arg(default=None)


@core.data(type="aws_ce_tags", namespace="aws_ce")
class DsTags(core.Data):

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    search_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sort_by: Optional[Union[List[SortBy], core.ArrayOut[SortBy]]] = core.attr(
        SortBy, default=None, kind=core.Kind.array
    )

    tag_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    time_period: TimePeriod = core.attr(TimePeriod)

    def __init__(
        self,
        data_name: str,
        *,
        time_period: TimePeriod,
        filter: Optional[Filter] = None,
        search_string: Optional[Union[str, core.StringOut]] = None,
        sort_by: Optional[Union[List[SortBy], core.ArrayOut[SortBy]]] = None,
        tag_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTags.Args(
                time_period=time_period,
                filter=filter,
                search_string=search_string,
                sort_by=sort_by,
                tag_key=tag_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Filter] = core.arg(default=None)

        search_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sort_by: Optional[Union[List[SortBy], core.ArrayOut[SortBy]]] = core.arg(default=None)

        tag_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        time_period: TimePeriod = core.arg()
