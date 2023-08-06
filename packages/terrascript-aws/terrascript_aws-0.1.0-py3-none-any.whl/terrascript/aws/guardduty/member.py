from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_guardduty_member", namespace="aws_guardduty")
class Member(core.Resource):

    account_id: Union[str, core.StringOut] = core.attr(str)

    detector_id: Union[str, core.StringOut] = core.attr(str)

    disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    email: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invitation_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    invite: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    relationship_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Union[str, core.StringOut],
        detector_id: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        disable_email_notification: Optional[Union[bool, core.BoolOut]] = None,
        invitation_message: Optional[Union[str, core.StringOut]] = None,
        invite: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                detector_id=detector_id,
                email=email,
                disable_email_notification=disable_email_notification,
                invitation_message=invitation_message,
                invite=invite,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Union[str, core.StringOut] = core.arg()

        detector_id: Union[str, core.StringOut] = core.arg()

        disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        email: Union[str, core.StringOut] = core.arg()

        invitation_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        invite: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
