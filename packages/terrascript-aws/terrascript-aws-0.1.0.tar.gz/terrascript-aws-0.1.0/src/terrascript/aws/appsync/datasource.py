from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ElasticsearchConfig(core.Schema):

    endpoint: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint: Union[str, core.StringOut],
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ElasticsearchConfig.Args(
                endpoint=endpoint,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DeltaSyncConfig(core.Schema):

    base_table_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    delta_sync_table_name: Union[str, core.StringOut] = core.attr(str)

    delta_sync_table_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        delta_sync_table_name: Union[str, core.StringOut],
        base_table_ttl: Optional[Union[int, core.IntOut]] = None,
        delta_sync_table_ttl: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DeltaSyncConfig.Args(
                delta_sync_table_name=delta_sync_table_name,
                base_table_ttl=base_table_ttl,
                delta_sync_table_ttl=delta_sync_table_ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base_table_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        delta_sync_table_name: Union[str, core.StringOut] = core.arg()

        delta_sync_table_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class DynamodbConfig(core.Schema):

    delta_sync_config: Optional[DeltaSyncConfig] = core.attr(DeltaSyncConfig, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    table_name: Union[str, core.StringOut] = core.attr(str)

    use_caller_credentials: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    versioned: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        table_name: Union[str, core.StringOut],
        delta_sync_config: Optional[DeltaSyncConfig] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        use_caller_credentials: Optional[Union[bool, core.BoolOut]] = None,
        versioned: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=DynamodbConfig.Args(
                table_name=table_name,
                delta_sync_config=delta_sync_config,
                region=region,
                use_caller_credentials=use_caller_credentials,
                versioned=versioned,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delta_sync_config: Optional[DeltaSyncConfig] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_name: Union[str, core.StringOut] = core.arg()

        use_caller_credentials: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        versioned: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class AwsIamConfig(core.Schema):

    signing_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    signing_service_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        signing_region: Optional[Union[str, core.StringOut]] = None,
        signing_service_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AwsIamConfig.Args(
                signing_region=signing_region,
                signing_service_name=signing_service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        signing_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        signing_service_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AuthorizationConfig(core.Schema):

    authorization_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    aws_iam_config: Optional[AwsIamConfig] = core.attr(AwsIamConfig, default=None)

    def __init__(
        self,
        *,
        authorization_type: Optional[Union[str, core.StringOut]] = None,
        aws_iam_config: Optional[AwsIamConfig] = None,
    ):
        super().__init__(
            args=AuthorizationConfig.Args(
                authorization_type=authorization_type,
                aws_iam_config=aws_iam_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        aws_iam_config: Optional[AwsIamConfig] = core.arg(default=None)


@core.schema
class HttpConfig(core.Schema):

    authorization_config: Optional[AuthorizationConfig] = core.attr(
        AuthorizationConfig, default=None
    )

    endpoint: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        endpoint: Union[str, core.StringOut],
        authorization_config: Optional[AuthorizationConfig] = None,
    ):
        super().__init__(
            args=HttpConfig.Args(
                endpoint=endpoint,
                authorization_config=authorization_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: Optional[AuthorizationConfig] = core.arg(default=None)

        endpoint: Union[str, core.StringOut] = core.arg()


@core.schema
class LambdaConfig(core.Schema):

    function_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        function_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LambdaConfig.Args(
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class HttpEndpointConfig(core.Schema):

    aws_secret_store_arn: Union[str, core.StringOut] = core.attr(str)

    database_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    schema: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        aws_secret_store_arn: Union[str, core.StringOut],
        db_cluster_identifier: Union[str, core.StringOut],
        database_name: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        schema: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=HttpEndpointConfig.Args(
                aws_secret_store_arn=aws_secret_store_arn,
                db_cluster_identifier=db_cluster_identifier,
                database_name=database_name,
                region=region,
                schema=schema,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aws_secret_store_arn: Union[str, core.StringOut] = core.arg()

        database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_cluster_identifier: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RelationalDatabaseConfig(core.Schema):

    http_endpoint_config: Optional[HttpEndpointConfig] = core.attr(HttpEndpointConfig, default=None)

    source_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint_config: Optional[HttpEndpointConfig] = None,
        source_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RelationalDatabaseConfig.Args(
                http_endpoint_config=http_endpoint_config,
                source_type=source_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint_config: Optional[HttpEndpointConfig] = core.arg(default=None)

        source_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_appsync_datasource", namespace="aws_appsync")
class Datasource(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynamodb_config: Optional[DynamodbConfig] = core.attr(DynamodbConfig, default=None)

    elasticsearch_config: Optional[ElasticsearchConfig] = core.attr(
        ElasticsearchConfig, default=None
    )

    http_config: Optional[HttpConfig] = core.attr(HttpConfig, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lambda_config: Optional[LambdaConfig] = core.attr(LambdaConfig, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    relational_database_config: Optional[RelationalDatabaseConfig] = core.attr(
        RelationalDatabaseConfig, default=None
    )

    service_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        dynamodb_config: Optional[DynamodbConfig] = None,
        elasticsearch_config: Optional[ElasticsearchConfig] = None,
        http_config: Optional[HttpConfig] = None,
        lambda_config: Optional[LambdaConfig] = None,
        relational_database_config: Optional[RelationalDatabaseConfig] = None,
        service_role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Datasource.Args(
                api_id=api_id,
                name=name,
                type=type,
                description=description,
                dynamodb_config=dynamodb_config,
                elasticsearch_config=elasticsearch_config,
                http_config=http_config,
                lambda_config=lambda_config,
                relational_database_config=relational_database_config,
                service_role_arn=service_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynamodb_config: Optional[DynamodbConfig] = core.arg(default=None)

        elasticsearch_config: Optional[ElasticsearchConfig] = core.arg(default=None)

        http_config: Optional[HttpConfig] = core.arg(default=None)

        lambda_config: Optional[LambdaConfig] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        relational_database_config: Optional[RelationalDatabaseConfig] = core.arg(default=None)

        service_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()
