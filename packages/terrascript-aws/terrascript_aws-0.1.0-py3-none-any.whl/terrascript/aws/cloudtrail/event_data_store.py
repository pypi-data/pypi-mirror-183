from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class FieldSelector(core.Schema):

    ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    not_ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    not_starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        field: Optional[Union[str, core.StringOut]] = None,
        not_ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=FieldSelector.Args(
                ends_with=ends_with,
                equals=equals,
                field=field,
                not_ends_with=not_ends_with,
                not_equals=not_equals,
                not_starts_with=not_starts_with,
                starts_with=starts_with,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        not_ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        not_starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class AdvancedEventSelector(core.Schema):

    field_selector: Optional[Union[List[FieldSelector], core.ArrayOut[FieldSelector]]] = core.attr(
        FieldSelector, default=None, computed=True, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        field_selector: Optional[Union[List[FieldSelector], core.ArrayOut[FieldSelector]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AdvancedEventSelector.Args(
                field_selector=field_selector,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_selector: Optional[
            Union[List[FieldSelector], core.ArrayOut[FieldSelector]]
        ] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_cloudtrail_event_data_store", namespace="aws_cloudtrail")
class EventDataStore(core.Resource):

    advanced_event_selector: Optional[
        Union[List[AdvancedEventSelector], core.ArrayOut[AdvancedEventSelector]]
    ] = core.attr(AdvancedEventSelector, default=None, computed=True, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    multi_region_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    organization_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    termination_protection_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        advanced_event_selector: Optional[
            Union[List[AdvancedEventSelector], core.ArrayOut[AdvancedEventSelector]]
        ] = None,
        multi_region_enabled: Optional[Union[bool, core.BoolOut]] = None,
        organization_enabled: Optional[Union[bool, core.BoolOut]] = None,
        retention_period: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        termination_protection_enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventDataStore.Args(
                name=name,
                advanced_event_selector=advanced_event_selector,
                multi_region_enabled=multi_region_enabled,
                organization_enabled=organization_enabled,
                retention_period=retention_period,
                tags=tags,
                tags_all=tags_all,
                termination_protection_enabled=termination_protection_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        advanced_event_selector: Optional[
            Union[List[AdvancedEventSelector], core.ArrayOut[AdvancedEventSelector]]
        ] = core.arg(default=None)

        multi_region_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        organization_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        termination_protection_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
