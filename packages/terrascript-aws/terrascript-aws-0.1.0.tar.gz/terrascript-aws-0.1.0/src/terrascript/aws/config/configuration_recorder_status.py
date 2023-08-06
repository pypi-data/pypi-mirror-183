from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_config_configuration_recorder_status", namespace="aws_config")
class ConfigurationRecorderStatus(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    is_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        is_enabled: Union[bool, core.BoolOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ConfigurationRecorderStatus.Args(
                is_enabled=is_enabled,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        is_enabled: Union[bool, core.BoolOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
