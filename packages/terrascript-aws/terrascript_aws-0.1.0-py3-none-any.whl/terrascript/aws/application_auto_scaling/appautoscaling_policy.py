from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class StepAdjustment(core.Schema):

    metric_interval_lower_bound: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric_interval_upper_bound: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    scaling_adjustment: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        scaling_adjustment: Union[int, core.IntOut],
        metric_interval_lower_bound: Optional[Union[str, core.StringOut]] = None,
        metric_interval_upper_bound: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StepAdjustment.Args(
                scaling_adjustment=scaling_adjustment,
                metric_interval_lower_bound=metric_interval_lower_bound,
                metric_interval_upper_bound=metric_interval_upper_bound,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_interval_lower_bound: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_interval_upper_bound: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scaling_adjustment: Union[int, core.IntOut] = core.arg()


@core.schema
class StepScalingPolicyConfiguration(core.Schema):

    adjustment_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    metric_aggregation_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    step_adjustment: Optional[
        Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
    ] = core.attr(StepAdjustment, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        adjustment_type: Optional[Union[str, core.StringOut]] = None,
        cooldown: Optional[Union[int, core.IntOut]] = None,
        metric_aggregation_type: Optional[Union[str, core.StringOut]] = None,
        min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = None,
        step_adjustment: Optional[
            Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
        ] = None,
    ):
        super().__init__(
            args=StepScalingPolicyConfiguration.Args(
                adjustment_type=adjustment_type,
                cooldown=cooldown,
                metric_aggregation_type=metric_aggregation_type,
                min_adjustment_magnitude=min_adjustment_magnitude,
                step_adjustment=step_adjustment,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        adjustment_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        metric_aggregation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        step_adjustment: Optional[
            Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
        ] = core.arg(default=None)


@core.schema
class Dimensions(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Dimensions.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CustomizedMetricSpecification(core.Schema):

    dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = core.attr(
        Dimensions, default=None, kind=core.Kind.array
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
        dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomizedMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = core.arg(
            default=None
        )

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        statistic: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PredefinedMetricSpecification(core.Schema):

    predefined_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        predefined_metric_type: Union[str, core.StringOut],
        resource_label: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PredefinedMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetTrackingScalingPolicyConfiguration(core.Schema):

    customized_metric_specification: Optional[CustomizedMetricSpecification] = core.attr(
        CustomizedMetricSpecification, default=None
    )

    disable_scale_in: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    predefined_metric_specification: Optional[PredefinedMetricSpecification] = core.attr(
        PredefinedMetricSpecification, default=None
    )

    scale_in_cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    scale_out_cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        target_value: Union[float, core.FloatOut],
        customized_metric_specification: Optional[CustomizedMetricSpecification] = None,
        disable_scale_in: Optional[Union[bool, core.BoolOut]] = None,
        predefined_metric_specification: Optional[PredefinedMetricSpecification] = None,
        scale_in_cooldown: Optional[Union[int, core.IntOut]] = None,
        scale_out_cooldown: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TargetTrackingScalingPolicyConfiguration.Args(
                target_value=target_value,
                customized_metric_specification=customized_metric_specification,
                disable_scale_in=disable_scale_in,
                predefined_metric_specification=predefined_metric_specification,
                scale_in_cooldown=scale_in_cooldown,
                scale_out_cooldown=scale_out_cooldown,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_metric_specification: Optional[CustomizedMetricSpecification] = core.arg(
            default=None
        )

        disable_scale_in: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        predefined_metric_specification: Optional[PredefinedMetricSpecification] = core.arg(
            default=None
        )

        scale_in_cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        scale_out_cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_value: Union[float, core.FloatOut] = core.arg()


@core.resource(type="aws_appautoscaling_policy", namespace="aws_application_auto_scaling")
class AppautoscalingPolicy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    policy_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    scalable_dimension: Union[str, core.StringOut] = core.attr(str)

    service_namespace: Union[str, core.StringOut] = core.attr(str)

    step_scaling_policy_configuration: Optional[StepScalingPolicyConfiguration] = core.attr(
        StepScalingPolicyConfiguration, default=None
    )

    target_tracking_scaling_policy_configuration: Optional[
        TargetTrackingScalingPolicyConfiguration
    ] = core.attr(TargetTrackingScalingPolicyConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        scalable_dimension: Union[str, core.StringOut],
        service_namespace: Union[str, core.StringOut],
        policy_type: Optional[Union[str, core.StringOut]] = None,
        step_scaling_policy_configuration: Optional[StepScalingPolicyConfiguration] = None,
        target_tracking_scaling_policy_configuration: Optional[
            TargetTrackingScalingPolicyConfiguration
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppautoscalingPolicy.Args(
                name=name,
                resource_id=resource_id,
                scalable_dimension=scalable_dimension,
                service_namespace=service_namespace,
                policy_type=policy_type,
                step_scaling_policy_configuration=step_scaling_policy_configuration,
                target_tracking_scaling_policy_configuration=target_tracking_scaling_policy_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        policy_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_id: Union[str, core.StringOut] = core.arg()

        scalable_dimension: Union[str, core.StringOut] = core.arg()

        service_namespace: Union[str, core.StringOut] = core.arg()

        step_scaling_policy_configuration: Optional[StepScalingPolicyConfiguration] = core.arg(
            default=None
        )

        target_tracking_scaling_policy_configuration: Optional[
            TargetTrackingScalingPolicyConfiguration
        ] = core.arg(default=None)
