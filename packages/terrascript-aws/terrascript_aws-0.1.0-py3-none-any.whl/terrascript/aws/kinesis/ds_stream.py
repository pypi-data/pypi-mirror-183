from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class StreamModeDetails(core.Schema):

    stream_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        stream_mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StreamModeDetails.Args(
                stream_mode=stream_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stream_mode: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_kinesis_stream", namespace="aws_kinesis")
class DsStream(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    closed_shards: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    creation_timestamp: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    open_shards: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    retention_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    shard_level_metrics: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_mode_details: Union[
        List[StreamModeDetails], core.ArrayOut[StreamModeDetails]
    ] = core.attr(StreamModeDetails, computed=True, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsStream.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
