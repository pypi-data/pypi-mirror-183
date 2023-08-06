from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CapacityProviderStrategy(core.Schema):

    base: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    capacity_provider: Union[str, core.StringOut] = core.attr(str)

    weight: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: Union[str, core.StringOut],
        base: Optional[Union[int, core.IntOut]] = None,
        weight: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        capacity_provider: Union[str, core.StringOut] = core.arg()

        weight: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class LoadBalancer(core.Schema):

    container_name: Union[str, core.StringOut] = core.attr(str)

    container_port: Union[int, core.IntOut] = core.attr(int)

    elb_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: Union[str, core.StringOut],
        container_port: Union[int, core.IntOut],
        elb_name: Optional[Union[str, core.StringOut]] = None,
        target_group_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LoadBalancer.Args(
                container_name=container_name,
                container_port=container_port,
                elb_name=elb_name,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Union[str, core.StringOut] = core.arg()

        container_port: Union[int, core.IntOut] = core.arg()

        elb_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ServiceRegistries(core.Schema):

    container_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    container_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    registry_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        registry_arn: Union[str, core.StringOut],
        container_name: Optional[Union[str, core.StringOut]] = None,
        container_port: Optional[Union[int, core.IntOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ServiceRegistries.Args(
                registry_arn=registry_arn,
                container_name=container_name,
                container_port=container_port,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        container_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        registry_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class DeploymentCircuitBreaker(core.Schema):

    enable: Union[bool, core.BoolOut] = core.attr(bool)

    rollback: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enable: Union[bool, core.BoolOut],
        rollback: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=DeploymentCircuitBreaker.Args(
                enable=enable,
                rollback=rollback,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable: Union[bool, core.BoolOut] = core.arg()

        rollback: Union[bool, core.BoolOut] = core.arg()


@core.schema
class PlacementConstraints(core.Schema):

    expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        expression: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PlacementConstraints.Args(
                type=type,
                expression=expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class DeploymentController(core.Schema):

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeploymentController.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NetworkConfiguration(core.Schema):

    assign_public_ip: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        assign_public_ip: Optional[Union[bool, core.BoolOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                subnets=subnets,
                assign_public_ip=assign_public_ip,
                security_groups=security_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assign_public_ip: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class OrderedPlacementStrategy(core.Schema):

    field: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        field: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OrderedPlacementStrategy.Args(
                type=type,
                field=field,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ecs_service", namespace="aws_ecs")
class Service(core.Resource):

    capacity_provider_strategy: Optional[
        Union[List[CapacityProviderStrategy], core.ArrayOut[CapacityProviderStrategy]]
    ] = core.attr(CapacityProviderStrategy, default=None, kind=core.Kind.array)

    cluster: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    deployment_circuit_breaker: Optional[DeploymentCircuitBreaker] = core.attr(
        DeploymentCircuitBreaker, default=None
    )

    deployment_controller: Optional[DeploymentController] = core.attr(
        DeploymentController, default=None
    )

    deployment_maximum_percent: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    deployment_minimum_healthy_percent: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    desired_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_execute_command: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    force_new_deployment: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check_grace_period_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    iam_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = core.attr(
        LoadBalancer, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    network_configuration: Optional[NetworkConfiguration] = core.attr(
        NetworkConfiguration, default=None
    )

    ordered_placement_strategy: Optional[
        Union[List[OrderedPlacementStrategy], core.ArrayOut[OrderedPlacementStrategy]]
    ] = core.attr(OrderedPlacementStrategy, default=None, kind=core.Kind.array)

    placement_constraints: Optional[
        Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
    ] = core.attr(PlacementConstraints, default=None, kind=core.Kind.array)

    platform_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    propagate_tags: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    scheduling_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    service_registries: Optional[ServiceRegistries] = core.attr(ServiceRegistries, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_definition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wait_for_steady_state: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        capacity_provider_strategy: Optional[
            Union[List[CapacityProviderStrategy], core.ArrayOut[CapacityProviderStrategy]]
        ] = None,
        cluster: Optional[Union[str, core.StringOut]] = None,
        deployment_circuit_breaker: Optional[DeploymentCircuitBreaker] = None,
        deployment_controller: Optional[DeploymentController] = None,
        deployment_maximum_percent: Optional[Union[int, core.IntOut]] = None,
        deployment_minimum_healthy_percent: Optional[Union[int, core.IntOut]] = None,
        desired_count: Optional[Union[int, core.IntOut]] = None,
        enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = None,
        enable_execute_command: Optional[Union[bool, core.BoolOut]] = None,
        force_new_deployment: Optional[Union[bool, core.BoolOut]] = None,
        health_check_grace_period_seconds: Optional[Union[int, core.IntOut]] = None,
        iam_role: Optional[Union[str, core.StringOut]] = None,
        launch_type: Optional[Union[str, core.StringOut]] = None,
        load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = None,
        network_configuration: Optional[NetworkConfiguration] = None,
        ordered_placement_strategy: Optional[
            Union[List[OrderedPlacementStrategy], core.ArrayOut[OrderedPlacementStrategy]]
        ] = None,
        placement_constraints: Optional[
            Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
        ] = None,
        platform_version: Optional[Union[str, core.StringOut]] = None,
        propagate_tags: Optional[Union[str, core.StringOut]] = None,
        scheduling_strategy: Optional[Union[str, core.StringOut]] = None,
        service_registries: Optional[ServiceRegistries] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        task_definition: Optional[Union[str, core.StringOut]] = None,
        wait_for_steady_state: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Service.Args(
                name=name,
                capacity_provider_strategy=capacity_provider_strategy,
                cluster=cluster,
                deployment_circuit_breaker=deployment_circuit_breaker,
                deployment_controller=deployment_controller,
                deployment_maximum_percent=deployment_maximum_percent,
                deployment_minimum_healthy_percent=deployment_minimum_healthy_percent,
                desired_count=desired_count,
                enable_ecs_managed_tags=enable_ecs_managed_tags,
                enable_execute_command=enable_execute_command,
                force_new_deployment=force_new_deployment,
                health_check_grace_period_seconds=health_check_grace_period_seconds,
                iam_role=iam_role,
                launch_type=launch_type,
                load_balancer=load_balancer,
                network_configuration=network_configuration,
                ordered_placement_strategy=ordered_placement_strategy,
                placement_constraints=placement_constraints,
                platform_version=platform_version,
                propagate_tags=propagate_tags,
                scheduling_strategy=scheduling_strategy,
                service_registries=service_registries,
                tags=tags,
                tags_all=tags_all,
                task_definition=task_definition,
                wait_for_steady_state=wait_for_steady_state,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_provider_strategy: Optional[
            Union[List[CapacityProviderStrategy], core.ArrayOut[CapacityProviderStrategy]]
        ] = core.arg(default=None)

        cluster: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_circuit_breaker: Optional[DeploymentCircuitBreaker] = core.arg(default=None)

        deployment_controller: Optional[DeploymentController] = core.arg(default=None)

        deployment_maximum_percent: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        deployment_minimum_healthy_percent: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        desired_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_execute_command: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        force_new_deployment: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check_grace_period_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        iam_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        network_configuration: Optional[NetworkConfiguration] = core.arg(default=None)

        ordered_placement_strategy: Optional[
            Union[List[OrderedPlacementStrategy], core.ArrayOut[OrderedPlacementStrategy]]
        ] = core.arg(default=None)

        placement_constraints: Optional[
            Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
        ] = core.arg(default=None)

        platform_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        propagate_tags: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scheduling_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        service_registries: Optional[ServiceRegistries] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        task_definition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wait_for_steady_state: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
