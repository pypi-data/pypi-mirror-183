from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EventFilter(core.Schema):

    source: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EventFilter.Args(
                source=source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_appintegrations_event_integration", namespace="aws_appintegrations")
class EventIntegration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_filter: EventFilter = core.attr(EventFilter)

    eventbridge_bus: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

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
        event_filter: EventFilter,
        eventbridge_bus: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventIntegration.Args(
                event_filter=event_filter,
                eventbridge_bus=eventbridge_bus,
                name=name,
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
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_filter: EventFilter = core.arg()

        eventbridge_bus: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
