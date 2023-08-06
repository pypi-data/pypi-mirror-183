from typing import Dict, List, Optional, Union

import terrascript.core as core


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
class Scale(core.Schema):

    unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        unit: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=Scale.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


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
class CapacityProviderStrategy(core.Schema):

    base: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    capacity_provider: Union[str, core.StringOut] = core.attr(str)

    weight: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        capacity_provider: Union[str, core.StringOut],
        weight: Union[int, core.IntOut],
        base: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                weight=weight,
                base=base,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        capacity_provider: Union[str, core.StringOut] = core.arg()

        weight: Union[int, core.IntOut] = core.arg()


@core.schema
class LoadBalancer(core.Schema):

    container_name: Union[str, core.StringOut] = core.attr(str)

    container_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    load_balancer_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: Union[str, core.StringOut],
        container_port: Optional[Union[int, core.IntOut]] = None,
        load_balancer_name: Optional[Union[str, core.StringOut]] = None,
        target_group_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LoadBalancer.Args(
                container_name=container_name,
                container_port=container_port,
                load_balancer_name=load_balancer_name,
                target_group_arn=target_group_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Union[str, core.StringOut] = core.arg()

        container_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        load_balancer_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ecs_task_set", namespace="aws_ecs")
class TaskSet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_provider_strategy: Optional[
        Union[List[CapacityProviderStrategy], core.ArrayOut[CapacityProviderStrategy]]
    ] = core.attr(CapacityProviderStrategy, default=None, kind=core.Kind.array)

    cluster: Union[str, core.StringOut] = core.attr(str)

    external_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    force_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = core.attr(
        LoadBalancer, default=None, kind=core.Kind.array
    )

    network_configuration: Optional[NetworkConfiguration] = core.attr(
        NetworkConfiguration, default=None
    )

    platform_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    scale: Optional[Scale] = core.attr(Scale, default=None, computed=True)

    service: Union[str, core.StringOut] = core.attr(str)

    service_registries: Optional[ServiceRegistries] = core.attr(ServiceRegistries, default=None)

    stability_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_definition: Union[str, core.StringOut] = core.attr(str)

    task_set_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    wait_until_stable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    wait_until_stable_timeout: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster: Union[str, core.StringOut],
        service: Union[str, core.StringOut],
        task_definition: Union[str, core.StringOut],
        capacity_provider_strategy: Optional[
            Union[List[CapacityProviderStrategy], core.ArrayOut[CapacityProviderStrategy]]
        ] = None,
        external_id: Optional[Union[str, core.StringOut]] = None,
        force_delete: Optional[Union[bool, core.BoolOut]] = None,
        launch_type: Optional[Union[str, core.StringOut]] = None,
        load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = None,
        network_configuration: Optional[NetworkConfiguration] = None,
        platform_version: Optional[Union[str, core.StringOut]] = None,
        scale: Optional[Scale] = None,
        service_registries: Optional[ServiceRegistries] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        wait_until_stable: Optional[Union[bool, core.BoolOut]] = None,
        wait_until_stable_timeout: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TaskSet.Args(
                cluster=cluster,
                service=service,
                task_definition=task_definition,
                capacity_provider_strategy=capacity_provider_strategy,
                external_id=external_id,
                force_delete=force_delete,
                launch_type=launch_type,
                load_balancer=load_balancer,
                network_configuration=network_configuration,
                platform_version=platform_version,
                scale=scale,
                service_registries=service_registries,
                tags=tags,
                tags_all=tags_all,
                wait_until_stable=wait_until_stable,
                wait_until_stable_timeout=wait_until_stable_timeout,
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

        cluster: Union[str, core.StringOut] = core.arg()

        external_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        launch_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        load_balancer: Optional[Union[List[LoadBalancer], core.ArrayOut[LoadBalancer]]] = core.arg(
            default=None
        )

        network_configuration: Optional[NetworkConfiguration] = core.arg(default=None)

        platform_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        scale: Optional[Scale] = core.arg(default=None)

        service: Union[str, core.StringOut] = core.arg()

        service_registries: Optional[ServiceRegistries] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        task_definition: Union[str, core.StringOut] = core.arg()

        wait_until_stable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        wait_until_stable_timeout: Optional[Union[str, core.StringOut]] = core.arg(default=None)
