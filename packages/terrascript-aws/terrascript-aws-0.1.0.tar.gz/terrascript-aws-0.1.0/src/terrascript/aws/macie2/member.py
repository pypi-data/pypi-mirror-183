from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_macie2_member", namespace="aws_macie2")
class Member(core.Resource):

    account_id: Union[str, core.StringOut] = core.attr(str)

    administrator_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    email: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invitation_disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    invitation_message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    invite: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    invited_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    relationship_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        invitation_disable_email_notification: Optional[Union[bool, core.BoolOut]] = None,
        invitation_message: Optional[Union[str, core.StringOut]] = None,
        invite: Optional[Union[bool, core.BoolOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email=email,
                invitation_disable_email_notification=invitation_disable_email_notification,
                invitation_message=invitation_message,
                invite=invite,
                status=status,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Union[str, core.StringOut] = core.arg()

        email: Union[str, core.StringOut] = core.arg()

        invitation_disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        invitation_message: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        invite: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
