from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Ebs(core.Schema):

    delete_on_termination: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[str, core.StringOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Ebs.Args(
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
        delete_on_termination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class BlockDeviceMappings(core.Schema):

    device_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs: Optional[Ebs] = core.attr(Ebs, default=None)

    no_device: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    virtual_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Optional[Union[str, core.StringOut]] = None,
        ebs: Optional[Ebs] = None,
        no_device: Optional[Union[str, core.StringOut]] = None,
        virtual_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=BlockDeviceMappings.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs: Optional[Ebs] = core.arg(default=None)

        no_device: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        virtual_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class HibernationOptions(core.Schema):

    configured: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        configured: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=HibernationOptions.Args(
                configured=configured,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        configured: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SpotOptions(core.Schema):

    block_duration_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    instance_interruption_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    max_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    spot_instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    valid_until: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        block_duration_minutes: Optional[Union[int, core.IntOut]] = None,
        instance_interruption_behavior: Optional[Union[str, core.StringOut]] = None,
        max_price: Optional[Union[str, core.StringOut]] = None,
        spot_instance_type: Optional[Union[str, core.StringOut]] = None,
        valid_until: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SpotOptions.Args(
                block_duration_minutes=block_duration_minutes,
                instance_interruption_behavior=instance_interruption_behavior,
                max_price=max_price,
                spot_instance_type=spot_instance_type,
                valid_until=valid_until,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_duration_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_interruption_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        max_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        spot_instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        valid_until: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InstanceMarketOptions(core.Schema):

    market_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    spot_options: Optional[SpotOptions] = core.attr(SpotOptions, default=None)

    def __init__(
        self,
        *,
        market_type: Optional[Union[str, core.StringOut]] = None,
        spot_options: Optional[SpotOptions] = None,
    ):
        super().__init__(
            args=InstanceMarketOptions.Args(
                market_type=market_type,
                spot_options=spot_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        market_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        spot_options: Optional[SpotOptions] = core.arg(default=None)


@core.schema
class PrivateDnsNameOptions(core.Schema):

    enable_resource_name_dns_a_record: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_resource_name_dns_aaaa_record: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    hostname_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    http_protocol_ipv6: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    http_tokens: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    instance_metadata_tags: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        http_endpoint: Optional[Union[str, core.StringOut]] = None,
        http_protocol_ipv6: Optional[Union[str, core.StringOut]] = None,
        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = None,
        http_tokens: Optional[Union[str, core.StringOut]] = None,
        instance_metadata_tags: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_protocol_ipv6=http_protocol_ipv6,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
                instance_metadata_tags=instance_metadata_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_protocol_ipv6: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        http_tokens: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_metadata_tags: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EnclaveOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

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
class CpuOptions(core.Schema):

    core_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    threads_per_core: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        core_count: Optional[Union[int, core.IntOut]] = None,
        threads_per_core: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CpuOptions.Args(
                core_count=core_count,
                threads_per_core=threads_per_core,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        core_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        threads_per_core: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ElasticGpuSpecifications(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ElasticGpuSpecifications.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class TagSpecifications(core.Schema):

    resource_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        resource_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=TagSpecifications.Args(
                resource_type=resource_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


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
class MemoryMib(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        min: Union[int, core.IntOut],
        max: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MemoryMib.Args(
                min=min,
                max=max,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Union[int, core.IntOut] = core.arg()


@core.schema
class VcpuCount(core.Schema):

    max: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        min: Union[int, core.IntOut],
        max: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=VcpuCount.Args(
                min=min,
                max=max,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min: Union[int, core.IntOut] = core.arg()


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

    memory_mib: MemoryMib = core.attr(MemoryMib)

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

    vcpu_count: VcpuCount = core.attr(VcpuCount)

    def __init__(
        self,
        *,
        memory_mib: MemoryMib,
        vcpu_count: VcpuCount,
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
        network_interface_count: Optional[NetworkInterfaceCount] = None,
        on_demand_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = None,
        require_hibernate_support: Optional[Union[bool, core.BoolOut]] = None,
        spot_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = None,
        total_local_storage_gb: Optional[TotalLocalStorageGb] = None,
    ):
        super().__init__(
            args=InstanceRequirements.Args(
                memory_mib=memory_mib,
                vcpu_count=vcpu_count,
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
                network_interface_count=network_interface_count,
                on_demand_max_price_percentage_over_lowest_price=on_demand_max_price_percentage_over_lowest_price,
                require_hibernate_support=require_hibernate_support,
                spot_max_price_percentage_over_lowest_price=spot_max_price_percentage_over_lowest_price,
                total_local_storage_gb=total_local_storage_gb,
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

        memory_mib: MemoryMib = core.arg()

        network_interface_count: Optional[NetworkInterfaceCount] = core.arg(default=None)

        on_demand_max_price_percentage_over_lowest_price: Optional[
            Union[int, core.IntOut]
        ] = core.arg(default=None)

        require_hibernate_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        spot_max_price_percentage_over_lowest_price: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        total_local_storage_gb: Optional[TotalLocalStorageGb] = core.arg(default=None)

        vcpu_count: VcpuCount = core.arg()


@core.schema
class IamInstanceProfile(core.Schema):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=IamInstanceProfile.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MaintenanceOptions(core.Schema):

    auto_recovery: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
class ElasticInferenceAccelerator(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ElasticInferenceAccelerator.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


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
class Monitoring(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Monitoring.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class NetworkInterfaces(core.Schema):

    associate_carrier_ip_address: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    associate_public_ip_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    delete_on_termination: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_index: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interface_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv4_address_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv4_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv4_prefix_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv6_address_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ipv6_prefix_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    network_card_index: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    network_interface_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    private_ip_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        associate_carrier_ip_address: Optional[Union[str, core.StringOut]] = None,
        associate_public_ip_address: Optional[Union[str, core.StringOut]] = None,
        delete_on_termination: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        device_index: Optional[Union[int, core.IntOut]] = None,
        interface_type: Optional[Union[str, core.StringOut]] = None,
        ipv4_address_count: Optional[Union[int, core.IntOut]] = None,
        ipv4_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv4_prefix_count: Optional[Union[int, core.IntOut]] = None,
        ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv6_address_count: Optional[Union[int, core.IntOut]] = None,
        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv6_prefix_count: Optional[Union[int, core.IntOut]] = None,
        ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        network_card_index: Optional[Union[int, core.IntOut]] = None,
        network_interface_id: Optional[Union[str, core.StringOut]] = None,
        private_ip_address: Optional[Union[str, core.StringOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NetworkInterfaces.Args(
                associate_carrier_ip_address=associate_carrier_ip_address,
                associate_public_ip_address=associate_public_ip_address,
                delete_on_termination=delete_on_termination,
                description=description,
                device_index=device_index,
                interface_type=interface_type,
                ipv4_address_count=ipv4_address_count,
                ipv4_addresses=ipv4_addresses,
                ipv4_prefix_count=ipv4_prefix_count,
                ipv4_prefixes=ipv4_prefixes,
                ipv6_address_count=ipv6_address_count,
                ipv6_addresses=ipv6_addresses,
                ipv6_prefix_count=ipv6_prefix_count,
                ipv6_prefixes=ipv6_prefixes,
                network_card_index=network_card_index,
                network_interface_id=network_interface_id,
                private_ip_address=private_ip_address,
                security_groups=security_groups,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        associate_carrier_ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        associate_public_ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delete_on_termination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_index: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interface_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv4_address_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv4_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv4_prefix_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv6_address_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv6_prefix_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        network_card_index: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        network_interface_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Placement(core.Schema):

    affinity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    host_resource_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    partition_number: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    spread_domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        affinity: Optional[Union[str, core.StringOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        group_name: Optional[Union[str, core.StringOut]] = None,
        host_id: Optional[Union[str, core.StringOut]] = None,
        host_resource_group_arn: Optional[Union[str, core.StringOut]] = None,
        partition_number: Optional[Union[int, core.IntOut]] = None,
        spread_domain: Optional[Union[str, core.StringOut]] = None,
        tenancy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Placement.Args(
                affinity=affinity,
                availability_zone=availability_zone,
                group_name=group_name,
                host_id=host_id,
                host_resource_group_arn=host_resource_group_arn,
                partition_number=partition_number,
                spread_domain=spread_domain,
                tenancy=tenancy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        affinity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        host_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        host_resource_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        partition_number: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        spread_domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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
class LicenseSpecification(core.Schema):

    license_configuration_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        license_configuration_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LicenseSpecification.Args(
                license_configuration_arn=license_configuration_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        license_configuration_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_launch_template", namespace="aws_ec2")
class LaunchTemplate(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    block_device_mappings: Optional[
        Union[List[BlockDeviceMappings], core.ArrayOut[BlockDeviceMappings]]
    ] = core.attr(BlockDeviceMappings, default=None, kind=core.Kind.array)

    capacity_reservation_specification: Optional[CapacityReservationSpecification] = core.attr(
        CapacityReservationSpecification, default=None
    )

    cpu_options: Optional[CpuOptions] = core.attr(CpuOptions, default=None)

    credit_specification: Optional[CreditSpecification] = core.attr(
        CreditSpecification, default=None
    )

    default_version: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    disable_api_stop: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    disable_api_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ebs_optimized: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    elastic_gpu_specifications: Optional[
        Union[List[ElasticGpuSpecifications], core.ArrayOut[ElasticGpuSpecifications]]
    ] = core.attr(ElasticGpuSpecifications, default=None, kind=core.Kind.array)

    elastic_inference_accelerator: Optional[ElasticInferenceAccelerator] = core.attr(
        ElasticInferenceAccelerator, default=None
    )

    enclave_options: Optional[EnclaveOptions] = core.attr(EnclaveOptions, default=None)

    hibernation_options: Optional[HibernationOptions] = core.attr(HibernationOptions, default=None)

    iam_instance_profile: Optional[IamInstanceProfile] = core.attr(IamInstanceProfile, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    instance_market_options: Optional[InstanceMarketOptions] = core.attr(
        InstanceMarketOptions, default=None
    )

    instance_requirements: Optional[InstanceRequirements] = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kernel_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    latest_version: Union[int, core.IntOut] = core.attr(int, computed=True)

    license_specification: Optional[
        Union[List[LicenseSpecification], core.ArrayOut[LicenseSpecification]]
    ] = core.attr(LicenseSpecification, default=None, kind=core.Kind.array)

    maintenance_options: Optional[MaintenanceOptions] = core.attr(MaintenanceOptions, default=None)

    metadata_options: Optional[MetadataOptions] = core.attr(
        MetadataOptions, default=None, computed=True
    )

    monitoring: Optional[Monitoring] = core.attr(Monitoring, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_interfaces: Optional[
        Union[List[NetworkInterfaces], core.ArrayOut[NetworkInterfaces]]
    ] = core.attr(NetworkInterfaces, default=None, kind=core.Kind.array)

    placement: Optional[Placement] = core.attr(Placement, default=None)

    private_dns_name_options: Optional[PrivateDnsNameOptions] = core.attr(
        PrivateDnsNameOptions, default=None
    )

    ram_disk_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag_specifications: Optional[
        Union[List[TagSpecifications], core.ArrayOut[TagSpecifications]]
    ] = core.attr(TagSpecifications, default=None, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_default_version: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    user_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        block_device_mappings: Optional[
            Union[List[BlockDeviceMappings], core.ArrayOut[BlockDeviceMappings]]
        ] = None,
        capacity_reservation_specification: Optional[CapacityReservationSpecification] = None,
        cpu_options: Optional[CpuOptions] = None,
        credit_specification: Optional[CreditSpecification] = None,
        default_version: Optional[Union[int, core.IntOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        disable_api_stop: Optional[Union[bool, core.BoolOut]] = None,
        disable_api_termination: Optional[Union[bool, core.BoolOut]] = None,
        ebs_optimized: Optional[Union[str, core.StringOut]] = None,
        elastic_gpu_specifications: Optional[
            Union[List[ElasticGpuSpecifications], core.ArrayOut[ElasticGpuSpecifications]]
        ] = None,
        elastic_inference_accelerator: Optional[ElasticInferenceAccelerator] = None,
        enclave_options: Optional[EnclaveOptions] = None,
        hibernation_options: Optional[HibernationOptions] = None,
        iam_instance_profile: Optional[IamInstanceProfile] = None,
        image_id: Optional[Union[str, core.StringOut]] = None,
        instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = None,
        instance_market_options: Optional[InstanceMarketOptions] = None,
        instance_requirements: Optional[InstanceRequirements] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        kernel_id: Optional[Union[str, core.StringOut]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        license_specification: Optional[
            Union[List[LicenseSpecification], core.ArrayOut[LicenseSpecification]]
        ] = None,
        maintenance_options: Optional[MaintenanceOptions] = None,
        metadata_options: Optional[MetadataOptions] = None,
        monitoring: Optional[Monitoring] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        network_interfaces: Optional[
            Union[List[NetworkInterfaces], core.ArrayOut[NetworkInterfaces]]
        ] = None,
        placement: Optional[Placement] = None,
        private_dns_name_options: Optional[PrivateDnsNameOptions] = None,
        ram_disk_id: Optional[Union[str, core.StringOut]] = None,
        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tag_specifications: Optional[
            Union[List[TagSpecifications], core.ArrayOut[TagSpecifications]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        update_default_version: Optional[Union[bool, core.BoolOut]] = None,
        user_data: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LaunchTemplate.Args(
                block_device_mappings=block_device_mappings,
                capacity_reservation_specification=capacity_reservation_specification,
                cpu_options=cpu_options,
                credit_specification=credit_specification,
                default_version=default_version,
                description=description,
                disable_api_stop=disable_api_stop,
                disable_api_termination=disable_api_termination,
                ebs_optimized=ebs_optimized,
                elastic_gpu_specifications=elastic_gpu_specifications,
                elastic_inference_accelerator=elastic_inference_accelerator,
                enclave_options=enclave_options,
                hibernation_options=hibernation_options,
                iam_instance_profile=iam_instance_profile,
                image_id=image_id,
                instance_initiated_shutdown_behavior=instance_initiated_shutdown_behavior,
                instance_market_options=instance_market_options,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                kernel_id=kernel_id,
                key_name=key_name,
                license_specification=license_specification,
                maintenance_options=maintenance_options,
                metadata_options=metadata_options,
                monitoring=monitoring,
                name=name,
                name_prefix=name_prefix,
                network_interfaces=network_interfaces,
                placement=placement,
                private_dns_name_options=private_dns_name_options,
                ram_disk_id=ram_disk_id,
                security_group_names=security_group_names,
                tag_specifications=tag_specifications,
                tags=tags,
                tags_all=tags_all,
                update_default_version=update_default_version,
                user_data=user_data,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_device_mappings: Optional[
            Union[List[BlockDeviceMappings], core.ArrayOut[BlockDeviceMappings]]
        ] = core.arg(default=None)

        capacity_reservation_specification: Optional[CapacityReservationSpecification] = core.arg(
            default=None
        )

        cpu_options: Optional[CpuOptions] = core.arg(default=None)

        credit_specification: Optional[CreditSpecification] = core.arg(default=None)

        default_version: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_api_stop: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        disable_api_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ebs_optimized: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        elastic_gpu_specifications: Optional[
            Union[List[ElasticGpuSpecifications], core.ArrayOut[ElasticGpuSpecifications]]
        ] = core.arg(default=None)

        elastic_inference_accelerator: Optional[ElasticInferenceAccelerator] = core.arg(
            default=None
        )

        enclave_options: Optional[EnclaveOptions] = core.arg(default=None)

        hibernation_options: Optional[HibernationOptions] = core.arg(default=None)

        iam_instance_profile: Optional[IamInstanceProfile] = core.arg(default=None)

        image_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_initiated_shutdown_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        instance_market_options: Optional[InstanceMarketOptions] = core.arg(default=None)

        instance_requirements: Optional[InstanceRequirements] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kernel_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        license_specification: Optional[
            Union[List[LicenseSpecification], core.ArrayOut[LicenseSpecification]]
        ] = core.arg(default=None)

        maintenance_options: Optional[MaintenanceOptions] = core.arg(default=None)

        metadata_options: Optional[MetadataOptions] = core.arg(default=None)

        monitoring: Optional[Monitoring] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interfaces: Optional[
            Union[List[NetworkInterfaces], core.ArrayOut[NetworkInterfaces]]
        ] = core.arg(default=None)

        placement: Optional[Placement] = core.arg(default=None)

        private_dns_name_options: Optional[PrivateDnsNameOptions] = core.arg(default=None)

        ram_disk_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tag_specifications: Optional[
            Union[List[TagSpecifications], core.ArrayOut[TagSpecifications]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        update_default_version: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        user_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
