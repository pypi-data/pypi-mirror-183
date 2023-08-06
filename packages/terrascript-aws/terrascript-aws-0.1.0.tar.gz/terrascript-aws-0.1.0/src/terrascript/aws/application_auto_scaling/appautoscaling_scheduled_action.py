from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ScalableTargetAction(core.Schema):

    max_capacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_capacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_capacity: Optional[Union[str, core.StringOut]] = None,
        min_capacity: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScalableTargetAction.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_capacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_appautoscaling_scheduled_action", namespace="aws_application_auto_scaling")
class AppautoscalingScheduledAction(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    end_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    scalable_dimension: Union[str, core.StringOut] = core.attr(str)

    scalable_target_action: ScalableTargetAction = core.attr(ScalableTargetAction)

    schedule: Union[str, core.StringOut] = core.attr(str)

    service_namespace: Union[str, core.StringOut] = core.attr(str)

    start_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timezone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        scalable_dimension: Union[str, core.StringOut],
        scalable_target_action: ScalableTargetAction,
        schedule: Union[str, core.StringOut],
        service_namespace: Union[str, core.StringOut],
        end_time: Optional[Union[str, core.StringOut]] = None,
        start_time: Optional[Union[str, core.StringOut]] = None,
        timezone: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppautoscalingScheduledAction.Args(
                name=name,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                scalable_target_action=scalable_target_action,
                schedule=schedule,
                service_namespace=service_namespace,
                end_time=end_time,
                start_time=start_time,
                timezone=timezone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        end_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()

        scalable_dimension: Union[str, core.StringOut] = core.arg()

        scalable_target_action: ScalableTargetAction = core.arg()

        schedule: Union[str, core.StringOut] = core.arg()

        service_namespace: Union[str, core.StringOut] = core.arg()

        start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timezone: Optional[Union[str, core.StringOut]] = core.arg(default=None)
