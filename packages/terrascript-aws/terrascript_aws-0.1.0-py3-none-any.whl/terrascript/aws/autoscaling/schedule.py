from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_autoscaling_schedule", namespace="aws_autoscaling")
class Schedule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    autoscaling_group_name: Union[str, core.StringOut] = core.attr(str)

    desired_capacity: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    end_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    min_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    recurrence: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    scheduled_action_name: Union[str, core.StringOut] = core.attr(str)

    start_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    time_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: Union[str, core.StringOut],
        scheduled_action_name: Union[str, core.StringOut],
        desired_capacity: Optional[Union[int, core.IntOut]] = None,
        end_time: Optional[Union[str, core.StringOut]] = None,
        max_size: Optional[Union[int, core.IntOut]] = None,
        min_size: Optional[Union[int, core.IntOut]] = None,
        recurrence: Optional[Union[str, core.StringOut]] = None,
        start_time: Optional[Union[str, core.StringOut]] = None,
        time_zone: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Schedule.Args(
                autoscaling_group_name=autoscaling_group_name,
                scheduled_action_name=scheduled_action_name,
                desired_capacity=desired_capacity,
                end_time=end_time,
                max_size=max_size,
                min_size=min_size,
                recurrence=recurrence,
                start_time=start_time,
                time_zone=time_zone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: Union[str, core.StringOut] = core.arg()

        desired_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        end_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        recurrence: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scheduled_action_name: Union[str, core.StringOut] = core.arg()

        start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        time_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)
