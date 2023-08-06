from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class KafkaSettings(core.Schema):

    broker: Union[str, core.StringOut] = core.attr(str)

    include_control_details: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_null_and_empty: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_partition_value: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    include_transaction_details: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    message_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    message_max_bytes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    no_hex_prefix: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    sasl_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sasl_username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_ca_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_client_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_client_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_client_key_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    topic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        broker: Union[str, core.StringOut],
        include_control_details: Optional[Union[bool, core.BoolOut]] = None,
        include_null_and_empty: Optional[Union[bool, core.BoolOut]] = None,
        include_partition_value: Optional[Union[bool, core.BoolOut]] = None,
        include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = None,
        include_transaction_details: Optional[Union[bool, core.BoolOut]] = None,
        message_format: Optional[Union[str, core.StringOut]] = None,
        message_max_bytes: Optional[Union[int, core.IntOut]] = None,
        no_hex_prefix: Optional[Union[bool, core.BoolOut]] = None,
        partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = None,
        sasl_password: Optional[Union[str, core.StringOut]] = None,
        sasl_username: Optional[Union[str, core.StringOut]] = None,
        security_protocol: Optional[Union[str, core.StringOut]] = None,
        ssl_ca_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        ssl_client_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        ssl_client_key_arn: Optional[Union[str, core.StringOut]] = None,
        ssl_client_key_password: Optional[Union[str, core.StringOut]] = None,
        topic: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KafkaSettings.Args(
                broker=broker,
                include_control_details=include_control_details,
                include_null_and_empty=include_null_and_empty,
                include_partition_value=include_partition_value,
                include_table_alter_operations=include_table_alter_operations,
                include_transaction_details=include_transaction_details,
                message_format=message_format,
                message_max_bytes=message_max_bytes,
                no_hex_prefix=no_hex_prefix,
                partition_include_schema_table=partition_include_schema_table,
                sasl_password=sasl_password,
                sasl_username=sasl_username,
                security_protocol=security_protocol,
                ssl_ca_certificate_arn=ssl_ca_certificate_arn,
                ssl_client_certificate_arn=ssl_client_certificate_arn,
                ssl_client_key_arn=ssl_client_key_arn,
                ssl_client_key_password=ssl_client_key_password,
                topic=topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker: Union[str, core.StringOut] = core.arg()

        include_control_details: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_null_and_empty: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_partition_value: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_transaction_details: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        message_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        message_max_bytes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        no_hex_prefix: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sasl_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sasl_username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_ca_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_client_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_client_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_client_key_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topic: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RedshiftSettings(core.Schema):

    bucket_folder: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    service_access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_folder: Optional[Union[str, core.StringOut]] = None,
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        encryption_mode: Optional[Union[str, core.StringOut]] = None,
        server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        service_access_role_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RedshiftSettings.Args(
                bucket_folder=bucket_folder,
                bucket_name=bucket_name,
                encryption_mode=encryption_mode,
                server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
                service_access_role_arn=service_access_role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_folder: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        service_access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MongodbSettings(core.Schema):

    auth_mechanism: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    auth_source: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    auth_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    docs_to_investigate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    extract_doc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    nesting_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auth_mechanism: Optional[Union[str, core.StringOut]] = None,
        auth_source: Optional[Union[str, core.StringOut]] = None,
        auth_type: Optional[Union[str, core.StringOut]] = None,
        docs_to_investigate: Optional[Union[str, core.StringOut]] = None,
        extract_doc_id: Optional[Union[str, core.StringOut]] = None,
        nesting_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MongodbSettings.Args(
                auth_mechanism=auth_mechanism,
                auth_source=auth_source,
                auth_type=auth_type,
                docs_to_investigate=docs_to_investigate,
                extract_doc_id=extract_doc_id,
                nesting_level=nesting_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth_mechanism: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auth_source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auth_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        docs_to_investigate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        extract_doc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nesting_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class KinesisSettings(core.Schema):

    include_control_details: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_null_and_empty: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_partition_value: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    include_transaction_details: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    message_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    service_access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stream_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        include_control_details: Optional[Union[bool, core.BoolOut]] = None,
        include_null_and_empty: Optional[Union[bool, core.BoolOut]] = None,
        include_partition_value: Optional[Union[bool, core.BoolOut]] = None,
        include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = None,
        include_transaction_details: Optional[Union[bool, core.BoolOut]] = None,
        message_format: Optional[Union[str, core.StringOut]] = None,
        partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = None,
        service_access_role_arn: Optional[Union[str, core.StringOut]] = None,
        stream_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KinesisSettings.Args(
                include_control_details=include_control_details,
                include_null_and_empty=include_null_and_empty,
                include_partition_value=include_partition_value,
                include_table_alter_operations=include_table_alter_operations,
                include_transaction_details=include_transaction_details,
                message_format=message_format,
                partition_include_schema_table=partition_include_schema_table,
                service_access_role_arn=service_access_role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        include_control_details: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_null_and_empty: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_partition_value: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_table_alter_operations: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_transaction_details: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        message_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        partition_include_schema_table: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        service_access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stream_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ElasticsearchSettings(core.Schema):

    endpoint_uri: Union[str, core.StringOut] = core.attr(str)

    error_retry_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    full_load_error_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    service_access_role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        endpoint_uri: Union[str, core.StringOut],
        service_access_role_arn: Union[str, core.StringOut],
        error_retry_duration: Optional[Union[int, core.IntOut]] = None,
        full_load_error_percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ElasticsearchSettings.Args(
                endpoint_uri=endpoint_uri,
                service_access_role_arn=service_access_role_arn,
                error_retry_duration=error_retry_duration,
                full_load_error_percentage=full_load_error_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_uri: Union[str, core.StringOut] = core.arg()

        error_retry_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        full_load_error_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        service_access_role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class S3Settings(core.Schema):

    add_column_name: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    bucket_folder: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    canned_acl_for_objects: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cdc_inserts_and_updates: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cdc_inserts_only: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cdc_max_batch_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cdc_min_file_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cdc_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compression_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    csv_delimiter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    csv_no_sup_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    csv_null_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    csv_row_delimiter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    data_page_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    date_partition_delimiter: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    date_partition_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    date_partition_sequence: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dict_page_size_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    enable_statistics: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    encoding_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    external_table_definition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ignore_headers_row: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    include_op_for_full_load: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    max_file_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    parquet_timestamp_in_millisecond: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    parquet_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    preserve_transactions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    rfc_4180: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    row_group_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    service_access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timestamp_column_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    use_csv_no_sup_value: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        add_column_name: Optional[Union[bool, core.BoolOut]] = None,
        bucket_folder: Optional[Union[str, core.StringOut]] = None,
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        canned_acl_for_objects: Optional[Union[str, core.StringOut]] = None,
        cdc_inserts_and_updates: Optional[Union[bool, core.BoolOut]] = None,
        cdc_inserts_only: Optional[Union[bool, core.BoolOut]] = None,
        cdc_max_batch_interval: Optional[Union[int, core.IntOut]] = None,
        cdc_min_file_size: Optional[Union[int, core.IntOut]] = None,
        cdc_path: Optional[Union[str, core.StringOut]] = None,
        compression_type: Optional[Union[str, core.StringOut]] = None,
        csv_delimiter: Optional[Union[str, core.StringOut]] = None,
        csv_no_sup_value: Optional[Union[str, core.StringOut]] = None,
        csv_null_value: Optional[Union[str, core.StringOut]] = None,
        csv_row_delimiter: Optional[Union[str, core.StringOut]] = None,
        data_format: Optional[Union[str, core.StringOut]] = None,
        data_page_size: Optional[Union[int, core.IntOut]] = None,
        date_partition_delimiter: Optional[Union[str, core.StringOut]] = None,
        date_partition_enabled: Optional[Union[bool, core.BoolOut]] = None,
        date_partition_sequence: Optional[Union[str, core.StringOut]] = None,
        dict_page_size_limit: Optional[Union[int, core.IntOut]] = None,
        enable_statistics: Optional[Union[bool, core.BoolOut]] = None,
        encoding_type: Optional[Union[str, core.StringOut]] = None,
        encryption_mode: Optional[Union[str, core.StringOut]] = None,
        external_table_definition: Optional[Union[str, core.StringOut]] = None,
        ignore_headers_row: Optional[Union[int, core.IntOut]] = None,
        include_op_for_full_load: Optional[Union[bool, core.BoolOut]] = None,
        max_file_size: Optional[Union[int, core.IntOut]] = None,
        parquet_timestamp_in_millisecond: Optional[Union[bool, core.BoolOut]] = None,
        parquet_version: Optional[Union[str, core.StringOut]] = None,
        preserve_transactions: Optional[Union[bool, core.BoolOut]] = None,
        rfc_4180: Optional[Union[bool, core.BoolOut]] = None,
        row_group_length: Optional[Union[int, core.IntOut]] = None,
        server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        service_access_role_arn: Optional[Union[str, core.StringOut]] = None,
        timestamp_column_name: Optional[Union[str, core.StringOut]] = None,
        use_csv_no_sup_value: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=S3Settings.Args(
                add_column_name=add_column_name,
                bucket_folder=bucket_folder,
                bucket_name=bucket_name,
                canned_acl_for_objects=canned_acl_for_objects,
                cdc_inserts_and_updates=cdc_inserts_and_updates,
                cdc_inserts_only=cdc_inserts_only,
                cdc_max_batch_interval=cdc_max_batch_interval,
                cdc_min_file_size=cdc_min_file_size,
                cdc_path=cdc_path,
                compression_type=compression_type,
                csv_delimiter=csv_delimiter,
                csv_no_sup_value=csv_no_sup_value,
                csv_null_value=csv_null_value,
                csv_row_delimiter=csv_row_delimiter,
                data_format=data_format,
                data_page_size=data_page_size,
                date_partition_delimiter=date_partition_delimiter,
                date_partition_enabled=date_partition_enabled,
                date_partition_sequence=date_partition_sequence,
                dict_page_size_limit=dict_page_size_limit,
                enable_statistics=enable_statistics,
                encoding_type=encoding_type,
                encryption_mode=encryption_mode,
                external_table_definition=external_table_definition,
                ignore_headers_row=ignore_headers_row,
                include_op_for_full_load=include_op_for_full_load,
                max_file_size=max_file_size,
                parquet_timestamp_in_millisecond=parquet_timestamp_in_millisecond,
                parquet_version=parquet_version,
                preserve_transactions=preserve_transactions,
                rfc_4180=rfc_4180,
                row_group_length=row_group_length,
                server_side_encryption_kms_key_id=server_side_encryption_kms_key_id,
                service_access_role_arn=service_access_role_arn,
                timestamp_column_name=timestamp_column_name,
                use_csv_no_sup_value=use_csv_no_sup_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        add_column_name: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        bucket_folder: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        canned_acl_for_objects: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cdc_inserts_and_updates: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cdc_inserts_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cdc_max_batch_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cdc_min_file_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cdc_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compression_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        csv_delimiter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        csv_no_sup_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        csv_null_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        csv_row_delimiter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        data_page_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        date_partition_delimiter: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        date_partition_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        date_partition_sequence: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dict_page_size_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enable_statistics: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        encoding_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        external_table_definition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ignore_headers_row: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        include_op_for_full_load: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_file_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parquet_timestamp_in_millisecond: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        parquet_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preserve_transactions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        rfc_4180: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        row_group_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        server_side_encryption_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        service_access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timestamp_column_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        use_csv_no_sup_value: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_dms_endpoint", namespace="aws_dms")
class Endpoint(core.Resource):

    certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    database_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elasticsearch_settings: Optional[ElasticsearchSettings] = core.attr(
        ElasticsearchSettings, default=None
    )

    endpoint_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_id: Union[str, core.StringOut] = core.attr(str)

    endpoint_type: Union[str, core.StringOut] = core.attr(str)

    engine_name: Union[str, core.StringOut] = core.attr(str)

    extra_connection_attributes: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kafka_settings: Optional[KafkaSettings] = core.attr(KafkaSettings, default=None)

    kinesis_settings: Optional[KinesisSettings] = core.attr(KinesisSettings, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    mongodb_settings: Optional[MongodbSettings] = core.attr(MongodbSettings, default=None)

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    redshift_settings: Optional[RedshiftSettings] = core.attr(
        RedshiftSettings, default=None, computed=True
    )

    s3_settings: Optional[S3Settings] = core.attr(S3Settings, default=None)

    secrets_manager_access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_access_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ssl_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint_id: Union[str, core.StringOut],
        endpoint_type: Union[str, core.StringOut],
        engine_name: Union[str, core.StringOut],
        certificate_arn: Optional[Union[str, core.StringOut]] = None,
        database_name: Optional[Union[str, core.StringOut]] = None,
        elasticsearch_settings: Optional[ElasticsearchSettings] = None,
        extra_connection_attributes: Optional[Union[str, core.StringOut]] = None,
        kafka_settings: Optional[KafkaSettings] = None,
        kinesis_settings: Optional[KinesisSettings] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        mongodb_settings: Optional[MongodbSettings] = None,
        password: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        redshift_settings: Optional[RedshiftSettings] = None,
        s3_settings: Optional[S3Settings] = None,
        secrets_manager_access_role_arn: Optional[Union[str, core.StringOut]] = None,
        secrets_manager_arn: Optional[Union[str, core.StringOut]] = None,
        server_name: Optional[Union[str, core.StringOut]] = None,
        service_access_role: Optional[Union[str, core.StringOut]] = None,
        ssl_mode: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        username: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                endpoint_id=endpoint_id,
                endpoint_type=endpoint_type,
                engine_name=engine_name,
                certificate_arn=certificate_arn,
                database_name=database_name,
                elasticsearch_settings=elasticsearch_settings,
                extra_connection_attributes=extra_connection_attributes,
                kafka_settings=kafka_settings,
                kinesis_settings=kinesis_settings,
                kms_key_arn=kms_key_arn,
                mongodb_settings=mongodb_settings,
                password=password,
                port=port,
                redshift_settings=redshift_settings,
                s3_settings=s3_settings,
                secrets_manager_access_role_arn=secrets_manager_access_role_arn,
                secrets_manager_arn=secrets_manager_arn,
                server_name=server_name,
                service_access_role=service_access_role,
                ssl_mode=ssl_mode,
                tags=tags,
                tags_all=tags_all,
                username=username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elasticsearch_settings: Optional[ElasticsearchSettings] = core.arg(default=None)

        endpoint_id: Union[str, core.StringOut] = core.arg()

        endpoint_type: Union[str, core.StringOut] = core.arg()

        engine_name: Union[str, core.StringOut] = core.arg()

        extra_connection_attributes: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafka_settings: Optional[KafkaSettings] = core.arg(default=None)

        kinesis_settings: Optional[KinesisSettings] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mongodb_settings: Optional[MongodbSettings] = core.arg(default=None)

        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        redshift_settings: Optional[RedshiftSettings] = core.arg(default=None)

        s3_settings: Optional[S3Settings] = core.arg(default=None)

        secrets_manager_access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_access_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ssl_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        username: Optional[Union[str, core.StringOut]] = core.arg(default=None)
