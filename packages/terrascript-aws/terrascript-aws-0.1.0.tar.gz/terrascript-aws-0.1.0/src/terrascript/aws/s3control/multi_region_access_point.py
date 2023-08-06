from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PublicAccessBlock(core.Schema):

    block_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    block_public_policy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        block_public_acls: Optional[Union[bool, core.BoolOut]] = None,
        block_public_policy: Optional[Union[bool, core.BoolOut]] = None,
        ignore_public_acls: Optional[Union[bool, core.BoolOut]] = None,
        restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=PublicAccessBlock.Args(
                block_public_acls=block_public_acls,
                block_public_policy=block_public_policy,
                ignore_public_acls=ignore_public_acls,
                restrict_public_buckets=restrict_public_buckets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        block_public_policy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Region(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Region.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()


@core.schema
class Details(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    public_access_block: Optional[PublicAccessBlock] = core.attr(PublicAccessBlock, default=None)

    region: Union[List[Region], core.ArrayOut[Region]] = core.attr(Region, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        region: Union[List[Region], core.ArrayOut[Region]],
        public_access_block: Optional[PublicAccessBlock] = None,
    ):
        super().__init__(
            args=Details.Args(
                name=name,
                region=region,
                public_access_block=public_access_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        public_access_block: Optional[PublicAccessBlock] = core.arg(default=None)

        region: Union[List[Region], core.ArrayOut[Region]] = core.arg()


@core.resource(type="aws_s3control_multi_region_access_point", namespace="aws_s3control")
class MultiRegionAccessPoint(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    details: Details = core.attr(Details)

    domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        details: Details,
        account_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MultiRegionAccessPoint.Args(
                details=details,
                account_id=account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        details: Details = core.arg()
