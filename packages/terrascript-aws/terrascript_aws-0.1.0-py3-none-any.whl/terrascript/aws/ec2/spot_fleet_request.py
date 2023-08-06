from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CapacityRebalance(core.Schema):

    replacement_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        replacement_strategy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CapacityRebalance.Args(
                replacement_strategy=replacement_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replacement_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SpotMaintenanceStrategies(core.Schema):

    capacity_rebalance: Optional[CapacityRebalance] = core.attr(CapacityRebalance, default=None)

    def __init__(
        self,
        *,
        capacity_rebalance: Optional[CapacityRebalance] = None,
    ):
        super().__init__(
            args=SpotMaintenanceStrategies.Args(
                capacity_rebalance=capacity_rebalance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_rebalance: Optional[CapacityRebalance] = core.arg(default=None)


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    virtual_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        virtual_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        virtual_name: Union[str, core.StringOut] = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
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

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LaunchSpecification(core.Schema):

    ami: Union[str, core.StringOut] = core.attr(str)

    associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    iam_instance_profile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_instance_profile_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    monitoring: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    placement_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    placement_tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_block_device: Optional[
        Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
    ] = core.attr(RootBlockDevice, default=None, computed=True, kind=core.Kind.array)

    spot_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    user_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    weighted_capacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        ami: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        iam_instance_profile: Optional[Union[str, core.StringOut]] = None,
        iam_instance_profile_arn: Optional[Union[str, core.StringOut]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        monitoring: Optional[Union[bool, core.BoolOut]] = None,
        placement_group: Optional[Union[str, core.StringOut]] = None,
        placement_tenancy: Optional[Union[str, core.StringOut]] = None,
        root_block_device: Optional[
            Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
        ] = None,
        spot_price: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_data: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        weighted_capacity: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchSpecification.Args(
                ami=ami,
                instance_type=instance_type,
                associate_public_ip_address=associate_public_ip_address,
                availability_zone=availability_zone,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                ephemeral_block_device=ephemeral_block_device,
                iam_instance_profile=iam_instance_profile,
                iam_instance_profile_arn=iam_instance_profile_arn,
                key_name=key_name,
                monitoring=monitoring,
                placement_group=placement_group,
                placement_tenancy=placement_tenancy,
                root_block_device=root_block_device,
                spot_price=spot_price,
                subnet_id=subnet_id,
                tags=tags,
                user_data=user_data,
                vpc_security_group_ids=vpc_security_group_ids,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ami: Union[str, core.StringOut] = core.arg()

        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        iam_instance_profile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_instance_profile_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        monitoring: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        placement_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        placement_tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_block_device: Optional[
            Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]]
        ] = core.arg(default=None)

        spot_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        user_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        weighted_capacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LaunchTemplateSpecification(core.Schema):

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
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
class AcceleratorTotalMemoryMib(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AcceleratorTotalMemoryMib.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class TotalLocalStorageGb(core.Schema):

    max: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    min: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[float, core.FloatOut]] = None,
        min: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=TotalLocalStorageGb.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        min: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class BaselineEbsBandwidthMbps(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=BaselineEbsBandwidthMbps.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class VcpuCount(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=VcpuCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class NetworkInterfaceCount(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NetworkInterfaceCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class MemoryMib(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MemoryMib.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class AcceleratorCount(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[int, core.IntOut]] = None,
        min: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AcceleratorCount.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class MemoryGibPerVcpu(core.Schema):

    max: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    min: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        max: Optional[Union[float, core.FloatOut]] = None,
        min: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=MemoryGibPerVcpu.Args(
                max=max,
                min=min,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        min: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class InstanceRequirements(core.Schema):

    accelerator_count: Optional[AcceleratorCount] = core.attr(AcceleratorCount, default=None)

    accelerator_manufacturers: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    accelerator_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    accelerator_total_memory_mib: Optional[AcceleratorTotalMemoryMib] = core.attr(
        AcceleratorTotalMemoryMib, default=None
    )

    accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    bare_metal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbps] = core.attr(
        BaselineEbsBandwidthMbps, default=None
    )

    burstable_performance: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cpu_manufacturers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    excluded_instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    instance_generations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    local_storage: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    local_storage_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    memory_gib_per_vcpu: Optional[MemoryGibPerVcpu] = core.attr(MemoryGibPerVcpu, default=None)

    memory_mib: Optional[MemoryMib] = core.attr(MemoryMib, default=None)

    network_interface_count: Optional[NetworkInterfaceCount] = core.attr(
        NetworkInterfaceCount, default=None
    )

    on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    require_hibernate_support: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    spot_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    total_local_storage_gb: Optional[TotalLocalStorageGb] = core.attr(
        TotalLocalStorageGb, default=None
    )

    vcpu_count: Optional[VcpuCount] = core.attr(VcpuCount, default=None)

    def __init__(
        self,
        *,
        accelerator_count: Optional[AcceleratorCount] = None,
        accelerator_manufacturers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        accelerator_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        accelerator_total_memory_mib: Optional[AcceleratorTotalMemoryMib] = None,
        accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        bare_metal: Optional[Union[str, core.StringOut]] = None,
        baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbps] = None,
        burstable_performance: Optional[Union[str, core.StringOut]] = None,
        cpu_manufacturers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        excluded_instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        instance_generations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        local_storage: Optional[Union[str, core.StringOut]] = None,
        local_storage_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        memory_gib_per_vcpu: Optional[MemoryGibPerVcpu] = None,
        memory_mib: Optional[MemoryMib] = None,
        network_interface_count: Optional[NetworkInterfaceCount] = None,
        on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = None,
        require_hibernate_support: Optional[Union[bool, core.BoolOut]] = None,
        spot_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = None,
        total_local_storage_gb: Optional[TotalLocalStorageGb] = None,
        vcpu_count: Optional[VcpuCount] = None,
    ):
        super().__init__(
            args=InstanceRequirements.Args(
                accelerator_count=accelerator_count,
                accelerator_manufacturers=accelerator_manufacturers,
                accelerator_names=accelerator_names,
                accelerator_total_memory_mib=accelerator_total_memory_mib,
                accelerator_types=accelerator_types,
                bare_metal=bare_metal,
                baseline_ebs_bandwidth_mbps=baseline_ebs_bandwidth_mbps,
                burstable_performance=burstable_performance,
                cpu_manufacturers=cpu_manufacturers,
                excluded_instance_types=excluded_instance_types,
                instance_generations=instance_generations,
                local_storage=local_storage,
                local_storage_types=local_storage_types,
                memory_gib_per_vcpu=memory_gib_per_vcpu,
                memory_mib=memory_mib,
                network_interface_count=network_interface_count,
                on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
                require_hibernate_support=require_hibernate_support,
                spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
                total_local_storage_gb=total_local_storage_gb,
                vcpu_count=vcpu_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accelerator_count: Optional[AcceleratorCount] = core.arg(default=None)

        accelerator_manufacturers: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        accelerator_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        accelerator_total_memory_mib: Optional[AcceleratorTotalMemoryMib] = core.arg(default=None)

        accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        bare_metal: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        baseline_ebs_bandwidth_mbps: Optional[BaselineEbsBandwidthMbps] = core.arg(default=None)

        burstable_performance: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cpu_manufacturers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        excluded_instance_types: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        instance_generations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        local_storage: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        local_storage_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        memory_gib_per_vcpu: Optional[MemoryGibPerVcpu] = core.arg(default=None)

        memory_mib: Optional[MemoryMib] = core.arg(default=None)

        network_interface_count: Optional[NetworkInterfaceCount] = core.arg(default=None)

        on_demand_max_price_percentage_over_lowest_price: Optional[
            Union[int, core.IntOut]
        ] = core.arg(default=None)

        require_hibernate_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        spot_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        total_local_storage_gb: Optional[TotalLocalStorageGb] = core.arg(default=None)

        vcpu_count: Optional[VcpuCount] = core.arg(default=None)


@core.schema
class Overrides(core.Schema):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_requirements: Optional[InstanceRequirements] = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    priority: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None, computed=True)

    spot_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    weighted_capacity: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None, computed=True
    )

    def __init__(
        self,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        instance_requirements: Optional[InstanceRequirements] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[float, core.FloatOut]] = None,
        spot_price: Optional[Union[str, core.StringOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        weighted_capacity: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=Overrides.Args(
                availability_zone=availability_zone,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                priority=priority,
                spot_price=spot_price,
                subnet_id=subnet_id,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_requirements: Optional[InstanceRequirements] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        priority: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        spot_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        weighted_capacity: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class LaunchTemplateConfig(core.Schema):

    launch_template_specification: LaunchTemplateSpecification = core.attr(
        LaunchTemplateSpecification
    )

    overrides: Optional[Union[List[Overrides], core.ArrayOut[Overrides]]] = core.attr(
        Overrides, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        launch_template_specification: LaunchTemplateSpecification,
        overrides: Optional[Union[List[Overrides], core.ArrayOut[Overrides]]] = None,
    ):
        super().__init__(
            args=LaunchTemplateConfig.Args(
                launch_template_specification=launch_template_specification,
                overrides=overrides,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        overrides: Optional[Union[List[Overrides], core.ArrayOut[Overrides]]] = core.arg(
            default=None
        )


@core.resource(type="aws_spot_fleet_request", namespace="aws_ec2")
class SpotFleetRequest(core.Resource):

    allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    fleet_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_fleet_role: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_interruption_behaviour: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    launch_specification: Optional[
        Union[List[LaunchSpecification], core.ArrayOut[LaunchSpecification]]
    ] = core.attr(LaunchSpecification, default=None, kind=core.Kind.array)

    launch_template_config: Optional[
        Union[List[LaunchTemplateConfig], core.ArrayOut[LaunchTemplateConfig]]
    ] = core.attr(LaunchTemplateConfig, default=None, kind=core.Kind.array)

    load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    on_demand_max_total_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    on_demand_target_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    spot_maintenance_strategies: Optional[SpotMaintenanceStrategies] = core.attr(
        SpotMaintenanceStrategies, default=None
    )

    spot_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    spot_request_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_capacity: Union[int, core.IntOut] = core.attr(int)

    target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    terminate_instances_on_delete: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    valid_from: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    valid_until: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wait_for_fulfillment: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        iam_fleet_role: Union[str, core.StringOut],
        target_capacity: Union[int, core.IntOut],
        allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = None,
        fleet_type: Optional[Union[str, core.StringOut]] = None,
        instance_interruption_behaviour: Optional[Union[str, core.StringOut]] = None,
        instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = None,
        launch_specification: Optional[
            Union[List[LaunchSpecification], core.ArrayOut[LaunchSpecification]]
        ] = None,
        launch_template_config: Optional[
            Union[List[LaunchTemplateConfig], core.ArrayOut[LaunchTemplateConfig]]
        ] = None,
        load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        on_demand_max_total_price: Optional[Union[str, core.StringOut]] = None,
        on_demand_target_capacity: Optional[Union[int, core.IntOut]] = None,
        replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = None,
        spot_maintenance_strategies: Optional[SpotMaintenanceStrategies] = None,
        spot_price: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        terminate_instances_on_delete: Optional[Union[str, core.StringOut]] = None,
        terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = None,
        valid_from: Optional[Union[str, core.StringOut]] = None,
        valid_until: Optional[Union[str, core.StringOut]] = None,
        wait_for_fulfillment: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SpotFleetRequest.Args(
                iam_fleet_role=iam_fleet_role,
                target_capacity=target_capacity,
                allocation_strategy=allocation_strategy,
                excess_capacity_termination_policy=excess_capacity_termination_policy,
                fleet_type=fleet_type,
                instance_interruption_behaviour=instance_interruption_behaviour,
                instance_pools_to_use_count=instance_pools_to_use_count,
                launch_specification=launch_specification,
                launch_template_config=launch_template_config,
                load_balancers=load_balancers,
                on_demand_allocation_strategy=on_demand_allocation_strategy,
                on_demand_max_total_price=on_demand_max_total_price,
                on_demand_target_capacity=on_demand_target_capacity,
                replace_unhealthy_instances=replace_unhealthy_instances,
                spot_maintenance_strategies=spot_maintenance_strategies,
                spot_price=spot_price,
                tags=tags,
                tags_all=tags_all,
                target_group_arns=target_group_arns,
                terminate_instances_on_delete=terminate_instances_on_delete,
                terminate_instances_with_expiration=terminate_instances_with_expiration,
                valid_from=valid_from,
                valid_until=valid_until,
                wait_for_fulfillment=wait_for_fulfillment,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        fleet_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_fleet_role: Union[str, core.StringOut] = core.arg()

        instance_interruption_behaviour: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        launch_specification: Optional[
            Union[List[LaunchSpecification], core.ArrayOut[LaunchSpecification]]
        ] = core.arg(default=None)

        launch_template_config: Optional[
            Union[List[LaunchTemplateConfig], core.ArrayOut[LaunchTemplateConfig]]
        ] = core.arg(default=None)

        load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_demand_max_total_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_demand_target_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        spot_maintenance_strategies: Optional[SpotMaintenanceStrategies] = core.arg(default=None)

        spot_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_capacity: Union[int, core.IntOut] = core.arg()

        target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        terminate_instances_on_delete: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        valid_from: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        valid_until: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wait_for_fulfillment: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
