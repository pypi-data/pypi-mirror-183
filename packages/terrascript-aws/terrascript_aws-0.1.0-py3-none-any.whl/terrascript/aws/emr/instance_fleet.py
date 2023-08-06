from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Configurations(core.Schema):

    classification: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        classification: Optional[Union[str, core.StringOut]] = None,
        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Configurations.Args(
                classification=classification,
                properties=properties,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classification: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class EbsConfig(core.Schema):

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    volumes_per_instance: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        iops: Optional[Union[int, core.IntOut]] = None,
        volumes_per_instance: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        volumes_per_instance: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class InstanceTypeConfigs(core.Schema):

    bid_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bid_price_as_percentage_of_on_demand_price: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    configurations: Optional[
        Union[List[Configurations], core.ArrayOut[Configurations]]
    ] = core.attr(Configurations, default=None, kind=core.Kind.array)

    ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = core.attr(
        EbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    instance_type: Union[str, core.StringOut] = core.attr(str)

    weighted_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        instance_type: Union[str, core.StringOut],
        bid_price: Optional[Union[str, core.StringOut]] = None,
        bid_price_as_percentage_of_on_demand_price: Optional[Union[float, core.FloatOut]] = None,
        configurations: Optional[Union[List[Configurations], core.ArrayOut[Configurations]]] = None,
        ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = None,
        weighted_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=InstanceTypeConfigs.Args(
                instance_type=instance_type,
                bid_price=bid_price,
                bid_price_as_percentage_of_on_demand_price=bid_price_as_percentage_of_on_demand_price,
                configurations=configurations,
                ebs_config=ebs_config,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bid_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bid_price_as_percentage_of_on_demand_price: Optional[
            Union[float, core.FloatOut]
        ] = core.arg(default=None)

        configurations: Optional[
            Union[List[Configurations], core.ArrayOut[Configurations]]
        ] = core.arg(default=None)

        ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = core.arg(
            default=None
        )

        instance_type: Union[str, core.StringOut] = core.arg()

        weighted_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class OnDemandSpecification(core.Schema):

    allocation_strategy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        allocation_strategy: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnDemandSpecification.Args(
                allocation_strategy=allocation_strategy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Union[str, core.StringOut] = core.arg()


@core.schema
class SpotSpecification(core.Schema):

    allocation_strategy: Union[str, core.StringOut] = core.attr(str)

    block_duration_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    timeout_action: Union[str, core.StringOut] = core.attr(str)

    timeout_duration_minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        allocation_strategy: Union[str, core.StringOut],
        timeout_action: Union[str, core.StringOut],
        timeout_duration_minutes: Union[int, core.IntOut],
        block_duration_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SpotSpecification.Args(
                allocation_strategy=allocation_strategy,
                timeout_action=timeout_action,
                timeout_duration_minutes=timeout_duration_minutes,
                block_duration_minutes=block_duration_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Union[str, core.StringOut] = core.arg()

        block_duration_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        timeout_action: Union[str, core.StringOut] = core.arg()

        timeout_duration_minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class LaunchSpecifications(core.Schema):

    on_demand_specification: Optional[
        Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
    ] = core.attr(OnDemandSpecification, default=None, kind=core.Kind.array)

    spot_specification: Optional[
        Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
    ] = core.attr(SpotSpecification, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        on_demand_specification: Optional[
            Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
        ] = None,
        spot_specification: Optional[
            Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
        ] = None,
    ):
        super().__init__(
            args=LaunchSpecifications.Args(
                on_demand_specification=on_demand_specification,
                spot_specification=spot_specification,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_demand_specification: Optional[
            Union[List[OnDemandSpecification], core.ArrayOut[OnDemandSpecification]]
        ] = core.arg(default=None)

        spot_specification: Optional[
            Union[List[SpotSpecification], core.ArrayOut[SpotSpecification]]
        ] = core.arg(default=None)


@core.resource(type="aws_emr_instance_fleet", namespace="aws_emr")
class InstanceFleet(core.Resource):

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type_configs: Optional[
        Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
    ] = core.attr(InstanceTypeConfigs, default=None, kind=core.Kind.array)

    launch_specifications: Optional[LaunchSpecifications] = core.attr(
        LaunchSpecifications, default=None
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    provisioned_on_demand_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    provisioned_spot_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_spot_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = None,
        launch_specifications: Optional[LaunchSpecifications] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = None,
        target_spot_capacity: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceFleet.Args(
                cluster_id=cluster_id,
                instance_type_configs=instance_type_configs,
                launch_specifications=launch_specifications,
                name=name,
                target_on_demand_capacity=target_on_demand_capacity,
                target_spot_capacity=target_spot_capacity,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_id: Union[str, core.StringOut] = core.arg()

        instance_type_configs: Optional[
            Union[List[InstanceTypeConfigs], core.ArrayOut[InstanceTypeConfigs]]
        ] = core.arg(default=None)

        launch_specifications: Optional[LaunchSpecifications] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_on_demand_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_spot_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)
