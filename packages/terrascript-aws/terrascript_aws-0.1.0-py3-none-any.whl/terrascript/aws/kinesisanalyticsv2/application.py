from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VpcConfiguration(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_configuration_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_configuration_id: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_configuration_id=vpc_configuration_id,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_configuration_id: Union[str, core.StringOut] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class S3ContentLocation(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    file_key: Union[str, core.StringOut] = core.attr(str)

    object_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        file_key: Union[str, core.StringOut],
        object_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3ContentLocation.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
                object_version=object_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        file_key: Union[str, core.StringOut] = core.arg()

        object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CodeContent(core.Schema):

    s3_content_location: Optional[S3ContentLocation] = core.attr(S3ContentLocation, default=None)

    text_content: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        s3_content_location: Optional[S3ContentLocation] = None,
        text_content: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CodeContent.Args(
                s3_content_location=s3_content_location,
                text_content=text_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_content_location: Optional[S3ContentLocation] = core.arg(default=None)

        text_content: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ApplicationCodeConfiguration(core.Schema):

    code_content: Optional[CodeContent] = core.attr(CodeContent, default=None)

    code_content_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        code_content_type: Union[str, core.StringOut],
        code_content: Optional[CodeContent] = None,
    ):
        super().__init__(
            args=ApplicationCodeConfiguration.Args(
                code_content_type=code_content_type,
                code_content=code_content,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_content: Optional[CodeContent] = core.arg(default=None)

        code_content_type: Union[str, core.StringOut] = core.arg()


@core.schema
class ApplicationSnapshotConfiguration(core.Schema):

    snapshots_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        snapshots_enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ApplicationSnapshotConfiguration.Args(
                snapshots_enabled=snapshots_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        snapshots_enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class PropertyGroup(core.Schema):

    property_group_id: Union[str, core.StringOut] = core.attr(str)

    property_map: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        property_group_id: Union[str, core.StringOut],
        property_map: Union[Dict[str, str], core.MapOut[core.StringOut]],
    ):
        super().__init__(
            args=PropertyGroup.Args(
                property_group_id=property_group_id,
                property_map=property_map,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        property_group_id: Union[str, core.StringOut] = core.arg()

        property_map: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()


@core.schema
class EnvironmentProperties(core.Schema):

    property_group: Union[List[PropertyGroup], core.ArrayOut[PropertyGroup]] = core.attr(
        PropertyGroup, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        property_group: Union[List[PropertyGroup], core.ArrayOut[PropertyGroup]],
    ):
        super().__init__(
            args=EnvironmentProperties.Args(
                property_group=property_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        property_group: Union[List[PropertyGroup], core.ArrayOut[PropertyGroup]] = core.arg()


@core.schema
class MonitoringConfiguration(core.Schema):

    configuration_type: Union[str, core.StringOut] = core.attr(str)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    metrics_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        configuration_type: Union[str, core.StringOut],
        log_level: Optional[Union[str, core.StringOut]] = None,
        metrics_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MonitoringConfiguration.Args(
                configuration_type=configuration_type,
                log_level=log_level,
                metrics_level=metrics_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configuration_type: Union[str, core.StringOut] = core.arg()

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metrics_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ParallelismConfiguration(core.Schema):

    auto_scaling_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    configuration_type: Union[str, core.StringOut] = core.attr(str)

    parallelism: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    parallelism_per_kpu: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        configuration_type: Union[str, core.StringOut],
        auto_scaling_enabled: Optional[Union[bool, core.BoolOut]] = None,
        parallelism: Optional[Union[int, core.IntOut]] = None,
        parallelism_per_kpu: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ParallelismConfiguration.Args(
                configuration_type=configuration_type,
                auto_scaling_enabled=auto_scaling_enabled,
                parallelism=parallelism,
                parallelism_per_kpu=parallelism_per_kpu,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_scaling_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        configuration_type: Union[str, core.StringOut] = core.arg()

        parallelism: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parallelism_per_kpu: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class CheckpointConfiguration(core.Schema):

    checkpoint_interval: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    checkpointing_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    configuration_type: Union[str, core.StringOut] = core.attr(str)

    min_pause_between_checkpoints: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    def __init__(
        self,
        *,
        configuration_type: Union[str, core.StringOut],
        checkpoint_interval: Optional[Union[int, core.IntOut]] = None,
        checkpointing_enabled: Optional[Union[bool, core.BoolOut]] = None,
        min_pause_between_checkpoints: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CheckpointConfiguration.Args(
                configuration_type=configuration_type,
                checkpoint_interval=checkpoint_interval,
                checkpointing_enabled=checkpointing_enabled,
                min_pause_between_checkpoints=min_pause_between_checkpoints,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        checkpointing_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        configuration_type: Union[str, core.StringOut] = core.arg()

        min_pause_between_checkpoints: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class FlinkApplicationConfiguration(core.Schema):

    checkpoint_configuration: Optional[CheckpointConfiguration] = core.attr(
        CheckpointConfiguration, default=None, computed=True
    )

    monitoring_configuration: Optional[MonitoringConfiguration] = core.attr(
        MonitoringConfiguration, default=None, computed=True
    )

    parallelism_configuration: Optional[ParallelismConfiguration] = core.attr(
        ParallelismConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        *,
        checkpoint_configuration: Optional[CheckpointConfiguration] = None,
        monitoring_configuration: Optional[MonitoringConfiguration] = None,
        parallelism_configuration: Optional[ParallelismConfiguration] = None,
    ):
        super().__init__(
            args=FlinkApplicationConfiguration.Args(
                checkpoint_configuration=checkpoint_configuration,
                monitoring_configuration=monitoring_configuration,
                parallelism_configuration=parallelism_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_configuration: Optional[CheckpointConfiguration] = core.arg(default=None)

        monitoring_configuration: Optional[MonitoringConfiguration] = core.arg(default=None)

        parallelism_configuration: Optional[ParallelismConfiguration] = core.arg(default=None)


@core.schema
class ApplicationRestoreConfiguration(core.Schema):

    application_restore_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    snapshot_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        application_restore_type: Optional[Union[str, core.StringOut]] = None,
        snapshot_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ApplicationRestoreConfiguration.Args(
                application_restore_type=application_restore_type,
                snapshot_name=snapshot_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_restore_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FlinkRunConfiguration(core.Schema):

    allow_non_restored_state: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        *,
        allow_non_restored_state: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=FlinkRunConfiguration.Args(
                allow_non_restored_state=allow_non_restored_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_non_restored_state: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class RunConfiguration(core.Schema):

    application_restore_configuration: Optional[ApplicationRestoreConfiguration] = core.attr(
        ApplicationRestoreConfiguration, default=None, computed=True
    )

    flink_run_configuration: Optional[FlinkRunConfiguration] = core.attr(
        FlinkRunConfiguration, default=None, computed=True
    )

    def __init__(
        self,
        *,
        application_restore_configuration: Optional[ApplicationRestoreConfiguration] = None,
        flink_run_configuration: Optional[FlinkRunConfiguration] = None,
    ):
        super().__init__(
            args=RunConfiguration.Args(
                application_restore_configuration=application_restore_configuration,
                flink_run_configuration=flink_run_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_restore_configuration: Optional[ApplicationRestoreConfiguration] = core.arg(
            default=None
        )

        flink_run_configuration: Optional[FlinkRunConfiguration] = core.arg(default=None)


@core.schema
class KinesisStreamsInput(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisStreamsInput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class InputParallelism(core.Schema):

    count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=InputParallelism.Args(
                count=count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class KinesisFirehoseInput(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisFirehoseInput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class RecordColumn(core.Schema):

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
            args=RecordColumn.Args(
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
class CsvMappingParameters(core.Schema):

    record_column_delimiter: Union[str, core.StringOut] = core.attr(str)

    record_row_delimiter: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_column_delimiter: Union[str, core.StringOut],
        record_row_delimiter: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CsvMappingParameters.Args(
                record_column_delimiter=record_column_delimiter,
                record_row_delimiter=record_row_delimiter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column_delimiter: Union[str, core.StringOut] = core.arg()

        record_row_delimiter: Union[str, core.StringOut] = core.arg()


@core.schema
class JsonMappingParameters(core.Schema):

    record_row_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_row_path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=JsonMappingParameters.Args(
                record_row_path=record_row_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_row_path: Union[str, core.StringOut] = core.arg()


@core.schema
class MappingParameters(core.Schema):

    csv_mapping_parameters: Optional[CsvMappingParameters] = core.attr(
        CsvMappingParameters, default=None
    )

    json_mapping_parameters: Optional[JsonMappingParameters] = core.attr(
        JsonMappingParameters, default=None
    )

    def __init__(
        self,
        *,
        csv_mapping_parameters: Optional[CsvMappingParameters] = None,
        json_mapping_parameters: Optional[JsonMappingParameters] = None,
    ):
        super().__init__(
            args=MappingParameters.Args(
                csv_mapping_parameters=csv_mapping_parameters,
                json_mapping_parameters=json_mapping_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        csv_mapping_parameters: Optional[CsvMappingParameters] = core.arg(default=None)

        json_mapping_parameters: Optional[JsonMappingParameters] = core.arg(default=None)


@core.schema
class RecordFormat(core.Schema):

    mapping_parameters: MappingParameters = core.attr(MappingParameters)

    record_format_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        mapping_parameters: MappingParameters,
        record_format_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RecordFormat.Args(
                mapping_parameters=mapping_parameters,
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mapping_parameters: MappingParameters = core.arg()

        record_format_type: Union[str, core.StringOut] = core.arg()


@core.schema
class InputSchema(core.Schema):

    record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]] = core.attr(
        RecordColumn, kind=core.Kind.array
    )

    record_encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]],
        record_format: RecordFormat,
        record_encoding: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InputSchema.Args(
                record_column=record_column,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]] = core.arg()

        record_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class InputStartingPositionConfiguration(core.Schema):

    input_starting_position: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        input_starting_position: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InputStartingPositionConfiguration.Args(
                input_starting_position=input_starting_position,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_starting_position: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InputLambdaProcessor(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InputLambdaProcessor.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class InputProcessingConfiguration(core.Schema):

    input_lambda_processor: InputLambdaProcessor = core.attr(InputLambdaProcessor)

    def __init__(
        self,
        *,
        input_lambda_processor: InputLambdaProcessor,
    ):
        super().__init__(
            args=InputProcessingConfiguration.Args(
                input_lambda_processor=input_lambda_processor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_lambda_processor: InputLambdaProcessor = core.arg()


@core.schema
class Input(core.Schema):

    in_app_stream_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    input_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_parallelism: Optional[InputParallelism] = core.attr(
        InputParallelism, default=None, computed=True
    )

    input_processing_configuration: Optional[InputProcessingConfiguration] = core.attr(
        InputProcessingConfiguration, default=None
    )

    input_schema: InputSchema = core.attr(InputSchema)

    input_starting_position_configuration: Optional[
        Union[
            List[InputStartingPositionConfiguration],
            core.ArrayOut[InputStartingPositionConfiguration],
        ]
    ] = core.attr(
        InputStartingPositionConfiguration, default=None, computed=True, kind=core.Kind.array
    )

    kinesis_firehose_input: Optional[KinesisFirehoseInput] = core.attr(
        KinesisFirehoseInput, default=None
    )

    kinesis_streams_input: Optional[KinesisStreamsInput] = core.attr(
        KinesisStreamsInput, default=None
    )

    name_prefix: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        in_app_stream_names: Union[List[str], core.ArrayOut[core.StringOut]],
        input_id: Union[str, core.StringOut],
        input_schema: InputSchema,
        name_prefix: Union[str, core.StringOut],
        input_parallelism: Optional[InputParallelism] = None,
        input_processing_configuration: Optional[InputProcessingConfiguration] = None,
        input_starting_position_configuration: Optional[
            Union[
                List[InputStartingPositionConfiguration],
                core.ArrayOut[InputStartingPositionConfiguration],
            ]
        ] = None,
        kinesis_firehose_input: Optional[KinesisFirehoseInput] = None,
        kinesis_streams_input: Optional[KinesisStreamsInput] = None,
    ):
        super().__init__(
            args=Input.Args(
                in_app_stream_names=in_app_stream_names,
                input_id=input_id,
                input_schema=input_schema,
                name_prefix=name_prefix,
                input_parallelism=input_parallelism,
                input_processing_configuration=input_processing_configuration,
                input_starting_position_configuration=input_starting_position_configuration,
                kinesis_firehose_input=kinesis_firehose_input,
                kinesis_streams_input=kinesis_streams_input,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        in_app_stream_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        input_id: Union[str, core.StringOut] = core.arg()

        input_parallelism: Optional[InputParallelism] = core.arg(default=None)

        input_processing_configuration: Optional[InputProcessingConfiguration] = core.arg(
            default=None
        )

        input_schema: InputSchema = core.arg()

        input_starting_position_configuration: Optional[
            Union[
                List[InputStartingPositionConfiguration],
                core.ArrayOut[InputStartingPositionConfiguration],
            ]
        ] = core.arg(default=None)

        kinesis_firehose_input: Optional[KinesisFirehoseInput] = core.arg(default=None)

        kinesis_streams_input: Optional[KinesisStreamsInput] = core.arg(default=None)

        name_prefix: Union[str, core.StringOut] = core.arg()


@core.schema
class LambdaOutput(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LambdaOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationSchema(core.Schema):

    record_format_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        record_format_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DestinationSchema.Args(
                record_format_type=record_format_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_format_type: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisFirehoseOutput(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisFirehoseOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisStreamsOutput(core.Schema):

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisStreamsOutput.Args(
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Output(core.Schema):

    destination_schema: DestinationSchema = core.attr(DestinationSchema)

    kinesis_firehose_output: Optional[KinesisFirehoseOutput] = core.attr(
        KinesisFirehoseOutput, default=None
    )

    kinesis_streams_output: Optional[KinesisStreamsOutput] = core.attr(
        KinesisStreamsOutput, default=None
    )

    lambda_output: Optional[LambdaOutput] = core.attr(LambdaOutput, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    output_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination_schema: DestinationSchema,
        name: Union[str, core.StringOut],
        output_id: Union[str, core.StringOut],
        kinesis_firehose_output: Optional[KinesisFirehoseOutput] = None,
        kinesis_streams_output: Optional[KinesisStreamsOutput] = None,
        lambda_output: Optional[LambdaOutput] = None,
    ):
        super().__init__(
            args=Output.Args(
                destination_schema=destination_schema,
                name=name,
                output_id=output_id,
                kinesis_firehose_output=kinesis_firehose_output,
                kinesis_streams_output=kinesis_streams_output,
                lambda_output=lambda_output,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_schema: DestinationSchema = core.arg()

        kinesis_firehose_output: Optional[KinesisFirehoseOutput] = core.arg(default=None)

        kinesis_streams_output: Optional[KinesisStreamsOutput] = core.arg(default=None)

        lambda_output: Optional[LambdaOutput] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        output_id: Union[str, core.StringOut] = core.arg()


@core.schema
class ReferenceSchema(core.Schema):

    record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]] = core.attr(
        RecordColumn, kind=core.Kind.array
    )

    record_encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    record_format: RecordFormat = core.attr(RecordFormat)

    def __init__(
        self,
        *,
        record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]],
        record_format: RecordFormat,
        record_encoding: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ReferenceSchema.Args(
                record_column=record_column,
                record_format=record_format,
                record_encoding=record_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        record_column: Union[List[RecordColumn], core.ArrayOut[RecordColumn]] = core.arg()

        record_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        record_format: RecordFormat = core.arg()


@core.schema
class S3ReferenceDataSource(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    file_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        file_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=S3ReferenceDataSource.Args(
                bucket_arn=bucket_arn,
                file_key=file_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        file_key: Union[str, core.StringOut] = core.arg()


@core.schema
class ReferenceDataSource(core.Schema):

    reference_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    reference_schema: ReferenceSchema = core.attr(ReferenceSchema)

    s3_reference_data_source: S3ReferenceDataSource = core.attr(S3ReferenceDataSource)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        reference_id: Union[str, core.StringOut],
        reference_schema: ReferenceSchema,
        s3_reference_data_source: S3ReferenceDataSource,
        table_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ReferenceDataSource.Args(
                reference_id=reference_id,
                reference_schema=reference_schema,
                s3_reference_data_source=s3_reference_data_source,
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reference_id: Union[str, core.StringOut] = core.arg()

        reference_schema: ReferenceSchema = core.arg()

        s3_reference_data_source: S3ReferenceDataSource = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()


@core.schema
class SqlApplicationConfiguration(core.Schema):

    input: Optional[Input] = core.attr(Input, default=None)

    output: Optional[Union[List[Output], core.ArrayOut[Output]]] = core.attr(
        Output, default=None, kind=core.Kind.array
    )

    reference_data_source: Optional[ReferenceDataSource] = core.attr(
        ReferenceDataSource, default=None
    )

    def __init__(
        self,
        *,
        input: Optional[Input] = None,
        output: Optional[Union[List[Output], core.ArrayOut[Output]]] = None,
        reference_data_source: Optional[ReferenceDataSource] = None,
    ):
        super().__init__(
            args=SqlApplicationConfiguration.Args(
                input=input,
                output=output,
                reference_data_source=reference_data_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input: Optional[Input] = core.arg(default=None)

        output: Optional[Union[List[Output], core.ArrayOut[Output]]] = core.arg(default=None)

        reference_data_source: Optional[ReferenceDataSource] = core.arg(default=None)


@core.schema
class ApplicationConfiguration(core.Schema):

    application_code_configuration: ApplicationCodeConfiguration = core.attr(
        ApplicationCodeConfiguration
    )

    application_snapshot_configuration: Optional[ApplicationSnapshotConfiguration] = core.attr(
        ApplicationSnapshotConfiguration, default=None, computed=True
    )

    environment_properties: Optional[EnvironmentProperties] = core.attr(
        EnvironmentProperties, default=None
    )

    flink_application_configuration: Optional[FlinkApplicationConfiguration] = core.attr(
        FlinkApplicationConfiguration, default=None, computed=True
    )

    run_configuration: Optional[RunConfiguration] = core.attr(
        RunConfiguration, default=None, computed=True
    )

    sql_application_configuration: Optional[SqlApplicationConfiguration] = core.attr(
        SqlApplicationConfiguration, default=None
    )

    vpc_configuration: Optional[VpcConfiguration] = core.attr(VpcConfiguration, default=None)

    def __init__(
        self,
        *,
        application_code_configuration: ApplicationCodeConfiguration,
        application_snapshot_configuration: Optional[ApplicationSnapshotConfiguration] = None,
        environment_properties: Optional[EnvironmentProperties] = None,
        flink_application_configuration: Optional[FlinkApplicationConfiguration] = None,
        run_configuration: Optional[RunConfiguration] = None,
        sql_application_configuration: Optional[SqlApplicationConfiguration] = None,
        vpc_configuration: Optional[VpcConfiguration] = None,
    ):
        super().__init__(
            args=ApplicationConfiguration.Args(
                application_code_configuration=application_code_configuration,
                application_snapshot_configuration=application_snapshot_configuration,
                environment_properties=environment_properties,
                flink_application_configuration=flink_application_configuration,
                run_configuration=run_configuration,
                sql_application_configuration=sql_application_configuration,
                vpc_configuration=vpc_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        application_code_configuration: ApplicationCodeConfiguration = core.arg()

        application_snapshot_configuration: Optional[ApplicationSnapshotConfiguration] = core.arg(
            default=None
        )

        environment_properties: Optional[EnvironmentProperties] = core.arg(default=None)

        flink_application_configuration: Optional[FlinkApplicationConfiguration] = core.arg(
            default=None
        )

        run_configuration: Optional[RunConfiguration] = core.arg(default=None)

        sql_application_configuration: Optional[SqlApplicationConfiguration] = core.arg(
            default=None
        )

        vpc_configuration: Optional[VpcConfiguration] = core.arg(default=None)


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    cloudwatch_logging_option_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_logging_option_id: Union[str, core.StringOut],
        log_stream_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                cloudwatch_logging_option_id=cloudwatch_logging_option_id,
                log_stream_arn=log_stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_option_id: Union[str, core.StringOut] = core.arg()

        log_stream_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_kinesisanalyticsv2_application", namespace="aws_kinesisanalyticsv2")
class Application(core.Resource):

    application_configuration: Optional[ApplicationConfiguration] = core.attr(
        ApplicationConfiguration, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None
    )

    create_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_stop: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_update_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    runtime_environment: Union[str, core.StringOut] = core.attr(str)

    service_execution_role: Union[str, core.StringOut] = core.attr(str)

    start_application: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        runtime_environment: Union[str, core.StringOut],
        service_execution_role: Union[str, core.StringOut],
        application_configuration: Optional[ApplicationConfiguration] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        force_stop: Optional[Union[bool, core.BoolOut]] = None,
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
                runtime_environment=runtime_environment,
                service_execution_role=service_execution_role,
                application_configuration=application_configuration,
                cloudwatch_logging_options=cloudwatch_logging_options,
                description=description,
                force_stop=force_stop,
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
        application_configuration: Optional[ApplicationConfiguration] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_stop: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        runtime_environment: Union[str, core.StringOut] = core.arg()

        service_execution_role: Union[str, core.StringOut] = core.arg()

        start_application: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
