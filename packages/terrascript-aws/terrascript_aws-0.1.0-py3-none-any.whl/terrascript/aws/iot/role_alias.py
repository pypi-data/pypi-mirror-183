from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_role_alias", namespace="aws_iot")
class RoleAlias(core.Resource):

    alias: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    credential_duration: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        alias: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        credential_duration: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoleAlias.Args(
                alias=alias,
                role_arn=role_arn,
                credential_duration=credential_duration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: Union[str, core.StringOut] = core.arg()

        credential_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()
