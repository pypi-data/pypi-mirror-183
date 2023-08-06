from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_autoscaling_attachment", namespace="aws_autoscaling")
class Attachment(core.Resource):

    alb_target_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    autoscaling_group_name: Union[str, core.StringOut] = core.attr(str)

    elb: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lb_target_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        autoscaling_group_name: Union[str, core.StringOut],
        alb_target_group_arn: Optional[Union[str, core.StringOut]] = None,
        elb: Optional[Union[str, core.StringOut]] = None,
        lb_target_group_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Attachment.Args(
                autoscaling_group_name=autoscaling_group_name,
                alb_target_group_arn=alb_target_group_arn,
                elb=elb,
                lb_target_group_arn=lb_target_group_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alb_target_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        autoscaling_group_name: Union[str, core.StringOut] = core.arg()

        elb: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lb_target_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
