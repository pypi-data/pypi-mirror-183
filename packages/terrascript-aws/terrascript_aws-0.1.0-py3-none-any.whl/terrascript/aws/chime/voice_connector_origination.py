from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Route(core.Schema):

    host: Union[str, core.StringOut] = core.attr(str)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    priority: Union[int, core.IntOut] = core.attr(int)

    protocol: Union[str, core.StringOut] = core.attr(str)

    weight: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        host: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        weight: Union[int, core.IntOut],
        port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Route.Args(
                host=host,
                priority=priority,
                protocol=protocol,
                weight=weight,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        host: Union[str, core.StringOut] = core.arg()

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        priority: Union[int, core.IntOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        weight: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_chime_voice_connector_origination", namespace="aws_chime")
class VoiceConnectorOrigination(core.Resource):

    disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    route: Union[List[Route], core.ArrayOut[Route]] = core.attr(Route, kind=core.Kind.array)

    voice_connector_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        route: Union[List[Route], core.ArrayOut[Route]],
        voice_connector_id: Union[str, core.StringOut],
        disabled: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorOrigination.Args(
                route=route,
                voice_connector_id=voice_connector_id,
                disabled=disabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        route: Union[List[Route], core.ArrayOut[Route]] = core.arg()

        voice_connector_id: Union[str, core.StringOut] = core.arg()
