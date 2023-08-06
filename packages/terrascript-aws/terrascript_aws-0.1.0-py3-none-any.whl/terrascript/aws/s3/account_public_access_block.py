from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_s3_account_public_access_block", namespace="aws_s3")
class AccountPublicAccessBlock(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    block_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    block_public_policy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Optional[Union[str, core.StringOut]] = None,
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
            args=AccountPublicAccessBlock.Args(
                account_id=account_id,
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
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        block_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        block_public_policy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ignore_public_acls: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        restrict_public_buckets: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
