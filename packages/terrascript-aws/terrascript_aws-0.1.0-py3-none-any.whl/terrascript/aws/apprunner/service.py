from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SourceCodeVersion(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceCodeVersion.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class CodeConfigurationValues(core.Schema):

    build_command: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    port: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    runtime: Union[str, core.StringOut] = core.attr(str)

    runtime_environment_variables: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    start_command: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        runtime: Union[str, core.StringOut],
        build_command: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[str, core.StringOut]] = None,
        runtime_environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        start_command: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CodeConfigurationValues.Args(
                runtime=runtime,
                build_command=build_command,
                port=port,
                runtime_environment_variables=runtime_environment_variables,
                start_command=start_command,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        build_command: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        runtime: Union[str, core.StringOut] = core.arg()

        runtime_environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        start_command: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CodeConfiguration(core.Schema):

    code_configuration_values: Optional[CodeConfigurationValues] = core.attr(
        CodeConfigurationValues, default=None
    )

    configuration_source: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        configuration_source: Union[str, core.StringOut],
        code_configuration_values: Optional[CodeConfigurationValues] = None,
    ):
        super().__init__(
            args=CodeConfiguration.Args(
                configuration_source=configuration_source,
                code_configuration_values=code_configuration_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_configuration_values: Optional[CodeConfigurationValues] = core.arg(default=None)

        configuration_source: Union[str, core.StringOut] = core.arg()


@core.schema
class CodeRepository(core.Schema):

    code_configuration: Optional[CodeConfiguration] = core.attr(CodeConfiguration, default=None)

    repository_url: Union[str, core.StringOut] = core.attr(str)

    source_code_version: SourceCodeVersion = core.attr(SourceCodeVersion)

    def __init__(
        self,
        *,
        repository_url: Union[str, core.StringOut],
        source_code_version: SourceCodeVersion,
        code_configuration: Optional[CodeConfiguration] = None,
    ):
        super().__init__(
            args=CodeRepository.Args(
                repository_url=repository_url,
                source_code_version=source_code_version,
                code_configuration=code_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_configuration: Optional[CodeConfiguration] = core.arg(default=None)

        repository_url: Union[str, core.StringOut] = core.arg()

        source_code_version: SourceCodeVersion = core.arg()


@core.schema
class ImageConfiguration(core.Schema):

    port: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    runtime_environment_variables: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    start_command: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        port: Optional[Union[str, core.StringOut]] = None,
        runtime_environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        start_command: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ImageConfiguration.Args(
                port=port,
                runtime_environment_variables=runtime_environment_variables,
                start_command=start_command,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        port: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        runtime_environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        start_command: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ImageRepository(core.Schema):

    image_configuration: Optional[ImageConfiguration] = core.attr(ImageConfiguration, default=None)

    image_identifier: Union[str, core.StringOut] = core.attr(str)

    image_repository_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        image_identifier: Union[str, core.StringOut],
        image_repository_type: Union[str, core.StringOut],
        image_configuration: Optional[ImageConfiguration] = None,
    ):
        super().__init__(
            args=ImageRepository.Args(
                image_identifier=image_identifier,
                image_repository_type=image_repository_type,
                image_configuration=image_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_configuration: Optional[ImageConfiguration] = core.arg(default=None)

        image_identifier: Union[str, core.StringOut] = core.arg()

        image_repository_type: Union[str, core.StringOut] = core.arg()


@core.schema
class AuthenticationConfiguration(core.Schema):

    access_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connection_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        access_role_arn: Optional[Union[str, core.StringOut]] = None,
        connection_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AuthenticationConfiguration.Args(
                access_role_arn=access_role_arn,
                connection_arn=connection_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connection_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SourceConfiguration(core.Schema):

    authentication_configuration: Optional[AuthenticationConfiguration] = core.attr(
        AuthenticationConfiguration, default=None
    )

    auto_deployments_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    code_repository: Optional[CodeRepository] = core.attr(CodeRepository, default=None)

    image_repository: Optional[ImageRepository] = core.attr(ImageRepository, default=None)

    def __init__(
        self,
        *,
        authentication_configuration: Optional[AuthenticationConfiguration] = None,
        auto_deployments_enabled: Optional[Union[bool, core.BoolOut]] = None,
        code_repository: Optional[CodeRepository] = None,
        image_repository: Optional[ImageRepository] = None,
    ):
        super().__init__(
            args=SourceConfiguration.Args(
                authentication_configuration=authentication_configuration,
                auto_deployments_enabled=auto_deployments_enabled,
                code_repository=code_repository,
                image_repository=image_repository,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_configuration: Optional[AuthenticationConfiguration] = core.arg(default=None)

        auto_deployments_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        code_repository: Optional[CodeRepository] = core.arg(default=None)

        image_repository: Optional[ImageRepository] = core.arg(default=None)


@core.schema
class InstanceConfiguration(core.Schema):

    cpu: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    memory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cpu: Optional[Union[str, core.StringOut]] = None,
        instance_role_arn: Optional[Union[str, core.StringOut]] = None,
        memory: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstanceConfiguration.Args(
                cpu=cpu,
                instance_role_arn=instance_role_arn,
                memory=memory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cpu: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        memory: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class HealthCheckConfiguration(core.Schema):

    healthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        healthy_threshold: Optional[Union[int, core.IntOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
        protocol: Optional[Union[str, core.StringOut]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
        unhealthy_threshold: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=HealthCheckConfiguration.Args(
                healthy_threshold=healthy_threshold,
                interval=interval,
                path=path,
                protocol=protocol,
                timeout=timeout,
                unhealthy_threshold=unhealthy_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        healthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        unhealthy_threshold: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class EgressConfiguration(core.Schema):

    egress_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    vpc_connector_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        egress_type: Optional[Union[str, core.StringOut]] = None,
        vpc_connector_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EgressConfiguration.Args(
                egress_type=egress_type,
                vpc_connector_arn=vpc_connector_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_connector_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NetworkConfiguration(core.Schema):

    egress_configuration: Optional[EgressConfiguration] = core.attr(
        EgressConfiguration, default=None
    )

    def __init__(
        self,
        *,
        egress_configuration: Optional[EgressConfiguration] = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                egress_configuration=egress_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        egress_configuration: Optional[EgressConfiguration] = core.arg(default=None)


@core.schema
class ObservabilityConfiguration(core.Schema):

    observability_configuration_arn: Union[str, core.StringOut] = core.attr(str)

    observability_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        observability_configuration_arn: Union[str, core.StringOut],
        observability_enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ObservabilityConfiguration.Args(
                observability_configuration_arn=observability_configuration_arn,
                observability_enabled=observability_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        observability_configuration_arn: Union[str, core.StringOut] = core.arg()

        observability_enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    kms_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        kms_key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                kms_key=kms_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_apprunner_service", namespace="aws_apprunner")
class Service(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_scaling_configuration_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    encryption_configuration: Optional[EncryptionConfiguration] = core.attr(
        EncryptionConfiguration, default=None
    )

    health_check_configuration: Optional[HealthCheckConfiguration] = core.attr(
        HealthCheckConfiguration, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_configuration: Optional[InstanceConfiguration] = core.attr(
        InstanceConfiguration, default=None, computed=True
    )

    network_configuration: Optional[NetworkConfiguration] = core.attr(
        NetworkConfiguration, default=None, computed=True
    )

    observability_configuration: Optional[ObservabilityConfiguration] = core.attr(
        ObservabilityConfiguration, default=None
    )

    service_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_name: Union[str, core.StringOut] = core.attr(str)

    service_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_configuration: SourceConfiguration = core.attr(SourceConfiguration)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        service_name: Union[str, core.StringOut],
        source_configuration: SourceConfiguration,
        auto_scaling_configuration_arn: Optional[Union[str, core.StringOut]] = None,
        encryption_configuration: Optional[EncryptionConfiguration] = None,
        health_check_configuration: Optional[HealthCheckConfiguration] = None,
        instance_configuration: Optional[InstanceConfiguration] = None,
        network_configuration: Optional[NetworkConfiguration] = None,
        observability_configuration: Optional[ObservabilityConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Service.Args(
                service_name=service_name,
                source_configuration=source_configuration,
                auto_scaling_configuration_arn=auto_scaling_configuration_arn,
                encryption_configuration=encryption_configuration,
                health_check_configuration=health_check_configuration,
                instance_configuration=instance_configuration,
                network_configuration=network_configuration,
                observability_configuration=observability_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_configuration_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        encryption_configuration: Optional[EncryptionConfiguration] = core.arg(default=None)

        health_check_configuration: Optional[HealthCheckConfiguration] = core.arg(default=None)

        instance_configuration: Optional[InstanceConfiguration] = core.arg(default=None)

        network_configuration: Optional[NetworkConfiguration] = core.arg(default=None)

        observability_configuration: Optional[ObservabilityConfiguration] = core.arg(default=None)

        service_name: Union[str, core.StringOut] = core.arg()

        source_configuration: SourceConfiguration = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
