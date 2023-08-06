from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appstream_user", namespace="aws_appstream")
class User(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_type: Union[str, core.StringOut] = core.attr(str)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    first_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    send_email_notification: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    user_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_type: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        first_name: Optional[Union[str, core.StringOut]] = None,
        last_name: Optional[Union[str, core.StringOut]] = None,
        send_email_notification: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=User.Args(
                authentication_type=authentication_type,
                user_name=user_name,
                enabled=enabled,
                first_name=first_name,
                last_name=last_name,
                send_email_notification=send_email_notification,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_type: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        first_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        last_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        send_email_notification: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        user_name: Union[str, core.StringOut] = core.arg()
