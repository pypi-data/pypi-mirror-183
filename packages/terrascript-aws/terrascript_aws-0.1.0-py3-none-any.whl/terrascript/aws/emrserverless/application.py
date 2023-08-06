from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class MaximumCapacity(core.Schema):

    cpu: Union[str, core.StringOut] = core.attr(str)

    disk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    memory: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cpu: Union[str, core.StringOut],
        memory: Union[str, core.StringOut],
        disk: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MaximumCapacity.Args(
                cpu=cpu,
                memory=memory,
                disk=disk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: Union[str, core.StringOut] = core.arg()

        disk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        memory: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoStartConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=AutoStartConfiguration.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class NetworkConfiguration(core.Schema):

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class WorkerConfiguration(core.Schema):

    cpu: Union[str, core.StringOut] = core.attr(str)

    disk: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    memory: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cpu: Union[str, core.StringOut],
        memory: Union[str, core.StringOut],
        disk: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WorkerConfiguration.Args(
                cpu=cpu,
                memory=memory,
                disk=disk,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: Union[str, core.StringOut] = core.arg()

        disk: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        memory: Union[str, core.StringOut] = core.arg()


@core.schema
class InitialCapacityConfig(core.Schema):

    worker_configuration: Optional[WorkerConfiguration] = core.attr(
        WorkerConfiguration, default=None
    )

    worker_count: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        worker_count: Union[int, core.IntOut],
        worker_configuration: Optional[WorkerConfiguration] = None,
    ):
        super().__init__(
            args=InitialCapacityConfig.Args(
                worker_count=worker_count,
                worker_configuration=worker_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        worker_configuration: Optional[WorkerConfiguration] = core.arg(default=None)

        worker_count: Union[int, core.IntOut] = core.arg()


@core.schema
class InitialCapacity(core.Schema):

    initial_capacity_config: Optional[InitialCapacityConfig] = core.attr(
        InitialCapacityConfig, default=None
    )

    initial_capacity_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        initial_capacity_type: Union[str, core.StringOut],
        initial_capacity_config: Optional[InitialCapacityConfig] = None,
    ):
        super().__init__(
            args=InitialCapacity.Args(
                initial_capacity_type=initial_capacity_type,
                initial_capacity_config=initial_capacity_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        initial_capacity_config: Optional[InitialCapacityConfig] = core.arg(default=None)

        initial_capacity_type: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoStopConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    idle_timeout_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        idle_timeout_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AutoStopConfiguration.Args(
                enabled=enabled,
                idle_timeout_minutes=idle_timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        idle_timeout_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_emrserverless_application", namespace="aws_emrserverless")
class Application(core.Resource):
    """
    ARN of the cluster.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_start_configuration: Optional[AutoStartConfiguration] = core.attr(
        AutoStartConfiguration, default=None, computed=True
    )

    auto_stop_configuration: Optional[AutoStopConfiguration] = core.attr(
        AutoStopConfiguration, default=None, computed=True
    )

    """
    The ID of the cluster.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    initial_capacity: Optional[
        Union[List[InitialCapacity], core.ArrayOut[InitialCapacity]]
    ] = core.attr(InitialCapacity, default=None, kind=core.Kind.array)

    maximum_capacity: Optional[MaximumCapacity] = core.attr(MaximumCapacity, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    network_configuration: Optional[NetworkConfiguration] = core.attr(
        NetworkConfiguration, default=None
    )

    release_label: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Key-value mapping of resource tags. If configured with a provider [`default_tags` configu
    ration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configu
    ration-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        release_label: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        auto_start_configuration: Optional[AutoStartConfiguration] = None,
        auto_stop_configuration: Optional[AutoStopConfiguration] = None,
        initial_capacity: Optional[
            Union[List[InitialCapacity], core.ArrayOut[InitialCapacity]]
        ] = None,
        maximum_capacity: Optional[MaximumCapacity] = None,
        network_configuration: Optional[NetworkConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Application.Args(
                name=name,
                release_label=release_label,
                type=type,
                auto_start_configuration=auto_start_configuration,
                auto_stop_configuration=auto_stop_configuration,
                initial_capacity=initial_capacity,
                maximum_capacity=maximum_capacity,
                network_configuration=network_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_start_configuration: Optional[AutoStartConfiguration] = core.arg(default=None)

        auto_stop_configuration: Optional[AutoStopConfiguration] = core.arg(default=None)

        initial_capacity: Optional[
            Union[List[InitialCapacity], core.ArrayOut[InitialCapacity]]
        ] = core.arg(default=None)

        maximum_capacity: Optional[MaximumCapacity] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        network_configuration: Optional[NetworkConfiguration] = core.arg(default=None)

        release_label: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
