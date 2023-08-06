from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SmbActiveDirectorySettings(core.Schema):

    active_directory_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_controllers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    domain_name: Union[str, core.StringOut] = core.attr(str)

    organizational_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    password: Union[str, core.StringOut] = core.attr(str)

    timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    username: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        active_directory_status: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        username: Union[str, core.StringOut],
        domain_controllers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        organizational_unit: Optional[Union[str, core.StringOut]] = None,
        timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SmbActiveDirectorySettings.Args(
                active_directory_status=active_directory_status,
                domain_name=domain_name,
                password=password,
                username=username,
                domain_controllers=domain_controllers,
                organizational_unit=organizational_unit,
                timeout_in_seconds=timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_directory_status: Union[str, core.StringOut] = core.arg()

        domain_controllers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        domain_name: Union[str, core.StringOut] = core.arg()

        organizational_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        password: Union[str, core.StringOut] = core.arg()

        timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        username: Union[str, core.StringOut] = core.arg()


@core.schema
class GatewayNetworkInterface(core.Schema):

    ipv4_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ipv4_address: Union[str, core.StringOut],
    ):
        super().__init__(
            args=GatewayNetworkInterface.Args(
                ipv4_address=ipv4_address,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ipv4_address: Union[str, core.StringOut] = core.arg()


@core.schema
class MaintenanceStartTime(core.Schema):

    day_of_month: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    day_of_week: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hour_of_day: Union[int, core.IntOut] = core.attr(int)

    minute_of_hour: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        hour_of_day: Union[int, core.IntOut],
        day_of_month: Optional[Union[str, core.StringOut]] = None,
        day_of_week: Optional[Union[str, core.StringOut]] = None,
        minute_of_hour: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MaintenanceStartTime.Args(
                hour_of_day=hour_of_day,
                day_of_month=day_of_month,
                day_of_week=day_of_week,
                minute_of_hour=minute_of_hour,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day_of_month: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        day_of_week: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hour_of_day: Union[int, core.IntOut] = core.arg()

        minute_of_hour: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_storagegateway_gateway", namespace="aws_storagegateway")
class Gateway(core.Resource):

    activation_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    average_download_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    average_upload_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ec2_instance_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_ip_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    gateway_name: Union[str, core.StringOut] = core.attr(str)

    gateway_network_interface: Union[
        List[GatewayNetworkInterface], core.ArrayOut[GatewayNetworkInterface]
    ] = core.attr(GatewayNetworkInterface, computed=True, kind=core.Kind.array)

    gateway_timezone: Union[str, core.StringOut] = core.attr(str)

    gateway_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    gateway_vpc_endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host_environment: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_start_time: Optional[MaintenanceStartTime] = core.attr(
        MaintenanceStartTime, default=None, computed=True
    )

    medium_changer_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    smb_active_directory_settings: Optional[SmbActiveDirectorySettings] = core.attr(
        SmbActiveDirectorySettings, default=None
    )

    smb_file_share_visibility: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    smb_guest_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    smb_security_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tape_drive_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_name: Union[str, core.StringOut],
        gateway_timezone: Union[str, core.StringOut],
        activation_key: Optional[Union[str, core.StringOut]] = None,
        average_download_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = None,
        average_upload_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = None,
        cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = None,
        gateway_ip_address: Optional[Union[str, core.StringOut]] = None,
        gateway_type: Optional[Union[str, core.StringOut]] = None,
        gateway_vpc_endpoint: Optional[Union[str, core.StringOut]] = None,
        maintenance_start_time: Optional[MaintenanceStartTime] = None,
        medium_changer_type: Optional[Union[str, core.StringOut]] = None,
        smb_active_directory_settings: Optional[SmbActiveDirectorySettings] = None,
        smb_file_share_visibility: Optional[Union[bool, core.BoolOut]] = None,
        smb_guest_password: Optional[Union[str, core.StringOut]] = None,
        smb_security_strategy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tape_drive_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Gateway.Args(
                gateway_name=gateway_name,
                gateway_timezone=gateway_timezone,
                activation_key=activation_key,
                average_download_rate_limit_in_bits_per_sec=average_download_rate_limit_in_bits_per_sec,
                average_upload_rate_limit_in_bits_per_sec=average_upload_rate_limit_in_bits_per_sec,
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                gateway_ip_address=gateway_ip_address,
                gateway_type=gateway_type,
                gateway_vpc_endpoint=gateway_vpc_endpoint,
                maintenance_start_time=maintenance_start_time,
                medium_changer_type=medium_changer_type,
                smb_active_directory_settings=smb_active_directory_settings,
                smb_file_share_visibility=smb_file_share_visibility,
                smb_guest_password=smb_guest_password,
                smb_security_strategy=smb_security_strategy,
                tags=tags,
                tags_all=tags_all,
                tape_drive_type=tape_drive_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activation_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        average_download_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        average_upload_rate_limit_in_bits_per_sec: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_name: Union[str, core.StringOut] = core.arg()

        gateway_timezone: Union[str, core.StringOut] = core.arg()

        gateway_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_vpc_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        maintenance_start_time: Optional[MaintenanceStartTime] = core.arg(default=None)

        medium_changer_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        smb_active_directory_settings: Optional[SmbActiveDirectorySettings] = core.arg(default=None)

        smb_file_share_visibility: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        smb_guest_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        smb_security_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tape_drive_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
