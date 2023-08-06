from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_pinpoint_baidu_channel", namespace="aws_pinpoint")
class BaiduChannel(core.Resource):
    """
    (Required) Platform credential API key from Baidu.
    """

    api_key: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The application ID.
    """
    application_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Specifies whether to enable the channel. Defaults to `true`.
    """
    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) Platform credential Secret key from Baidu.
    """
    secret_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_key: Union[str, core.StringOut],
        application_id: Union[str, core.StringOut],
        secret_key: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BaiduChannel.Args(
                api_key=api_key,
                application_id=application_id,
                secret_key=secret_key,
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key: Union[str, core.StringOut] = core.arg()

        application_id: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        secret_key: Union[str, core.StringOut] = core.arg()
