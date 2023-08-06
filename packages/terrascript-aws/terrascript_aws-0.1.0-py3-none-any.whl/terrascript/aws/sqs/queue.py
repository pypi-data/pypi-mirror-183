from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sqs_queue", namespace="aws_sqs")
class Queue(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_based_deduplication: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    deduplication_scope: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    delay_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    fifo_queue: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    fifo_throughput_limit: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_data_key_reuse_period_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    kms_master_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_message_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    message_retention_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    receive_wait_time_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    redrive_allow_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redrive_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sqs_managed_sse_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    visibility_timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        content_based_deduplication: Optional[Union[bool, core.BoolOut]] = None,
        deduplication_scope: Optional[Union[str, core.StringOut]] = None,
        delay_seconds: Optional[Union[int, core.IntOut]] = None,
        fifo_queue: Optional[Union[bool, core.BoolOut]] = None,
        fifo_throughput_limit: Optional[Union[str, core.StringOut]] = None,
        kms_data_key_reuse_period_seconds: Optional[Union[int, core.IntOut]] = None,
        kms_master_key_id: Optional[Union[str, core.StringOut]] = None,
        max_message_size: Optional[Union[int, core.IntOut]] = None,
        message_retention_seconds: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        receive_wait_time_seconds: Optional[Union[int, core.IntOut]] = None,
        redrive_allow_policy: Optional[Union[str, core.StringOut]] = None,
        redrive_policy: Optional[Union[str, core.StringOut]] = None,
        sqs_managed_sse_enabled: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        visibility_timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Queue.Args(
                content_based_deduplication=content_based_deduplication,
                deduplication_scope=deduplication_scope,
                delay_seconds=delay_seconds,
                fifo_queue=fifo_queue,
                fifo_throughput_limit=fifo_throughput_limit,
                kms_data_key_reuse_period_seconds=kms_data_key_reuse_period_seconds,
                kms_master_key_id=kms_master_key_id,
                max_message_size=max_message_size,
                message_retention_seconds=message_retention_seconds,
                name=name,
                name_prefix=name_prefix,
                policy=policy,
                receive_wait_time_seconds=receive_wait_time_seconds,
                redrive_allow_policy=redrive_allow_policy,
                redrive_policy=redrive_policy,
                sqs_managed_sse_enabled=sqs_managed_sse_enabled,
                tags=tags,
                tags_all=tags_all,
                visibility_timeout_seconds=visibility_timeout_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_based_deduplication: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        deduplication_scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delay_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        fifo_queue: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        fifo_throughput_limit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_data_key_reuse_period_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        kms_master_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_message_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        message_retention_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        receive_wait_time_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        redrive_allow_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redrive_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sqs_managed_sse_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        visibility_timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
