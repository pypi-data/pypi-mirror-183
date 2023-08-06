from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_route53recoverycontrolconfig_control_panel",
    namespace="aws_route53recoverycontrolconfig",
)
class ControlPanel(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_arn: Union[str, core.StringOut] = core.attr(str)

    default_control_panel: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    routing_control_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ControlPanel.Args(
                cluster_arn=cluster_arn,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_arn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
