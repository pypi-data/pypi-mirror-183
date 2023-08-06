from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_prometheus_alert_manager_definition", namespace="aws_amp")
class PrometheusAlertManagerDefinition(core.Resource):

    definition: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    workspace_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        definition: Union[str, core.StringOut],
        workspace_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrometheusAlertManagerDefinition.Args(
                definition=definition,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        definition: Union[str, core.StringOut] = core.arg()

        workspace_id: Union[str, core.StringOut] = core.arg()
