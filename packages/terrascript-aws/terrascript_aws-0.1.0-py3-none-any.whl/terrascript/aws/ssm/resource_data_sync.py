from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Union[str, core.StringOut] = core.attr(str)

    sync_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        sync_format: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket_name=bucket_name,
                region=region,
                kms_key_arn=kms_key_arn,
                prefix=prefix,
                sync_format=sync_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Union[str, core.StringOut] = core.arg()

        sync_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ssm_resource_data_sync", namespace="aws_ssm")
class ResourceDataSync(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    s3_destination: S3Destination = core.attr(S3Destination)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        s3_destination: S3Destination,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceDataSync.Args(
                name=name,
                s3_destination=s3_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        s3_destination: S3Destination = core.arg()
