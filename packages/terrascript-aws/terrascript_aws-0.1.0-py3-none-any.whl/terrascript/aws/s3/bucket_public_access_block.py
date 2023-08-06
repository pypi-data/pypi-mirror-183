from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_s3_bucket_public_access_block", namespace="aws_s3")
class BucketPublicAccessBlock(core.Resource):

    block_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    block_public_policy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        block_public_acls: Optional[Union[bool, core.BoolOut]] = None,
        block_public_policy: Optional[Union[bool, core.BoolOut]] = None,
        ignore_public_acls: Optional[Union[bool, core.BoolOut]] = None,
        restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketPublicAccessBlock.Args(
                bucket=bucket,
                block_public_acls=block_public_acls,
                block_public_policy=block_public_policy,
                ignore_public_acls=ignore_public_acls,
                restrict_public_buckets=restrict_public_buckets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        block_public_policy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
