from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OnFailure(core.Schema):

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnFailure.Args(
                destination_arn=destination_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationConfig(core.Schema):

    on_failure: Optional[OnFailure] = core.attr(OnFailure, default=None)

    def __init__(
        self,
        *,
        on_failure: Optional[OnFailure] = None,
    ):
        super().__init__(
            args=DestinationConfig.Args(
                on_failure=on_failure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_failure: Optional[OnFailure] = core.arg(default=None)


@core.schema
class SelfManagedEventSource(core.Schema):

    endpoints: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        endpoints: Union[Dict[str, str], core.MapOut[core.StringOut]],
    ):
        super().__init__(
            args=SelfManagedEventSource.Args(
                endpoints=endpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoints: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()


@core.schema
class SourceAccessConfiguration(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceAccessConfiguration.Args(
                type=type,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        uri: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        pattern: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                pattern=pattern,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FilterCriteria(core.Schema):

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
    ):
        super().__init__(
            args=FilterCriteria.Args(
                filter=filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)


@core.resource(type="aws_lambda_event_source_mapping", namespace="aws_lambda")
class EventSourceMapping(core.Resource):

    batch_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    bisect_batch_on_function_error: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    destination_config: Optional[DestinationConfig] = core.attr(DestinationConfig, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    event_source_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_criteria: Optional[FilterCriteria] = core.attr(FilterCriteria, default=None)

    function_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_response_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_processing_result: Union[str, core.StringOut] = core.attr(str, computed=True)

    maximum_batching_window_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    maximum_record_age_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    parallelization_factor: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    queues: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_managed_event_source: Optional[SelfManagedEventSource] = core.attr(
        SelfManagedEventSource, default=None
    )

    source_access_configuration: Optional[
        Union[List[SourceAccessConfiguration], core.ArrayOut[SourceAccessConfiguration]]
    ] = core.attr(SourceAccessConfiguration, default=None, kind=core.Kind.array)

    starting_position: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    starting_position_timestamp: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    state_transition_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    topics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tumbling_window_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    uuid: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        batch_size: Optional[Union[int, core.IntOut]] = None,
        bisect_batch_on_function_error: Optional[Union[bool, core.BoolOut]] = None,
        destination_config: Optional[DestinationConfig] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        event_source_arn: Optional[Union[str, core.StringOut]] = None,
        filter_criteria: Optional[FilterCriteria] = None,
        function_response_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        maximum_batching_window_in_seconds: Optional[Union[int, core.IntOut]] = None,
        maximum_record_age_in_seconds: Optional[Union[int, core.IntOut]] = None,
        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = None,
        parallelization_factor: Optional[Union[int, core.IntOut]] = None,
        queues: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_managed_event_source: Optional[SelfManagedEventSource] = None,
        source_access_configuration: Optional[
            Union[List[SourceAccessConfiguration], core.ArrayOut[SourceAccessConfiguration]]
        ] = None,
        starting_position: Optional[Union[str, core.StringOut]] = None,
        starting_position_timestamp: Optional[Union[str, core.StringOut]] = None,
        topics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tumbling_window_in_seconds: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventSourceMapping.Args(
                function_name=function_name,
                batch_size=batch_size,
                bisect_batch_on_function_error=bisect_batch_on_function_error,
                destination_config=destination_config,
                enabled=enabled,
                event_source_arn=event_source_arn,
                filter_criteria=filter_criteria,
                function_response_types=function_response_types,
                maximum_batching_window_in_seconds=maximum_batching_window_in_seconds,
                maximum_record_age_in_seconds=maximum_record_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
                parallelization_factor=parallelization_factor,
                queues=queues,
                self_managed_event_source=self_managed_event_source,
                source_access_configuration=source_access_configuration,
                starting_position=starting_position,
                starting_position_timestamp=starting_position_timestamp,
                topics=topics,
                tumbling_window_in_seconds=tumbling_window_in_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        batch_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        bisect_batch_on_function_error: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        destination_config: Optional[DestinationConfig] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        event_source_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_criteria: Optional[FilterCriteria] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        function_response_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        maximum_batching_window_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        maximum_record_age_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parallelization_factor: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        queues: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        self_managed_event_source: Optional[SelfManagedEventSource] = core.arg(default=None)

        source_access_configuration: Optional[
            Union[List[SourceAccessConfiguration], core.ArrayOut[SourceAccessConfiguration]]
        ] = core.arg(default=None)

        starting_position: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        starting_position_timestamp: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        tumbling_window_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
