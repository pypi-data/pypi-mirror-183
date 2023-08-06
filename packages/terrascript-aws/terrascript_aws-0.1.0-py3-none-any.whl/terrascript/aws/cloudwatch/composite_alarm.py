from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_composite_alarm", namespace="aws_cloudwatch")
class CompositeAlarm(core.Resource):

    actions_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    alarm_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    alarm_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    alarm_name: Union[str, core.StringOut] = core.attr(str)

    alarm_rule: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    insufficient_data_actions: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

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
        alarm_name: Union[str, core.StringOut],
        alarm_rule: Union[str, core.StringOut],
        actions_enabled: Optional[Union[bool, core.BoolOut]] = None,
        alarm_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        alarm_description: Optional[Union[str, core.StringOut]] = None,
        insufficient_data_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CompositeAlarm.Args(
                alarm_name=alarm_name,
                alarm_rule=alarm_rule,
                actions_enabled=actions_enabled,
                alarm_actions=alarm_actions,
                alarm_description=alarm_description,
                insufficient_data_actions=insufficient_data_actions,
                ok_actions=ok_actions,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        actions_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        alarm_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        alarm_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        alarm_name: Union[str, core.StringOut] = core.arg()

        alarm_rule: Union[str, core.StringOut] = core.arg()

        insufficient_data_actions: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
