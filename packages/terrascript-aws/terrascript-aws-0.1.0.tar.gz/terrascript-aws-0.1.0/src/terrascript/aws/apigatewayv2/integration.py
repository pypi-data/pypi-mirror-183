from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ResponseParameters(core.Schema):

    mappings: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    status_code: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        mappings: Union[Dict[str, str], core.MapOut[core.StringOut]],
        status_code: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResponseParameters.Args(
                mappings=mappings,
                status_code=status_code,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mappings: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        status_code: Union[str, core.StringOut] = core.arg()


@core.schema
class TlsConfig(core.Schema):

    server_name_to_verify: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        server_name_to_verify: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TlsConfig.Args(
                server_name_to_verify=server_name_to_verify,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        server_name_to_verify: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_integration", namespace="aws_apigatewayv2")
class Integration(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    connection_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connection_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_handling_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    credentials_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    integration_method: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    integration_response_selection_expression: Union[str, core.StringOut] = core.attr(
        str, computed=True
    )

    integration_subtype: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    integration_type: Union[str, core.StringOut] = core.attr(str)

    integration_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    passthrough_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    payload_format_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_parameters: Optional[
        Union[List[ResponseParameters], core.ArrayOut[ResponseParameters]]
    ] = core.attr(ResponseParameters, default=None, kind=core.Kind.array)

    template_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    timeout_milliseconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    tls_config: Optional[TlsConfig] = core.attr(TlsConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        integration_type: Union[str, core.StringOut],
        connection_id: Optional[Union[str, core.StringOut]] = None,
        connection_type: Optional[Union[str, core.StringOut]] = None,
        content_handling_strategy: Optional[Union[str, core.StringOut]] = None,
        credentials_arn: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        integration_method: Optional[Union[str, core.StringOut]] = None,
        integration_subtype: Optional[Union[str, core.StringOut]] = None,
        integration_uri: Optional[Union[str, core.StringOut]] = None,
        passthrough_behavior: Optional[Union[str, core.StringOut]] = None,
        payload_format_version: Optional[Union[str, core.StringOut]] = None,
        request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        response_parameters: Optional[
            Union[List[ResponseParameters], core.ArrayOut[ResponseParameters]]
        ] = None,
        template_selection_expression: Optional[Union[str, core.StringOut]] = None,
        timeout_milliseconds: Optional[Union[int, core.IntOut]] = None,
        tls_config: Optional[TlsConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Integration.Args(
                api_id=api_id,
                integration_type=integration_type,
                connection_id=connection_id,
                connection_type=connection_type,
                content_handling_strategy=content_handling_strategy,
                credentials_arn=credentials_arn,
                description=description,
                integration_method=integration_method,
                integration_subtype=integration_subtype,
                integration_uri=integration_uri,
                passthrough_behavior=passthrough_behavior,
                payload_format_version=payload_format_version,
                request_parameters=request_parameters,
                request_templates=request_templates,
                response_parameters=response_parameters,
                template_selection_expression=template_selection_expression,
                timeout_milliseconds=timeout_milliseconds,
                tls_config=tls_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        connection_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_handling_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        credentials_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        integration_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        integration_subtype: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        integration_type: Union[str, core.StringOut] = core.arg()

        integration_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        passthrough_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        payload_format_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        request_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        request_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        response_parameters: Optional[
            Union[List[ResponseParameters], core.ArrayOut[ResponseParameters]]
        ] = core.arg(default=None)

        template_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout_milliseconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tls_config: Optional[TlsConfig] = core.arg(default=None)
