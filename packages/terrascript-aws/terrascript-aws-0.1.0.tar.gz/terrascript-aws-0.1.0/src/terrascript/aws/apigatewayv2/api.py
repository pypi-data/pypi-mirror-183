from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CorsConfiguration(core.Schema):

    allow_credentials: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allow_credentials: Optional[Union[bool, core.BoolOut]] = None,
        allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        max_age: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CorsConfiguration.Args(
                allow_credentials=allow_credentials,
                allow_headers=allow_headers,
                allow_methods=allow_methods,
                allow_origins=allow_origins,
                expose_headers=expose_headers,
                max_age=max_age,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_credentials: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        allow_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allow_methods: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allow_origins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_age: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_api", namespace="aws_apigatewayv2")
class Api(core.Resource):

    api_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    api_key_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cors_configuration: Optional[CorsConfiguration] = core.attr(CorsConfiguration, default=None)

    credentials_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    fail_on_warnings: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    protocol_type: Union[str, core.StringOut] = core.attr(str)

    route_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    route_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        protocol_type: Union[str, core.StringOut],
        api_key_selection_expression: Optional[Union[str, core.StringOut]] = None,
        body: Optional[Union[str, core.StringOut]] = None,
        cors_configuration: Optional[CorsConfiguration] = None,
        credentials_arn: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = None,
        fail_on_warnings: Optional[Union[bool, core.BoolOut]] = None,
        route_key: Optional[Union[str, core.StringOut]] = None,
        route_selection_expression: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Api.Args(
                name=name,
                protocol_type=protocol_type,
                api_key_selection_expression=api_key_selection_expression,
                body=body,
                cors_configuration=cors_configuration,
                credentials_arn=credentials_arn,
                description=description,
                disable_execute_api_endpoint=disable_execute_api_endpoint,
                fail_on_warnings=fail_on_warnings,
                route_key=route_key,
                route_selection_expression=route_selection_expression,
                tags=tags,
                tags_all=tags_all,
                target=target,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cors_configuration: Optional[CorsConfiguration] = core.arg(default=None)

        credentials_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        fail_on_warnings: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        protocol_type: Union[str, core.StringOut] = core.arg()

        route_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        route_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
