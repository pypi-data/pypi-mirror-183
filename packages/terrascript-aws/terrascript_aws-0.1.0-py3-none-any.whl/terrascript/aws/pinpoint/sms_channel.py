from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_pinpoint_sms_channel", namespace="aws_pinpoint")
class SmsChannel(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Whether the channel is enabled or disabled. Defaults to `true`.
    """
    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Promotional messages per second that can be sent.
    """
    promotional_messages_per_second: Union[int, core.IntOut] = core.attr(int, computed=True)

    """
    (Optional) Sender identifier of your messages.
    """
    sender_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) The Short Code registered with the phone provider.
    """
    short_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    Transactional messages per second that can be sent.
    """
    transactional_messages_per_second: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        sender_id: Optional[Union[str, core.StringOut]] = None,
        short_code: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SmsChannel.Args(
                application_id=application_id,
                enabled=enabled,
                sender_id=sender_id,
                short_code=short_code,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        sender_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        short_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)
