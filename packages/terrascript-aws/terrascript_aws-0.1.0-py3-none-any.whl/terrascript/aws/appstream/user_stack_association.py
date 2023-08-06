from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appstream_user_stack_association", namespace="aws_appstream")
class UserStackAssociation(core.Resource):

    authentication_type: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    send_email_notification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stack_name: Union[str, core.StringOut] = core.attr(str)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: Union[str, core.StringOut],
        stack_name: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        send_email_notification: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserStackAssociation.Args(
                authentication_type=authentication_type,
                stack_name=stack_name,
                user_name=user_name,
                send_email_notification=send_email_notification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_type: Union[str, core.StringOut] = core.arg()

        send_email_notification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stack_name: Union[str, core.StringOut] = core.arg()

        user_name: Union[str, core.StringOut] = core.arg()
