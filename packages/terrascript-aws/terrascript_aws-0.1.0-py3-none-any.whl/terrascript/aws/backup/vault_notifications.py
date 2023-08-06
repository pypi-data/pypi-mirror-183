from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_backup_vault_notifications", namespace="aws_backup")
class VaultNotifications(core.Resource):

    backup_vault_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    backup_vault_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    backup_vault_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    sns_topic_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        backup_vault_events: Union[List[str], core.ArrayOut[core.StringOut]],
        backup_vault_name: Union[str, core.StringOut],
        sns_topic_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=VaultNotifications.Args(
                backup_vault_events=backup_vault_events,
                backup_vault_name=backup_vault_name,
                sns_topic_arn=sns_topic_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        backup_vault_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        backup_vault_name: Union[str, core.StringOut] = core.arg()

        sns_topic_arn: Union[str, core.StringOut] = core.arg()
