from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SelfManagedActiveDirectory(core.Schema):

    dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    file_system_administrators_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    password: Union[str, core.StringOut] = core.attr(str)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]],
        domain_name: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        file_system_administrators_group: Optional[Union[str, core.StringOut]] = None,
        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SelfManagedActiveDirectory.Args(
                dns_ips=dns_ips,
                domain_name=domain_name,
                password=password,
                username=username,
                file_system_administrators_group=file_system_administrators_group,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        domain_name: Union[str, core.StringOut] = core.arg()

        file_system_administrators_group: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        password: Union[str, core.StringOut] = core.arg()

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class AuditLogConfiguration(core.Schema):

    audit_log_destination: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    file_access_audit_log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file_share_access_audit_log_level: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        audit_log_destination: Optional[Union[str, core.StringOut]] = None,
        file_access_audit_log_level: Optional[Union[str, core.StringOut]] = None,
        file_share_access_audit_log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AuditLogConfiguration.Args(
                audit_log_destination=audit_log_destination,
                file_access_audit_log_level=file_access_audit_log_level,
                file_share_access_audit_log_level=file_share_access_audit_log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audit_log_destination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_access_audit_log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_share_access_audit_log_level: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_fsx_windows_file_system", namespace="aws_fsx")
class WindowsFileSystem(core.Resource):

    active_directory_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audit_log_configuration: Optional[AuditLogConfiguration] = core.attr(
        AuditLogConfiguration, default=None, computed=True
    )

    automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    backup_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    deployment_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_file_server_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_subnet_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    remote_administration_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_managed_active_directory: Optional[SelfManagedActiveDirectory] = core.attr(
        SelfManagedActiveDirectory, default=None
    )

    skip_final_backup: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    storage_capacity: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    storage_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_capacity: Union[int, core.IntOut] = core.attr(int)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        throughput_capacity: Union[int, core.IntOut],
        active_directory_id: Optional[Union[str, core.StringOut]] = None,
        aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        audit_log_configuration: Optional[AuditLogConfiguration] = None,
        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = None,
        backup_id: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = None,
        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = None,
        deployment_type: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        preferred_subnet_id: Optional[Union[str, core.StringOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_managed_active_directory: Optional[SelfManagedActiveDirectory] = None,
        skip_final_backup: Optional[Union[bool, core.BoolOut]] = None,
        storage_capacity: Optional[Union[int, core.IntOut]] = None,
        storage_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WindowsFileSystem.Args(
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                active_directory_id=active_directory_id,
                aliases=aliases,
                audit_log_configuration=audit_log_configuration,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                deployment_type=deployment_type,
                kms_key_id=kms_key_id,
                preferred_subnet_id=preferred_subnet_id,
                security_group_ids=security_group_ids,
                self_managed_active_directory=self_managed_active_directory,
                skip_final_backup=skip_final_backup,
                storage_capacity=storage_capacity,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                weekly_maintenance_start_time=weekly_maintenance_start_time,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        active_directory_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        aliases: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        audit_log_configuration: Optional[AuditLogConfiguration] = core.arg(default=None)

        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        backup_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        deployment_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        self_managed_active_directory: Optional[SelfManagedActiveDirectory] = core.arg(default=None)

        skip_final_backup: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        storage_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        throughput_capacity: Union[int, core.IntOut] = core.arg()

        weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)
