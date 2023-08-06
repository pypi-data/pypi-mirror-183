from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_member", namespace="aws_securityhub")
class Member(core.Resource):
    """
    (Required) The ID of the member AWS account.
    """

    account_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The email of the member AWS account.
    """
    email: Union[str, core.StringOut] = core.attr(str)

    """
    The ID of the member AWS account (matches `account_id`).
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Boolean whether to invite the account to Security Hub as a member. Defaults to `false`.
    """
    invite: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    The ID of the master Security Hub AWS account.
    """
    master_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The status of the member account relationship.
    """
    member_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        invite: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email=email,
                invite=invite,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Union[str, core.StringOut] = core.arg()

        email: Union[str, core.StringOut] = core.arg()

        invite: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
