from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class StreamModeDetails(core.Schema):

    stream_mode: Union[str, core.StringOut] = core.attr(str)

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


@core.resource(type="aws_kinesis_stream", namespace="aws_kinesis")
class Stream(core.Resource):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    encryption_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enforce_consumer_deletion: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    shard_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    shard_level_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    stream_mode_details: Optional[StreamModeDetails] = core.attr(
        StreamModeDetails, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        arn: Optional[Union[str, core.StringOut]] = None,
        encryption_type: Optional[Union[str, core.StringOut]] = None,
        enforce_consumer_deletion: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        retention_period: Optional[Union[int, core.IntOut]] = None,
        shard_count: Optional[Union[int, core.IntOut]] = None,
        shard_level_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        stream_mode_details: Optional[StreamModeDetails] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stream.Args(
                name=name,
                arn=arn,
                encryption_type=encryption_type,
                enforce_consumer_deletion=enforce_consumer_deletion,
                kms_key_id=kms_key_id,
                retention_period=retention_period,
                shard_count=shard_count,
                shard_level_metrics=shard_level_metrics,
                stream_mode_details=stream_mode_details,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enforce_consumer_deletion: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        shard_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        shard_level_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        stream_mode_details: Optional[StreamModeDetails] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
