from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_autoscaling_lifecycle_hook", namespace="aws_autoscaling")
class LifecycleHook(core.Resource):

    autoscaling_group_name: Union[str, core.StringOut] = core.attr(str)

    default_result: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    heartbeat_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lifecycle_transition: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    notification_metadata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_target_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: Union[str, core.StringOut],
        lifecycle_transition: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        default_result: Optional[Union[str, core.StringOut]] = None,
        heartbeat_timeout: Optional[Union[int, core.IntOut]] = None,
        notification_metadata: Optional[Union[str, core.StringOut]] = None,
        notification_target_arn: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LifecycleHook.Args(
                autoscaling_group_name=autoscaling_group_name,
                lifecycle_transition=lifecycle_transition,
                name=name,
                default_result=default_result,
                heartbeat_timeout=heartbeat_timeout,
                notification_metadata=notification_metadata,
                notification_target_arn=notification_target_arn,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_group_name: Union[str, core.StringOut] = core.arg()

        default_result: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        heartbeat_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        lifecycle_transition: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        notification_metadata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_target_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
