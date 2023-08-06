from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_rule", namespace="aws_eventbridge")
class CloudwatchEventRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_bus_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedule_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        description: Optional[Union[str, core.StringOut]] = None,
        event_bus_name: Optional[Union[str, core.StringOut]] = None,
        event_pattern: Optional[Union[str, core.StringOut]] = None,
        is_enabled: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        schedule_expression: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventRule.Args(
                description=description,
                event_bus_name=event_bus_name,
                event_pattern=event_pattern,
                is_enabled=is_enabled,
                name=name,
                name_prefix=name_prefix,
                role_arn=role_arn,
                schedule_expression=schedule_expression,
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

        event_bus_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        is_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedule_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
