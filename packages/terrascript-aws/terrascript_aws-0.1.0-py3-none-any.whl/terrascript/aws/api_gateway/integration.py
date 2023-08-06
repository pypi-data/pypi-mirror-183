from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TlsConfig(core.Schema):

    insecure_skip_verification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        insecure_skip_verification: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=TlsConfig.Args(
                insecure_skip_verification=insecure_skip_verification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        insecure_skip_verification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_api_gateway_integration", namespace="aws_api_gateway")
class Integration(core.Resource):

    cache_key_parameters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    cache_namespace: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    connection_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connection_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_handling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_method: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    integration_http_method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    passthrough_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    resource_id: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    timeout_milliseconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tls_config: Optional[TlsConfig] = core.attr(TlsConfig, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        cache_key_parameters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        cache_namespace: Optional[Union[str, core.StringOut]] = None,
        connection_id: Optional[Union[str, core.StringOut]] = None,
        connection_type: Optional[Union[str, core.StringOut]] = None,
        content_handling: Optional[Union[str, core.StringOut]] = None,
        credentials: Optional[Union[str, core.StringOut]] = None,
        integration_http_method: Optional[Union[str, core.StringOut]] = None,
        passthrough_behavior: Optional[Union[str, core.StringOut]] = None,
        request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout_milliseconds: Optional[Union[int, core.IntOut]] = None,
        tls_config: Optional[TlsConfig] = None,
        uri: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Integration.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                type=type,
                cache_key_parameters=cache_key_parameters,
                cache_namespace=cache_namespace,
                connection_id=connection_id,
                connection_type=connection_type,
                content_handling=content_handling,
                credentials=credentials,
                integration_http_method=integration_http_method,
                passthrough_behavior=passthrough_behavior,
                request_parameters=request_parameters,
                request_templates=request_templates,
                timeout_milliseconds=timeout_milliseconds,
                tls_config=tls_config,
                uri=uri,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cache_key_parameters: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        cache_namespace: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_handling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_method: Union[str, core.StringOut] = core.arg()

        integration_http_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        passthrough_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_id: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()

        timeout_milliseconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tls_config: Optional[TlsConfig] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)
