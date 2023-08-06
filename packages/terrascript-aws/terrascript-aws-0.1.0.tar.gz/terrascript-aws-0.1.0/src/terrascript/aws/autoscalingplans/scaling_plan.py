from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TagFilter(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=TagFilter.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class ApplicationSource(core.Schema):

    cloudformation_stack_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = core.attr(
        TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cloudformation_stack_arn: Optional[Union[str, core.StringOut]] = None,
        tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = None,
    ):
        super().__init__(
            args=ApplicationSource.Args(
                cloudformation_stack_arn=cloudformation_stack_arn,
                tag_filter=tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudformation_stack_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_filter: Optional[Union[List[TagFilter], core.ArrayOut[TagFilter]]] = core.arg(
            default=None
        )


@core.schema
class PredefinedLoadMetricSpecification(core.Schema):

    predefined_load_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_load_metric_type: Union[str, core.StringOut],
        resource_label: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PredefinedLoadMetricSpecification.Args(
                predefined_load_metric_type=predefined_load_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_load_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CustomizedScalingMetricSpecification(core.Schema):

    dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    statistic: Union[str, core.StringOut] = core.attr(str)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        statistic: Union[str, core.StringOut],
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomizedScalingMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        statistic: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PredefinedScalingMetricSpecification(core.Schema):

    predefined_scaling_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_scaling_metric_type: Union[str, core.StringOut],
        resource_label: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PredefinedScalingMetricSpecification.Args(
                predefined_scaling_metric_type=predefined_scaling_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_scaling_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetTrackingConfiguration(core.Schema):

    customized_scaling_metric_specification: Optional[
        CustomizedScalingMetricSpecification
    ] = core.attr(CustomizedScalingMetricSpecification, default=None)

    disable_scale_in: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    predefined_scaling_metric_specification: Optional[
        PredefinedScalingMetricSpecification
    ] = core.attr(PredefinedScalingMetricSpecification, default=None)

    scale_in_cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    scale_out_cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        target_value: Union[float, core.FloatOut],
        customized_scaling_metric_specification: Optional[
            CustomizedScalingMetricSpecification
        ] = None,
        disable_scale_in: Optional[Union[bool, core.BoolOut]] = None,
        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = None,
        predefined_scaling_metric_specification: Optional[
            PredefinedScalingMetricSpecification
        ] = None,
        scale_in_cooldown: Optional[Union[int, core.IntOut]] = None,
        scale_out_cooldown: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
                customized_scaling_metric_specification=customized_scaling_metric_specification,
                disable_scale_in=disable_scale_in,
                estimated_instance_warmup=estimated_instance_warmup,
                predefined_scaling_metric_specification=predefined_scaling_metric_specification,
                scale_in_cooldown=scale_in_cooldown,
                scale_out_cooldown=scale_out_cooldown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_scaling_metric_specification: Optional[
            CustomizedScalingMetricSpecification
        ] = core.arg(default=None)

        disable_scale_in: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        predefined_scaling_metric_specification: Optional[
            PredefinedScalingMetricSpecification
        ] = core.arg(default=None)

        scale_in_cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        scale_out_cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_value: Union[float, core.FloatOut] = core.arg()


@core.schema
class CustomizedLoadMetricSpecification(core.Schema):

    dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    statistic: Union[str, core.StringOut] = core.attr(str)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        statistic: Union[str, core.StringOut],
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomizedLoadMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        statistic: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ScalingInstruction(core.Schema):

    customized_load_metric_specification: Optional[CustomizedLoadMetricSpecification] = core.attr(
        CustomizedLoadMetricSpecification, default=None
    )

    disable_dynamic_scaling: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    max_capacity: Union[int, core.IntOut] = core.attr(int)

    min_capacity: Union[int, core.IntOut] = core.attr(int)

    predefined_load_metric_specification: Optional[PredefinedLoadMetricSpecification] = core.attr(
        PredefinedLoadMetricSpecification, default=None
    )

    predictive_scaling_max_capacity_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    predictive_scaling_max_capacity_buffer: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    predictive_scaling_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    scalable_dimension: Union[str, core.StringOut] = core.attr(str)

    scaling_policy_update_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    scheduled_action_buffer_time: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    service_namespace: Union[str, core.StringOut] = core.attr(str)

    target_tracking_configuration: Union[
        List[TargetTrackingConfiguration], core.ArrayOut[TargetTrackingConfiguration]
    ] = core.attr(TargetTrackingConfiguration, kind=core.Kind.array)

    def __init__(
        self,
        *,
        max_capacity: Union[int, core.IntOut],
        min_capacity: Union[int, core.IntOut],
        resource_id: Union[str, core.StringOut],
        scalable_dimension: Union[str, core.StringOut],
        service_namespace: Union[str, core.StringOut],
        target_tracking_configuration: Union[
            List[TargetTrackingConfiguration], core.ArrayOut[TargetTrackingConfiguration]
        ],
        customized_load_metric_specification: Optional[CustomizedLoadMetricSpecification] = None,
        disable_dynamic_scaling: Optional[Union[bool, core.BoolOut]] = None,
        predefined_load_metric_specification: Optional[PredefinedLoadMetricSpecification] = None,
        predictive_scaling_max_capacity_behavior: Optional[Union[str, core.StringOut]] = None,
        predictive_scaling_max_capacity_buffer: Optional[Union[int, core.IntOut]] = None,
        predictive_scaling_mode: Optional[Union[str, core.StringOut]] = None,
        scaling_policy_update_behavior: Optional[Union[str, core.StringOut]] = None,
        scheduled_action_buffer_time: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ScalingInstruction.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                service_namespace=service_namespace,
                target_tracking_configuration=target_tracking_configuration,
                customized_load_metric_specification=customized_load_metric_specification,
                disable_dynamic_scaling=disable_dynamic_scaling,
                predefined_load_metric_specification=predefined_load_metric_specification,
                predictive_scaling_max_capacity_behavior=predictive_scaling_max_capacity_behavior,
                predictive_scaling_max_capacity_buffer=predictive_scaling_max_capacity_buffer,
                predictive_scaling_mode=predictive_scaling_mode,
                scaling_policy_update_behavior=scaling_policy_update_behavior,
                scheduled_action_buffer_time=scheduled_action_buffer_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_load_metric_specification: Optional[
            CustomizedLoadMetricSpecification
        ] = core.arg(default=None)

        disable_dynamic_scaling: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_capacity: Union[int, core.IntOut] = core.arg()

        min_capacity: Union[int, core.IntOut] = core.arg()

        predefined_load_metric_specification: Optional[
            PredefinedLoadMetricSpecification
        ] = core.arg(default=None)

        predictive_scaling_max_capacity_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        predictive_scaling_max_capacity_buffer: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        predictive_scaling_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_id: Union[str, core.StringOut] = core.arg()

        scalable_dimension: Union[str, core.StringOut] = core.arg()

        scaling_policy_update_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        scheduled_action_buffer_time: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        service_namespace: Union[str, core.StringOut] = core.arg()

        target_tracking_configuration: Union[
            List[TargetTrackingConfiguration], core.ArrayOut[TargetTrackingConfiguration]
        ] = core.arg()


@core.resource(type="aws_autoscalingplans_scaling_plan", namespace="aws_autoscalingplans")
class ScalingPlan(core.Resource):

    application_source: ApplicationSource = core.attr(ApplicationSource)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    scaling_instruction: Union[
        List[ScalingInstruction], core.ArrayOut[ScalingInstruction]
    ] = core.attr(ScalingInstruction, kind=core.Kind.array)

    scaling_plan_version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_source: ApplicationSource,
        name: Union[str, core.StringOut],
        scaling_instruction: Union[List[ScalingInstruction], core.ArrayOut[ScalingInstruction]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ScalingPlan.Args(
                application_source=application_source,
                name=name,
                scaling_instruction=scaling_instruction,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_source: ApplicationSource = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        scaling_instruction: Union[
            List[ScalingInstruction], core.ArrayOut[ScalingInstruction]
        ] = core.arg()
