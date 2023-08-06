from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class NotificationProperty(core.Schema):

    notify_delay_after: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        notify_delay_after: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NotificationProperty.Args(
                notify_delay_after=notify_delay_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notify_delay_after: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Actions(core.Schema):

    arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    crawler_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    job_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_property: Optional[NotificationProperty] = core.attr(
        NotificationProperty, default=None
    )

    security_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        crawler_name: Optional[Union[str, core.StringOut]] = None,
        job_name: Optional[Union[str, core.StringOut]] = None,
        notification_property: Optional[NotificationProperty] = None,
        security_configuration: Optional[Union[str, core.StringOut]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Actions.Args(
                arguments=arguments,
                crawler_name=crawler_name,
                job_name=job_name,
                notification_property=notification_property,
                security_configuration=security_configuration,
                timeout=timeout,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        crawler_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        job_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_property: Optional[NotificationProperty] = core.arg(default=None)

        security_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Conditions(core.Schema):

    crawl_state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    crawler_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    job_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    logical_operator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        crawl_state: Optional[Union[str, core.StringOut]] = None,
        crawler_name: Optional[Union[str, core.StringOut]] = None,
        job_name: Optional[Union[str, core.StringOut]] = None,
        logical_operator: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Conditions.Args(
                crawl_state=crawl_state,
                crawler_name=crawler_name,
                job_name=job_name,
                logical_operator=logical_operator,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crawl_state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        crawler_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        job_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logical_operator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Predicate(core.Schema):

    conditions: Union[List[Conditions], core.ArrayOut[Conditions]] = core.attr(
        Conditions, kind=core.Kind.array
    )

    logical: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        conditions: Union[List[Conditions], core.ArrayOut[Conditions]],
        logical: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Predicate.Args(
                conditions=conditions,
                logical=logical,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        conditions: Union[List[Conditions], core.ArrayOut[Conditions]] = core.arg()

        logical: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EventBatchingCondition(core.Schema):

    batch_size: Union[int, core.IntOut] = core.attr(int)

    batch_window: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        batch_size: Union[int, core.IntOut],
        batch_window: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EventBatchingCondition.Args(
                batch_size=batch_size,
                batch_window=batch_window,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        batch_size: Union[int, core.IntOut] = core.arg()

        batch_window: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_glue_trigger", namespace="aws_glue")
class Trigger(core.Resource):

    actions: Union[List[Actions], core.ArrayOut[Actions]] = core.attr(Actions, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    event_batching_condition: Optional[
        Union[List[EventBatchingCondition], core.ArrayOut[EventBatchingCondition]]
    ] = core.attr(EventBatchingCondition, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    predicate: Optional[Predicate] = core.attr(Predicate, default=None)

    schedule: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start_on_creation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    workflow_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        actions: Union[List[Actions], core.ArrayOut[Actions]],
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        event_batching_condition: Optional[
            Union[List[EventBatchingCondition], core.ArrayOut[EventBatchingCondition]]
        ] = None,
        predicate: Optional[Predicate] = None,
        schedule: Optional[Union[str, core.StringOut]] = None,
        start_on_creation: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        workflow_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Trigger.Args(
                actions=actions,
                name=name,
                type=type,
                description=description,
                enabled=enabled,
                event_batching_condition=event_batching_condition,
                predicate=predicate,
                schedule=schedule,
                start_on_creation=start_on_creation,
                tags=tags,
                tags_all=tags_all,
                workflow_name=workflow_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions: Union[List[Actions], core.ArrayOut[Actions]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        event_batching_condition: Optional[
            Union[List[EventBatchingCondition], core.ArrayOut[EventBatchingCondition]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        predicate: Optional[Predicate] = core.arg(default=None)

        schedule: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start_on_creation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()

        workflow_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
