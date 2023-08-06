from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Credentials(core.Schema):

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Credentials.Args(
                password=password,
                username=username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_chime_voice_connector_termination_credentials", namespace="aws_chime")
class VoiceConnectorTerminationCredentials(core.Resource):

    credentials: Union[List[Credentials], core.ArrayOut[Credentials]] = core.attr(
        Credentials, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    voice_connector_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        credentials: Union[List[Credentials], core.ArrayOut[Credentials]],
        voice_connector_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VoiceConnectorTerminationCredentials.Args(
                credentials=credentials,
                voice_connector_id=voice_connector_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        credentials: Union[List[Credentials], core.ArrayOut[Credentials]] = core.arg()

        voice_connector_id: Union[str, core.StringOut] = core.arg()
