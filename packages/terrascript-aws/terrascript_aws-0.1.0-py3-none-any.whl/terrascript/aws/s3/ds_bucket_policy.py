from typing import Union

import terrascript.core as core


@core.data(type="aws_s3_bucket_policy", namespace="aws_s3")
class DsBucketPolicy(core.Data):

    bucket: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsBucketPolicy.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()
