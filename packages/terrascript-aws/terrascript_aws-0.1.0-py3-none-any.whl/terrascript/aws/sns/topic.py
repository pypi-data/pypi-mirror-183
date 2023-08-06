from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sns_topic", namespace="aws_sns")
class Topic(core.Resource):

    application_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    application_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    application_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_based_deduplication: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    delivery_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fifo_topic: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    firehose_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    firehose_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    firehose_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    http_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    http_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    http_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_master_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lambda_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    lambda_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    lambda_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    sqs_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    sqs_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    sqs_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
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
        application_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        application_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        application_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = None,
        content_based_deduplication: Optional[Union[bool, core.BoolOut]] = None,
        delivery_policy: Optional[Union[str, core.StringOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        fifo_topic: Optional[Union[bool, core.BoolOut]] = None,
        firehose_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        firehose_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        firehose_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = None,
        http_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        http_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        http_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = None,
        kms_master_key_id: Optional[Union[str, core.StringOut]] = None,
        lambda_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        lambda_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        lambda_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        sqs_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        sqs_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        sqs_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Topic.Args(
                application_failure_feedback_role_arn=application_failure_feedback_role_arn,
                application_success_feedback_role_arn=application_success_feedback_role_arn,
                application_success_feedback_sample_rate=application_success_feedback_sample_rate,
                content_based_deduplication=content_based_deduplication,
                delivery_policy=delivery_policy,
                display_name=display_name,
                fifo_topic=fifo_topic,
                firehose_failure_feedback_role_arn=firehose_failure_feedback_role_arn,
                firehose_success_feedback_role_arn=firehose_success_feedback_role_arn,
                firehose_success_feedback_sample_rate=firehose_success_feedback_sample_rate,
                http_failure_feedback_role_arn=http_failure_feedback_role_arn,
                http_success_feedback_role_arn=http_success_feedback_role_arn,
                http_success_feedback_sample_rate=http_success_feedback_sample_rate,
                kms_master_key_id=kms_master_key_id,
                lambda_failure_feedback_role_arn=lambda_failure_feedback_role_arn,
                lambda_success_feedback_role_arn=lambda_success_feedback_role_arn,
                lambda_success_feedback_sample_rate=lambda_success_feedback_sample_rate,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                sqs_failure_feedback_role_arn=sqs_failure_feedback_role_arn,
                sqs_success_feedback_role_arn=sqs_success_feedback_role_arn,
                sqs_success_feedback_sample_rate=sqs_success_feedback_sample_rate,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        application_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        application_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        application_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        content_based_deduplication: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        delivery_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fifo_topic: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        firehose_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        firehose_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        firehose_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        http_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        http_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        http_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        kms_master_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        lambda_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        lambda_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sqs_failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sqs_success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sqs_success_feedback_sample_rate: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
