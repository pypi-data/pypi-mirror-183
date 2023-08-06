from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_mskconnect_worker_configuration", namespace="aws_managed_streaming_for_kafka_connect"
)
class MskconnectWorkerConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latest_revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    properties_file_content: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        properties_file_content: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskconnectWorkerConfiguration.Args(
                name=name,
                properties_file_content=properties_file_content,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        properties_file_content: Union[str, core.StringOut] = core.arg()
