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
class MaintenanceStrategies(core.Schema):

    capacity_rebalance: Optional[CapacityRebalance] = core.attr(CapacityRebalance, default=None)

    def __init__(
        self,
        *,
        capacity_rebalance: Optional[CapacityRebalance] = None,
    ):
        super().__init__(
            args=MaintenanceStrategies.Args(
                capacity_rebalance=capacity_rebalance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_rebalance: Optional[CapacityRebalance] = core.arg(default=None)


@core.schema
class SpotOptions(core.Schema):

    allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_interruption_behavior: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    maintenance_strategies: Optional[MaintenanceStrategies] = core.attr(
        MaintenanceStrategies, default=None
    )

    def __init__(
        self,
        *,
        allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        instance_interruption_behavior: Optional[Union[str, core.StringOut]] = None,
        instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = None,
        maintenance_strategies: Optional[MaintenanceStrategies] = None,
    ):
        super().__init__(
            args=SpotOptions.Args(
                allocation_strategy=allocation_strategy,
                instance_interruption_behavior=instance_interruption_behavior,
                instance_pools_to_use_count=instance_pools_to_use_count,
                maintenance_strategies=maintenance_strategies,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_interruption_behavior: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        instance_pools_to_use_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maintenance_strategies: Optional[MaintenanceStrategies] = core.arg(default=None)


@core.schema
class TargetCapacitySpecification(core.Schema):

    default_target_capacity_type: Union[str, core.StringOut] = core.attr(str)

    on_demand_target_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    spot_target_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    total_target_capacity: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        default_target_capacity_type: Union[str, core.StringOut],
        total_target_capacity: Union[int, core.IntOut],
        on_demand_target_capacity: Optional[Union[int, core.IntOut]] = None,
        spot_target_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TargetCapacitySpecification.Args(
                default_target_capacity_type=default_target_capacity_type,
                total_target_capacity=total_target_capacity,
                on_demand_target_capacity=on_demand_target_capacity,
                spot_target_capacity=spot_target_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_target_capacity_type: Union[str, core.StringOut] = core.arg()

        on_demand_target_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        spot_target_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        total_target_capacity: Union[int, core.IntOut] = core.arg()


@core.schema
class LaunchTemplateSpecification(core.Schema):

    launch_template_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        version: Union[str, core.StringOut],
        launch_template_id: Optional[Union[str, core.StringOut]] = None,
        launch_template_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplateSpecification.Args(
                version=version,
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()


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
class Override(core.Schema):

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_requirements: Optional[InstanceRequirements] = core.attr(
        InstanceRequirements, default=None
    )

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    priority: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    weighted_capacity: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        instance_requirements: Optional[InstanceRequirements] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        max_price: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[float, core.FloatOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        weighted_capacity: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=Override.Args(
                availability_zone=availability_zone,
                instance_requirements=instance_requirements,
                instance_type=instance_type,
                max_price=max_price,
                priority=priority,
                subnet_id=subnet_id,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_requirements: Optional[InstanceRequirements] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        priority: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        weighted_capacity: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class LaunchTemplateConfig(core.Schema):

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
            args=LaunchTemplateConfig.Args(
                launch_template_specification=launch_template_specification,
                override=override,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_specification: LaunchTemplateSpecification = core.arg()

        override: Optional[Union[List[Override], core.ArrayOut[Override]]] = core.arg(default=None)


@core.schema
class OnDemandOptions(core.Schema):

    allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        allocation_strategy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OnDemandOptions.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ec2_fleet", namespace="aws_ec2")
class Fleet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    context: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_template_config: LaunchTemplateConfig = core.attr(LaunchTemplateConfig)

    on_demand_options: Optional[OnDemandOptions] = core.attr(OnDemandOptions, default=None)

    replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    spot_options: Optional[SpotOptions] = core.attr(SpotOptions, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_capacity_specification: TargetCapacitySpecification = core.attr(
        TargetCapacitySpecification
    )

    terminate_instances: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        launch_template_config: LaunchTemplateConfig,
        target_capacity_specification: TargetCapacitySpecification,
        context: Optional[Union[str, core.StringOut]] = None,
        excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = None,
        on_demand_options: Optional[OnDemandOptions] = None,
        replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = None,
        spot_options: Optional[SpotOptions] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        terminate_instances: Optional[Union[bool, core.BoolOut]] = None,
        terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                launch_template_config=launch_template_config,
                target_capacity_specification=target_capacity_specification,
                context=context,
                excess_capacity_termination_policy=excess_capacity_termination_policy,
                on_demand_options=on_demand_options,
                replace_unhealthy_instances=replace_unhealthy_instances,
                spot_options=spot_options,
                tags=tags,
                tags_all=tags_all,
                terminate_instances=terminate_instances,
                terminate_instances_with_expiration=terminate_instances_with_expiration,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        context: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        excess_capacity_termination_policy: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        launch_template_config: LaunchTemplateConfig = core.arg()

        on_demand_options: Optional[OnDemandOptions] = core.arg(default=None)

        replace_unhealthy_instances: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        spot_options: Optional[SpotOptions] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_capacity_specification: TargetCapacitySpecification = core.arg()

        terminate_instances: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        terminate_instances_with_expiration: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
