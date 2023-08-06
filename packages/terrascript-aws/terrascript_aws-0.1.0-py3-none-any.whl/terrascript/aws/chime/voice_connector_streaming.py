from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_chime_voice_connector_streaming", namespace="aws_chime")
class VoiceConnectorStreaming(core.Resource):

    data_retention: Union[int, core.IntOut] = core.attr(int)

    disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    streaming_notification_targets: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    voice_connector_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        data_retention: Union[int, core.IntOut],
        voice_connector_id: Union[str, core.StringOut],
        disabled: Optional[Union[bool, core.BoolOut]] = None,
        streaming_notification_targets: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorStreaming.Args(
                data_retention=data_retention,
                voice_connector_id=voice_connector_id,
                disabled=disabled,
                streaming_notification_targets=streaming_notification_targets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        data_retention: Union[int, core.IntOut] = core.arg()

        disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        streaming_notification_targets: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        voice_connector_id: Union[str, core.StringOut] = core.arg()
