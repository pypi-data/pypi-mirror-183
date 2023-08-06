from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lb_target_group_attachment", namespace="aws_elb")
class LbTargetGroupAttachment(core.Resource):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_group_arn: Union[str, core.StringOut] = core.attr(str)

    target_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        target_group_arn: Union[str, core.StringOut],
        target_id: Union[str, core.StringOut],
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbTargetGroupAttachment.Args(
                target_group_arn=target_group_arn,
                target_id=target_id,
                availability_zone=availability_zone,
                port=port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_group_arn: Union[str, core.StringOut] = core.arg()

        target_id: Union[str, core.StringOut] = core.arg()
