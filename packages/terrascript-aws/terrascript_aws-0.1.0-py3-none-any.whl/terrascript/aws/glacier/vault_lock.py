from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_glacier_vault_lock", namespace="aws_glacier")
class VaultLock(core.Resource):

    complete_lock: Union[bool, core.BoolOut] = core.attr(bool)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_deletion_error: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    policy: Union[str, core.StringOut] = core.attr(str)

    vault_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        complete_lock: Union[bool, core.BoolOut],
        policy: Union[str, core.StringOut],
        vault_name: Union[str, core.StringOut],
        ignore_deletion_error: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultLock.Args(
                complete_lock=complete_lock,
                policy=policy,
                vault_name=vault_name,
                ignore_deletion_error=ignore_deletion_error,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        complete_lock: Union[bool, core.BoolOut] = core.arg()

        ignore_deletion_error: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Union[str, core.StringOut] = core.arg()

        vault_name: Union[str, core.StringOut] = core.arg()
