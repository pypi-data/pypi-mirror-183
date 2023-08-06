from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Connector(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int)

    voice_connector_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        voice_connector_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Connector.Args(
                priority=priority,
                voice_connector_id=voice_connector_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Union[int, core.IntOut] = core.arg()

        voice_connector_id: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_chime_voice_connector_group", namespace="aws_chime")
class VoiceConnectorGroup(core.Resource):

    connector: Optional[Union[List[Connector], core.ArrayOut[Connector]]] = core.attr(
        Connector, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        connector: Optional[Union[List[Connector], core.ArrayOut[Connector]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorGroup.Args(
                name=name,
                connector=connector,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connector: Optional[Union[List[Connector], core.ArrayOut[Connector]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()
