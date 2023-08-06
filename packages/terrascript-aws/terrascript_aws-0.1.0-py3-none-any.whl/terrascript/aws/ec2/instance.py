from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        volume_id: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                volume_id=volume_id,
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                tags=tags,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_id: Union[str, core.StringOut] = core.arg()

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu_credits: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    http_tokens: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    instance_metadata_tags: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint: Optional[Union[str, core.StringOut]] = None,
        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = None,
        http_tokens: Optional[Union[str, core.StringOut]] = None,
        instance_metadata_tags: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
                instance_metadata_tags=instance_metadata_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        http_tokens: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_metadata_tags: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        volume_id: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                device_name=device_name,
                volume_id=volume_id,
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                tags=tags,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_id: Union[str, core.StringOut] = core.arg()

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NetworkInterface(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_index: Union[int, core.IntOut] = core.attr(int)

    network_card_index: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        device_index: Union[int, core.IntOut],
        network_interface_id: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        network_card_index: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NetworkInterface.Args(
                device_index=device_index,
                network_interface_id=network_interface_id,
                delete_on_termination=delete_on_termination,
                network_card_index=network_card_index,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        device_index: Union[int, core.IntOut] = core.arg()

        network_card_index: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        network_interface_id: Union[str, core.StringOut] = core.arg()


@core.schema
class EnclaveOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class CapacityReservationTarget(core.Schema):

    capacity_reservation_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    capacity_reservation_resource_group_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_id: Optional[Union[str, core.StringOut]] = None,
        capacity_reservation_resource_group_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CapacityReservationTarget.Args(
                capacity_reservation_id=capacity_reservation_id,
                capacity_reservation_resource_group_arn=capacity_reservation_resource_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        capacity_reservation_resource_group_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class CapacityReservationSpecification(core.Schema):

    capacity_reservation_preference: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    capacity_reservation_target: Optional[CapacityReservationTarget] = core.attr(
        CapacityReservationTarget, default=None
    )

    def __init__(
        self,
        *,
        capacity_reservation_preference: Optional[Union[str, core.StringOut]] = None,
        capacity_reservation_target: Optional[CapacityReservationTarget] = None,
    ):
        super().__init__(
            args=CapacityReservationSpecification.Args(
                capacity_reservation_preference=capacity_reservation_preference,
                capacity_reservation_target=capacity_reservation_target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_reservation_preference: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        capacity_reservation_target: Optional[CapacityReservationTarget] = core.arg(default=None)


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        auto_recovery: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    no_device: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    virtual_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        no_device: Optional[Union[bool, core.BoolOut]] = None,
        virtual_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        no_device: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        virtual_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enable_resource_name_dns_aaaa_record: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    hostname_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: Optional[Union[bool, core.BoolOut]] = None,
        enable_resource_name_dns_aaaa_record: Optional[Union[bool, core.BoolOut]] = None,
        hostname_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PrivateDnsNameOptions.Args(
                enable_resource_name_dns_a_record=enable_resource_name_dns_a_record,
                enable_resource_name_dns_aaaa_record=enable_resource_name_dns_aaaa_record,
                hostname_type=hostname_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_resource_name_dns_a_record: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        enable_resource_name_dns_aaaa_record: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        hostname_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_instance", namespace="aws_ec2")
class Instance(core.Resource):

    ami: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    capacity_reservation_specification: Optional[CapacityReservationSpecification] = core.attr(
        CapacityReservationSpecification, default=None, computed=True
    )

    cpu_core_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    cpu_threads_per_core: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    credit_specification: Optional[CreditSpecification] = core.attr(
        CreditSpecification, default=None
    )

    disable_api_stop: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    disable_api_termination: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enclave_options: Optional[EnclaveOptions] = core.attr(
        EnclaveOptions, default=None, computed=True
    )

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    get_password_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    hibernation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    host_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    iam_instance_profile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_address_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    launch_template: Optional[LaunchTemplate] = core.attr(LaunchTemplate, default=None)

    maintenance_options: Optional[MaintenanceOptions] = core.attr(
        MaintenanceOptions, default=None, computed=True
    )

    metadata_options: Optional[MetadataOptions] = core.attr(
        MetadataOptions, default=None, computed=True
    )

    monitoring: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    network_interface: Optional[
        Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]]
    ] = core.attr(NetworkInterface, default=None, computed=True, kind=core.Kind.array)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    password_data: Union[str, core.StringOut] = core.attr(str, computed=True)

    placement_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    placement_partition_number: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    primary_network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_name_options: Optional[PrivateDnsNameOptions] = core.attr(
        PrivateDnsNameOptions, default=None, computed=True
    )

    private_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    public_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_block_device: Optional[RootBlockDevice] = core.attr(
        RootBlockDevice, default=None, computed=True
    )

    secondary_private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    source_dest_check: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    user_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    user_data_base64: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    user_data_replace_on_change: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    volume_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        ami: Optional[Union[str, core.StringOut]] = None,
        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        capacity_reservation_specification: Optional[CapacityReservationSpecification] = None,
        cpu_core_count: Optional[Union[int, core.IntOut]] = None,
        cpu_threads_per_core: Optional[Union[int, core.IntOut]] = None,
        credit_specification: Optional[CreditSpecification] = None,
        disable_api_stop: Optional[Union[bool, core.BoolOut]] = None,
        disable_api_termination: Optional[Union[bool, core.BoolOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        enclave_options: Optional[EnclaveOptions] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        get_password_data: Optional[Union[bool, core.BoolOut]] = None,
        hibernation: Optional[Union[bool, core.BoolOut]] = None,
        host_id: Optional[Union[str, core.StringOut]] = None,
        iam_instance_profile: Optional[Union[str, core.StringOut]] = None,
        instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        ipv6_address_count: Optional[Union[int, core.IntOut]] = None,
        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        launch_template: Optional[LaunchTemplate] = None,
        maintenance_options: Optional[MaintenanceOptions] = None,
        metadata_options: Optional[MetadataOptions] = None,
        monitoring: Optional[Union[bool, core.BoolOut]] = None,
        network_interface: Optional[
            Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]]
        ] = None,
        placement_group: Optional[Union[str, core.StringOut]] = None,
        placement_partition_number: Optional[Union[int, core.IntOut]] = None,
        private_dns_name_options: Optional[PrivateDnsNameOptions] = None,
        private_ip: Optional[Union[str, core.StringOut]] = None,
        root_block_device: Optional[RootBlockDevice] = None,
        secondary_private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        source_dest_check: Optional[Union[bool, core.BoolOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tenancy: Optional[Union[str, core.StringOut]] = None,
        user_data: Optional[Union[str, core.StringOut]] = None,
        user_data_base64: Optional[Union[str, core.StringOut]] = None,
        user_data_replace_on_change: Optional[Union[bool, core.BoolOut]] = None,
        volume_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Instance.Args(
                ami=ami,
                associate_public_ip_address=associate_public_ip_address,
                availability_zone=availability_zone,
                capacity_reservation_specification=capacity_reservation_specification,
                cpu_core_count=cpu_core_count,
                cpu_threads_per_core=cpu_threads_per_core,
                credit_specification=credit_specification,
                disable_api_stop=disable_api_stop,
                disable_api_termination=disable_api_termination,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                enclave_options=enclave_options,
                ephemeral_block_device=ephemeral_block_device,
                get_password_data=get_password_data,
                hibernation=hibernation,
                host_id=host_id,
                iam_instance_profile=iam_instance_profile,
                instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
                instance_type=instance_type,
                ipv6_address_count=ipv6_address_count,
                ipv6_addresses=ipv6_addresses,
                key_name=key_name,
                launch_template=launch_template,
                maintenance_options=maintenance_options,
                metadata_options=metadata_options,
                monitoring=monitoring,
                network_interface=network_interface,
                placement_group=placement_group,
                placement_partition_number=placement_partition_number,
                private_dns_name_options=private_dns_name_options,
                private_ip=private_ip,
                root_block_device=root_block_device,
                secondary_private_ips=secondary_private_ips,
                security_groups=security_groups,
                source_dest_check=source_dest_check,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                tenancy=tenancy,
                user_data=user_data,
                user_data_base64=user_data_base64,
                user_data_replace_on_change=user_data_replace_on_change,
                volume_tags=volume_tags,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ami: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        capacity_reservation_specification: Optional[CapacityReservationSpecification] = core.arg(
            default=None
        )

        cpu_core_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cpu_threads_per_core: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        credit_specification: Optional[CreditSpecification] = core.arg(default=None)

        disable_api_stop: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        disable_api_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enclave_options: Optional[EnclaveOptions] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        get_password_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        hibernation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        host_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_instance_profile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_address_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template: Optional[LaunchTemplate] = core.arg(default=None)

        maintenance_options: Optional[MaintenanceOptions] = core.arg(default=None)

        metadata_options: Optional[MetadataOptions] = core.arg(default=None)

        monitoring: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        network_interface: Optional[
            Union[List[NetworkInterface], core.ArrayOut[NetworkInterface]]
        ] = core.arg(default=None)

        placement_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        placement_partition_number: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        private_dns_name_options: Optional[PrivateDnsNameOptions] = core.arg(default=None)

        private_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_block_device: Optional[RootBlockDevice] = core.arg(default=None)

        secondary_private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        source_dest_check: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_data_base64: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_data_replace_on_change: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        volume_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
