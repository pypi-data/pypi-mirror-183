from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_xray_encryption_config", namespace="aws_x_ray")
class XrayEncryptionConfig(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: Union[str, core.StringOut],
        key_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=XrayEncryptionConfig.Args(
                type=type,
                key_id=key_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()
