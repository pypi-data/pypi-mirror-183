from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Target(core.Schema):

    connection_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dlq_event_queue_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_queue_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    path: Union[str, core.StringOut] = core.attr(str)

    sample_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        path: Union[str, core.StringOut],
        connection_name: Optional[Union[str, core.StringOut]] = None,
        dlq_event_queue_arn: Optional[Union[str, core.StringOut]] = None,
        event_queue_arn: Optional[Union[str, core.StringOut]] = None,
        exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        sample_size: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=S3Target.Args(
                path=path,
                connection_name=connection_name,
                dlq_event_queue_arn=dlq_event_queue_arn,
                event_queue_arn=event_queue_arn,
                exclusions=exclusions,
                sample_size=sample_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dlq_event_queue_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_queue_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        path: Union[str, core.StringOut] = core.arg()

        sample_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class CatalogTarget(core.Schema):

    database_name: Union[str, core.StringOut] = core.attr(str)

    tables: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        tables: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=CatalogTarget.Args(
                database_name=database_name,
                tables=tables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database_name: Union[str, core.StringOut] = core.arg()

        tables: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class DeltaTarget(core.Schema):

    connection_name: Union[str, core.StringOut] = core.attr(str)

    delta_tables: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    write_manifest: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        connection_name: Union[str, core.StringOut],
        delta_tables: Union[List[str], core.ArrayOut[core.StringOut]],
        write_manifest: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=DeltaTarget.Args(
                connection_name=connection_name,
                delta_tables=delta_tables,
                write_manifest=write_manifest,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: Union[str, core.StringOut] = core.arg()

        delta_tables: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        write_manifest: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SchemaChangePolicy(core.Schema):

    delete_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    update_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delete_behavior: Optional[Union[str, core.StringOut]] = None,
        update_behavior: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SchemaChangePolicy.Args(
                delete_behavior=delete_behavior,
                update_behavior=update_behavior,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        update_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MongodbTarget(core.Schema):

    connection_name: Union[str, core.StringOut] = core.attr(str)

    path: Union[str, core.StringOut] = core.attr(str)

    scan_all: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        connection_name: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        scan_all: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=MongodbTarget.Args(
                connection_name=connection_name,
                path=path,
                scan_all=scan_all,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: Union[str, core.StringOut] = core.arg()

        path: Union[str, core.StringOut] = core.arg()

        scan_all: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class JdbcTarget(core.Schema):

    connection_name: Union[str, core.StringOut] = core.attr(str)

    exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        connection_name: Union[str, core.StringOut],
        path: Union[str, core.StringOut],
        exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=JdbcTarget.Args(
                connection_name=connection_name,
                path=path,
                exclusions=exclusions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_name: Union[str, core.StringOut] = core.arg()

        exclusions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        path: Union[str, core.StringOut] = core.arg()


@core.schema
class LineageConfiguration(core.Schema):

    crawler_lineage_settings: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        crawler_lineage_settings: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LineageConfiguration.Args(
                crawler_lineage_settings=crawler_lineage_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crawler_lineage_settings: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DynamodbTarget(core.Schema):

    path: Union[str, core.StringOut] = core.attr(str)

    scan_all: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    scan_rate: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        path: Union[str, core.StringOut],
        scan_all: Optional[Union[bool, core.BoolOut]] = None,
        scan_rate: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=DynamodbTarget.Args(
                path=path,
                scan_all=scan_all,
                scan_rate=scan_rate,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        path: Union[str, core.StringOut] = core.arg()

        scan_all: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        scan_rate: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class RecrawlPolicy(core.Schema):

    recrawl_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        recrawl_behavior: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RecrawlPolicy.Args(
                recrawl_behavior=recrawl_behavior,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        recrawl_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_glue_crawler", namespace="aws_glue")
class Crawler(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_target: Optional[Union[List[CatalogTarget], core.ArrayOut[CatalogTarget]]] = core.attr(
        CatalogTarget, default=None, kind=core.Kind.array
    )

    classifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    database_name: Union[str, core.StringOut] = core.attr(str)

    delta_target: Optional[Union[List[DeltaTarget], core.ArrayOut[DeltaTarget]]] = core.attr(
        DeltaTarget, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynamodb_target: Optional[
        Union[List[DynamodbTarget], core.ArrayOut[DynamodbTarget]]
    ] = core.attr(DynamodbTarget, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    jdbc_target: Optional[Union[List[JdbcTarget], core.ArrayOut[JdbcTarget]]] = core.attr(
        JdbcTarget, default=None, kind=core.Kind.array
    )

    lineage_configuration: Optional[LineageConfiguration] = core.attr(
        LineageConfiguration, default=None
    )

    mongodb_target: Optional[Union[List[MongodbTarget], core.ArrayOut[MongodbTarget]]] = core.attr(
        MongodbTarget, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    recrawl_policy: Optional[RecrawlPolicy] = core.attr(RecrawlPolicy, default=None)

    role: Union[str, core.StringOut] = core.attr(str)

    s3_target: Optional[Union[List[S3Target], core.ArrayOut[S3Target]]] = core.attr(
        S3Target, default=None, kind=core.Kind.array
    )

    schedule: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schema_change_policy: Optional[SchemaChangePolicy] = core.attr(SchemaChangePolicy, default=None)

    security_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    table_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        database_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role: Union[str, core.StringOut],
        catalog_target: Optional[Union[List[CatalogTarget], core.ArrayOut[CatalogTarget]]] = None,
        classifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        configuration: Optional[Union[str, core.StringOut]] = None,
        delta_target: Optional[Union[List[DeltaTarget], core.ArrayOut[DeltaTarget]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        dynamodb_target: Optional[
            Union[List[DynamodbTarget], core.ArrayOut[DynamodbTarget]]
        ] = None,
        jdbc_target: Optional[Union[List[JdbcTarget], core.ArrayOut[JdbcTarget]]] = None,
        lineage_configuration: Optional[LineageConfiguration] = None,
        mongodb_target: Optional[Union[List[MongodbTarget], core.ArrayOut[MongodbTarget]]] = None,
        recrawl_policy: Optional[RecrawlPolicy] = None,
        s3_target: Optional[Union[List[S3Target], core.ArrayOut[S3Target]]] = None,
        schedule: Optional[Union[str, core.StringOut]] = None,
        schema_change_policy: Optional[SchemaChangePolicy] = None,
        security_configuration: Optional[Union[str, core.StringOut]] = None,
        table_prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Crawler.Args(
                database_name=database_name,
                name=name,
                role=role,
                catalog_target=catalog_target,
                classifiers=classifiers,
                configuration=configuration,
                delta_target=delta_target,
                description=description,
                dynamodb_target=dynamodb_target,
                jdbc_target=jdbc_target,
                lineage_configuration=lineage_configuration,
                mongodb_target=mongodb_target,
                recrawl_policy=recrawl_policy,
                s3_target=s3_target,
                schedule=schedule,
                schema_change_policy=schema_change_policy,
                security_configuration=security_configuration,
                table_prefix=table_prefix,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_target: Optional[
            Union[List[CatalogTarget], core.ArrayOut[CatalogTarget]]
        ] = core.arg(default=None)

        classifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        delta_target: Optional[Union[List[DeltaTarget], core.ArrayOut[DeltaTarget]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynamodb_target: Optional[
            Union[List[DynamodbTarget], core.ArrayOut[DynamodbTarget]]
        ] = core.arg(default=None)

        jdbc_target: Optional[Union[List[JdbcTarget], core.ArrayOut[JdbcTarget]]] = core.arg(
            default=None
        )

        lineage_configuration: Optional[LineageConfiguration] = core.arg(default=None)

        mongodb_target: Optional[
            Union[List[MongodbTarget], core.ArrayOut[MongodbTarget]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        recrawl_policy: Optional[RecrawlPolicy] = core.arg(default=None)

        role: Union[str, core.StringOut] = core.arg()

        s3_target: Optional[Union[List[S3Target], core.ArrayOut[S3Target]]] = core.arg(default=None)

        schedule: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema_change_policy: Optional[SchemaChangePolicy] = core.arg(default=None)

        security_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
