from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_msk_configuration", namespace="aws_managed_streaming_for_kafka")
class MskConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kafka_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    latest_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    server_properties: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        server_properties: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        kafka_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskConfiguration.Args(
                name=name,
                server_properties=server_properties,
                description=description,
                kafka_versions=kafka_versions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafka_versions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        server_properties: Union[str, core.StringOut] = core.arg()
