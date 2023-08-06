from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_sns_platform_application", namespace="aws_sns")
class PlatformApplication(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    event_delivery_failure_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    event_endpoint_created_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    event_endpoint_deleted_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    event_endpoint_updated_topic_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    platform: Union[str, core.StringOut] = core.attr(str)

    platform_credential: Union[str, core.StringOut] = core.attr(str)

    platform_principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    success_feedback_sample_rate: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        platform: Union[str, core.StringOut],
        platform_credential: Union[str, core.StringOut],
        event_delivery_failure_topic_arn: Optional[Union[str, core.StringOut]] = None,
        event_endpoint_created_topic_arn: Optional[Union[str, core.StringOut]] = None,
        event_endpoint_deleted_topic_arn: Optional[Union[str, core.StringOut]] = None,
        event_endpoint_updated_topic_arn: Optional[Union[str, core.StringOut]] = None,
        failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        platform_principal: Optional[Union[str, core.StringOut]] = None,
        success_feedback_role_arn: Optional[Union[str, core.StringOut]] = None,
        success_feedback_sample_rate: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlatformApplication.Args(
                name=name,
                platform=platform,
                platform_credential=platform_credential,
                event_delivery_failure_topic_arn=event_delivery_failure_topic_arn,
                event_endpoint_created_topic_arn=event_endpoint_created_topic_arn,
                event_endpoint_deleted_topic_arn=event_endpoint_deleted_topic_arn,
                event_endpoint_updated_topic_arn=event_endpoint_updated_topic_arn,
                failure_feedback_role_arn=failure_feedback_role_arn,
                platform_principal=platform_principal,
                success_feedback_role_arn=success_feedback_role_arn,
                success_feedback_sample_rate=success_feedback_sample_rate,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        event_delivery_failure_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        event_endpoint_created_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        event_endpoint_deleted_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        event_endpoint_updated_topic_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        failure_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        platform: Union[str, core.StringOut] = core.arg()

        platform_credential: Union[str, core.StringOut] = core.arg()

        platform_principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        success_feedback_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        success_feedback_sample_rate: Optional[Union[str, core.StringOut]] = core.arg(default=None)
