from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InitialLifecycleHook(core.Schema):

    default_result: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    heartbeat_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    lifecycle_transition: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    notification_metadata: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_target_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        lifecycle_transition: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        default_result: Optional[Union[str, core.StringOut]] = None,
        heartbeat_timeout: Optional[Union[int, core.IntOut]] = None,
        notification_metadata: Optional[Union[str, core.StringOut]] = None,
        notification_target_arn: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InitialLifecycleHook.Args(
                lifecycle_transition=lifecycle_transition,
                name=name,
                default_result=default_result,
                heartbeat_timeout=heartbeat_timeout,
                notification_metadata=notification_metadata,
                notification_target_arn=notification_target_arn,
                role_arn=role_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_result: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        heartbeat_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        lifecycle_transition: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        notification_metadata: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_target_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InstanceReusePolicy(core.Schema):

    reuse_on_scale_in: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        reuse_on_scale_in: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=InstanceReusePolicy.Args(
                reuse_on_scale_in=reuse_on_scale_in,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reuse_on_scale_in: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class WarmPool(core.Schema):

    instance_reuse_policy: Optional[InstanceReusePolicy] = core.attr(
        InstanceReusePolicy, default=None
    )

    max_group_prepared_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    pool_state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_reuse_policy: Optional[InstanceReusePolicy] = None,
        max_group_prepared_capacity: Optional[Union[int, core.IntOut]] = None,
        min_size: Optional[Union[int, core.IntOut]] = None,
        pool_state: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WarmPool.Args(
                instance_reuse_policy=instance_reuse_policy,
                max_group_prepared_capacity=max_group_prepared_capacity,
                min_size=min_size,
                pool_state=pool_state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_reuse_policy: Optional[InstanceReusePolicy] = core.arg(default=None)

        max_group_prepared_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        pool_state: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Tag(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    propagate_at_launch: Union[bool, core.BoolOut] = core.attr(bool)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        propagate_at_launch: Union[bool, core.BoolOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                propagate_at_launch=propagate_at_launch,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        propagate_at_launch: Union[bool, core.BoolOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Preferences(core.Schema):

    checkpoint_delay: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    checkpoint_percentages: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.attr(
        int, default=None, kind=core.Kind.array
    )

    instance_warmup: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_healthy_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    skip_matching: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        checkpoint_delay: Optional[Union[str, core.StringOut]] = None,
        checkpoint_percentages: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = None,
        instance_warmup: Optional[Union[str, core.StringOut]] = None,
        min_healthy_percentage: Optional[Union[int, core.IntOut]] = None,
        skip_matching: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Preferences.Args(
                checkpoint_delay=checkpoint_delay,
                checkpoint_percentages=checkpoint_percentages,
                instance_warmup=instance_warmup,
                min_healthy_percentage=min_healthy_percentage,
                skip_matching=skip_matching,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        checkpoint_delay: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        checkpoint_percentages: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.arg(
            default=None
        )

        instance_warmup: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_healthy_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        skip_matching: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class InstanceRefresh(core.Schema):

    preferences: Optional[Preferences] = core.attr(Preferences, default=None)

    strategy: Union[str, core.StringOut] = core.attr(str)

    triggers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        strategy: Union[str, core.StringOut],
        preferences: Optional[Preferences] = None,
        triggers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=InstanceRefresh.Args(
                strategy=strategy,
                preferences=preferences,
                triggers=triggers,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        preferences: Optional[Preferences] = core.arg(default=None)

        strategy: Union[str, core.StringOut] = core.arg()

        triggers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


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
class InstancesDistribution(core.Schema):

    on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    on_demand_base_capacity: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    on_demand_percentage_above_base_capacity: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    spot_allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    spot_instance_pools: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    spot_max_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        on_demand_base_capacity: Optional[Union[int, core.IntOut]] = None,
        on_demand_percentage_above_base_capacity: Optional[Union[int, core.IntOut]] = None,
        spot_allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        spot_instance_pools: Optional[Union[int, core.IntOut]] = None,
        spot_max_price: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstancesDistribution.Args(
                on_demand_allocation_strategy=on_demand_allocation_strategy,
                on_demand_base_capacity=on_demand_base_capacity,
                on_demand_percentage_above_base_capacity=on_demand_percentage_above_base_capacity,
                spot_allocation_strategy=spot_allocation_strategy,
                spot_instance_pools=spot_instance_pools,
                spot_max_price=spot_max_price,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_demand_base_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        on_demand_percentage_above_base_capacity: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        spot_allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        spot_instance_pools: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        spot_max_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LaunchTemplateSpecification(core.Schema):

    launch_template_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    launch_template_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: Optional[Union[str, core.StringOut]] = None,
        launch_template_name: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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
class Override(core.Schema):

    instance_requirements: Optional[InstanceRequirements] = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template_specification: Optional[LaunchTemplateSpecification] = core.attr(
        LaunchTemplateSpecification, default=None
    )

    weighted_capacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_requirements: Optional[InstanceRequirements] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        launch_template_specification: Optional[LaunchTemplateSpecification] = None,
        weighted_capacity: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Override.Args(
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                launch_template_specification=launch_template_specification,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_requirements: Optional[InstanceRequirements] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_specification: Optional[LaunchTemplateSpecification] = core.arg(
            default=None
        )

        weighted_capacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MixedInstancesPolicyLaunchTemplate(core.Schema):

    launch_template_specification: LaunchTemplateSpecification = core.attr(
        LaunchTemplateSpecification
    )

    override: Optional[Union[List[Override], core.ArrayOut[Override]]] = core.attr(
        Override, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        launch_template_specification: LaunchTemplateSpecification,
        override: Optional[Union[List[Override], core.ArrayOut[Override]]] = None,
    ):
        super().__init__(
            args=MixedInstancesPolicyLaunchTemplate.Args(
                launch_template_specification=launch_template_specification,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        override: Optional[Union[List[Override], core.ArrayOut[Override]]] = core.arg(default=None)


@core.schema
class MixedInstancesPolicy(core.Schema):

    instances_distribution: Optional[InstancesDistribution] = core.attr(
        InstancesDistribution, default=None, computed=True
    )

    launch_template: MixedInstancesPolicyLaunchTemplate = core.attr(
        MixedInstancesPolicyLaunchTemplate
    )

    def __init__(
        self,
        *,
        launch_template: MixedInstancesPolicyLaunchTemplate,
        instances_distribution: Optional[InstancesDistribution] = None,
    ):
        super().__init__(
            args=MixedInstancesPolicy.Args(
                launch_template=launch_template,
                instances_distribution=instances_distribution,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instances_distribution: Optional[InstancesDistribution] = core.arg(default=None)

        launch_template: MixedInstancesPolicyLaunchTemplate = core.arg()


@core.resource(type="aws_autoscaling_group", namespace="aws_autoscaling")
class Group(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    capacity_rebalance: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    context: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_cooldown: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    default_instance_warmup: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    desired_capacity: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    enabled_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    force_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    force_delete_warm_pool: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check_grace_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    health_check_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    initial_lifecycle_hook: Optional[
        Union[List[InitialLifecycleHook], core.ArrayOut[InitialLifecycleHook]]
    ] = core.attr(InitialLifecycleHook, default=None, kind=core.Kind.array)

    instance_refresh: Optional[InstanceRefresh] = core.attr(InstanceRefresh, default=None)

    launch_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template: Optional[LaunchTemplate] = core.attr(LaunchTemplate, default=None)

    load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_instance_lifetime: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_size: Union[int, core.IntOut] = core.attr(int)

    metrics_granularity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    min_elb_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_size: Union[int, core.IntOut] = core.attr(int)

    mixed_instances_policy: Optional[MixedInstancesPolicy] = core.attr(
        MixedInstancesPolicy, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    placement_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protect_from_scale_in: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    service_linked_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    suspended_processes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag: Optional[Union[List[Tag], core.ArrayOut[Tag]]] = core.attr(
        Tag, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[List[Dict[str, str]], core.MapArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map_array
    )

    target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    termination_policies: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_zone_identifier: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    wait_for_capacity_timeout: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wait_for_elb_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    warm_pool: Optional[WarmPool] = core.attr(WarmPool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        max_size: Union[int, core.IntOut],
        min_size: Union[int, core.IntOut],
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        capacity_rebalance: Optional[Union[bool, core.BoolOut]] = None,
        context: Optional[Union[str, core.StringOut]] = None,
        default_cooldown: Optional[Union[int, core.IntOut]] = None,
        default_instance_warmup: Optional[Union[int, core.IntOut]] = None,
        desired_capacity: Optional[Union[int, core.IntOut]] = None,
        enabled_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        force_delete: Optional[Union[bool, core.BoolOut]] = None,
        force_delete_warm_pool: Optional[Union[bool, core.BoolOut]] = None,
        health_check_grace_period: Optional[Union[int, core.IntOut]] = None,
        health_check_type: Optional[Union[str, core.StringOut]] = None,
        initial_lifecycle_hook: Optional[
            Union[List[InitialLifecycleHook], core.ArrayOut[InitialLifecycleHook]]
        ] = None,
        instance_refresh: Optional[InstanceRefresh] = None,
        launch_configuration: Optional[Union[str, core.StringOut]] = None,
        launch_template: Optional[LaunchTemplate] = None,
        load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        max_instance_lifetime: Optional[Union[int, core.IntOut]] = None,
        metrics_granularity: Optional[Union[str, core.StringOut]] = None,
        min_elb_capacity: Optional[Union[int, core.IntOut]] = None,
        mixed_instances_policy: Optional[MixedInstancesPolicy] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        placement_group: Optional[Union[str, core.StringOut]] = None,
        protect_from_scale_in: Optional[Union[bool, core.BoolOut]] = None,
        service_linked_role_arn: Optional[Union[str, core.StringOut]] = None,
        suspended_processes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tag: Optional[Union[List[Tag], core.ArrayOut[Tag]]] = None,
        tags: Optional[Union[List[Dict[str, str]], core.MapArrayOut[core.StringOut]]] = None,
        target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        termination_policies: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        vpc_zone_identifier: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        wait_for_capacity_timeout: Optional[Union[str, core.StringOut]] = None,
        wait_for_elb_capacity: Optional[Union[int, core.IntOut]] = None,
        warm_pool: Optional[WarmPool] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Group.Args(
                max_size=max_size,
                min_size=min_size,
                availability_zones=availability_zones,
                capacity_rebalance=capacity_rebalance,
                context=context,
                default_cooldown=default_cooldown,
                default_instance_warmup=default_instance_warmup,
                desired_capacity=desired_capacity,
                enabled_metrics=enabled_metrics,
                force_delete=force_delete,
                force_delete_warm_pool=force_delete_warm_pool,
                health_check_grace_period=health_check_grace_period,
                health_check_type=health_check_type,
                initial_lifecycle_hook=initial_lifecycle_hook,
                instance_refresh=instance_refresh,
                launch_configuration=launch_configuration,
                launch_template=launch_template,
                load_balancers=load_balancers,
                max_instance_lifetime=max_instance_lifetime,
                metrics_granularity=metrics_granularity,
                min_elb_capacity=min_elb_capacity,
                mixed_instances_policy=mixed_instances_policy,
                name=name,
                name_prefix=name_prefix,
                placement_group=placement_group,
                protect_from_scale_in=protect_from_scale_in,
                service_linked_role_arn=service_linked_role_arn,
                suspended_processes=suspended_processes,
                tag=tag,
                tags=tags,
                target_group_arns=target_group_arns,
                termination_policies=termination_policies,
                vpc_zone_identifier=vpc_zone_identifier,
                wait_for_capacity_timeout=wait_for_capacity_timeout,
                wait_for_elb_capacity=wait_for_elb_capacity,
                warm_pool=warm_pool,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        capacity_rebalance: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        context: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_cooldown: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        default_instance_warmup: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        desired_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enabled_metrics: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        force_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        force_delete_warm_pool: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check_grace_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        health_check_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        initial_lifecycle_hook: Optional[
            Union[List[InitialLifecycleHook], core.ArrayOut[InitialLifecycleHook]]
        ] = core.arg(default=None)

        instance_refresh: Optional[InstanceRefresh] = core.arg(default=None)

        launch_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template: Optional[LaunchTemplate] = core.arg(default=None)

        load_balancers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_instance_lifetime: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_size: Union[int, core.IntOut] = core.arg()

        metrics_granularity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        min_elb_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_size: Union[int, core.IntOut] = core.arg()

        mixed_instances_policy: Optional[MixedInstancesPolicy] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        placement_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protect_from_scale_in: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        service_linked_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        suspended_processes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tag: Optional[Union[List[Tag], core.ArrayOut[Tag]]] = core.arg(default=None)

        tags: Optional[Union[List[Dict[str, str]], core.MapArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_group_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        termination_policies: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_zone_identifier: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        wait_for_capacity_timeout: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wait_for_elb_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        warm_pool: Optional[WarmPool] = core.arg(default=None)
