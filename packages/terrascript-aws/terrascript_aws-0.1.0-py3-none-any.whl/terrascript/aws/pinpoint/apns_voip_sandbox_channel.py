from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_pinpoint_apns_voip_sandbox_channel", namespace="aws_pinpoint")
class ApnsVoipSandboxChannel(core.Resource):
    """
    (Required) The application ID.
    """

    application_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The ID assigned to your iOS app. To find this value, choose Certificates, IDs & Profiles,
    choose App IDs in the Identifiers section, and choose your app.
    """
    bundle_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The pem encoded TLS Certificate from Apple.
    """
    certificate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) The default authentication method used for APNs.
    """
    default_authentication_method: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    """
    (Optional) Whether the channel is enabled or disabled. Defaults to `true`.
    """
    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The Certificate Private Key file (ie. `.key` file).
    """
    private_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The ID assigned to your Apple developer account team. This value is provided on the Membe
    rship page.
    """
    team_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The `.p8` file that you download from your Apple developer account when you create an aut
    hentication key.
    """
    token_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The ID assigned to your signing key. To find this value, choose Certificates, IDs & Profi
    les, and choose your key in the Keys section.
    """
    token_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        application_id: Union[str, core.StringOut],
        bundle_id: Optional[Union[str, core.StringOut]] = None,
        certificate: Optional[Union[str, core.StringOut]] = None,
        default_authentication_method: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        private_key: Optional[Union[str, core.StringOut]] = None,
        team_id: Optional[Union[str, core.StringOut]] = None,
        token_key: Optional[Union[str, core.StringOut]] = None,
        token_key_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApnsVoipSandboxChannel.Args(
                application_id=application_id,
                bundle_id=bundle_id,
                certificate=certificate,
                default_authentication_method=default_authentication_method,
                enabled=enabled,
                private_key=private_key,
                team_id=team_id,
                token_key=token_key,
                token_key_id=token_key_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_id: Union[str, core.StringOut] = core.arg()

        bundle_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_authentication_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        private_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        team_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        token_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        token_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
