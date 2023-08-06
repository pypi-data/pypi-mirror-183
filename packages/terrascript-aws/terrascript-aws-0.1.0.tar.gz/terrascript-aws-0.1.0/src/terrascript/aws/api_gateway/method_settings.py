from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Settings(core.Schema):

    cache_data_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    cache_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    caching_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    logging_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    require_authorization_for_cache_control: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    unauthorized_cache_control_header_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        cache_data_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        cache_ttl_in_seconds: Optional[Union[int, core.IntOut]] = None,
        caching_enabled: Optional[Union[bool, core.BoolOut]] = None,
        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = None,
        logging_level: Optional[Union[str, core.StringOut]] = None,
        metrics_enabled: Optional[Union[bool, core.BoolOut]] = None,
        require_authorization_for_cache_control: Optional[Union[bool, core.BoolOut]] = None,
        throttling_burst_limit: Optional[Union[int, core.IntOut]] = None,
        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = None,
        unauthorized_cache_control_header_strategy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Settings.Args(
                cache_data_encrypted=cache_data_encrypted,
                cache_ttl_in_seconds=cache_ttl_in_seconds,
                caching_enabled=caching_enabled,
                data_trace_enabled=data_trace_enabled,
                logging_level=logging_level,
                metrics_enabled=metrics_enabled,
                require_authorization_for_cache_control=require_authorization_for_cache_control,
                throttling_burst_limit=throttling_burst_limit,
                throttling_rate_limit=throttling_rate_limit,
                unauthorized_cache_control_header_strategy=unauthorized_cache_control_header_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_data_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cache_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        caching_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        data_trace_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        logging_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metrics_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        require_authorization_for_cache_control: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        throttling_burst_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throttling_rate_limit: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        unauthorized_cache_control_header_strategy: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_api_gateway_method_settings", namespace="aws_api_gateway")
class MethodSettings(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    method_path: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    settings: Settings = core.attr(Settings)

    stage_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        method_path: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        settings: Settings,
        stage_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MethodSettings.Args(
                method_path=method_path,
                rest_api_id=rest_api_id,
                settings=settings,
                stage_name=stage_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        method_path: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()

        settings: Settings = core.arg()

        stage_name: Union[str, core.StringOut] = core.arg()
