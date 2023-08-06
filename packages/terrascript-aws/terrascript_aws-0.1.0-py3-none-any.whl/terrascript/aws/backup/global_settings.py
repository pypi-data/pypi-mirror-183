from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_backup_global_settings", namespace="aws_backup")
class GlobalSettings(core.Resource):

    global_settings: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        global_settings: Union[Dict[str, str], core.MapOut[core.StringOut]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GlobalSettings.Args(
                global_settings=global_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        global_settings: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()
