from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_efs_file_system_policy", namespace="aws_efs")
class FileSystemPolicy(core.Resource):

    bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystemPolicy.Args(
                file_system_id=file_system_id,
                policy=policy,
                bypass_policy_lockout_safety_check=bypass_policy_lockout_safety_check,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bypass_policy_lockout_safety_check: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        file_system_id: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()
