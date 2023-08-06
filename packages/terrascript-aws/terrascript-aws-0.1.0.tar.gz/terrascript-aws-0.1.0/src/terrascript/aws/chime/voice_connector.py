from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_chime_voice_connector", namespace="aws_chime")
class VoiceConnector(core.Resource):

    aws_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    outbound_host_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    require_encryption: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        require_encryption: Union[bool, core.BoolOut],
        aws_region: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnector.Args(
                name=name,
                require_encryption=require_encryption,
                aws_region=aws_region,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        require_encryption: Union[bool, core.BoolOut] = core.arg()
