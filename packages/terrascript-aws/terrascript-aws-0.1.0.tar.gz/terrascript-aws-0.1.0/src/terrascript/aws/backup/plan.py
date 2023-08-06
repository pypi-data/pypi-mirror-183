from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Lifecycle(core.Schema):

    cold_storage_after: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    delete_after: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cold_storage_after: Optional[Union[int, core.IntOut]] = None,
        delete_after: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Lifecycle.Args(
                cold_storage_after=cold_storage_after,
                delete_after=delete_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cold_storage_after: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        delete_after: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class CopyAction(core.Schema):

    destination_vault_arn: Union[str, core.StringOut] = core.attr(str)

    lifecycle: Optional[Lifecycle] = core.attr(Lifecycle, default=None)

    def __init__(
        self,
        *,
        destination_vault_arn: Union[str, core.StringOut],
        lifecycle: Optional[Lifecycle] = None,
    ):
        super().__init__(
            args=CopyAction.Args(
                destination_vault_arn=destination_vault_arn,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination_vault_arn: Union[str, core.StringOut] = core.arg()

        lifecycle: Optional[Lifecycle] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    completion_window: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    copy_action: Optional[Union[List[CopyAction], core.ArrayOut[CopyAction]]] = core.attr(
        CopyAction, default=None, kind=core.Kind.array
    )

    enable_continuous_backup: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    lifecycle: Optional[Lifecycle] = core.attr(Lifecycle, default=None)

    recovery_point_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rule_name: Union[str, core.StringOut] = core.attr(str)

    schedule: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start_window: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_vault_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        rule_name: Union[str, core.StringOut],
        target_vault_name: Union[str, core.StringOut],
        completion_window: Optional[Union[int, core.IntOut]] = None,
        copy_action: Optional[Union[List[CopyAction], core.ArrayOut[CopyAction]]] = None,
        enable_continuous_backup: Optional[Union[bool, core.BoolOut]] = None,
        lifecycle: Optional[Lifecycle] = None,
        recovery_point_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        schedule: Optional[Union[str, core.StringOut]] = None,
        start_window: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                rule_name=rule_name,
                target_vault_name=target_vault_name,
                completion_window=completion_window,
                copy_action=copy_action,
                enable_continuous_backup=enable_continuous_backup,
                lifecycle=lifecycle,
                recovery_point_tags=recovery_point_tags,
                schedule=schedule,
                start_window=start_window,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        completion_window: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        copy_action: Optional[Union[List[CopyAction], core.ArrayOut[CopyAction]]] = core.arg(
            default=None
        )

        enable_continuous_backup: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        lifecycle: Optional[Lifecycle] = core.arg(default=None)

        recovery_point_tags: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        rule_name: Union[str, core.StringOut] = core.arg()

        schedule: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start_window: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_vault_name: Union[str, core.StringOut] = core.arg()


@core.schema
class AdvancedBackupSetting(core.Schema):

    backup_options: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    resource_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        backup_options: Union[Dict[str, str], core.MapOut[core.StringOut]],
        resource_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AdvancedBackupSetting.Args(
                backup_options=backup_options,
                resource_type=resource_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        backup_options: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        resource_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_backup_plan", namespace="aws_backup")
class Plan(core.Resource):

    advanced_backup_setting: Optional[
        Union[List[AdvancedBackupSetting], core.ArrayOut[AdvancedBackupSetting]]
    ] = core.attr(AdvancedBackupSetting, default=None, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        advanced_backup_setting: Optional[
            Union[List[AdvancedBackupSetting], core.ArrayOut[AdvancedBackupSetting]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Plan.Args(
                name=name,
                rule=rule,
                advanced_backup_setting=advanced_backup_setting,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        advanced_backup_setting: Optional[
            Union[List[AdvancedBackupSetting], core.ArrayOut[AdvancedBackupSetting]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
