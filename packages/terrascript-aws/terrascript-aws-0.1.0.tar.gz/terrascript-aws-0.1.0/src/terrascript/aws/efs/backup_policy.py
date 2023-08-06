from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class BackupPolicyBlk(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=BackupPolicyBlk.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_efs_backup_policy", namespace="aws_efs")
class BackupPolicy(core.Resource):

    backup_policy: BackupPolicyBlk = core.attr(BackupPolicyBlk)

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_policy: BackupPolicyBlk,
        file_system_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BackupPolicy.Args(
                backup_policy=backup_policy,
                file_system_id=file_system_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_policy: BackupPolicyBlk = core.arg()

        file_system_id: Union[str, core.StringOut] = core.arg()
