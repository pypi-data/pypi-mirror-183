from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Configuration(core.Schema):

    bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_option: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: Optional[Union[str, core.StringOut]] = None,
        encryption_option: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        object_key_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Configuration.Args(
                bucket_name=bucket_name,
                encryption_option=encryption_option,
                kms_key_id=kms_key_id,
                object_key_prefix=object_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_option: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MagneticStoreRejectedDataLocation(core.Schema):

    s3_configuration: Optional[S3Configuration] = core.attr(S3Configuration, default=None)

    def __init__(
        self,
        *,
        s3_configuration: Optional[S3Configuration] = None,
    ):
        super().__init__(
            args=MagneticStoreRejectedDataLocation.Args(
                s3_configuration=s3_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_configuration: Optional[S3Configuration] = core.arg(default=None)


@core.schema
class MagneticStoreWriteProperties(core.Schema):

    enable_magnetic_store_writes: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    magnetic_store_rejected_data_location: Optional[MagneticStoreRejectedDataLocation] = core.attr(
        MagneticStoreRejectedDataLocation, default=None
    )

    def __init__(
        self,
        *,
        enable_magnetic_store_writes: Optional[Union[bool, core.BoolOut]] = None,
        magnetic_store_rejected_data_location: Optional[MagneticStoreRejectedDataLocation] = None,
    ):
        super().__init__(
            args=MagneticStoreWriteProperties.Args(
                enable_magnetic_store_writes=enable_magnetic_store_writes,
                magnetic_store_rejected_data_location=magnetic_store_rejected_data_location,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_magnetic_store_writes: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        magnetic_store_rejected_data_location: Optional[
            MagneticStoreRejectedDataLocation
        ] = core.arg(default=None)


@core.schema
class RetentionProperties(core.Schema):

    magnetic_store_retention_period_in_days: Union[int, core.IntOut] = core.attr(int)

    memory_store_retention_period_in_hours: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        magnetic_store_retention_period_in_days: Union[int, core.IntOut],
        memory_store_retention_period_in_hours: Union[int, core.IntOut],
    ):
        super().__init__(
            args=RetentionProperties.Args(
                magnetic_store_retention_period_in_days=magnetic_store_retention_period_in_days,
                memory_store_retention_period_in_hours=memory_store_retention_period_in_hours,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        magnetic_store_retention_period_in_days: Union[int, core.IntOut] = core.arg()

        memory_store_retention_period_in_hours: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_timestreamwrite_table", namespace="aws_timestreamwrite")
class Table(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    magnetic_store_write_properties: Optional[MagneticStoreWriteProperties] = core.attr(
        MagneticStoreWriteProperties, default=None, computed=True
    )

    retention_properties: Optional[RetentionProperties] = core.attr(
        RetentionProperties, default=None, computed=True
    )

    table_name: Union[str, core.StringOut] = core.attr(str)

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
        table_name: Union[str, core.StringOut],
        magnetic_store_write_properties: Optional[MagneticStoreWriteProperties] = None,
        retention_properties: Optional[RetentionProperties] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Table.Args(
                database_name=database_name,
                table_name=table_name,
                magnetic_store_write_properties=magnetic_store_write_properties,
                retention_properties=retention_properties,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        database_name: Union[str, core.StringOut] = core.arg()

        magnetic_store_write_properties: Optional[MagneticStoreWriteProperties] = core.arg(
            default=None
        )

        retention_properties: Optional[RetentionProperties] = core.arg(default=None)

        table_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
