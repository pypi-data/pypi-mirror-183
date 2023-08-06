from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_backup_vault_lock_configuration", namespace="aws_backup")
class VaultLockConfiguration(core.Resource):

    backup_vault_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    backup_vault_name: Union[str, core.StringOut] = core.attr(str)

    changeable_for_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_retention_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_retention_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_vault_name: Union[str, core.StringOut],
        changeable_for_days: Optional[Union[int, core.IntOut]] = None,
        max_retention_days: Optional[Union[int, core.IntOut]] = None,
        min_retention_days: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultLockConfiguration.Args(
                backup_vault_name=backup_vault_name,
                changeable_for_days=changeable_for_days,
                max_retention_days=max_retention_days,
                min_retention_days=min_retention_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_vault_name: Union[str, core.StringOut] = core.arg()

        changeable_for_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)
