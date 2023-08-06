from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_s3_account_public_access_block", namespace="aws_s3")
class DsAccountPublicAccessBlock(core.Data):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    block_public_acls: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    block_public_policy: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_public_acls: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    restrict_public_buckets: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        account_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAccountPublicAccessBlock.Args(
                account_id=account_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
