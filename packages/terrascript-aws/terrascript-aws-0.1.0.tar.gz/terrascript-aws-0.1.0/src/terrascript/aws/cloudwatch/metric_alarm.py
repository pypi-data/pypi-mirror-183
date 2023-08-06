from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Metric(core.Schema):

    dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    metric_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    period: Union[int, core.IntOut] = core.attr(int)

    stat: Union[str, core.StringOut] = core.attr(str)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        period: Union[int, core.IntOut],
        stat: Union[str, core.StringOut],
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        namespace: Optional[Union[str, core.StringOut]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Metric.Args(
                metric_name=metric_name,
                period=period,
                stat=stat,
                dimensions=dimensions,
                namespace=namespace,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        period: Union[int, core.IntOut] = core.arg()

        stat: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MetricQuery(core.Schema):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str)

    label: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric: Optional[Metric] = core.attr(Metric, default=None)

    return_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        expression: Optional[Union[str, core.StringOut]] = None,
        label: Optional[Union[str, core.StringOut]] = None,
        metric: Optional[Metric] = None,
        return_data: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=MetricQuery.Args(
                id=id,
                account_id=account_id,
                expression=expression,
                label=label,
                metric=metric,
                return_data=return_data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        label: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric: Optional[Metric] = core.arg(default=None)

        return_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_cloudwatch_metric_alarm", namespace="aws_cloudwatch")
class MetricAlarm(core.Resource):

    actions_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    alarm_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    alarm_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    alarm_name: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    comparison_operator: Union[str, core.StringOut] = core.attr(str)

    datapoints_to_alarm: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    evaluate_low_sample_count_percentiles: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    evaluation_periods: Union[int, core.IntOut] = core.attr(int)

    extended_statistic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    insufficient_data_actions: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    metric_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric_query: Optional[Union[List[MetricQuery], core.ArrayOut[MetricQuery]]] = core.attr(
        MetricQuery, default=None, kind=core.Kind.array
    )

    namespace: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    statistic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    threshold: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    threshold_metric_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    treat_missing_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        alarm_name: Union[str, core.StringOut],
        comparison_operator: Union[str, core.StringOut],
        evaluation_periods: Union[int, core.IntOut],
        actions_enabled: Optional[Union[bool, core.BoolOut]] = None,
        alarm_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        alarm_description: Optional[Union[str, core.StringOut]] = None,
        datapoints_to_alarm: Optional[Union[int, core.IntOut]] = None,
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        evaluate_low_sample_count_percentiles: Optional[Union[str, core.StringOut]] = None,
        extended_statistic: Optional[Union[str, core.StringOut]] = None,
        insufficient_data_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        metric_name: Optional[Union[str, core.StringOut]] = None,
        metric_query: Optional[Union[List[MetricQuery], core.ArrayOut[MetricQuery]]] = None,
        namespace: Optional[Union[str, core.StringOut]] = None,
        ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        period: Optional[Union[int, core.IntOut]] = None,
        statistic: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        threshold: Optional[Union[float, core.FloatOut]] = None,
        threshold_metric_id: Optional[Union[str, core.StringOut]] = None,
        treat_missing_data: Optional[Union[str, core.StringOut]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MetricAlarm.Args(
                alarm_name=alarm_name,
                comparison_operator=comparison_operator,
                evaluation_periods=evaluation_periods,
                actions_enabled=actions_enabled,
                alarm_actions=alarm_actions,
                alarm_description=alarm_description,
                datapoints_to_alarm=datapoints_to_alarm,
                dimensions=dimensions,
                evaluate_low_sample_count_percentiles=evaluate_low_sample_count_percentiles,
                extended_statistic=extended_statistic,
                insufficient_data_actions=insufficient_data_actions,
                metric_name=metric_name,
                metric_query=metric_query,
                namespace=namespace,
                ok_actions=ok_actions,
                period=period,
                statistic=statistic,
                tags=tags,
                tags_all=tags_all,
                threshold=threshold,
                threshold_metric_id=threshold_metric_id,
                treat_missing_data=treat_missing_data,
                unit=unit,
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

        comparison_operator: Union[str, core.StringOut] = core.arg()

        datapoints_to_alarm: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        evaluate_low_sample_count_percentiles: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        evaluation_periods: Union[int, core.IntOut] = core.arg()

        extended_statistic: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        insufficient_data_actions: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        metric_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_query: Optional[Union[List[MetricQuery], core.ArrayOut[MetricQuery]]] = core.arg(
            default=None
        )

        namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ok_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        statistic: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        threshold: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        threshold_metric_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        treat_missing_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)
