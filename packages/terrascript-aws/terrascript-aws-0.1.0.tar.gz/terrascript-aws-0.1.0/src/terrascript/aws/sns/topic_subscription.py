from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sns_topic_subscription", namespace="aws_sns")
class TopicSubscription(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    confirmation_timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    confirmation_was_authenticated: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    delivery_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint: Union[str, core.StringOut] = core.attr(str)

    endpoint_auto_confirms: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    filter_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    pending_confirmation: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    protocol: Union[str, core.StringOut] = core.attr(str)

    raw_message_delivery: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    redrive_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subscription_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        endpoint: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        topic_arn: Union[str, core.StringOut],
        confirmation_timeout_in_minutes: Optional[Union[int, core.IntOut]] = None,
        delivery_policy: Optional[Union[str, core.StringOut]] = None,
        endpoint_auto_confirms: Optional[Union[bool, core.BoolOut]] = None,
        filter_policy: Optional[Union[str, core.StringOut]] = None,
        raw_message_delivery: Optional[Union[bool, core.BoolOut]] = None,
        redrive_policy: Optional[Union[str, core.StringOut]] = None,
        subscription_role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TopicSubscription.Args(
                endpoint=endpoint,
                protocol=protocol,
                topic_arn=topic_arn,
                confirmation_timeout_in_minutes=confirmation_timeout_in_minutes,
                delivery_policy=delivery_policy,
                endpoint_auto_confirms=endpoint_auto_confirms,
                filter_policy=filter_policy,
                raw_message_delivery=raw_message_delivery,
                redrive_policy=redrive_policy,
                subscription_role_arn=subscription_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        confirmation_timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        delivery_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        endpoint: Union[str, core.StringOut] = core.arg()

        endpoint_auto_confirms: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        filter_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Union[str, core.StringOut] = core.arg()

        raw_message_delivery: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        redrive_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subscription_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        topic_arn: Union[str, core.StringOut] = core.arg()
