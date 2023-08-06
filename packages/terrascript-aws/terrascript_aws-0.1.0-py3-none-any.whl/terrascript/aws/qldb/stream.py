from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class KinesisConfiguration(core.Schema):

    aggregation_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        stream_arn: Union[str, core.StringOut],
        aggregation_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=KinesisConfiguration.Args(
                stream_arn=stream_arn,
                aggregation_enabled=aggregation_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        aggregation_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stream_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_qldb_stream", namespace="aws_qldb")
class Stream(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    exclusive_end_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inclusive_start_time: Union[str, core.StringOut] = core.attr(str)

    kinesis_configuration: KinesisConfiguration = core.attr(KinesisConfiguration)

    ledger_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    stream_name: Union[str, core.StringOut] = core.attr(str)

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
        inclusive_start_time: Union[str, core.StringOut],
        kinesis_configuration: KinesisConfiguration,
        ledger_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        stream_name: Union[str, core.StringOut],
        exclusive_end_time: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stream.Args(
                inclusive_start_time=inclusive_start_time,
                kinesis_configuration=kinesis_configuration,
                ledger_name=ledger_name,
                role_arn=role_arn,
                stream_name=stream_name,
                exclusive_end_time=exclusive_end_time,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        exclusive_end_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        inclusive_start_time: Union[str, core.StringOut] = core.arg()

        kinesis_configuration: KinesisConfiguration = core.arg()

        ledger_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        stream_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
