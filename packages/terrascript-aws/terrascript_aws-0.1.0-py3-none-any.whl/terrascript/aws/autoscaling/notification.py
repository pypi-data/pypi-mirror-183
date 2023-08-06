from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_autoscaling_notification", namespace="aws_autoscaling")
class Notification(core.Resource):

    group_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    notifications: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_names: Union[List[str], core.ArrayOut[core.StringOut]],
        notifications: Union[List[str], core.ArrayOut[core.StringOut]],
        topic_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Notification.Args(
                group_names=group_names,
                notifications=notifications,
                topic_arn=topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        notifications: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        topic_arn: Union[str, core.StringOut] = core.arg()
