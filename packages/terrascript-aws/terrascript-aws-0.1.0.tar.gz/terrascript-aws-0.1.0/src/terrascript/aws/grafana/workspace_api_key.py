from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_grafana_workspace_api_key", namespace="aws_grafana")
class WorkspaceApiKey(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_name: Union[str, core.StringOut] = core.attr(str)

    key_role: Union[str, core.StringOut] = core.attr(str)

    seconds_to_live: Union[int, core.IntOut] = core.attr(int)

    workspace_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        key_name: Union[str, core.StringOut],
        key_role: Union[str, core.StringOut],
        seconds_to_live: Union[int, core.IntOut],
        workspace_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkspaceApiKey.Args(
                key_name=key_name,
                key_role=key_role,
                seconds_to_live=seconds_to_live,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_name: Union[str, core.StringOut] = core.arg()

        key_role: Union[str, core.StringOut] = core.arg()

        seconds_to_live: Union[int, core.IntOut] = core.arg()

        workspace_id: Union[str, core.StringOut] = core.arg()
