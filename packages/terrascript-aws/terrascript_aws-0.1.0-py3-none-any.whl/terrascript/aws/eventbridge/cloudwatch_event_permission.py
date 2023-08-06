from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Condition(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Condition.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudwatch_event_permission", namespace="aws_eventbridge")
class CloudwatchEventPermission(core.Resource):

    action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    condition: Optional[Condition] = core.attr(Condition, default=None)

    event_bus_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    statement_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal: Union[str, core.StringOut],
        statement_id: Union[str, core.StringOut],
        action: Optional[Union[str, core.StringOut]] = None,
        condition: Optional[Condition] = None,
        event_bus_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventPermission.Args(
                principal=principal,
                statement_id=statement_id,
                action=action,
                condition=condition,
                event_bus_name=event_bus_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        condition: Optional[Condition] = core.arg(default=None)

        event_bus_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        principal: Union[str, core.StringOut] = core.arg()

        statement_id: Union[str, core.StringOut] = core.arg()
