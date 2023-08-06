from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionConfig(core.Schema):

    encryption_type: Union[str, core.StringOut] = core.attr(str)

    key_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        encryption_type: Union[str, core.StringOut],
        key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfig.Args(
                encryption_type=encryption_type,
                key_id=key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_type: Union[str, core.StringOut] = core.arg()

        key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class S3Config(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Union[str, core.StringOut] = core.attr(str)

    encryption_config: Optional[EncryptionConfig] = core.attr(EncryptionConfig, default=None)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        bucket_prefix: Union[str, core.StringOut],
        encryption_config: Optional[EncryptionConfig] = None,
    ):
        super().__init__(
            args=S3Config.Args(
                bucket_name=bucket_name,
                bucket_prefix=bucket_prefix,
                encryption_config=encryption_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Union[str, core.StringOut] = core.arg()

        encryption_config: Optional[EncryptionConfig] = core.arg(default=None)


@core.schema
class KinesisFirehoseConfig(core.Schema):

    firehose_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        firehose_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisFirehoseConfig.Args(
                firehose_arn=firehose_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        firehose_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisStreamConfig(core.Schema):

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        stream_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisStreamConfig.Args(
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stream_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisVideoStreamConfig(core.Schema):

    encryption_config: EncryptionConfig = core.attr(EncryptionConfig)

    prefix: Union[str, core.StringOut] = core.attr(str)

    retention_period_hours: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        encryption_config: EncryptionConfig,
        prefix: Union[str, core.StringOut],
        retention_period_hours: Union[int, core.IntOut],
    ):
        super().__init__(
            args=KinesisVideoStreamConfig.Args(
                encryption_config=encryption_config,
                prefix=prefix,
                retention_period_hours=retention_period_hours,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_config: EncryptionConfig = core.arg()

        prefix: Union[str, core.StringOut] = core.arg()

        retention_period_hours: Union[int, core.IntOut] = core.arg()


@core.schema
class StorageConfig(core.Schema):

    kinesis_firehose_config: Optional[KinesisFirehoseConfig] = core.attr(
        KinesisFirehoseConfig, default=None
    )

    kinesis_stream_config: Optional[KinesisStreamConfig] = core.attr(
        KinesisStreamConfig, default=None
    )

    kinesis_video_stream_config: Optional[KinesisVideoStreamConfig] = core.attr(
        KinesisVideoStreamConfig, default=None
    )

    s3_config: Optional[S3Config] = core.attr(S3Config, default=None)

    storage_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        storage_type: Union[str, core.StringOut],
        kinesis_firehose_config: Optional[KinesisFirehoseConfig] = None,
        kinesis_stream_config: Optional[KinesisStreamConfig] = None,
        kinesis_video_stream_config: Optional[KinesisVideoStreamConfig] = None,
        s3_config: Optional[S3Config] = None,
    ):
        super().__init__(
            args=StorageConfig.Args(
                storage_type=storage_type,
                kinesis_firehose_config=kinesis_firehose_config,
                kinesis_stream_config=kinesis_stream_config,
                kinesis_video_stream_config=kinesis_video_stream_config,
                s3_config=s3_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_firehose_config: Optional[KinesisFirehoseConfig] = core.arg(default=None)

        kinesis_stream_config: Optional[KinesisStreamConfig] = core.arg(default=None)

        kinesis_video_stream_config: Optional[KinesisVideoStreamConfig] = core.arg(default=None)

        s3_config: Optional[S3Config] = core.arg(default=None)

        storage_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_connect_instance_storage_config", namespace="aws_connect")
class InstanceStorageConfig(core.Resource):

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    resource_type: Union[str, core.StringOut] = core.attr(str)

    storage_config: StorageConfig = core.attr(StorageConfig)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        resource_type: Union[str, core.StringOut],
        storage_config: StorageConfig,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceStorageConfig.Args(
                instance_id=instance_id,
                resource_type=resource_type,
                storage_config=storage_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_id: Union[str, core.StringOut] = core.arg()

        resource_type: Union[str, core.StringOut] = core.arg()

        storage_config: StorageConfig = core.arg()
