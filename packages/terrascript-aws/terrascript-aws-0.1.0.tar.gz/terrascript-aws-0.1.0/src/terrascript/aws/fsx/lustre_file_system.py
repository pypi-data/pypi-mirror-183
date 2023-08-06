from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LogConfiguration(core.Schema):

    destination: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        destination: Optional[Union[str, core.StringOut]] = None,
        level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LogConfiguration.Args(
                destination=destination,
                level=level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_fsx_lustre_file_system", namespace="aws_fsx")
class LustreFileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_import_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    backup_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    data_compression_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    drive_cache_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    export_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    file_system_type_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    import_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    imported_file_chunk_size: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    log_configuration: Optional[LogConfiguration] = core.attr(
        LogConfiguration, default=None, computed=True
    )

    mount_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    per_unit_storage_throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    storage_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

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

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        auto_import_policy: Optional[Union[str, core.StringOut]] = None,
        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = None,
        backup_id: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = None,
        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = None,
        data_compression_type: Optional[Union[str, core.StringOut]] = None,
        deployment_type: Optional[Union[str, core.StringOut]] = None,
        drive_cache_type: Optional[Union[str, core.StringOut]] = None,
        export_path: Optional[Union[str, core.StringOut]] = None,
        file_system_type_version: Optional[Union[str, core.StringOut]] = None,
        import_path: Optional[Union[str, core.StringOut]] = None,
        imported_file_chunk_size: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        log_configuration: Optional[LogConfiguration] = None,
        per_unit_storage_throughput: Optional[Union[int, core.IntOut]] = None,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
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
            args=LustreFileSystem.Args(
                subnet_ids=subnet_ids,
                auto_import_policy=auto_import_policy,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                data_compression_type=data_compression_type,
                deployment_type=deployment_type,
                drive_cache_type=drive_cache_type,
                export_path=export_path,
                file_system_type_version=file_system_type_version,
                import_path=import_path,
                imported_file_chunk_size=imported_file_chunk_size,
                kms_key_id=kms_key_id,
                log_configuration=log_configuration,
                per_unit_storage_throughput=per_unit_storage_throughput,
                security_group_ids=security_group_ids,
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
        auto_import_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        backup_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        data_compression_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        drive_cache_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        export_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_system_type_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        import_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        imported_file_chunk_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_configuration: Optional[LogConfiguration] = core.arg(default=None)

        per_unit_storage_throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        storage_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)
