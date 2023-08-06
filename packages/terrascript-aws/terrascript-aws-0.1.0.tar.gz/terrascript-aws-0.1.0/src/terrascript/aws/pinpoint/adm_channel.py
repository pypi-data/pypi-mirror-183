from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_pinpoint_adm_channel", namespace="aws_pinpoint")
class AdmChannel(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    client_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    client_secret: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Specifies whether to enable the channel. Defaults to `true`.
    """
    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AdmChannel.Args(
                application_id=application_id,
                client_id=client_id,
                client_secret=client_secret,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
