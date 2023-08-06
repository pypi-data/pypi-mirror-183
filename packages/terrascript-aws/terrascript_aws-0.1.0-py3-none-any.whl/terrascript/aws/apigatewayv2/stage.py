from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DefaultRouteSettings(core.Schema):

    data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    logging_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = None,
        detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = None,
        logging_level: Optional[Union[str, core.StringOut]] = None,
        throttling_burst_limit: Optional[Union[int, core.IntOut]] = None,
        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=DefaultRouteSettings.Args(
                data_trace_enabled=data_trace_enabled,
                detailed_metrics_enabled=detailed_metrics_enabled,
                logging_level=logging_level,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        logging_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class RouteSettings(core.Schema):

    data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    logging_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    route_key: Union[str, core.StringOut] = core.attr(str)

    throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        route_key: Union[str, core.StringOut],
        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = None,
        detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = None,
        logging_level: Optional[Union[str, core.StringOut]] = None,
        throttling_burst_limit: Optional[Union[int, core.IntOut]] = None,
        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=RouteSettings.Args(
                route_key=route_key,
                data_trace_enabled=data_trace_enabled,
                detailed_metrics_enabled=detailed_metrics_enabled,
                logging_level=logging_level,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        detailed_metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        logging_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route_key: Union[str, core.StringOut] = core.arg()

        throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class AccessLogSettings(core.Schema):

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    format: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination_arn: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AccessLogSettings.Args(
                destination_arn=destination_arn,
                format=format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_arn: Union[str, core.StringOut] = core.arg()

        format: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_apigatewayv2_stage", namespace="aws_apigatewayv2")
class Stage(core.Resource):

    access_log_settings: Optional[AccessLogSettings] = core.attr(AccessLogSettings, default=None)

    api_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_deploy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    client_certificate_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_route_settings: Optional[DefaultRouteSettings] = core.attr(
        DefaultRouteSettings, default=None
    )

    deployment_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    route_settings: Optional[Union[List[RouteSettings], core.ArrayOut[RouteSettings]]] = core.attr(
        RouteSettings, default=None, kind=core.Kind.array
    )

    stage_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
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
        api_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        access_log_settings: Optional[AccessLogSettings] = None,
        auto_deploy: Optional[Union[bool, core.BoolOut]] = None,
        client_certificate_id: Optional[Union[str, core.StringOut]] = None,
        default_route_settings: Optional[DefaultRouteSettings] = None,
        deployment_id: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        route_settings: Optional[Union[List[RouteSettings], core.ArrayOut[RouteSettings]]] = None,
        stage_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stage.Args(
                api_id=api_id,
                name=name,
                access_log_settings=access_log_settings,
                auto_deploy=auto_deploy,
                client_certificate_id=client_certificate_id,
                default_route_settings=default_route_settings,
                deployment_id=deployment_id,
                description=description,
                route_settings=route_settings,
                stage_variables=stage_variables,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_log_settings: Optional[AccessLogSettings] = core.arg(default=None)

        api_id: Union[str, core.StringOut] = core.arg()

        auto_deploy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        client_certificate_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_route_settings: Optional[DefaultRouteSettings] = core.arg(default=None)

        deployment_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        route_settings: Optional[
            Union[List[RouteSettings], core.ArrayOut[RouteSettings]]
        ] = core.arg(default=None)

        stage_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
