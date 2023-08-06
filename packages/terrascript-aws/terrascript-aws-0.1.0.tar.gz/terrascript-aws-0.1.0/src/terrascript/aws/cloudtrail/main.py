from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DataResource(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=DataResource.Args(
                type=type,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class EventSelector(core.Schema):

    data_resource: Optional[Union[List[DataResource], core.ArrayOut[DataResource]]] = core.attr(
        DataResource, default=None, kind=core.Kind.array
    )

    exclude_management_event_sources: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    include_management_events: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    read_write_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        data_resource: Optional[Union[List[DataResource], core.ArrayOut[DataResource]]] = None,
        exclude_management_event_sources: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        include_management_events: Optional[Union[bool, core.BoolOut]] = None,
        read_write_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EventSelector.Args(
                data_resource=data_resource,
                exclude_management_event_sources=exclude_management_event_sources,
                include_management_events=include_management_events,
                read_write_type=read_write_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_resource: Optional[Union[List[DataResource], core.ArrayOut[DataResource]]] = core.arg(
            default=None
        )

        exclude_management_event_sources: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        include_management_events: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        read_write_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FieldSelector(core.Schema):

    ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    field: Union[str, core.StringOut] = core.attr(str)

    not_ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field: Union[str, core.StringOut],
        ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_ends_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_equals: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        starts_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=FieldSelector.Args(
                field=field,
                ends_with=ends_with,
                equals=equals,
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

        field: Union[str, core.StringOut] = core.arg()

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

    field_selector: Union[List[FieldSelector], core.ArrayOut[FieldSelector]] = core.attr(
        FieldSelector, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        field_selector: Union[List[FieldSelector], core.ArrayOut[FieldSelector]],
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
        field_selector: Union[List[FieldSelector], core.ArrayOut[FieldSelector]] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InsightSelector(core.Schema):

    insight_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        insight_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InsightSelector.Args(
                insight_type=insight_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insight_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudtrail", namespace="aws_cloudtrail")
class Main(core.Resource):

    advanced_event_selector: Optional[
        Union[List[AdvancedEventSelector], core.ArrayOut[AdvancedEventSelector]]
    ] = core.attr(AdvancedEventSelector, default=None, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloud_watch_logs_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cloud_watch_logs_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_log_file_validation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_logging: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    event_selector: Optional[Union[List[EventSelector], core.ArrayOut[EventSelector]]] = core.attr(
        EventSelector, default=None, kind=core.Kind.array
    )

    home_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_global_service_events: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    insight_selector: Optional[
        Union[List[InsightSelector], core.ArrayOut[InsightSelector]]
    ] = core.attr(InsightSelector, default=None, kind=core.Kind.array)

    is_multi_region_trail: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    is_organization_trail: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sns_topic_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        s3_bucket_name: Union[str, core.StringOut],
        advanced_event_selector: Optional[
            Union[List[AdvancedEventSelector], core.ArrayOut[AdvancedEventSelector]]
        ] = None,
        cloud_watch_logs_group_arn: Optional[Union[str, core.StringOut]] = None,
        cloud_watch_logs_role_arn: Optional[Union[str, core.StringOut]] = None,
        enable_log_file_validation: Optional[Union[bool, core.BoolOut]] = None,
        enable_logging: Optional[Union[bool, core.BoolOut]] = None,
        event_selector: Optional[Union[List[EventSelector], core.ArrayOut[EventSelector]]] = None,
        include_global_service_events: Optional[Union[bool, core.BoolOut]] = None,
        insight_selector: Optional[
            Union[List[InsightSelector], core.ArrayOut[InsightSelector]]
        ] = None,
        is_multi_region_trail: Optional[Union[bool, core.BoolOut]] = None,
        is_organization_trail: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
        sns_topic_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Main.Args(
                name=name,
                s3_bucket_name=s3_bucket_name,
                advanced_event_selector=advanced_event_selector,
                cloud_watch_logs_group_arn=cloud_watch_logs_group_arn,
                cloud_watch_logs_role_arn=cloud_watch_logs_role_arn,
                enable_log_file_validation=enable_log_file_validation,
                enable_logging=enable_logging,
                event_selector=event_selector,
                include_global_service_events=include_global_service_events,
                insight_selector=insight_selector,
                is_multi_region_trail=is_multi_region_trail,
                is_organization_trail=is_organization_trail,
                kms_key_id=kms_key_id,
                s3_key_prefix=s3_key_prefix,
                sns_topic_name=sns_topic_name,
                tags=tags,
                tags_all=tags_all,
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

        cloud_watch_logs_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloud_watch_logs_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_log_file_validation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_logging: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        event_selector: Optional[
            Union[List[EventSelector], core.ArrayOut[EventSelector]]
        ] = core.arg(default=None)

        include_global_service_events: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        insight_selector: Optional[
            Union[List[InsightSelector], core.ArrayOut[InsightSelector]]
        ] = core.arg(default=None)

        is_multi_region_trail: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        is_organization_trail: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sns_topic_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
