from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class S3Destination(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        kms_key_arn: Union[str, core.StringOut],
        key_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Destination.Args(
                bucket_name=bucket_name,
                kms_key_arn=kms_key_arn,
                key_prefix=key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_macie2_classification_export_configuration", namespace="aws_macie2")
class ClassificationExportConfiguration(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_destination: Optional[S3Destination] = core.attr(S3Destination, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        s3_destination: Optional[S3Destination] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClassificationExportConfiguration.Args(
                s3_destination=s3_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        s3_destination: Optional[S3Destination] = core.arg(default=None)
