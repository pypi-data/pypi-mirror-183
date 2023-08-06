from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RuntimePlatform(core.Schema):

    cpu_architecture: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operating_system_family: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu_architecture: Optional[Union[str, core.StringOut]] = None,
        operating_system_family: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RuntimePlatform.Args(
                cpu_architecture=cpu_architecture,
                operating_system_family=operating_system_family,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu_architecture: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operating_system_family: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InferenceAccelerator(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    device_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        device_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InferenceAccelerator.Args(
                device_name=device_name,
                device_type=device_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        device_type: Union[str, core.StringOut] = core.arg()


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
class ProxyConfiguration(core.Schema):

    container_name: Union[str, core.StringOut] = core.attr(str)

    properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        container_name: Union[str, core.StringOut],
        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProxyConfiguration.Args(
                container_name=container_name,
                properties=properties,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_name: Union[str, core.StringOut] = core.arg()

        properties: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EphemeralStorage(core.Schema):

    size_in_gib: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        size_in_gib: Union[int, core.IntOut],
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size_in_gib=size_in_gib,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size_in_gib: Union[int, core.IntOut] = core.arg()


@core.schema
class DockerVolumeConfiguration(core.Schema):

    autoprovision: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    driver: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    driver_opts: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        autoprovision: Optional[Union[bool, core.BoolOut]] = None,
        driver: Optional[Union[str, core.StringOut]] = None,
        driver_opts: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        scope: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DockerVolumeConfiguration.Args(
                autoprovision=autoprovision,
                driver=driver,
                driver_opts=driver_opts,
                labels=labels,
                scope=scope,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoprovision: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        driver: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        driver_opts: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EfsVolumeConfigurationAuthorizationConfig(core.Schema):

    access_point_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_point_id: Optional[Union[str, core.StringOut]] = None,
        iam: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EfsVolumeConfigurationAuthorizationConfig.Args(
                access_point_id=access_point_id,
                iam=iam,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EfsVolumeConfiguration(core.Schema):

    authorization_config: Optional[EfsVolumeConfigurationAuthorizationConfig] = core.attr(
        EfsVolumeConfigurationAuthorizationConfig, default=None
    )

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    root_directory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transit_encryption: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transit_encryption_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        file_system_id: Union[str, core.StringOut],
        authorization_config: Optional[EfsVolumeConfigurationAuthorizationConfig] = None,
        root_directory: Optional[Union[str, core.StringOut]] = None,
        transit_encryption: Optional[Union[str, core.StringOut]] = None,
        transit_encryption_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EfsVolumeConfiguration.Args(
                file_system_id=file_system_id,
                authorization_config=authorization_config,
                root_directory=root_directory,
                transit_encryption=transit_encryption,
                transit_encryption_port=transit_encryption_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: Optional[EfsVolumeConfigurationAuthorizationConfig] = core.arg(
            default=None
        )

        file_system_id: Union[str, core.StringOut] = core.arg()

        root_directory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_encryption: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_encryption_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class FsxWindowsFileServerVolumeConfigurationAuthorizationConfig(core.Schema):

    credentials_parameter: Union[str, core.StringOut] = core.attr(str)

    domain: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        credentials_parameter: Union[str, core.StringOut],
        domain: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FsxWindowsFileServerVolumeConfigurationAuthorizationConfig.Args(
                credentials_parameter=credentials_parameter,
                domain=domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credentials_parameter: Union[str, core.StringOut] = core.arg()

        domain: Union[str, core.StringOut] = core.arg()


@core.schema
class FsxWindowsFileServerVolumeConfiguration(core.Schema):

    authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig = core.attr(
        FsxWindowsFileServerVolumeConfigurationAuthorizationConfig
    )

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    root_directory: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig,
        file_system_id: Union[str, core.StringOut],
        root_directory: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FsxWindowsFileServerVolumeConfiguration.Args(
                authorization_config=authorization_config,
                file_system_id=file_system_id,
                root_directory=root_directory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_config: FsxWindowsFileServerVolumeConfigurationAuthorizationConfig = (
            core.arg()
        )

        file_system_id: Union[str, core.StringOut] = core.arg()

        root_directory: Union[str, core.StringOut] = core.arg()


@core.schema
class Volume(core.Schema):

    docker_volume_configuration: Optional[DockerVolumeConfiguration] = core.attr(
        DockerVolumeConfiguration, default=None
    )

    efs_volume_configuration: Optional[EfsVolumeConfiguration] = core.attr(
        EfsVolumeConfiguration, default=None
    )

    fsx_windows_file_server_volume_configuration: Optional[
        FsxWindowsFileServerVolumeConfiguration
    ] = core.attr(FsxWindowsFileServerVolumeConfiguration, default=None)

    host_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        docker_volume_configuration: Optional[DockerVolumeConfiguration] = None,
        efs_volume_configuration: Optional[EfsVolumeConfiguration] = None,
        fsx_windows_file_server_volume_configuration: Optional[
            FsxWindowsFileServerVolumeConfiguration
        ] = None,
        host_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Volume.Args(
                name=name,
                docker_volume_configuration=docker_volume_configuration,
                efs_volume_configuration=efs_volume_configuration,
                fsx_windows_file_server_volume_configuration=fsx_windows_file_server_volume_configuration,
                host_path=host_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        docker_volume_configuration: Optional[DockerVolumeConfiguration] = core.arg(default=None)

        efs_volume_configuration: Optional[EfsVolumeConfiguration] = core.arg(default=None)

        fsx_windows_file_server_volume_configuration: Optional[
            FsxWindowsFileServerVolumeConfiguration
        ] = core.arg(default=None)

        host_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ecs_task_definition", namespace="aws_ecs")
class TaskDefinition(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container_definitions: Union[str, core.StringOut] = core.attr(str)

    cpu: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ephemeral_storage: Optional[EphemeralStorage] = core.attr(EphemeralStorage, default=None)

    execution_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    family: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inference_accelerator: Optional[
        Union[List[InferenceAccelerator], core.ArrayOut[InferenceAccelerator]]
    ] = core.attr(InferenceAccelerator, default=None, kind=core.Kind.array)

    ipc_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    memory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    network_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    pid_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    placement_constraints: Optional[
        Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
    ] = core.attr(PlacementConstraints, default=None, kind=core.Kind.array)

    proxy_configuration: Optional[ProxyConfiguration] = core.attr(ProxyConfiguration, default=None)

    requires_compatibilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    runtime_platform: Optional[RuntimePlatform] = core.attr(RuntimePlatform, default=None)

    skip_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    volume: Optional[Union[List[Volume], core.ArrayOut[Volume]]] = core.attr(
        Volume, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        container_definitions: Union[str, core.StringOut],
        family: Union[str, core.StringOut],
        cpu: Optional[Union[str, core.StringOut]] = None,
        ephemeral_storage: Optional[EphemeralStorage] = None,
        execution_role_arn: Optional[Union[str, core.StringOut]] = None,
        inference_accelerator: Optional[
            Union[List[InferenceAccelerator], core.ArrayOut[InferenceAccelerator]]
        ] = None,
        ipc_mode: Optional[Union[str, core.StringOut]] = None,
        memory: Optional[Union[str, core.StringOut]] = None,
        network_mode: Optional[Union[str, core.StringOut]] = None,
        pid_mode: Optional[Union[str, core.StringOut]] = None,
        placement_constraints: Optional[
            Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
        ] = None,
        proxy_configuration: Optional[ProxyConfiguration] = None,
        requires_compatibilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        runtime_platform: Optional[RuntimePlatform] = None,
        skip_destroy: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        task_role_arn: Optional[Union[str, core.StringOut]] = None,
        volume: Optional[Union[List[Volume], core.ArrayOut[Volume]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TaskDefinition.Args(
                container_definitions=container_definitions,
                family=family,
                cpu=cpu,
                ephemeral_storage=ephemeral_storage,
                execution_role_arn=execution_role_arn,
                inference_accelerator=inference_accelerator,
                ipc_mode=ipc_mode,
                memory=memory,
                network_mode=network_mode,
                pid_mode=pid_mode,
                placement_constraints=placement_constraints,
                proxy_configuration=proxy_configuration,
                requires_compatibilities=requires_compatibilities,
                runtime_platform=runtime_platform,
                skip_destroy=skip_destroy,
                tags=tags,
                tags_all=tags_all,
                task_role_arn=task_role_arn,
                volume=volume,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_definitions: Union[str, core.StringOut] = core.arg()

        cpu: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ephemeral_storage: Optional[EphemeralStorage] = core.arg(default=None)

        execution_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        family: Union[str, core.StringOut] = core.arg()

        inference_accelerator: Optional[
            Union[List[InferenceAccelerator], core.ArrayOut[InferenceAccelerator]]
        ] = core.arg(default=None)

        ipc_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        memory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pid_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        placement_constraints: Optional[
            Union[List[PlacementConstraints], core.ArrayOut[PlacementConstraints]]
        ] = core.arg(default=None)

        proxy_configuration: Optional[ProxyConfiguration] = core.arg(default=None)

        requires_compatibilities: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        runtime_platform: Optional[RuntimePlatform] = core.arg(default=None)

        skip_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        task_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        volume: Optional[Union[List[Volume], core.ArrayOut[Volume]]] = core.arg(default=None)
