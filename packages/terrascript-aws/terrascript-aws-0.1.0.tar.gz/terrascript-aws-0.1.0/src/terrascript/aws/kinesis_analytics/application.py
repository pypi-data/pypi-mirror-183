from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    file_key: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        file_key: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        file_key: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Csv(core.Schema):

    record_column_delimiter: Union[str, core.StringOut] = core.attr(str)

    record_row_delimiter: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_column_delimiter: Union[str, core.StringOut],
        record_row_delimiter: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Csv.Args(
                record_column_delimiter=record_column_delimiter,
                record_row_delimiter=record_row_delimiter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column_delimiter: Union[str, core.StringOut] = core.arg()

        record_row_delimiter: Union[str, core.StringOut] = core.arg()


@core.schema
class Json(core.Schema):

    record_row_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_row_path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Json.Args(
                record_row_path=record_row_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_row_path: Union[str, core.StringOut] = core.arg()


@core.schema
class MappingParameters(core.Schema):

    csv: Optional[Csv] = core.attr(Csv, default=None)

    json: Optional[Json] = core.attr(Json, default=None)

    def __init__(
        self,
        *,
        csv: Optional[Csv] = None,
        json: Optional[Json] = None,
    ):
        super().__init__(
            args=MappingParameters.Args(
                csv=csv,
                json=json,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv: Optional[Csv] = core.arg(default=None)

        json: Optional[Json] = core.arg(default=None)


@core.schema
class RecordFormat(core.Schema):

    mapping_parameters: Optional[MappingParameters] = core.attr(MappingParameters, default=None)

    record_format_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        record_format_type: Union[str, core.StringOut],
        mapping_parameters: Optional[MappingParameters] = None,
    ):
        super().__init__(
            args=RecordFormat.Args(
                record_format_type=record_format_type,
                mapping_parameters=mapping_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping_parameters: Optional[MappingParameters] = core.arg(default=None)

        record_format_type: Union[str, core.StringOut] = core.arg()


@core.schema
class RecordColumns(core.Schema):

    mapping: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    sql_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        sql_type: Union[str, core.StringOut],
        mapping: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RecordColumns.Args(
                name=name,
                sql_type=sql_type,
                mapping=mapping,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        sql_type: Union[str, core.StringOut] = core.arg()


@core.schema
class ReferenceDataSourcesSchema(core.Schema):

    record_columns: Union[List[RecordColumns], core.ArrayOut[RecordColumns]] = core.attr(
        RecordColumns, kind=core.Kind.array
    )

    record_encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_columns: Union[List[RecordColumns], core.ArrayOut[RecordColumns]],
        record_format: RecordFormat,
        record_encoding: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ReferenceDataSourcesSchema.Args(
                record_columns=record_columns,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_columns: Union[List[RecordColumns], core.ArrayOut[RecordColumns]] = core.arg()

        record_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class ReferenceDataSources(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3: S3 = core.attr(S3)

    schema: ReferenceDataSourcesSchema = core.attr(ReferenceDataSourcesSchema)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        s3: S3,
        schema: ReferenceDataSourcesSchema,
        table_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ReferenceDataSources.Args(
                id=id,
                s3=s3,
                schema=schema,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        s3: S3 = core.arg()

        schema: ReferenceDataSourcesSchema = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisFirehose(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisFirehose.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisStream(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisStream.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Lambda(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Lambda.Args(
                resource_arn=resource_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class OutputsSchema(core.Schema):

    record_format_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_format_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OutputsSchema.Args(
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_format_type: Union[str, core.StringOut] = core.arg()


@core.schema
class Outputs(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kinesis_firehose: Optional[KinesisFirehose] = core.attr(KinesisFirehose, default=None)

    kinesis_stream: Optional[KinesisStream] = core.attr(KinesisStream, default=None)

    lambda_: Optional[Lambda] = core.attr(Lambda, default=None, alias="lambda")

    name: Union[str, core.StringOut] = core.attr(str)

    schema: OutputsSchema = core.attr(OutputsSchema)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        schema: OutputsSchema,
        kinesis_firehose: Optional[KinesisFirehose] = None,
        kinesis_stream: Optional[KinesisStream] = None,
        lambda_: Optional[Lambda] = None,
    ):
        super().__init__(
            args=Outputs.Args(
                id=id,
                name=name,
                schema=schema,
                kinesis_firehose=kinesis_firehose,
                kinesis_stream=kinesis_stream,
                lambda_=lambda_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        kinesis_firehose: Optional[KinesisFirehose] = core.arg(default=None)

        kinesis_stream: Optional[KinesisStream] = core.arg(default=None)

        lambda_: Optional[Lambda] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        schema: OutputsSchema = core.arg()


@core.schema
class Parallelism(core.Schema):

    count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Parallelism.Args(
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class StartingPositionConfiguration(core.Schema):

    starting_position: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        starting_position: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StartingPositionConfiguration.Args(
                starting_position=starting_position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        starting_position: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ProcessingConfiguration(core.Schema):

    lambda_: Lambda = core.attr(Lambda, alias="lambda")

    def __init__(
        self,
        *,
        lambda_: Lambda,
    ):
        super().__init__(
            args=ProcessingConfiguration.Args(
                lambda_=lambda_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_: Lambda = core.arg()


@core.schema
class Inputs(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kinesis_firehose: Optional[KinesisFirehose] = core.attr(KinesisFirehose, default=None)

    kinesis_stream: Optional[KinesisStream] = core.attr(KinesisStream, default=None)

    name_prefix: Union[str, core.StringOut] = core.attr(str)

    parallelism: Optional[Parallelism] = core.attr(Parallelism, default=None, computed=True)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    schema: ReferenceDataSourcesSchema = core.attr(ReferenceDataSourcesSchema)

    starting_position_configuration: Optional[
        Union[List[StartingPositionConfiguration], core.ArrayOut[StartingPositionConfiguration]]
    ] = core.attr(StartingPositionConfiguration, default=None, computed=True, kind=core.Kind.array)

    stream_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        name_prefix: Union[str, core.StringOut],
        schema: ReferenceDataSourcesSchema,
        stream_names: Union[List[str], core.ArrayOut[core.StringOut]],
        kinesis_firehose: Optional[KinesisFirehose] = None,
        kinesis_stream: Optional[KinesisStream] = None,
        parallelism: Optional[Parallelism] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        starting_position_configuration: Optional[
            Union[List[StartingPositionConfiguration], core.ArrayOut[StartingPositionConfiguration]]
        ] = None,
    ):
        super().__init__(
            args=Inputs.Args(
                id=id,
                name_prefix=name_prefix,
                schema=schema,
                stream_names=stream_names,
                kinesis_firehose=kinesis_firehose,
                kinesis_stream=kinesis_stream,
                parallelism=parallelism,
                processing_configuration=processing_configuration,
                starting_position_configuration=starting_position_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        kinesis_firehose: Optional[KinesisFirehose] = core.arg(default=None)

        kinesis_stream: Optional[KinesisStream] = core.arg(default=None)

        name_prefix: Union[str, core.StringOut] = core.arg()

        parallelism: Optional[Parallelism] = core.arg(default=None)

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        schema: ReferenceDataSourcesSchema = core.arg()

        starting_position_configuration: Optional[
            Union[List[StartingPositionConfiguration], core.ArrayOut[StartingPositionConfiguration]]
        ] = core.arg(default=None)

        stream_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_stream_arn: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        log_stream_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                id=id,
                log_stream_arn=log_stream_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        log_stream_arn: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_kinesis_analytics_application", namespace="aws_kinesis_analytics")
class Application(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None
    )

    code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    create_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inputs: Optional[Inputs] = core.attr(Inputs, default=None)

    last_update_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    outputs: Optional[Union[List[Outputs], core.ArrayOut[Outputs]]] = core.attr(
        Outputs, default=None, kind=core.Kind.array
    )

    reference_data_sources: Optional[ReferenceDataSources] = core.attr(
        ReferenceDataSources, default=None
    )

    start_application: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        code: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        inputs: Optional[Inputs] = None,
        outputs: Optional[Union[List[Outputs], core.ArrayOut[Outputs]]] = None,
        reference_data_sources: Optional[ReferenceDataSources] = None,
        start_application: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                cloudwatch_logging_options=cloudwatch_logging_options,
                code=code,
                description=description,
                inputs=inputs,
                outputs=outputs,
                reference_data_sources=reference_data_sources,
                start_application=start_application,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        inputs: Optional[Inputs] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        outputs: Optional[Union[List[Outputs], core.ArrayOut[Outputs]]] = core.arg(default=None)

        reference_data_sources: Optional[ReferenceDataSources] = core.arg(default=None)

        start_application: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
