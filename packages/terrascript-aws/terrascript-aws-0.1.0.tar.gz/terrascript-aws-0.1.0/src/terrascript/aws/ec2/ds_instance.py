from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Union[bool, core.BoolOut],
        device_name: Union[str, core.StringOut],
        encrypted: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        kms_key_id: Union[str, core.StringOut],
        snapshot_id: Union[str, core.StringOut],
        throughput: Union[int, core.IntOut],
        volume_id: Union[str, core.StringOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Union[bool, core.BoolOut] = core.arg()

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Union[bool, core.BoolOut] = core.arg()

        iops: Union[int, core.IntOut] = core.arg()

        kms_key_id: Union[str, core.StringOut] = core.arg()

        snapshot_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        throughput: Union[int, core.IntOut] = core.arg()

        volume_id: Union[str, core.StringOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_resource_name_dns_aaaa_record: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    hostname_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enable_resource_name_dns_a_record: Union[bool, core.BoolOut],
        enable_resource_name_dns_aaaa_record: Union[bool, core.BoolOut],
        hostname_type: Union[str, core.StringOut],
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
        enable_resource_name_dns_a_record: Union[bool, core.BoolOut] = core.arg()

        enable_resource_name_dns_aaaa_record: Union[bool, core.BoolOut] = core.arg()

        hostname_type: Union[str, core.StringOut] = core.arg()


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
class EnclaveOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=EnclaveOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Union[bool, core.BoolOut],
        device_name: Union[str, core.StringOut],
        encrypted: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        kms_key_id: Union[str, core.StringOut],
        throughput: Union[int, core.IntOut],
        volume_id: Union[str, core.StringOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                throughput=throughput,
                volume_id=volume_id,
                volume_size=volume_size,
                volume_type=volume_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Union[bool, core.BoolOut] = core.arg()

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Union[bool, core.BoolOut] = core.arg()

        iops: Union[int, core.IntOut] = core.arg()

        kms_key_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        throughput: Union[int, core.IntOut] = core.arg()

        volume_id: Union[str, core.StringOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        auto_recovery: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MaintenanceOptions.Args(
                auto_recovery=auto_recovery,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_recovery: Union[str, core.StringOut] = core.arg()


@core.schema
class CreditSpecification(core.Schema):

    cpu_credits: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cpu_credits: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CreditSpecification.Args(
                cpu_credits=cpu_credits,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_credits: Union[str, core.StringOut] = core.arg()


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    http_put_response_hop_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    http_tokens: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_metadata_tags: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: Union[str, core.StringOut],
        http_put_response_hop_limit: Union[int, core.IntOut],
        http_tokens: Union[str, core.StringOut],
        instance_metadata_tags: Union[str, core.StringOut],
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
        http_endpoint: Union[str, core.StringOut] = core.arg()

        http_put_response_hop_limit: Union[int, core.IntOut] = core.arg()

        http_tokens: Union[str, core.StringOut] = core.arg()

        instance_metadata_tags: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_instance", namespace="aws_ec2")
class DsInstance(core.Data):

    ami: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associate_public_ip_address: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    credit_specification: Union[
        List[CreditSpecification], core.ArrayOut[CreditSpecification]
    ] = core.attr(CreditSpecification, computed=True, kind=core.Kind.array)

    disable_api_stop: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    disable_api_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ebs_block_device: Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    ebs_optimized: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enclave_options: Union[List[EnclaveOptions], core.ArrayOut[EnclaveOptions]] = core.attr(
        EnclaveOptions, computed=True, kind=core.Kind.array
    )

    ephemeral_block_device: Union[
        List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    get_password_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    get_user_data: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    host_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_instance_profile: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    instance_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    key_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_options: Union[
        List[MaintenanceOptions], core.ArrayOut[MaintenanceOptions]
    ] = core.attr(MaintenanceOptions, computed=True, kind=core.Kind.array)

    metadata_options: Union[List[MetadataOptions], core.ArrayOut[MetadataOptions]] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    monitoring: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    password_data: Union[str, core.StringOut] = core.attr(str, computed=True)

    placement_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    placement_partition_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    private_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_name_options: Union[
        List[PrivateDnsNameOptions], core.ArrayOut[PrivateDnsNameOptions]
    ] = core.attr(PrivateDnsNameOptions, computed=True, kind=core.Kind.array)

    private_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_block_device: Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    secondary_private_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    source_dest_check: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tenancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_data: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_data_base64: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        get_password_data: Optional[Union[bool, core.BoolOut]] = None,
        get_user_data: Optional[Union[bool, core.BoolOut]] = None,
        instance_id: Optional[Union[str, core.StringOut]] = None,
        instance_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsInstance.Args(
                filter=filter,
                get_password_data=get_password_data,
                get_user_data=get_user_data,
                instance_id=instance_id,
                instance_tags=instance_tags,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        get_password_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        get_user_data: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
