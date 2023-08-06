from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_routing_control",
    namespace="aws_route53recoverycontrolconfig",
)
class RoutingControl(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_arn: Union[str, core.StringOut] = core.attr(str)

    control_panel_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        control_panel_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoutingControl.Args(
                cluster_arn=cluster_arn,
                name=name,
                control_panel_arn=control_panel_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: Union[str, core.StringOut] = core.arg()

        control_panel_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
