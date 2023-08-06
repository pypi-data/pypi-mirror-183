from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_kinesis_stream_consumer", namespace="aws_kinesis")
class StreamConsumer(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        stream_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StreamConsumer.Args(
                name=name,
                stream_arn=stream_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        stream_arn: Union[str, core.StringOut] = core.arg()
