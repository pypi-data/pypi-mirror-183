from typing import List, Union

import terrascript.core as core


@core.schema
class InstanceDisks(core.Schema):

    count: Union[int, core.IntOut] = core.attr(int, computed=True)

    size: Union[int, core.IntOut] = core.attr(int, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: Union[int, core.IntOut],
        size: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InstanceDisks.Args(
                count=count,
                size=size,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Union[int, core.IntOut] = core.arg()

        size: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class InferenceAccelerators(core.Schema):

    count: Union[int, core.IntOut] = core.attr(int, computed=True)

    manufacturer: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: Union[int, core.IntOut],
        manufacturer: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InferenceAccelerators.Args(
                count=count,
                manufacturer=manufacturer,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Union[int, core.IntOut] = core.arg()

        manufacturer: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Fpgas(core.Schema):

    count: Union[int, core.IntOut] = core.attr(int, computed=True)

    manufacturer: Union[str, core.StringOut] = core.attr(str, computed=True)

    memory_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: Union[int, core.IntOut],
        manufacturer: Union[str, core.StringOut],
        memory_size: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Fpgas.Args(
                count=count,
                manufacturer=manufacturer,
                memory_size=memory_size,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Union[int, core.IntOut] = core.arg()

        manufacturer: Union[str, core.StringOut] = core.arg()

        memory_size: Union[int, core.IntOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Gpus(core.Schema):

    count: Union[int, core.IntOut] = core.attr(int, computed=True)

    manufacturer: Union[str, core.StringOut] = core.attr(str, computed=True)

    memory_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        count: Union[int, core.IntOut],
        manufacturer: Union[str, core.StringOut],
        memory_size: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Gpus.Args(
                count=count,
                manufacturer=manufacturer,
                memory_size=memory_size,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Union[int, core.IntOut] = core.arg()

        manufacturer: Union[str, core.StringOut] = core.arg()

        memory_size: Union[int, core.IntOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_ec2_instance_type", namespace="aws_ec2")
class DsInstanceType(core.Data):

    auto_recovery_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    bare_metal: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    burstable_performance_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    current_generation: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    dedicated_hosts_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    default_cores: Union[int, core.IntOut] = core.attr(int, computed=True)

    default_threads_per_core: Union[int, core.IntOut] = core.attr(int, computed=True)

    default_vcpus: Union[int, core.IntOut] = core.attr(int, computed=True)

    ebs_encryption_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    ebs_nvme_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    ebs_optimized_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    ebs_performance_baseline_bandwidth: Union[int, core.IntOut] = core.attr(int, computed=True)

    ebs_performance_baseline_iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    ebs_performance_baseline_throughput: Union[float, core.FloatOut] = core.attr(
        float, computed=True
    )

    ebs_performance_maximum_bandwidth: Union[int, core.IntOut] = core.attr(int, computed=True)

    ebs_performance_maximum_iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    ebs_performance_maximum_throughput: Union[float, core.FloatOut] = core.attr(
        float, computed=True
    )

    efa_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ena_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_in_transit_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    fpgas: Union[List[Fpgas], core.ArrayOut[Fpgas]] = core.attr(
        Fpgas, computed=True, kind=core.Kind.array
    )

    free_tier_eligible: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    gpus: Union[List[Gpus], core.ArrayOut[Gpus]] = core.attr(
        Gpus, computed=True, kind=core.Kind.array
    )

    hibernation_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    hypervisor: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inference_accelerators: Union[
        List[InferenceAccelerators], core.ArrayOut[InferenceAccelerators]
    ] = core.attr(InferenceAccelerators, computed=True, kind=core.Kind.array)

    instance_disks: Union[List[InstanceDisks], core.ArrayOut[InstanceDisks]] = core.attr(
        InstanceDisks, computed=True, kind=core.Kind.array
    )

    instance_storage_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    ipv6_supported: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    maximum_ipv4_addresses_per_interface: Union[int, core.IntOut] = core.attr(int, computed=True)

    maximum_ipv6_addresses_per_interface: Union[int, core.IntOut] = core.attr(int, computed=True)

    maximum_network_interfaces: Union[int, core.IntOut] = core.attr(int, computed=True)

    memory_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    network_performance: Union[str, core.StringOut] = core.attr(str, computed=True)

    supported_architectures: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_placement_strategies: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_root_device_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_usages_classes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    supported_virtualization_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    sustained_clock_speed: Union[float, core.FloatOut] = core.attr(float, computed=True)

    total_fpga_memory: Union[int, core.IntOut] = core.attr(int, computed=True)

    total_gpu_memory: Union[int, core.IntOut] = core.attr(int, computed=True)

    total_instance_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    valid_cores: Union[List[int], core.ArrayOut[core.IntOut]] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    valid_threads_per_core: Union[List[int], core.ArrayOut[core.IntOut]] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_type: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsInstanceType.Args(
                instance_type=instance_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: Union[str, core.StringOut] = core.arg()
