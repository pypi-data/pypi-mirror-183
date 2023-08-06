from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SnsDestination(core.Schema):

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        topic_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SnsDestination.Args(
                topic_arn=topic_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        topic_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class CloudwatchDestination(core.Schema):

    default_value: Union[str, core.StringOut] = core.attr(str)

    dimension_name: Union[str, core.StringOut] = core.attr(str)

    value_source: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        default_value: Union[str, core.StringOut],
        dimension_name: Union[str, core.StringOut],
        value_source: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CloudwatchDestination.Args(
                default_value=default_value,
                dimension_name=dimension_name,
                value_source=value_source,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_value: Union[str, core.StringOut] = core.arg()

        dimension_name: Union[str, core.StringOut] = core.arg()

        value_source: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisDestination(core.Schema):

    role_arn: Union[str, core.StringOut] = core.attr(str)

    stream_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        stream_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=KinesisDestination.Args(
                role_arn=role_arn,
                stream_arn=stream_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role_arn: Union[str, core.StringOut] = core.arg()

        stream_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ses_event_destination", namespace="aws_ses")
class EventDestination(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_destination: Optional[
        Union[List[CloudwatchDestination], core.ArrayOut[CloudwatchDestination]]
    ] = core.attr(CloudwatchDestination, default=None, kind=core.Kind.array)

    configuration_set_name: Union[str, core.StringOut] = core.attr(str)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kinesis_destination: Optional[KinesisDestination] = core.attr(KinesisDestination, default=None)

    matching_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    sns_destination: Optional[SnsDestination] = core.attr(SnsDestination, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        configuration_set_name: Union[str, core.StringOut],
        matching_types: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        cloudwatch_destination: Optional[
            Union[List[CloudwatchDestination], core.ArrayOut[CloudwatchDestination]]
        ] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        kinesis_destination: Optional[KinesisDestination] = None,
        sns_destination: Optional[SnsDestination] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EventDestination.Args(
                configuration_set_name=configuration_set_name,
                matching_types=matching_types,
                name=name,
                cloudwatch_destination=cloudwatch_destination,
                enabled=enabled,
                kinesis_destination=kinesis_destination,
                sns_destination=sns_destination,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_destination: Optional[
            Union[List[CloudwatchDestination], core.ArrayOut[CloudwatchDestination]]
        ] = core.arg(default=None)

        configuration_set_name: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kinesis_destination: Optional[KinesisDestination] = core.arg(default=None)

        matching_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        sns_destination: Optional[SnsDestination] = core.arg(default=None)
