from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DiskIopsConfiguration(core.Schema):

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        iops: Optional[Union[int, core.IntOut]] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DiskIopsConfiguration.Args(
                iops=iops,
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ClientConfigurations(core.Schema):

    clients: Union[str, core.StringOut] = core.attr(str)

    options: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        clients: Union[str, core.StringOut],
        options: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ClientConfigurations.Args(
                clients=clients,
                options=options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        clients: Union[str, core.StringOut] = core.arg()

        options: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class NfsExports(core.Schema):

    client_configurations: Union[
        List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
    ] = core.attr(ClientConfigurations, kind=core.Kind.array)

    def __init__(
        self,
        *,
        client_configurations: Union[
            List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
        ],
    ):
        super().__init__(
            args=NfsExports.Args(
                client_configurations=client_configurations,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_configurations: Union[
            List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
        ] = core.arg()


@core.schema
class UserAndGroupQuotas(core.Schema):

    id: Union[int, core.IntOut] = core.attr(int)

    storage_capacity_quota_gib: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[int, core.IntOut],
        storage_capacity_quota_gib: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserAndGroupQuotas.Args(
                id=id,
                storage_capacity_quota_gib=storage_capacity_quota_gib,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[int, core.IntOut] = core.arg()

        storage_capacity_quota_gib: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class RootVolumeConfiguration(core.Schema):

    copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    data_compression_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    nfs_exports: Optional[NfsExports] = core.attr(NfsExports, default=None)

    read_only: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    record_size_kib: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    user_and_group_quotas: Optional[
        Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
    ] = core.attr(UserAndGroupQuotas, default=None, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = None,
        data_compression_type: Optional[Union[str, core.StringOut]] = None,
        nfs_exports: Optional[NfsExports] = None,
        read_only: Optional[Union[bool, core.BoolOut]] = None,
        record_size_kib: Optional[Union[int, core.IntOut]] = None,
        user_and_group_quotas: Optional[
            Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
        ] = None,
    ):
        super().__init__(
            args=RootVolumeConfiguration.Args(
                copy_tags_to_snapshots=copy_tags_to_snapshots,
                data_compression_type=data_compression_type,
                nfs_exports=nfs_exports,
                read_only=read_only,
                record_size_kib=record_size_kib,
                user_and_group_quotas=user_and_group_quotas,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        data_compression_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nfs_exports: Optional[NfsExports] = core.arg(default=None)

        read_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        record_size_kib: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        user_and_group_quotas: Optional[
            Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
        ] = core.arg(default=None)


@core.resource(type="aws_fsx_openzfs_file_system", namespace="aws_fsx")
class OpenzfsFileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    backup_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    copy_tags_to_volumes: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    deployment_type: Union[str, core.StringOut] = core.attr(str)

    disk_iops_configuration: Optional[DiskIopsConfiguration] = core.attr(
        DiskIopsConfiguration, default=None, computed=True
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_volume_configuration: Optional[RootVolumeConfiguration] = core.attr(
        RootVolumeConfiguration, default=None, computed=True
    )

    root_volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    throughput_capacity: Union[int, core.IntOut] = core.attr(int)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_type: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        throughput_capacity: Union[int, core.IntOut],
        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = None,
        backup_id: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = None,
        copy_tags_to_volumes: Optional[Union[bool, core.BoolOut]] = None,
        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = None,
        disk_iops_configuration: Optional[DiskIopsConfiguration] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        root_volume_configuration: Optional[RootVolumeConfiguration] = None,
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
            args=OpenzfsFileSystem.Args(
                deployment_type=deployment_type,
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                automatic_backup_retention_days=automatic_backup_retention_days,
                backup_id=backup_id,
                copy_tags_to_backups=copy_tags_to_backups,
                copy_tags_to_volumes=copy_tags_to_volumes,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                disk_iops_configuration=disk_iops_configuration,
                kms_key_id=kms_key_id,
                root_volume_configuration=root_volume_configuration,
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
        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        backup_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags_to_backups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        copy_tags_to_volumes: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        deployment_type: Union[str, core.StringOut] = core.arg()

        disk_iops_configuration: Optional[DiskIopsConfiguration] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_volume_configuration: Optional[RootVolumeConfiguration] = core.arg(default=None)

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

        throughput_capacity: Union[int, core.IntOut] = core.arg()

        weekly_maintenance_start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)
