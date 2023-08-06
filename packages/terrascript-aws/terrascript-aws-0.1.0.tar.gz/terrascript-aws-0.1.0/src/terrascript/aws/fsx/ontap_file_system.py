from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Intercluster(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Intercluster.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Management(core.Schema):

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dns_name: Union[str, core.StringOut],
        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Management.Args(
                dns_name=dns_name,
                ip_addresses=ip_addresses,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dns_name: Union[str, core.StringOut] = core.arg()

        ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Endpoints(core.Schema):

    intercluster: Union[List[Intercluster], core.ArrayOut[Intercluster]] = core.attr(
        Intercluster, computed=True, kind=core.Kind.array
    )

    management: Union[List[Management], core.ArrayOut[Management]] = core.attr(
        Management, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        intercluster: Union[List[Intercluster], core.ArrayOut[Intercluster]],
        management: Union[List[Management], core.ArrayOut[Management]],
    ):
        super().__init__(
            args=Endpoints.Args(
                intercluster=intercluster,
                management=management,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intercluster: Union[List[Intercluster], core.ArrayOut[Intercluster]] = core.arg()

        management: Union[List[Management], core.ArrayOut[Management]] = core.arg()


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


@core.resource(type="aws_fsx_ontap_file_system", namespace="aws_fsx")
class OntapFileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    deployment_type: Union[str, core.StringOut] = core.attr(str)

    disk_iops_configuration: Optional[DiskIopsConfiguration] = core.attr(
        DiskIopsConfiguration, default=None, computed=True
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_ip_address_range: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    endpoints: Union[List[Endpoints], core.ArrayOut[Endpoints]] = core.attr(
        Endpoints, computed=True, kind=core.Kind.array
    )

    fsx_admin_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_interface_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_subnet_id: Union[str, core.StringOut] = core.attr(str)

    route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

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
        preferred_subnet_id: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        throughput_capacity: Union[int, core.IntOut],
        automatic_backup_retention_days: Optional[Union[int, core.IntOut]] = None,
        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = None,
        disk_iops_configuration: Optional[DiskIopsConfiguration] = None,
        endpoint_ip_address_range: Optional[Union[str, core.StringOut]] = None,
        fsx_admin_password: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
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
            args=OntapFileSystem.Args(
                deployment_type=deployment_type,
                preferred_subnet_id=preferred_subnet_id,
                subnet_ids=subnet_ids,
                throughput_capacity=throughput_capacity,
                automatic_backup_retention_days=automatic_backup_retention_days,
                daily_automatic_backup_start_time=daily_automatic_backup_start_time,
                disk_iops_configuration=disk_iops_configuration,
                endpoint_ip_address_range=endpoint_ip_address_range,
                fsx_admin_password=fsx_admin_password,
                kms_key_id=kms_key_id,
                route_table_ids=route_table_ids,
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

        daily_automatic_backup_start_time: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        deployment_type: Union[str, core.StringOut] = core.arg()

        disk_iops_configuration: Optional[DiskIopsConfiguration] = core.arg(default=None)

        endpoint_ip_address_range: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fsx_admin_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_subnet_id: Union[str, core.StringOut] = core.arg()

        route_table_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

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
