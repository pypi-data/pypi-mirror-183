from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_kinesis_stream_consumer", namespace="aws_kinesis")
class DsStreamConsumer(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    creation_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        stream_arn: Union[str, core.StringOut],
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsStreamConsumer.Args(
                stream_arn=stream_arn,
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stream_arn: Union[str, core.StringOut] = core.arg()
