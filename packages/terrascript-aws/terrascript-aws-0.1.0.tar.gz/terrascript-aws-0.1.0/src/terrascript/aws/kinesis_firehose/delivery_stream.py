from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CommonAttributes(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CommonAttributes.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RequestConfiguration(core.Schema):

    common_attributes: Optional[
        Union[List[CommonAttributes], core.ArrayOut[CommonAttributes]]
    ] = core.attr(CommonAttributes, default=None, kind=core.Kind.array)

    content_encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        common_attributes: Optional[
            Union[List[CommonAttributes], core.ArrayOut[CommonAttributes]]
        ] = None,
        content_encoding: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RequestConfiguration.Args(
                common_attributes=common_attributes,
                content_encoding=content_encoding,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        common_attributes: Optional[
            Union[List[CommonAttributes], core.ArrayOut[CommonAttributes]]
        ] = core.arg(default=None)

        content_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CloudwatchLoggingOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    log_group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_stream_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_group_name: Optional[Union[str, core.StringOut]] = None,
        log_stream_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CloudwatchLoggingOptions.Args(
                enabled=enabled,
                log_group_name=log_group_name,
                log_stream_name=log_stream_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_stream_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Parameters(core.Schema):

    parameter_name: Union[str, core.StringOut] = core.attr(str)

    parameter_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        parameter_name: Union[str, core.StringOut],
        parameter_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Parameters.Args(
                parameter_name=parameter_name,
                parameter_value=parameter_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameter_name: Union[str, core.StringOut] = core.arg()

        parameter_value: Union[str, core.StringOut] = core.arg()


@core.schema
class Processors(core.Schema):

    parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = core.attr(
        Parameters, default=None, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = None,
    ):
        super().__init__(
            args=Processors.Args(
                type=type,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: Optional[Union[List[Parameters], core.ArrayOut[Parameters]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ProcessingConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    processors: Optional[Union[List[Processors], core.ArrayOut[Processors]]] = core.attr(
        Processors, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        processors: Optional[Union[List[Processors], core.ArrayOut[Processors]]] = None,
    ):
        super().__init__(
            args=ProcessingConfiguration.Args(
                enabled=enabled,
                processors=processors,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        processors: Optional[Union[List[Processors], core.ArrayOut[Processors]]] = core.arg(
            default=None
        )


@core.schema
class HttpEndpointConfiguration(core.Schema):

    access_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    buffering_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffering_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    request_configuration: Optional[RequestConfiguration] = core.attr(
        RequestConfiguration, default=None, computed=True
    )

    retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_backup_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        url: Union[str, core.StringOut],
        access_key: Optional[Union[str, core.StringOut]] = None,
        buffering_interval: Optional[Union[int, core.IntOut]] = None,
        buffering_size: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        request_configuration: Optional[RequestConfiguration] = None,
        retry_duration: Optional[Union[int, core.IntOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        s3_backup_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=HttpEndpointConfiguration.Args(
                url=url,
                access_key=access_key,
                buffering_interval=buffering_interval,
                buffering_size=buffering_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                name=name,
                processing_configuration=processing_configuration,
                request_configuration=request_configuration,
                retry_duration=retry_duration,
                role_arn=role_arn,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        buffering_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffering_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        request_configuration: Optional[RequestConfiguration] = core.arg(default=None)

        retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_backup_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        url: Union[str, core.StringOut] = core.arg()


@core.schema
class S3Configuration(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    buffer_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffer_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_output_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        buffer_interval: Optional[Union[int, core.IntOut]] = None,
        buffer_size: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        compression_format: Optional[Union[str, core.StringOut]] = None,
        error_output_prefix: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        buffer_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffer_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        compression_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        error_output_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ServerSideEncryption(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        key_arn: Optional[Union[str, core.StringOut]] = None,
        key_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ServerSideEncryption.Args(
                enabled=enabled,
                key_arn=key_arn,
                key_type=key_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class S3BackupConfiguration(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    buffer_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffer_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    error_output_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        buffer_interval: Optional[Union[int, core.IntOut]] = None,
        buffer_size: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        compression_format: Optional[Union[str, core.StringOut]] = None,
        error_output_prefix: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3BackupConfiguration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        buffer_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffer_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        compression_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        error_output_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class RedshiftConfiguration(core.Schema):

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    cluster_jdbcurl: Union[str, core.StringOut] = core.attr(str)

    copy_options: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_table_columns: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_table_name: Union[str, core.StringOut] = core.attr(str)

    password: Union[str, core.StringOut] = core.attr(str)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    s3_backup_configuration: Optional[S3BackupConfiguration] = core.attr(
        S3BackupConfiguration, default=None
    )

    s3_backup_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cluster_jdbcurl: Union[str, core.StringOut],
        data_table_name: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        copy_options: Optional[Union[str, core.StringOut]] = None,
        data_table_columns: Optional[Union[str, core.StringOut]] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        retry_duration: Optional[Union[int, core.IntOut]] = None,
        s3_backup_configuration: Optional[S3BackupConfiguration] = None,
        s3_backup_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RedshiftConfiguration.Args(
                cluster_jdbcurl=cluster_jdbcurl,
                data_table_name=data_table_name,
                password=password,
                role_arn=role_arn,
                username=username,
                cloudwatch_logging_options=cloudwatch_logging_options,
                copy_options=copy_options,
                data_table_columns=data_table_columns,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_configuration=s3_backup_configuration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        cluster_jdbcurl: Union[str, core.StringOut] = core.arg()

        copy_options: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_table_columns: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_table_name: Union[str, core.StringOut] = core.arg()

        password: Union[str, core.StringOut] = core.arg()

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        s3_backup_configuration: Optional[S3BackupConfiguration] = core.arg(default=None)

        s3_backup_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class HiveJsonSerDe(core.Schema):

    timestamp_formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        timestamp_formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=HiveJsonSerDe.Args(
                timestamp_formats=timestamp_formats,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        timestamp_formats: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class OpenXJsonSerDe(core.Schema):

    case_insensitive: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    column_to_json_key_mappings: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    convert_dots_in_json_keys_to_underscores: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        case_insensitive: Optional[Union[bool, core.BoolOut]] = None,
        column_to_json_key_mappings: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        convert_dots_in_json_keys_to_underscores: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=OpenXJsonSerDe.Args(
                case_insensitive=case_insensitive,
                column_to_json_key_mappings=column_to_json_key_mappings,
                convert_dots_in_json_keys_to_underscores=convert_dots_in_json_keys_to_underscores,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        case_insensitive: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        column_to_json_key_mappings: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        convert_dots_in_json_keys_to_underscores: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class Deserializer(core.Schema):

    hive_json_ser_de: Optional[HiveJsonSerDe] = core.attr(HiveJsonSerDe, default=None)

    open_x_json_ser_de: Optional[OpenXJsonSerDe] = core.attr(OpenXJsonSerDe, default=None)

    def __init__(
        self,
        *,
        hive_json_ser_de: Optional[HiveJsonSerDe] = None,
        open_x_json_ser_de: Optional[OpenXJsonSerDe] = None,
    ):
        super().__init__(
            args=Deserializer.Args(
                hive_json_ser_de=hive_json_ser_de,
                open_x_json_ser_de=open_x_json_ser_de,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hive_json_ser_de: Optional[HiveJsonSerDe] = core.arg(default=None)

        open_x_json_ser_de: Optional[OpenXJsonSerDe] = core.arg(default=None)


@core.schema
class InputFormatConfiguration(core.Schema):

    deserializer: Deserializer = core.attr(Deserializer)

    def __init__(
        self,
        *,
        deserializer: Deserializer,
    ):
        super().__init__(
            args=InputFormatConfiguration.Args(
                deserializer=deserializer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deserializer: Deserializer = core.arg()


@core.schema
class ParquetSerDe(core.Schema):

    block_size_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    compression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_dictionary_compression: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    max_padding_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    page_size_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    writer_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        block_size_bytes: Optional[Union[int, core.IntOut]] = None,
        compression: Optional[Union[str, core.StringOut]] = None,
        enable_dictionary_compression: Optional[Union[bool, core.BoolOut]] = None,
        max_padding_bytes: Optional[Union[int, core.IntOut]] = None,
        page_size_bytes: Optional[Union[int, core.IntOut]] = None,
        writer_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ParquetSerDe.Args(
                block_size_bytes=block_size_bytes,
                compression=compression,
                enable_dictionary_compression=enable_dictionary_compression,
                max_padding_bytes=max_padding_bytes,
                page_size_bytes=page_size_bytes,
                writer_version=writer_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_size_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        compression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_dictionary_compression: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_padding_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        page_size_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        writer_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OrcSerDe(core.Schema):

    block_size_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    bloom_filter_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    bloom_filter_false_positive_probability: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    compression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dictionary_key_threshold: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    enable_padding: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    format_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    padding_tolerance: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    row_index_stride: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    stripe_size_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        block_size_bytes: Optional[Union[int, core.IntOut]] = None,
        bloom_filter_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        bloom_filter_false_positive_probability: Optional[Union[float, core.FloatOut]] = None,
        compression: Optional[Union[str, core.StringOut]] = None,
        dictionary_key_threshold: Optional[Union[float, core.FloatOut]] = None,
        enable_padding: Optional[Union[bool, core.BoolOut]] = None,
        format_version: Optional[Union[str, core.StringOut]] = None,
        padding_tolerance: Optional[Union[float, core.FloatOut]] = None,
        row_index_stride: Optional[Union[int, core.IntOut]] = None,
        stripe_size_bytes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=OrcSerDe.Args(
                block_size_bytes=block_size_bytes,
                bloom_filter_columns=bloom_filter_columns,
                bloom_filter_false_positive_probability=bloom_filter_false_positive_probability,
                compression=compression,
                dictionary_key_threshold=dictionary_key_threshold,
                enable_padding=enable_padding,
                format_version=format_version,
                padding_tolerance=padding_tolerance,
                row_index_stride=row_index_stride,
                stripe_size_bytes=stripe_size_bytes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_size_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        bloom_filter_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        bloom_filter_false_positive_probability: Optional[Union[float, core.FloatOut]] = core.arg(
            default=None
        )

        compression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dictionary_key_threshold: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        enable_padding: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        format_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        padding_tolerance: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        row_index_stride: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        stripe_size_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Serializer(core.Schema):

    orc_ser_de: Optional[OrcSerDe] = core.attr(OrcSerDe, default=None)

    parquet_ser_de: Optional[ParquetSerDe] = core.attr(ParquetSerDe, default=None)

    def __init__(
        self,
        *,
        orc_ser_de: Optional[OrcSerDe] = None,
        parquet_ser_de: Optional[ParquetSerDe] = None,
    ):
        super().__init__(
            args=Serializer.Args(
                orc_ser_de=orc_ser_de,
                parquet_ser_de=parquet_ser_de,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        orc_ser_de: Optional[OrcSerDe] = core.arg(default=None)

        parquet_ser_de: Optional[ParquetSerDe] = core.arg(default=None)


@core.schema
class OutputFormatConfiguration(core.Schema):

    serializer: Serializer = core.attr(Serializer)

    def __init__(
        self,
        *,
        serializer: Serializer,
    ):
        super().__init__(
            args=OutputFormatConfiguration.Args(
                serializer=serializer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        serializer: Serializer = core.arg()


@core.schema
class SchemaConfiguration(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    table_name: Union[str, core.StringOut] = core.attr(str)

    version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        version_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SchemaConfiguration.Args(
                database_name=database_name,
                role_arn=role_arn,
                table_name=table_name,
                catalog_id=catalog_id,
                region=region,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()

        version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DataFormatConversionConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    input_format_configuration: InputFormatConfiguration = core.attr(InputFormatConfiguration)

    output_format_configuration: OutputFormatConfiguration = core.attr(OutputFormatConfiguration)

    schema_configuration: SchemaConfiguration = core.attr(SchemaConfiguration)

    def __init__(
        self,
        *,
        input_format_configuration: InputFormatConfiguration,
        output_format_configuration: OutputFormatConfiguration,
        schema_configuration: SchemaConfiguration,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=DataFormatConversionConfiguration.Args(
                input_format_configuration=input_format_configuration,
                output_format_configuration=output_format_configuration,
                schema_configuration=schema_configuration,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        input_format_configuration: InputFormatConfiguration = core.arg()

        output_format_configuration: OutputFormatConfiguration = core.arg()

        schema_configuration: SchemaConfiguration = core.arg()


@core.schema
class DynamicPartitioningConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        retry_duration: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DynamicPartitioningConfiguration.Args(
                enabled=enabled,
                retry_duration=retry_duration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ExtendedS3Configuration(core.Schema):

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    buffer_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffer_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    compression_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_format_conversion_configuration: Optional[DataFormatConversionConfiguration] = core.attr(
        DataFormatConversionConfiguration, default=None
    )

    dynamic_partitioning_configuration: Optional[DynamicPartitioningConfiguration] = core.attr(
        DynamicPartitioningConfiguration, default=None
    )

    error_output_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    role_arn: Union[str, core.StringOut] = core.attr(str)

    s3_backup_configuration: Optional[S3BackupConfiguration] = core.attr(
        S3BackupConfiguration, default=None
    )

    s3_backup_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        buffer_interval: Optional[Union[int, core.IntOut]] = None,
        buffer_size: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        compression_format: Optional[Union[str, core.StringOut]] = None,
        data_format_conversion_configuration: Optional[DataFormatConversionConfiguration] = None,
        dynamic_partitioning_configuration: Optional[DynamicPartitioningConfiguration] = None,
        error_output_prefix: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        s3_backup_configuration: Optional[S3BackupConfiguration] = None,
        s3_backup_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ExtendedS3Configuration.Args(
                bucket_arn=bucket_arn,
                role_arn=role_arn,
                buffer_interval=buffer_interval,
                buffer_size=buffer_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                compression_format=compression_format,
                data_format_conversion_configuration=data_format_conversion_configuration,
                dynamic_partitioning_configuration=dynamic_partitioning_configuration,
                error_output_prefix=error_output_prefix,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
                processing_configuration=processing_configuration,
                s3_backup_configuration=s3_backup_configuration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_arn: Union[str, core.StringOut] = core.arg()

        buffer_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffer_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        compression_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_format_conversion_configuration: Optional[
            DataFormatConversionConfiguration
        ] = core.arg(default=None)

        dynamic_partitioning_configuration: Optional[DynamicPartitioningConfiguration] = core.arg(
            default=None
        )

        error_output_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        s3_backup_configuration: Optional[S3BackupConfiguration] = core.arg(default=None)

        s3_backup_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    role_arn: Union[str, core.StringOut] = core.attr(str)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                role_arn=role_arn,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: Union[str, core.StringOut] = core.arg()

        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class ElasticsearchConfiguration(core.Schema):

    buffering_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    buffering_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    cluster_endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    index_name: Union[str, core.StringOut] = core.attr(str)

    index_rotation_period: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    s3_backup_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        *,
        index_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        buffering_interval: Optional[Union[int, core.IntOut]] = None,
        buffering_size: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        cluster_endpoint: Optional[Union[str, core.StringOut]] = None,
        domain_arn: Optional[Union[str, core.StringOut]] = None,
        index_rotation_period: Optional[Union[str, core.StringOut]] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        retry_duration: Optional[Union[int, core.IntOut]] = None,
        s3_backup_mode: Optional[Union[str, core.StringOut]] = None,
        type_name: Optional[Union[str, core.StringOut]] = None,
        vpc_config: Optional[VpcConfig] = None,
    ):
        super().__init__(
            args=ElasticsearchConfiguration.Args(
                index_name=index_name,
                role_arn=role_arn,
                buffering_interval=buffering_interval,
                buffering_size=buffering_size,
                cloudwatch_logging_options=cloudwatch_logging_options,
                cluster_endpoint=cluster_endpoint,
                domain_arn=domain_arn,
                index_rotation_period=index_rotation_period,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_mode=s3_backup_mode,
                type_name=type_name,
                vpc_config=vpc_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        buffering_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        buffering_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        cluster_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_name: Union[str, core.StringOut] = core.arg()

        index_rotation_period: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        s3_backup_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_config: Optional[VpcConfig] = core.arg(default=None)


@core.schema
class SplunkConfiguration(core.Schema):

    cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.attr(
        CloudwatchLoggingOptions, default=None, computed=True
    )

    hec_acknowledgment_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    hec_endpoint: Union[str, core.StringOut] = core.attr(str)

    hec_endpoint_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hec_token: Union[str, core.StringOut] = core.attr(str)

    processing_configuration: Optional[ProcessingConfiguration] = core.attr(
        ProcessingConfiguration, default=None
    )

    retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    s3_backup_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        hec_endpoint: Union[str, core.StringOut],
        hec_token: Union[str, core.StringOut],
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = None,
        hec_acknowledgment_timeout: Optional[Union[int, core.IntOut]] = None,
        hec_endpoint_type: Optional[Union[str, core.StringOut]] = None,
        processing_configuration: Optional[ProcessingConfiguration] = None,
        retry_duration: Optional[Union[int, core.IntOut]] = None,
        s3_backup_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SplunkConfiguration.Args(
                hec_endpoint=hec_endpoint,
                hec_token=hec_token,
                cloudwatch_logging_options=cloudwatch_logging_options,
                hec_acknowledgment_timeout=hec_acknowledgment_timeout,
                hec_endpoint_type=hec_endpoint_type,
                processing_configuration=processing_configuration,
                retry_duration=retry_duration,
                s3_backup_mode=s3_backup_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logging_options: Optional[CloudwatchLoggingOptions] = core.arg(default=None)

        hec_acknowledgment_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        hec_endpoint: Union[str, core.StringOut] = core.arg()

        hec_endpoint_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hec_token: Union[str, core.StringOut] = core.arg()

        processing_configuration: Optional[ProcessingConfiguration] = core.arg(default=None)

        retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        s3_backup_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class KinesisSourceConfiguration(core.Schema):

    kinesis_stream_arn: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        kinesis_stream_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisSourceConfiguration.Args(
                kinesis_stream_arn=kinesis_stream_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_stream_arn: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_kinesis_firehose_delivery_stream", namespace="aws_kinesis_firehose")
class DeliveryStream(core.Resource):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    destination: Union[str, core.StringOut] = core.attr(str)

    destination_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    elasticsearch_configuration: Optional[ElasticsearchConfiguration] = core.attr(
        ElasticsearchConfiguration, default=None
    )

    extended_s3_configuration: Optional[ExtendedS3Configuration] = core.attr(
        ExtendedS3Configuration, default=None
    )

    http_endpoint_configuration: Optional[HttpEndpointConfiguration] = core.attr(
        HttpEndpointConfiguration, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kinesis_source_configuration: Optional[KinesisSourceConfiguration] = core.attr(
        KinesisSourceConfiguration, default=None
    )

    name: Union[str, core.StringOut] = core.attr(str)

    redshift_configuration: Optional[RedshiftConfiguration] = core.attr(
        RedshiftConfiguration, default=None
    )

    s3_configuration: Optional[S3Configuration] = core.attr(S3Configuration, default=None)

    server_side_encryption: Optional[ServerSideEncryption] = core.attr(
        ServerSideEncryption, default=None
    )

    splunk_configuration: Optional[SplunkConfiguration] = core.attr(
        SplunkConfiguration, default=None
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        arn: Optional[Union[str, core.StringOut]] = None,
        destination_id: Optional[Union[str, core.StringOut]] = None,
        elasticsearch_configuration: Optional[ElasticsearchConfiguration] = None,
        extended_s3_configuration: Optional[ExtendedS3Configuration] = None,
        http_endpoint_configuration: Optional[HttpEndpointConfiguration] = None,
        kinesis_source_configuration: Optional[KinesisSourceConfiguration] = None,
        redshift_configuration: Optional[RedshiftConfiguration] = None,
        s3_configuration: Optional[S3Configuration] = None,
        server_side_encryption: Optional[ServerSideEncryption] = None,
        splunk_configuration: Optional[SplunkConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        version_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeliveryStream.Args(
                destination=destination,
                name=name,
                arn=arn,
                destination_id=destination_id,
                elasticsearch_configuration=elasticsearch_configuration,
                extended_s3_configuration=extended_s3_configuration,
                http_endpoint_configuration=http_endpoint_configuration,
                kinesis_source_configuration=kinesis_source_configuration,
                redshift_configuration=redshift_configuration,
                s3_configuration=s3_configuration,
                server_side_encryption=server_side_encryption,
                splunk_configuration=splunk_configuration,
                tags=tags,
                tags_all=tags_all,
                version_id=version_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination: Union[str, core.StringOut] = core.arg()

        destination_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticsearch_configuration: Optional[ElasticsearchConfiguration] = core.arg(default=None)

        extended_s3_configuration: Optional[ExtendedS3Configuration] = core.arg(default=None)

        http_endpoint_configuration: Optional[HttpEndpointConfiguration] = core.arg(default=None)

        kinesis_source_configuration: Optional[KinesisSourceConfiguration] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        redshift_configuration: Optional[RedshiftConfiguration] = core.arg(default=None)

        s3_configuration: Optional[S3Configuration] = core.arg(default=None)

        server_side_encryption: Optional[ServerSideEncryption] = core.arg(default=None)

        splunk_configuration: Optional[SplunkConfiguration] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
