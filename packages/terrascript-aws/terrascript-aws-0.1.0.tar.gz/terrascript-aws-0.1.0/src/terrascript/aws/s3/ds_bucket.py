from typing import Union

import terrascript.core as core


@core.data(type="aws_s3_bucket", namespace="aws_s3")
class DsBucket(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket: Union[str, core.StringOut] = core.attr(str)

    bucket_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket_regional_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsBucket.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()
