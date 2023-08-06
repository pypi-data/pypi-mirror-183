from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class MetricTransformation(core.Schema):

    default_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        default_value: Optional[Union[str, core.StringOut]] = None,
        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MetricTransformation.Args(
                name=name,
                namespace=namespace,
                value=value,
                default_value=default_value,
                dimensions=dimensions,
                unit=unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dimensions: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()

        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudwatch_log_metric_filter", namespace="aws_cloudwatch")
class LogMetricFilter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    metric_transformation: MetricTransformation = core.attr(MetricTransformation)

    name: Union[str, core.StringOut] = core.attr(str)

    pattern: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_group_name: Union[str, core.StringOut],
        metric_transformation: MetricTransformation,
        name: Union[str, core.StringOut],
        pattern: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogMetricFilter.Args(
                log_group_name=log_group_name,
                metric_transformation=metric_transformation,
                name=name,
                pattern=pattern,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_name: Union[str, core.StringOut] = core.arg()

        metric_transformation: MetricTransformation = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        pattern: Union[str, core.StringOut] = core.arg()
