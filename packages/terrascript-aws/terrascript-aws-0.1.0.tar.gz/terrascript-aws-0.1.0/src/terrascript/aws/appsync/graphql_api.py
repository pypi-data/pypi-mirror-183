from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OpenidConnectConfig(core.Schema):

    auth_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    client_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iat_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    issuer: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        issuer: Union[str, core.StringOut],
        auth_ttl: Optional[Union[int, core.IntOut]] = None,
        client_id: Optional[Union[str, core.StringOut]] = None,
        iat_ttl: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=OpenidConnectConfig.Args(
                issuer=issuer,
                auth_ttl=auth_ttl,
                client_id=client_id,
                iat_ttl=iat_ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        client_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iat_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        issuer: Union[str, core.StringOut] = core.arg()


@core.schema
class UserPoolConfig(core.Schema):

    app_id_client_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    aws_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    default_action: Union[str, core.StringOut] = core.attr(str)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        default_action: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        app_id_client_regex: Optional[Union[str, core.StringOut]] = None,
        aws_region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=UserPoolConfig.Args(
                default_action=default_action,
                user_pool_id=user_pool_id,
                app_id_client_regex=app_id_client_regex,
                aws_region=aws_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_id_client_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        aws_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_action: Union[str, core.StringOut] = core.arg()

        user_pool_id: Union[str, core.StringOut] = core.arg()


@core.schema
class LambdaAuthorizerConfig(core.Schema):

    authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    authorizer_uri: Union[str, core.StringOut] = core.attr(str)

    identity_validation_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        authorizer_uri: Union[str, core.StringOut],
        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = None,
        identity_validation_expression: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaAuthorizerConfig.Args(
                authorizer_uri=authorizer_uri,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                identity_validation_expression=identity_validation_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        authorizer_uri: Union[str, core.StringOut] = core.arg()

        identity_validation_expression: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class AdditionalAuthenticationProviderUserPoolConfig(core.Schema):

    app_id_client_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    aws_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        user_pool_id: Union[str, core.StringOut],
        app_id_client_regex: Optional[Union[str, core.StringOut]] = None,
        aws_region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AdditionalAuthenticationProviderUserPoolConfig.Args(
                user_pool_id=user_pool_id,
                app_id_client_regex=app_id_client_regex,
                aws_region=aws_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_id_client_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        aws_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()


@core.schema
class AdditionalAuthenticationProvider(core.Schema):

    authentication_type: Union[str, core.StringOut] = core.attr(str)

    lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = core.attr(
        LambdaAuthorizerConfig, default=None
    )

    openid_connect_config: Optional[OpenidConnectConfig] = core.attr(
        OpenidConnectConfig, default=None
    )

    user_pool_config: Optional[AdditionalAuthenticationProviderUserPoolConfig] = core.attr(
        AdditionalAuthenticationProviderUserPoolConfig, default=None
    )

    def __init__(
        self,
        *,
        authentication_type: Union[str, core.StringOut],
        lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = None,
        openid_connect_config: Optional[OpenidConnectConfig] = None,
        user_pool_config: Optional[AdditionalAuthenticationProviderUserPoolConfig] = None,
    ):
        super().__init__(
            args=AdditionalAuthenticationProvider.Args(
                authentication_type=authentication_type,
                lambda_authorizer_config=lambda_authorizer_config,
                openid_connect_config=openid_connect_config,
                user_pool_config=user_pool_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_type: Union[str, core.StringOut] = core.arg()

        lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = core.arg(default=None)

        openid_connect_config: Optional[OpenidConnectConfig] = core.arg(default=None)

        user_pool_config: Optional[AdditionalAuthenticationProviderUserPoolConfig] = core.arg(
            default=None
        )


@core.schema
class LogConfig(core.Schema):

    cloudwatch_logs_role_arn: Union[str, core.StringOut] = core.attr(str)

    exclude_verbose_content: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    field_log_level: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_logs_role_arn: Union[str, core.StringOut],
        field_log_level: Union[str, core.StringOut],
        exclude_verbose_content: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=LogConfig.Args(
                cloudwatch_logs_role_arn=cloudwatch_logs_role_arn,
                field_log_level=field_log_level,
                exclude_verbose_content=exclude_verbose_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs_role_arn: Union[str, core.StringOut] = core.arg()

        exclude_verbose_content: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        field_log_level: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_appsync_graphql_api", namespace="aws_appsync")
class GraphqlApi(core.Resource):

    additional_authentication_provider: Optional[
        Union[
            List[AdditionalAuthenticationProvider], core.ArrayOut[AdditionalAuthenticationProvider]
        ]
    ] = core.attr(AdditionalAuthenticationProvider, default=None, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = core.attr(
        LambdaAuthorizerConfig, default=None
    )

    log_config: Optional[LogConfig] = core.attr(LogConfig, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    openid_connect_config: Optional[OpenidConnectConfig] = core.attr(
        OpenidConnectConfig, default=None
    )

    schema: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uris: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    user_pool_config: Optional[UserPoolConfig] = core.attr(UserPoolConfig, default=None)

    xray_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        additional_authentication_provider: Optional[
            Union[
                List[AdditionalAuthenticationProvider],
                core.ArrayOut[AdditionalAuthenticationProvider],
            ]
        ] = None,
        lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = None,
        log_config: Optional[LogConfig] = None,
        openid_connect_config: Optional[OpenidConnectConfig] = None,
        schema: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_pool_config: Optional[UserPoolConfig] = None,
        xray_enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GraphqlApi.Args(
                authentication_type=authentication_type,
                name=name,
                additional_authentication_provider=additional_authentication_provider,
                lambda_authorizer_config=lambda_authorizer_config,
                log_config=log_config,
                openid_connect_config=openid_connect_config,
                schema=schema,
                tags=tags,
                tags_all=tags_all,
                user_pool_config=user_pool_config,
                xray_enabled=xray_enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        additional_authentication_provider: Optional[
            Union[
                List[AdditionalAuthenticationProvider],
                core.ArrayOut[AdditionalAuthenticationProvider],
            ]
        ] = core.arg(default=None)

        authentication_type: Union[str, core.StringOut] = core.arg()

        lambda_authorizer_config: Optional[LambdaAuthorizerConfig] = core.arg(default=None)

        log_config: Optional[LogConfig] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        openid_connect_config: Optional[OpenidConnectConfig] = core.arg(default=None)

        schema: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_pool_config: Optional[UserPoolConfig] = core.arg(default=None)

        xray_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
