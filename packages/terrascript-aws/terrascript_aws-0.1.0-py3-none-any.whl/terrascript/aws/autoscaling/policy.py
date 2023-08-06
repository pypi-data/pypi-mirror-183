from typing import List, Optional, Union

import terrascript.core as core


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
class MetricDimension(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MetricDimension.Args(
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

    metric_dimension: Optional[
        Union[List[MetricDimension], core.ArrayOut[MetricDimension]]
    ] = core.attr(MetricDimension, default=None, kind=core.Kind.array)

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
        metric_dimension: Optional[
            Union[List[MetricDimension], core.ArrayOut[MetricDimension]]
        ] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CustomizedMetricSpecification.Args(
                metric_name=metric_name,
                namespace=namespace,
                statistic=statistic,
                metric_dimension=metric_dimension,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_dimension: Optional[
            Union[List[MetricDimension], core.ArrayOut[MetricDimension]]
        ] = core.arg(default=None)

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        statistic: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetTrackingConfiguration(core.Schema):

    customized_metric_specification: Optional[CustomizedMetricSpecification] = core.attr(
        CustomizedMetricSpecification, default=None
    )

    disable_scale_in: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    predefined_metric_specification: Optional[PredefinedMetricSpecification] = core.attr(
        PredefinedMetricSpecification, default=None
    )

    target_value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        target_value: Union[float, core.FloatOut],
        customized_metric_specification: Optional[CustomizedMetricSpecification] = None,
        disable_scale_in: Optional[Union[bool, core.BoolOut]] = None,
        predefined_metric_specification: Optional[PredefinedMetricSpecification] = None,
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
                customized_metric_specification=customized_metric_specification,
                disable_scale_in=disable_scale_in,
                predefined_metric_specification=predefined_metric_specification,
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

        target_value: Union[float, core.FloatOut] = core.arg()


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
class Metric(core.Schema):

    dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = core.attr(
        Dimensions, default=None, kind=core.Kind.array
    )

    metric_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = None,
    ):
        super().__init__(
            args=Metric.Args(
                metric_name=metric_name,
                namespace=namespace,
                dimensions=dimensions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: Optional[Union[List[Dimensions], core.ArrayOut[Dimensions]]] = core.arg(
            default=None
        )

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()


@core.schema
class MetricStat(core.Schema):

    metric: Metric = core.attr(Metric)

    stat: Union[str, core.StringOut] = core.attr(str)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric: Metric,
        stat: Union[str, core.StringOut],
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MetricStat.Args(
                metric=metric,
                stat=stat,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric: Metric = core.arg()

        stat: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MetricDataQueries(core.Schema):

    expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str)

    label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric_stat: Optional[MetricStat] = core.attr(MetricStat, default=None)

    return_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        expression: Optional[Union[str, core.StringOut]] = None,
        label: Optional[Union[str, core.StringOut]] = None,
        metric_stat: Optional[MetricStat] = None,
        return_data: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=MetricDataQueries.Args(
                id=id,
                expression=expression,
                label=label,
                metric_stat=metric_stat,
                return_data=return_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        label: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_stat: Optional[MetricStat] = core.arg(default=None)

        return_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class CustomizedCapacityMetricSpecification(core.Schema):

    metric_data_queries: Union[
        List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
    ] = core.attr(MetricDataQueries, kind=core.Kind.array)

    def __init__(
        self,
        *,
        metric_data_queries: Union[List[MetricDataQueries], core.ArrayOut[MetricDataQueries]],
    ):
        super().__init__(
            args=CustomizedCapacityMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: Union[
            List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
        ] = core.arg()


@core.schema
class CustomizedLoadMetricSpecification(core.Schema):

    metric_data_queries: Union[
        List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
    ] = core.attr(MetricDataQueries, kind=core.Kind.array)

    def __init__(
        self,
        *,
        metric_data_queries: Union[List[MetricDataQueries], core.ArrayOut[MetricDataQueries]],
    ):
        super().__init__(
            args=CustomizedLoadMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: Union[
            List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
        ] = core.arg()


@core.schema
class CustomizedScalingMetricSpecification(core.Schema):

    metric_data_queries: Union[
        List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
    ] = core.attr(MetricDataQueries, kind=core.Kind.array)

    def __init__(
        self,
        *,
        metric_data_queries: Union[List[MetricDataQueries], core.ArrayOut[MetricDataQueries]],
    ):
        super().__init__(
            args=CustomizedScalingMetricSpecification.Args(
                metric_data_queries=metric_data_queries,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_data_queries: Union[
            List[MetricDataQueries], core.ArrayOut[MetricDataQueries]
        ] = core.arg()


@core.schema
class PredefinedLoadMetricSpecification(core.Schema):

    predefined_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: Union[str, core.StringOut],
        resource_label: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PredefinedLoadMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Union[str, core.StringOut] = core.arg()


@core.schema
class PredefinedMetricPairSpecification(core.Schema):

    predefined_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: Union[str, core.StringOut],
        resource_label: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PredefinedMetricPairSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Union[str, core.StringOut] = core.arg()


@core.schema
class PredefinedScalingMetricSpecification(core.Schema):

    predefined_metric_type: Union[str, core.StringOut] = core.attr(str)

    resource_label: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        predefined_metric_type: Union[str, core.StringOut],
        resource_label: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PredefinedScalingMetricSpecification.Args(
                predefined_metric_type=predefined_metric_type,
                resource_label=resource_label,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        predefined_metric_type: Union[str, core.StringOut] = core.arg()

        resource_label: Union[str, core.StringOut] = core.arg()


@core.schema
class MetricSpecification(core.Schema):

    customized_capacity_metric_specification: Optional[
        CustomizedCapacityMetricSpecification
    ] = core.attr(CustomizedCapacityMetricSpecification, default=None)

    customized_load_metric_specification: Optional[CustomizedLoadMetricSpecification] = core.attr(
        CustomizedLoadMetricSpecification, default=None
    )

    customized_scaling_metric_specification: Optional[
        CustomizedScalingMetricSpecification
    ] = core.attr(CustomizedScalingMetricSpecification, default=None)

    predefined_load_metric_specification: Optional[PredefinedLoadMetricSpecification] = core.attr(
        PredefinedLoadMetricSpecification, default=None
    )

    predefined_metric_pair_specification: Optional[PredefinedMetricPairSpecification] = core.attr(
        PredefinedMetricPairSpecification, default=None
    )

    predefined_scaling_metric_specification: Optional[
        PredefinedScalingMetricSpecification
    ] = core.attr(PredefinedScalingMetricSpecification, default=None)

    target_value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        target_value: Union[int, core.IntOut],
        customized_capacity_metric_specification: Optional[
            CustomizedCapacityMetricSpecification
        ] = None,
        customized_load_metric_specification: Optional[CustomizedLoadMetricSpecification] = None,
        customized_scaling_metric_specification: Optional[
            CustomizedScalingMetricSpecification
        ] = None,
        predefined_load_metric_specification: Optional[PredefinedLoadMetricSpecification] = None,
        predefined_metric_pair_specification: Optional[PredefinedMetricPairSpecification] = None,
        predefined_scaling_metric_specification: Optional[
            PredefinedScalingMetricSpecification
        ] = None,
    ):
        super().__init__(
            args=MetricSpecification.Args(
                target_value=target_value,
                customized_capacity_metric_specification=customized_capacity_metric_specification,
                customized_load_metric_specification=customized_load_metric_specification,
                customized_scaling_metric_specification=customized_scaling_metric_specification,
                predefined_load_metric_specification=predefined_load_metric_specification,
                predefined_metric_pair_specification=predefined_metric_pair_specification,
                predefined_scaling_metric_specification=predefined_scaling_metric_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        customized_capacity_metric_specification: Optional[
            CustomizedCapacityMetricSpecification
        ] = core.arg(default=None)

        customized_load_metric_specification: Optional[
            CustomizedLoadMetricSpecification
        ] = core.arg(default=None)

        customized_scaling_metric_specification: Optional[
            CustomizedScalingMetricSpecification
        ] = core.arg(default=None)

        predefined_load_metric_specification: Optional[
            PredefinedLoadMetricSpecification
        ] = core.arg(default=None)

        predefined_metric_pair_specification: Optional[
            PredefinedMetricPairSpecification
        ] = core.arg(default=None)

        predefined_scaling_metric_specification: Optional[
            PredefinedScalingMetricSpecification
        ] = core.arg(default=None)

        target_value: Union[int, core.IntOut] = core.arg()


@core.schema
class PredictiveScalingConfiguration(core.Schema):

    max_capacity_breach_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    max_capacity_buffer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric_specification: MetricSpecification = core.attr(MetricSpecification)

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    scheduling_buffer_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_specification: MetricSpecification,
        max_capacity_breach_behavior: Optional[Union[str, core.StringOut]] = None,
        max_capacity_buffer: Optional[Union[str, core.StringOut]] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
        scheduling_buffer_time: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PredictiveScalingConfiguration.Args(
                metric_specification=metric_specification,
                max_capacity_breach_behavior=max_capacity_breach_behavior,
                max_capacity_buffer=max_capacity_buffer,
                mode=mode,
                scheduling_buffer_time=scheduling_buffer_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity_breach_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_capacity_buffer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_specification: MetricSpecification = core.arg()

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scheduling_buffer_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_autoscaling_policy", namespace="aws_autoscaling")
class Policy(core.Resource):

    adjustment_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    autoscaling_group_name: Union[str, core.StringOut] = core.attr(str)

    cooldown: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metric_aggregation_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    policy_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    predictive_scaling_configuration: Optional[PredictiveScalingConfiguration] = core.attr(
        PredictiveScalingConfiguration, default=None
    )

    scaling_adjustment: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    step_adjustment: Optional[
        Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
    ] = core.attr(StepAdjustment, default=None, kind=core.Kind.array)

    target_tracking_configuration: Optional[TargetTrackingConfiguration] = core.attr(
        TargetTrackingConfiguration, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        adjustment_type: Optional[Union[str, core.StringOut]] = None,
        cooldown: Optional[Union[int, core.IntOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = None,
        metric_aggregation_type: Optional[Union[str, core.StringOut]] = None,
        min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = None,
        policy_type: Optional[Union[str, core.StringOut]] = None,
        predictive_scaling_configuration: Optional[PredictiveScalingConfiguration] = None,
        scaling_adjustment: Optional[Union[int, core.IntOut]] = None,
        step_adjustment: Optional[
            Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
        ] = None,
        target_tracking_configuration: Optional[TargetTrackingConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Policy.Args(
                autoscaling_group_name=autoscaling_group_name,
                name=name,
                adjustment_type=adjustment_type,
                cooldown=cooldown,
                enabled=enabled,
                estimated_instance_warmup=estimated_instance_warmup,
                metric_aggregation_type=metric_aggregation_type,
                min_adjustment_magnitude=min_adjustment_magnitude,
                policy_type=policy_type,
                predictive_scaling_configuration=predictive_scaling_configuration,
                scaling_adjustment=scaling_adjustment,
                step_adjustment=step_adjustment,
                target_tracking_configuration=target_tracking_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        adjustment_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        autoscaling_group_name: Union[str, core.StringOut] = core.arg()

        cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        metric_aggregation_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_adjustment_magnitude: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        policy_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        predictive_scaling_configuration: Optional[PredictiveScalingConfiguration] = core.arg(
            default=None
        )

        scaling_adjustment: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        step_adjustment: Optional[
            Union[List[StepAdjustment], core.ArrayOut[StepAdjustment]]
        ] = core.arg(default=None)

        target_tracking_configuration: Optional[TargetTrackingConfiguration] = core.arg(
            default=None
        )
