from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class IncludeMetric(core.Schema):

    metric_name: Union[str, core.StringOut] = core.attr(str)

    namespace: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        namespace: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IncludeMetric.Args(
                metric_name=metric_name,
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: Union[str, core.StringOut] = core.arg()

        namespace: Union[str, core.StringOut] = core.arg()


@core.schema
class StatisticsConfiguration(core.Schema):

    additional_statistics: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    include_metric: Union[List[IncludeMetric], core.ArrayOut[IncludeMetric]] = core.attr(
        IncludeMetric, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        additional_statistics: Union[List[str], core.ArrayOut[core.StringOut]],
        include_metric: Union[List[IncludeMetric], core.ArrayOut[IncludeMetric]],
    ):
        super().__init__(
            args=StatisticsConfiguration.Args(
                additional_statistics=additional_statistics,
                include_metric=include_metric,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_statistics: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        include_metric: Union[List[IncludeMetric], core.ArrayOut[IncludeMetric]] = core.arg()


@core.schema
class IncludeFilter(core.Schema):

    namespace: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        namespace: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IncludeFilter.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: Union[str, core.StringOut] = core.arg()


@core.schema
class ExcludeFilter(core.Schema):

    namespace: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        namespace: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ExcludeFilter.Args(
                namespace=namespace,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        namespace: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudwatch_metric_stream", namespace="aws_cloudwatch")
class MetricStream(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    exclude_filter: Optional[Union[List[ExcludeFilter], core.ArrayOut[ExcludeFilter]]] = core.attr(
        ExcludeFilter, default=None, kind=core.Kind.array
    )

    firehose_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_filter: Optional[Union[List[IncludeFilter], core.ArrayOut[IncludeFilter]]] = core.attr(
        IncludeFilter, default=None, kind=core.Kind.array
    )

    last_update_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    output_format: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    statistics_configuration: Optional[
        Union[List[StatisticsConfiguration], core.ArrayOut[StatisticsConfiguration]]
    ] = core.attr(StatisticsConfiguration, default=None, kind=core.Kind.array)

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
        firehose_arn: Union[str, core.StringOut],
        output_format: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        exclude_filter: Optional[Union[List[ExcludeFilter], core.ArrayOut[ExcludeFilter]]] = None,
        include_filter: Optional[Union[List[IncludeFilter], core.ArrayOut[IncludeFilter]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        statistics_configuration: Optional[
            Union[List[StatisticsConfiguration], core.ArrayOut[StatisticsConfiguration]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MetricStream.Args(
                firehose_arn=firehose_arn,
                output_format=output_format,
                role_arn=role_arn,
                exclude_filter=exclude_filter,
                include_filter=include_filter,
                name=name,
                name_prefix=name_prefix,
                statistics_configuration=statistics_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        exclude_filter: Optional[
            Union[List[ExcludeFilter], core.ArrayOut[ExcludeFilter]]
        ] = core.arg(default=None)

        firehose_arn: Union[str, core.StringOut] = core.arg()

        include_filter: Optional[
            Union[List[IncludeFilter], core.ArrayOut[IncludeFilter]]
        ] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        output_format: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        statistics_configuration: Optional[
            Union[List[StatisticsConfiguration], core.ArrayOut[StatisticsConfiguration]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
