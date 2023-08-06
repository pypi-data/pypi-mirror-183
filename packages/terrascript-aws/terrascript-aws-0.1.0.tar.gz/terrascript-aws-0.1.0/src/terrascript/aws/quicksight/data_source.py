from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Postgresql(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Postgresql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class SqlServer(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SqlServer.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Jira(core.Schema):

    site_base_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        site_base_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Jira.Args(
                site_base_url=site_base_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_base_url: Union[str, core.StringOut] = core.arg()


@core.schema
class MariaDb(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=MariaDb.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Rds(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Rds.Args(
                database=database,
                instance_id=instance_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Aurora(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Aurora.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Oracle(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Oracle.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Snowflake(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    warehouse: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        warehouse: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Snowflake.Args(
                database=database,
                host=host,
                warehouse=warehouse,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        warehouse: Union[str, core.StringOut] = core.arg()


@core.schema
class ServiceNow(core.Schema):

    site_base_url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        site_base_url: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ServiceNow.Args(
                site_base_url=site_base_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        site_base_url: Union[str, core.StringOut] = core.arg()


@core.schema
class Redshift(core.Schema):

    cluster_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    database: Union[str, core.StringOut] = core.attr(str)

    host: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        cluster_id: Optional[Union[str, core.StringOut]] = None,
        host: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Redshift.Args(
                database=database,
                cluster_id=cluster_id,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database: Union[str, core.StringOut] = core.arg()

        host: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Spark(core.Schema):

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Spark.Args(
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class AuroraPostgresql(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=AuroraPostgresql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class AwsIotAnalytics(core.Schema):

    data_set_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        data_set_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AwsIotAnalytics.Args(
                data_set_name=data_set_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_set_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Twitter(core.Schema):

    max_rows: Union[int, core.IntOut] = core.attr(int)

    query: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        max_rows: Union[int, core.IntOut],
        query: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Twitter.Args(
                max_rows=max_rows,
                query=query,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_rows: Union[int, core.IntOut] = core.arg()

        query: Union[str, core.StringOut] = core.arg()


@core.schema
class Presto(core.Schema):

    catalog: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        catalog: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Presto.Args(
                catalog=catalog,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Athena(core.Schema):

    work_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        work_group: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Athena.Args(
                work_group=work_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        work_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ManifestFileLocation(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ManifestFileLocation.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.schema
class S3(core.Schema):

    manifest_file_location: ManifestFileLocation = core.attr(ManifestFileLocation)

    def __init__(
        self,
        *,
        manifest_file_location: ManifestFileLocation,
    ):
        super().__init__(
            args=S3.Args(
                manifest_file_location=manifest_file_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        manifest_file_location: ManifestFileLocation = core.arg()


@core.schema
class Teradata(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Teradata.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class AmazonElasticsearch(core.Schema):

    domain: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        domain: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AmazonElasticsearch.Args(
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain: Union[str, core.StringOut] = core.arg()


@core.schema
class Mysql(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    host: Union[str, core.StringOut] = core.attr(str)

    port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        host: Union[str, core.StringOut],
        port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Mysql.Args(
                database=database,
                host=host,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        host: Union[str, core.StringOut] = core.arg()

        port: Union[int, core.IntOut] = core.arg()


@core.schema
class Parameters(core.Schema):

    amazon_elasticsearch: Optional[AmazonElasticsearch] = core.attr(
        AmazonElasticsearch, default=None
    )

    athena: Optional[Athena] = core.attr(Athena, default=None)

    aurora: Optional[Aurora] = core.attr(Aurora, default=None)

    aurora_postgresql: Optional[AuroraPostgresql] = core.attr(AuroraPostgresql, default=None)

    aws_iot_analytics: Optional[AwsIotAnalytics] = core.attr(AwsIotAnalytics, default=None)

    jira: Optional[Jira] = core.attr(Jira, default=None)

    maria_db: Optional[MariaDb] = core.attr(MariaDb, default=None)

    mysql: Optional[Mysql] = core.attr(Mysql, default=None)

    oracle: Optional[Oracle] = core.attr(Oracle, default=None)

    postgresql: Optional[Postgresql] = core.attr(Postgresql, default=None)

    presto: Optional[Presto] = core.attr(Presto, default=None)

    rds: Optional[Rds] = core.attr(Rds, default=None)

    redshift: Optional[Redshift] = core.attr(Redshift, default=None)

    s3: Optional[S3] = core.attr(S3, default=None)

    service_now: Optional[ServiceNow] = core.attr(ServiceNow, default=None)

    snowflake: Optional[Snowflake] = core.attr(Snowflake, default=None)

    spark: Optional[Spark] = core.attr(Spark, default=None)

    sql_server: Optional[SqlServer] = core.attr(SqlServer, default=None)

    teradata: Optional[Teradata] = core.attr(Teradata, default=None)

    twitter: Optional[Twitter] = core.attr(Twitter, default=None)

    def __init__(
        self,
        *,
        amazon_elasticsearch: Optional[AmazonElasticsearch] = None,
        athena: Optional[Athena] = None,
        aurora: Optional[Aurora] = None,
        aurora_postgresql: Optional[AuroraPostgresql] = None,
        aws_iot_analytics: Optional[AwsIotAnalytics] = None,
        jira: Optional[Jira] = None,
        maria_db: Optional[MariaDb] = None,
        mysql: Optional[Mysql] = None,
        oracle: Optional[Oracle] = None,
        postgresql: Optional[Postgresql] = None,
        presto: Optional[Presto] = None,
        rds: Optional[Rds] = None,
        redshift: Optional[Redshift] = None,
        s3: Optional[S3] = None,
        service_now: Optional[ServiceNow] = None,
        snowflake: Optional[Snowflake] = None,
        spark: Optional[Spark] = None,
        sql_server: Optional[SqlServer] = None,
        teradata: Optional[Teradata] = None,
        twitter: Optional[Twitter] = None,
    ):
        super().__init__(
            args=Parameters.Args(
                amazon_elasticsearch=amazon_elasticsearch,
                athena=athena,
                aurora=aurora,
                aurora_postgresql=aurora_postgresql,
                aws_iot_analytics=aws_iot_analytics,
                jira=jira,
                maria_db=maria_db,
                mysql=mysql,
                oracle=oracle,
                postgresql=postgresql,
                presto=presto,
                rds=rds,
                redshift=redshift,
                s3=s3,
                service_now=service_now,
                snowflake=snowflake,
                spark=spark,
                sql_server=sql_server,
                teradata=teradata,
                twitter=twitter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amazon_elasticsearch: Optional[AmazonElasticsearch] = core.arg(default=None)

        athena: Optional[Athena] = core.arg(default=None)

        aurora: Optional[Aurora] = core.arg(default=None)

        aurora_postgresql: Optional[AuroraPostgresql] = core.arg(default=None)

        aws_iot_analytics: Optional[AwsIotAnalytics] = core.arg(default=None)

        jira: Optional[Jira] = core.arg(default=None)

        maria_db: Optional[MariaDb] = core.arg(default=None)

        mysql: Optional[Mysql] = core.arg(default=None)

        oracle: Optional[Oracle] = core.arg(default=None)

        postgresql: Optional[Postgresql] = core.arg(default=None)

        presto: Optional[Presto] = core.arg(default=None)

        rds: Optional[Rds] = core.arg(default=None)

        redshift: Optional[Redshift] = core.arg(default=None)

        s3: Optional[S3] = core.arg(default=None)

        service_now: Optional[ServiceNow] = core.arg(default=None)

        snowflake: Optional[Snowflake] = core.arg(default=None)

        spark: Optional[Spark] = core.arg(default=None)

        sql_server: Optional[SqlServer] = core.arg(default=None)

        teradata: Optional[Teradata] = core.arg(default=None)

        twitter: Optional[Twitter] = core.arg(default=None)


@core.schema
class CredentialPair(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CredentialPair.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class Credentials(core.Schema):

    copy_source_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    credential_pair: Optional[CredentialPair] = core.attr(CredentialPair, default=None)

    def __init__(
        self,
        *,
        copy_source_arn: Optional[Union[str, core.StringOut]] = None,
        credential_pair: Optional[CredentialPair] = None,
    ):
        super().__init__(
            args=Credentials.Args(
                copy_source_arn=copy_source_arn,
                credential_pair=credential_pair,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_source_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        credential_pair: Optional[CredentialPair] = core.arg(default=None)


@core.schema
class Permission(core.Schema):

    actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    principal: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        actions: Union[List[str], core.ArrayOut[core.StringOut]],
        principal: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Permission.Args(
                actions=actions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        principal: Union[str, core.StringOut] = core.arg()


@core.schema
class SslProperties(core.Schema):

    disable_ssl: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        disable_ssl: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=SslProperties.Args(
                disable_ssl=disable_ssl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        disable_ssl: Union[bool, core.BoolOut] = core.arg()


@core.schema
class VpcConnectionProperties(core.Schema):

    vpc_connection_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        vpc_connection_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConnectionProperties.Args(
                vpc_connection_arn=vpc_connection_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_connection_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_quicksight_data_source", namespace="aws_quicksight")
class DataSource(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_account_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    credentials: Optional[Credentials] = core.attr(Credentials, default=None)

    data_source_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters: Parameters = core.attr(Parameters)

    permission: Optional[Union[List[Permission], core.ArrayOut[Permission]]] = core.attr(
        Permission, default=None, kind=core.Kind.array
    )

    ssl_properties: Optional[SslProperties] = core.attr(SslProperties, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    vpc_connection_properties: Optional[VpcConnectionProperties] = core.attr(
        VpcConnectionProperties, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        data_source_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        parameters: Parameters,
        type: Union[str, core.StringOut],
        aws_account_id: Optional[Union[str, core.StringOut]] = None,
        credentials: Optional[Credentials] = None,
        permission: Optional[Union[List[Permission], core.ArrayOut[Permission]]] = None,
        ssl_properties: Optional[SslProperties] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_connection_properties: Optional[VpcConnectionProperties] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataSource.Args(
                data_source_id=data_source_id,
                name=name,
                parameters=parameters,
                type=type,
                aws_account_id=aws_account_id,
                credentials=credentials,
                permission=permission,
                ssl_properties=ssl_properties,
                tags=tags,
                tags_all=tags_all,
                vpc_connection_properties=vpc_connection_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        credentials: Optional[Credentials] = core.arg(default=None)

        data_source_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        parameters: Parameters = core.arg()

        permission: Optional[Union[List[Permission], core.ArrayOut[Permission]]] = core.arg(
            default=None
        )

        ssl_properties: Optional[SslProperties] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()

        vpc_connection_properties: Optional[VpcConnectionProperties] = core.arg(default=None)
