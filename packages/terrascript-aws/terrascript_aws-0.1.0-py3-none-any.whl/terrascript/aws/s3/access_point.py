from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PublicAccessBlockConfiguration(core.Schema):

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
            args=PublicAccessBlockConfiguration.Args(
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
class VpcConfiguration(core.Schema):

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfiguration.Args(
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        vpc_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_access_point", namespace="aws_s3")
class AccessPoint(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket: Union[str, core.StringOut] = core.attr(str)

    domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoints: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    has_public_access_policy: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    network_origin: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    public_access_block_configuration: Optional[PublicAccessBlockConfiguration] = core.attr(
        PublicAccessBlockConfiguration, default=None
    )

    vpc_configuration: Optional[VpcConfiguration] = core.attr(VpcConfiguration, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        public_access_block_configuration: Optional[PublicAccessBlockConfiguration] = None,
        vpc_configuration: Optional[VpcConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPoint.Args(
                bucket=bucket,
                name=name,
                account_id=account_id,
                policy=policy,
                public_access_block_configuration=public_access_block_configuration,
                vpc_configuration=vpc_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_access_block_configuration: Optional[PublicAccessBlockConfiguration] = core.arg(
            default=None
        )

        vpc_configuration: Optional[VpcConfiguration] = core.arg(default=None)
