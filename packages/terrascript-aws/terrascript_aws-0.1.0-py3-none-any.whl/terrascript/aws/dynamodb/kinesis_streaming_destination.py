from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dynamodb_kinesis_streaming_destination", namespace="aws_dynamodb")
class KinesisStreamingDestination(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        stream_arn: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=KinesisStreamingDestination.Args(
                stream_arn=stream_arn,
                table_name=table_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        stream_arn: Union[str, core.StringOut] = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()
