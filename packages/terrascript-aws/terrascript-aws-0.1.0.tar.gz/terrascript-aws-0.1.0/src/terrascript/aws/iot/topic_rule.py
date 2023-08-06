from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CloudwatchMetric(core.Schema):

    metric_name: Union[str, core.StringOut] = core.attr(str)

    metric_namespace: Union[str, core.StringOut] = core.attr(str)

    metric_timestamp: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    metric_unit: Union[str, core.StringOut] = core.attr(str)

    metric_value: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        metric_name: Union[str, core.StringOut],
        metric_namespace: Union[str, core.StringOut],
        metric_unit: Union[str, core.StringOut],
        metric_value: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        metric_timestamp: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CloudwatchMetric.Args(
                metric_name=metric_name,
                metric_namespace=metric_namespace,
                metric_unit=metric_unit,
                metric_value=metric_value,
                role_arn=role_arn,
                metric_timestamp=metric_timestamp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        metric_name: Union[str, core.StringOut] = core.arg()

        metric_namespace: Union[str, core.StringOut] = core.arg()

        metric_timestamp: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_unit: Union[str, core.StringOut] = core.arg()

        metric_value: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Sqs(core.Schema):

    queue_url: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    use_base64: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        queue_url: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        use_base64: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=Sqs.Args(
                queue_url=queue_url,
                role_arn=role_arn,
                use_base64=use_base64,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        queue_url: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        use_base64: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Timestamp(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Timestamp.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Dimension(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Dimension.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Timestream(core.Schema):

    database_name: Union[str, core.StringOut] = core.attr(str)

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, kind=core.Kind.array
    )

    role_arn: Union[str, core.StringOut] = core.attr(str)

    table_name: Union[str, core.StringOut] = core.attr(str)

    timestamp: Optional[Timestamp] = core.attr(Timestamp, default=None)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
        role_arn: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        timestamp: Optional[Timestamp] = None,
    ):
        super().__init__(
            args=Timestream.Args(
                database_name=database_name,
                dimension=dimension,
                role_arn=role_arn,
                table_name=table_name,
                timestamp=timestamp,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database_name: Union[str, core.StringOut] = core.arg()

        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()

        timestamp: Optional[Timestamp] = core.arg(default=None)


@core.schema
class Lambda(core.Schema):

    function_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        function_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Lambda.Args(
                function_arn=function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class CloudwatchAlarm(core.Schema):

    alarm_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    state_reason: Union[str, core.StringOut] = core.attr(str)

    state_value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        alarm_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        state_reason: Union[str, core.StringOut],
        state_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CloudwatchAlarm.Args(
                alarm_name=alarm_name,
                role_arn=role_arn,
                state_reason=state_reason,
                state_value=state_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        state_reason: Union[str, core.StringOut] = core.arg()

        state_value: Union[str, core.StringOut] = core.arg()


@core.schema
class Dynamodb(core.Schema):

    hash_key_field: Union[str, core.StringOut] = core.attr(str)

    hash_key_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hash_key_value: Union[str, core.StringOut] = core.attr(str)

    operation: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    payload_field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    range_key_field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    range_key_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    range_key_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        hash_key_field: Union[str, core.StringOut],
        hash_key_value: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        table_name: Union[str, core.StringOut],
        hash_key_type: Optional[Union[str, core.StringOut]] = None,
        operation: Optional[Union[str, core.StringOut]] = None,
        payload_field: Optional[Union[str, core.StringOut]] = None,
        range_key_field: Optional[Union[str, core.StringOut]] = None,
        range_key_type: Optional[Union[str, core.StringOut]] = None,
        range_key_value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Dynamodb.Args(
                hash_key_field=hash_key_field,
                hash_key_value=hash_key_value,
                role_arn=role_arn,
                table_name=table_name,
                hash_key_type=hash_key_type,
                operation=operation,
                payload_field=payload_field,
                range_key_field=range_key_field,
                range_key_type=range_key_type,
                range_key_value=range_key_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hash_key_field: Union[str, core.StringOut] = core.arg()

        hash_key_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hash_key_value: Union[str, core.StringOut] = core.arg()

        operation: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        payload_field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        range_key_field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        range_key_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        range_key_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        table_name: Union[str, core.StringOut] = core.arg()


@core.schema
class IotAnalytics(core.Schema):

    channel_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        channel_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IotAnalytics.Args(
                channel_name=channel_name,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class PutItem(core.Schema):

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        table_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PutItem.Args(
                table_name=table_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        table_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Dynamodbv2(core.Schema):

    put_item: Optional[PutItem] = core.attr(PutItem, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        put_item: Optional[PutItem] = None,
    ):
        super().__init__(
            args=Dynamodbv2.Args(
                role_arn=role_arn,
                put_item=put_item,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        put_item: Optional[PutItem] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class S3(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    canned_acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        canned_acl: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3.Args(
                bucket_name=bucket_name,
                key=key,
                role_arn=role_arn,
                canned_acl=canned_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        canned_acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Firehose(core.Schema):

    delivery_stream_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    separator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delivery_stream_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        separator: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Firehose.Args(
                delivery_stream_name=delivery_stream_name,
                role_arn=role_arn,
                separator=separator,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_stream_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        separator: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CloudwatchLogs(core.Schema):

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        log_group_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                log_group_name=log_group_name,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_group_name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class StepFunctions(core.Schema):

    execution_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    state_machine_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        state_machine_name: Union[str, core.StringOut],
        execution_name_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StepFunctions.Args(
                role_arn=role_arn,
                state_machine_name=state_machine_name,
                execution_name_prefix=execution_name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        state_machine_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Kinesis(core.Schema):

    partition_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    stream_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        stream_name: Union[str, core.StringOut],
        partition_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Kinesis.Args(
                role_arn=role_arn,
                stream_name=stream_name,
                partition_key=partition_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        partition_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        stream_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Elasticsearch(core.Schema):

    endpoint: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str)

    index: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        endpoint: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        index: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Elasticsearch.Args(
                endpoint=endpoint,
                id=id,
                index=index,
                role_arn=role_arn,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        index: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Republish(core.Schema):

    qos: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    topic: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        topic: Union[str, core.StringOut],
        qos: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Republish.Args(
                role_arn=role_arn,
                topic=topic,
                qos=qos,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        qos: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        topic: Union[str, core.StringOut] = core.arg()


@core.schema
class Kafka(core.Schema):

    client_properties: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    partition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    topic: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        client_properties: Union[Dict[str, str], core.MapOut[core.StringOut]],
        destination_arn: Union[str, core.StringOut],
        topic: Union[str, core.StringOut],
        key: Optional[Union[str, core.StringOut]] = None,
        partition: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Kafka.Args(
                client_properties=client_properties,
                destination_arn=destination_arn,
                topic=topic,
                key=key,
                partition=partition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_properties: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        destination_arn: Union[str, core.StringOut] = core.arg()

        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        partition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topic: Union[str, core.StringOut] = core.arg()


@core.schema
class Sns(core.Schema):

    message_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        role_arn: Union[str, core.StringOut],
        target_arn: Union[str, core.StringOut],
        message_format: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Sns.Args(
                role_arn=role_arn,
                target_arn=target_arn,
                message_format=message_format,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        target_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class HttpHeader(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=HttpHeader.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Http(core.Schema):

    confirmation_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_header: Optional[Union[List[HttpHeader], core.ArrayOut[HttpHeader]]] = core.attr(
        HttpHeader, default=None, kind=core.Kind.array
    )

    url: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        url: Union[str, core.StringOut],
        confirmation_url: Optional[Union[str, core.StringOut]] = None,
        http_header: Optional[Union[List[HttpHeader], core.ArrayOut[HttpHeader]]] = None,
    ):
        super().__init__(
            args=Http.Args(
                url=url,
                confirmation_url=confirmation_url,
                http_header=http_header,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        confirmation_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_header: Optional[Union[List[HttpHeader], core.ArrayOut[HttpHeader]]] = core.arg(
            default=None
        )

        url: Union[str, core.StringOut] = core.arg()


@core.schema
class IotEvents(core.Schema):

    input_name: Union[str, core.StringOut] = core.attr(str)

    message_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        input_name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        message_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IotEvents.Args(
                input_name=input_name,
                role_arn=role_arn,
                message_id=message_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_name: Union[str, core.StringOut] = core.arg()

        message_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ErrorAction(core.Schema):

    cloudwatch_alarm: Optional[CloudwatchAlarm] = core.attr(CloudwatchAlarm, default=None)

    cloudwatch_logs: Optional[CloudwatchLogs] = core.attr(CloudwatchLogs, default=None)

    cloudwatch_metric: Optional[CloudwatchMetric] = core.attr(CloudwatchMetric, default=None)

    dynamodb: Optional[Dynamodb] = core.attr(Dynamodb, default=None)

    dynamodbv2: Optional[Dynamodbv2] = core.attr(Dynamodbv2, default=None)

    elasticsearch: Optional[Elasticsearch] = core.attr(Elasticsearch, default=None)

    firehose: Optional[Firehose] = core.attr(Firehose, default=None)

    http: Optional[Http] = core.attr(Http, default=None)

    iot_analytics: Optional[IotAnalytics] = core.attr(IotAnalytics, default=None)

    iot_events: Optional[IotEvents] = core.attr(IotEvents, default=None)

    kafka: Optional[Kafka] = core.attr(Kafka, default=None)

    kinesis: Optional[Kinesis] = core.attr(Kinesis, default=None)

    lambda_: Optional[Lambda] = core.attr(Lambda, default=None, alias="lambda")

    republish: Optional[Republish] = core.attr(Republish, default=None)

    s3: Optional[S3] = core.attr(S3, default=None)

    sns: Optional[Sns] = core.attr(Sns, default=None)

    sqs: Optional[Sqs] = core.attr(Sqs, default=None)

    step_functions: Optional[StepFunctions] = core.attr(StepFunctions, default=None)

    timestream: Optional[Timestream] = core.attr(Timestream, default=None)

    def __init__(
        self,
        *,
        cloudwatch_alarm: Optional[CloudwatchAlarm] = None,
        cloudwatch_logs: Optional[CloudwatchLogs] = None,
        cloudwatch_metric: Optional[CloudwatchMetric] = None,
        dynamodb: Optional[Dynamodb] = None,
        dynamodbv2: Optional[Dynamodbv2] = None,
        elasticsearch: Optional[Elasticsearch] = None,
        firehose: Optional[Firehose] = None,
        http: Optional[Http] = None,
        iot_analytics: Optional[IotAnalytics] = None,
        iot_events: Optional[IotEvents] = None,
        kafka: Optional[Kafka] = None,
        kinesis: Optional[Kinesis] = None,
        lambda_: Optional[Lambda] = None,
        republish: Optional[Republish] = None,
        s3: Optional[S3] = None,
        sns: Optional[Sns] = None,
        sqs: Optional[Sqs] = None,
        step_functions: Optional[StepFunctions] = None,
        timestream: Optional[Timestream] = None,
    ):
        super().__init__(
            args=ErrorAction.Args(
                cloudwatch_alarm=cloudwatch_alarm,
                cloudwatch_logs=cloudwatch_logs,
                cloudwatch_metric=cloudwatch_metric,
                dynamodb=dynamodb,
                dynamodbv2=dynamodbv2,
                elasticsearch=elasticsearch,
                firehose=firehose,
                http=http,
                iot_analytics=iot_analytics,
                iot_events=iot_events,
                kafka=kafka,
                kinesis=kinesis,
                lambda_=lambda_,
                republish=republish,
                s3=s3,
                sns=sns,
                sqs=sqs,
                step_functions=step_functions,
                timestream=timestream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_alarm: Optional[CloudwatchAlarm] = core.arg(default=None)

        cloudwatch_logs: Optional[CloudwatchLogs] = core.arg(default=None)

        cloudwatch_metric: Optional[CloudwatchMetric] = core.arg(default=None)

        dynamodb: Optional[Dynamodb] = core.arg(default=None)

        dynamodbv2: Optional[Dynamodbv2] = core.arg(default=None)

        elasticsearch: Optional[Elasticsearch] = core.arg(default=None)

        firehose: Optional[Firehose] = core.arg(default=None)

        http: Optional[Http] = core.arg(default=None)

        iot_analytics: Optional[IotAnalytics] = core.arg(default=None)

        iot_events: Optional[IotEvents] = core.arg(default=None)

        kafka: Optional[Kafka] = core.arg(default=None)

        kinesis: Optional[Kinesis] = core.arg(default=None)

        lambda_: Optional[Lambda] = core.arg(default=None)

        republish: Optional[Republish] = core.arg(default=None)

        s3: Optional[S3] = core.arg(default=None)

        sns: Optional[Sns] = core.arg(default=None)

        sqs: Optional[Sqs] = core.arg(default=None)

        step_functions: Optional[StepFunctions] = core.arg(default=None)

        timestream: Optional[Timestream] = core.arg(default=None)


@core.resource(type="aws_iot_topic_rule", namespace="aws_iot")
class TopicRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_alarm: Optional[
        Union[List[CloudwatchAlarm], core.ArrayOut[CloudwatchAlarm]]
    ] = core.attr(CloudwatchAlarm, default=None, kind=core.Kind.array)

    cloudwatch_logs: Optional[
        Union[List[CloudwatchLogs], core.ArrayOut[CloudwatchLogs]]
    ] = core.attr(CloudwatchLogs, default=None, kind=core.Kind.array)

    cloudwatch_metric: Optional[
        Union[List[CloudwatchMetric], core.ArrayOut[CloudwatchMetric]]
    ] = core.attr(CloudwatchMetric, default=None, kind=core.Kind.array)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dynamodb: Optional[Union[List[Dynamodb], core.ArrayOut[Dynamodb]]] = core.attr(
        Dynamodb, default=None, kind=core.Kind.array
    )

    dynamodbv2: Optional[Union[List[Dynamodbv2], core.ArrayOut[Dynamodbv2]]] = core.attr(
        Dynamodbv2, default=None, kind=core.Kind.array
    )

    elasticsearch: Optional[Union[List[Elasticsearch], core.ArrayOut[Elasticsearch]]] = core.attr(
        Elasticsearch, default=None, kind=core.Kind.array
    )

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    error_action: Optional[ErrorAction] = core.attr(ErrorAction, default=None)

    firehose: Optional[Union[List[Firehose], core.ArrayOut[Firehose]]] = core.attr(
        Firehose, default=None, kind=core.Kind.array
    )

    http: Optional[Union[List[Http], core.ArrayOut[Http]]] = core.attr(
        Http, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iot_analytics: Optional[Union[List[IotAnalytics], core.ArrayOut[IotAnalytics]]] = core.attr(
        IotAnalytics, default=None, kind=core.Kind.array
    )

    iot_events: Optional[Union[List[IotEvents], core.ArrayOut[IotEvents]]] = core.attr(
        IotEvents, default=None, kind=core.Kind.array
    )

    kafka: Optional[Union[List[Kafka], core.ArrayOut[Kafka]]] = core.attr(
        Kafka, default=None, kind=core.Kind.array
    )

    kinesis: Optional[Union[List[Kinesis], core.ArrayOut[Kinesis]]] = core.attr(
        Kinesis, default=None, kind=core.Kind.array
    )

    lambda_: Optional[Union[List[Lambda], core.ArrayOut[Lambda]]] = core.attr(
        Lambda, default=None, kind=core.Kind.array, alias="lambda"
    )

    name: Union[str, core.StringOut] = core.attr(str)

    republish: Optional[Union[List[Republish], core.ArrayOut[Republish]]] = core.attr(
        Republish, default=None, kind=core.Kind.array
    )

    s3: Optional[Union[List[S3], core.ArrayOut[S3]]] = core.attr(
        S3, default=None, kind=core.Kind.array
    )

    sns: Optional[Union[List[Sns], core.ArrayOut[Sns]]] = core.attr(
        Sns, default=None, kind=core.Kind.array
    )

    sql: Union[str, core.StringOut] = core.attr(str)

    sql_version: Union[str, core.StringOut] = core.attr(str)

    sqs: Optional[Union[List[Sqs], core.ArrayOut[Sqs]]] = core.attr(
        Sqs, default=None, kind=core.Kind.array
    )

    step_functions: Optional[Union[List[StepFunctions], core.ArrayOut[StepFunctions]]] = core.attr(
        StepFunctions, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timestream: Optional[Union[List[Timestream], core.ArrayOut[Timestream]]] = core.attr(
        Timestream, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        enabled: Union[bool, core.BoolOut],
        name: Union[str, core.StringOut],
        sql: Union[str, core.StringOut],
        sql_version: Union[str, core.StringOut],
        cloudwatch_alarm: Optional[
            Union[List[CloudwatchAlarm], core.ArrayOut[CloudwatchAlarm]]
        ] = None,
        cloudwatch_logs: Optional[
            Union[List[CloudwatchLogs], core.ArrayOut[CloudwatchLogs]]
        ] = None,
        cloudwatch_metric: Optional[
            Union[List[CloudwatchMetric], core.ArrayOut[CloudwatchMetric]]
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        dynamodb: Optional[Union[List[Dynamodb], core.ArrayOut[Dynamodb]]] = None,
        dynamodbv2: Optional[Union[List[Dynamodbv2], core.ArrayOut[Dynamodbv2]]] = None,
        elasticsearch: Optional[Union[List[Elasticsearch], core.ArrayOut[Elasticsearch]]] = None,
        error_action: Optional[ErrorAction] = None,
        firehose: Optional[Union[List[Firehose], core.ArrayOut[Firehose]]] = None,
        http: Optional[Union[List[Http], core.ArrayOut[Http]]] = None,
        iot_analytics: Optional[Union[List[IotAnalytics], core.ArrayOut[IotAnalytics]]] = None,
        iot_events: Optional[Union[List[IotEvents], core.ArrayOut[IotEvents]]] = None,
        kafka: Optional[Union[List[Kafka], core.ArrayOut[Kafka]]] = None,
        kinesis: Optional[Union[List[Kinesis], core.ArrayOut[Kinesis]]] = None,
        lambda_: Optional[Union[List[Lambda], core.ArrayOut[Lambda]]] = None,
        republish: Optional[Union[List[Republish], core.ArrayOut[Republish]]] = None,
        s3: Optional[Union[List[S3], core.ArrayOut[S3]]] = None,
        sns: Optional[Union[List[Sns], core.ArrayOut[Sns]]] = None,
        sqs: Optional[Union[List[Sqs], core.ArrayOut[Sqs]]] = None,
        step_functions: Optional[Union[List[StepFunctions], core.ArrayOut[StepFunctions]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timestream: Optional[Union[List[Timestream], core.ArrayOut[Timestream]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicRule.Args(
                enabled=enabled,
                name=name,
                sql=sql,
                sql_version=sql_version,
                cloudwatch_alarm=cloudwatch_alarm,
                cloudwatch_logs=cloudwatch_logs,
                cloudwatch_metric=cloudwatch_metric,
                description=description,
                dynamodb=dynamodb,
                dynamodbv2=dynamodbv2,
                elasticsearch=elasticsearch,
                error_action=error_action,
                firehose=firehose,
                http=http,
                iot_analytics=iot_analytics,
                iot_events=iot_events,
                kafka=kafka,
                kinesis=kinesis,
                lambda_=lambda_,
                republish=republish,
                s3=s3,
                sns=sns,
                sqs=sqs,
                step_functions=step_functions,
                tags=tags,
                tags_all=tags_all,
                timestream=timestream,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_alarm: Optional[
            Union[List[CloudwatchAlarm], core.ArrayOut[CloudwatchAlarm]]
        ] = core.arg(default=None)

        cloudwatch_logs: Optional[
            Union[List[CloudwatchLogs], core.ArrayOut[CloudwatchLogs]]
        ] = core.arg(default=None)

        cloudwatch_metric: Optional[
            Union[List[CloudwatchMetric], core.ArrayOut[CloudwatchMetric]]
        ] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dynamodb: Optional[Union[List[Dynamodb], core.ArrayOut[Dynamodb]]] = core.arg(default=None)

        dynamodbv2: Optional[Union[List[Dynamodbv2], core.ArrayOut[Dynamodbv2]]] = core.arg(
            default=None
        )

        elasticsearch: Optional[
            Union[List[Elasticsearch], core.ArrayOut[Elasticsearch]]
        ] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()

        error_action: Optional[ErrorAction] = core.arg(default=None)

        firehose: Optional[Union[List[Firehose], core.ArrayOut[Firehose]]] = core.arg(default=None)

        http: Optional[Union[List[Http], core.ArrayOut[Http]]] = core.arg(default=None)

        iot_analytics: Optional[Union[List[IotAnalytics], core.ArrayOut[IotAnalytics]]] = core.arg(
            default=None
        )

        iot_events: Optional[Union[List[IotEvents], core.ArrayOut[IotEvents]]] = core.arg(
            default=None
        )

        kafka: Optional[Union[List[Kafka], core.ArrayOut[Kafka]]] = core.arg(default=None)

        kinesis: Optional[Union[List[Kinesis], core.ArrayOut[Kinesis]]] = core.arg(default=None)

        lambda_: Optional[Union[List[Lambda], core.ArrayOut[Lambda]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        republish: Optional[Union[List[Republish], core.ArrayOut[Republish]]] = core.arg(
            default=None
        )

        s3: Optional[Union[List[S3], core.ArrayOut[S3]]] = core.arg(default=None)

        sns: Optional[Union[List[Sns], core.ArrayOut[Sns]]] = core.arg(default=None)

        sql: Union[str, core.StringOut] = core.arg()

        sql_version: Union[str, core.StringOut] = core.arg()

        sqs: Optional[Union[List[Sqs], core.ArrayOut[Sqs]]] = core.arg(default=None)

        step_functions: Optional[
            Union[List[StepFunctions], core.ArrayOut[StepFunctions]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timestream: Optional[Union[List[Timestream], core.ArrayOut[Timestream]]] = core.arg(
            default=None
        )
