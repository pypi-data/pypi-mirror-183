from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3BucketDestination(core.Schema):

    bucket_account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        bucket_account_id: Optional[Union[str, core.StringOut]] = None,
        format: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3BucketDestination.Args(
                bucket_arn=bucket_arn,
                bucket_account_id=bucket_account_id,
                format=format,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_arn: Union[str, core.StringOut] = core.arg()

        format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    s3_bucket_destination: S3BucketDestination = core.attr(S3BucketDestination)

    def __init__(
        self,
        *,
        s3_bucket_destination: S3BucketDestination,
    ):
        super().__init__(
            args=Destination.Args(
                s3_bucket_destination=s3_bucket_destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_bucket_destination: S3BucketDestination = core.arg()


@core.schema
class DataExport(core.Schema):

    destination: Destination = core.attr(Destination)

    output_schema_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination: Destination,
        output_schema_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DataExport.Args(
                destination=destination,
                output_schema_version=output_schema_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Destination = core.arg()

        output_schema_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class StorageClassAnalysis(core.Schema):

    data_export: DataExport = core.attr(DataExport)

    def __init__(
        self,
        *,
        data_export: DataExport,
    ):
        super().__init__(
            args=StorageClassAnalysis.Args(
                data_export=data_export,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_export: DataExport = core.arg()


@core.schema
class Filter(core.Schema):

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.resource(type="aws_s3_bucket_analytics_configuration", namespace="aws_s3")
class BucketAnalyticsConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    storage_class_analysis: Optional[StorageClassAnalysis] = core.attr(
        StorageClassAnalysis, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        filter: Optional[Filter] = None,
        storage_class_analysis: Optional[StorageClassAnalysis] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketAnalyticsConfiguration.Args(
                bucket=bucket,
                name=name,
                filter=filter,
                storage_class_analysis=storage_class_analysis,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        filter: Optional[Filter] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        storage_class_analysis: Optional[StorageClassAnalysis] = core.arg(default=None)
