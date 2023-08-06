from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_dashboard", namespace="aws_cloudwatch")
class Dashboard(core.Resource):

    dashboard_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    dashboard_body: Union[str, core.StringOut] = core.attr(str)

    dashboard_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        dashboard_body: Union[str, core.StringOut],
        dashboard_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Dashboard.Args(
                dashboard_body=dashboard_body,
                dashboard_name=dashboard_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        dashboard_body: Union[str, core.StringOut] = core.arg()

        dashboard_name: Union[str, core.StringOut] = core.arg()
