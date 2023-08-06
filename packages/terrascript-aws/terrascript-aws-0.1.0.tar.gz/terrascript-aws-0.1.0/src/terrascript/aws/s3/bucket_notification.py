from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Topic(core.Schema):

    events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    filter_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        events: Union[List[str], core.ArrayOut[core.StringOut]],
        topic_arn: Union[str, core.StringOut],
        filter_prefix: Optional[Union[str, core.StringOut]] = None,
        filter_suffix: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Topic.Args(
                events=events,
                topic_arn=topic_arn,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        filter_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topic_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Queue(core.Schema):

    events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    filter_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    queue_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        events: Union[List[str], core.ArrayOut[core.StringOut]],
        queue_arn: Union[str, core.StringOut],
        filter_prefix: Optional[Union[str, core.StringOut]] = None,
        filter_suffix: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Queue.Args(
                events=events,
                queue_arn=queue_arn,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        filter_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        queue_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class LambdaFunction(core.Schema):

    events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    filter_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_suffix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    lambda_function_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        events: Union[List[str], core.ArrayOut[core.StringOut]],
        filter_prefix: Optional[Union[str, core.StringOut]] = None,
        filter_suffix: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        lambda_function_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaFunction.Args(
                events=events,
                filter_prefix=filter_prefix,
                filter_suffix=filter_suffix,
                id=id,
                lambda_function_arn=lambda_function_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        filter_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_suffix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_function_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_s3_bucket_notification", namespace="aws_s3")
class BucketNotification(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    eventbridge: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lambda_function: Optional[
        Union[List[LambdaFunction], core.ArrayOut[LambdaFunction]]
    ] = core.attr(LambdaFunction, default=None, kind=core.Kind.array)

    queue: Optional[Union[List[Queue], core.ArrayOut[Queue]]] = core.attr(
        Queue, default=None, kind=core.Kind.array
    )

    topic: Optional[Union[List[Topic], core.ArrayOut[Topic]]] = core.attr(
        Topic, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        eventbridge: Optional[Union[bool, core.BoolOut]] = None,
        lambda_function: Optional[
            Union[List[LambdaFunction], core.ArrayOut[LambdaFunction]]
        ] = None,
        queue: Optional[Union[List[Queue], core.ArrayOut[Queue]]] = None,
        topic: Optional[Union[List[Topic], core.ArrayOut[Topic]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketNotification.Args(
                bucket=bucket,
                eventbridge=eventbridge,
                lambda_function=lambda_function,
                queue=queue,
                topic=topic,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        eventbridge: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        lambda_function: Optional[
            Union[List[LambdaFunction], core.ArrayOut[LambdaFunction]]
        ] = core.arg(default=None)

        queue: Optional[Union[List[Queue], core.ArrayOut[Queue]]] = core.arg(default=None)

        topic: Optional[Union[List[Topic], core.ArrayOut[Topic]]] = core.arg(default=None)
