from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class KinesisStreamConfig(core.Schema):

    role_arn: Union[str, core.StringOut] = core.attr(str)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        stream_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisStreamConfig.Args(
                role_arn=role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: Union[str, core.StringOut] = core.arg()

        stream_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Endpoint(core.Schema):

    kinesis_stream_config: KinesisStreamConfig = core.attr(KinesisStreamConfig)

    stream_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        kinesis_stream_config: KinesisStreamConfig,
        stream_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Endpoint.Args(
                kinesis_stream_config=kinesis_stream_config,
                stream_type=stream_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kinesis_stream_config: KinesisStreamConfig = core.arg()

        stream_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudfront_realtime_log_config", namespace="aws_cloudfront")
class RealtimeLogConfig(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Endpoint = core.attr(Endpoint)

    fields: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    sampling_rate: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint: Endpoint,
        fields: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        sampling_rate: Union[int, core.IntOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RealtimeLogConfig.Args(
                endpoint=endpoint,
                fields=fields,
                name=name,
                sampling_rate=sampling_rate,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        endpoint: Endpoint = core.arg()

        fields: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        sampling_rate: Union[int, core.IntOut] = core.arg()
