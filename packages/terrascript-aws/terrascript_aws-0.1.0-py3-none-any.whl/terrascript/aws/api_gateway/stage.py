from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.schema
class CanarySettings(core.Schema):

    percent_traffic: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    stage_variable_overrides: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    use_stage_cache: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        percent_traffic: Optional[Union[float, core.FloatOut]] = None,
        stage_variable_overrides: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        use_stage_cache: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CanarySettings.Args(
                percent_traffic=percent_traffic,
                stage_variable_overrides=stage_variable_overrides,
                use_stage_cache=use_stage_cache,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        percent_traffic: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        stage_variable_overrides: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        use_stage_cache: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_api_gateway_stage", namespace="aws_api_gateway")
class Stage(core.Resource):

    access_log_settings: Optional[AccessLogSettings] = core.attr(AccessLogSettings, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cache_cluster_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cache_cluster_size: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    canary_settings: Optional[CanarySettings] = core.attr(CanarySettings, default=None)

    client_certificate_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    documentation_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    stage_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    web_acl_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    xray_tracing_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_id: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        stage_name: Union[str, core.StringOut],
        access_log_settings: Optional[AccessLogSettings] = None,
        cache_cluster_enabled: Optional[Union[bool, core.BoolOut]] = None,
        cache_cluster_size: Optional[Union[str, core.StringOut]] = None,
        canary_settings: Optional[CanarySettings] = None,
        client_certificate_id: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        documentation_version: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        xray_tracing_enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stage.Args(
                deployment_id=deployment_id,
                rest_api_id=rest_api_id,
                stage_name=stage_name,
                access_log_settings=access_log_settings,
                cache_cluster_enabled=cache_cluster_enabled,
                cache_cluster_size=cache_cluster_size,
                canary_settings=canary_settings,
                client_certificate_id=client_certificate_id,
                description=description,
                documentation_version=documentation_version,
                tags=tags,
                tags_all=tags_all,
                variables=variables,
                xray_tracing_enabled=xray_tracing_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_log_settings: Optional[AccessLogSettings] = core.arg(default=None)

        cache_cluster_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cache_cluster_size: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        canary_settings: Optional[CanarySettings] = core.arg(default=None)

        client_certificate_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        documentation_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rest_api_id: Union[str, core.StringOut] = core.arg()

        stage_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        xray_tracing_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
