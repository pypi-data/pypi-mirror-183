from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_detective_member", namespace="aws_detective")
class Member(core.Resource):

    account_id: Union[str, core.StringOut] = core.attr(str)

    administrator_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    disabled_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    email_address: Union[str, core.StringOut] = core.attr(str)

    graph_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invited_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    message: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    updated_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_usage_in_bytes: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Union[str, core.StringOut],
        email_address: Union[str, core.StringOut],
        graph_arn: Union[str, core.StringOut],
        disable_email_notification: Optional[Union[bool, core.BoolOut]] = None,
        message: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Member.Args(
                account_id=account_id,
                email_address=email_address,
                graph_arn=graph_arn,
                disable_email_notification=disable_email_notification,
                message=message,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Union[str, core.StringOut] = core.arg()

        disable_email_notification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        email_address: Union[str, core.StringOut] = core.arg()

        graph_arn: Union[str, core.StringOut] = core.arg()

        message: Optional[Union[str, core.StringOut]] = core.arg(default=None)
