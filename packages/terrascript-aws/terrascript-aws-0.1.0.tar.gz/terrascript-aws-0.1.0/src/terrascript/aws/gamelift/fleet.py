from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ResourceCreationLimitPolicy(core.Schema):

    new_game_sessions_per_creator: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    policy_period_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        new_game_sessions_per_creator: Optional[Union[int, core.IntOut]] = None,
        policy_period_in_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ResourceCreationLimitPolicy.Args(
                new_game_sessions_per_creator=new_game_sessions_per_creator,
                policy_period_in_minutes=policy_period_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        new_game_sessions_per_creator: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        policy_period_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ServerProcess(core.Schema):

    concurrent_executions: Union[int, core.IntOut] = core.attr(int)

    launch_path: Union[str, core.StringOut] = core.attr(str)

    parameters: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        concurrent_executions: Union[int, core.IntOut],
        launch_path: Union[str, core.StringOut],
        parameters: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ServerProcess.Args(
                concurrent_executions=concurrent_executions,
                launch_path=launch_path,
                parameters=parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        concurrent_executions: Union[int, core.IntOut] = core.arg()

        launch_path: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RuntimeConfiguration(core.Schema):

    game_session_activation_timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    max_concurrent_game_session_activations: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    server_process: Optional[Union[List[ServerProcess], core.ArrayOut[ServerProcess]]] = core.attr(
        ServerProcess, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        game_session_activation_timeout_seconds: Optional[Union[int, core.IntOut]] = None,
        max_concurrent_game_session_activations: Optional[Union[int, core.IntOut]] = None,
        server_process: Optional[Union[List[ServerProcess], core.ArrayOut[ServerProcess]]] = None,
    ):
        super().__init__(
            args=RuntimeConfiguration.Args(
                game_session_activation_timeout_seconds=game_session_activation_timeout_seconds,
                max_concurrent_game_session_activations=max_concurrent_game_session_activations,
                server_process=server_process,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        game_session_activation_timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        max_concurrent_game_session_activations: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        server_process: Optional[
            Union[List[ServerProcess], core.ArrayOut[ServerProcess]]
        ] = core.arg(default=None)


@core.schema
class CertificateConfiguration(core.Schema):

    certificate_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        certificate_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CertificateConfiguration.Args(
                certificate_type=certificate_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Ec2InboundPermission(core.Schema):

    from_port: Union[int, core.IntOut] = core.attr(int)

    ip_range: Union[str, core.StringOut] = core.attr(str)

    protocol: Union[str, core.StringOut] = core.attr(str)

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        ip_range: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        to_port: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Ec2InboundPermission.Args(
                from_port=from_port,
                ip_range=ip_range,
                protocol=protocol,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Union[int, core.IntOut] = core.arg()

        ip_range: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        to_port: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_gamelift_fleet", namespace="aws_gamelift")
class Fleet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    build_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    build_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_configuration: Optional[CertificateConfiguration] = core.attr(
        CertificateConfiguration, default=None, computed=True
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ec2_inbound_permission: Optional[
        Union[List[Ec2InboundPermission], core.ArrayOut[Ec2InboundPermission]]
    ] = core.attr(Ec2InboundPermission, default=None, computed=True, kind=core.Kind.array)

    ec2_instance_type: Union[str, core.StringOut] = core.attr(str)

    fleet_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_paths: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    metric_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    new_game_session_protection_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    operating_system: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_creation_limit_policy: Optional[ResourceCreationLimitPolicy] = core.attr(
        ResourceCreationLimitPolicy, default=None
    )

    runtime_configuration: Optional[RuntimeConfiguration] = core.attr(
        RuntimeConfiguration, default=None
    )

    script_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    script_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        ec2_instance_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        build_id: Optional[Union[str, core.StringOut]] = None,
        certificate_configuration: Optional[CertificateConfiguration] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ec2_inbound_permission: Optional[
            Union[List[Ec2InboundPermission], core.ArrayOut[Ec2InboundPermission]]
        ] = None,
        fleet_type: Optional[Union[str, core.StringOut]] = None,
        instance_role_arn: Optional[Union[str, core.StringOut]] = None,
        metric_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        new_game_session_protection_policy: Optional[Union[str, core.StringOut]] = None,
        resource_creation_limit_policy: Optional[ResourceCreationLimitPolicy] = None,
        runtime_configuration: Optional[RuntimeConfiguration] = None,
        script_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                ec2_instance_type=ec2_instance_type,
                name=name,
                build_id=build_id,
                certificate_configuration=certificate_configuration,
                description=description,
                ec2_inbound_permission=ec2_inbound_permission,
                fleet_type=fleet_type,
                instance_role_arn=instance_role_arn,
                metric_groups=metric_groups,
                new_game_session_protection_policy=new_game_session_protection_policy,
                resource_creation_limit_policy=resource_creation_limit_policy,
                runtime_configuration=runtime_configuration,
                script_id=script_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        build_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_configuration: Optional[CertificateConfiguration] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ec2_inbound_permission: Optional[
            Union[List[Ec2InboundPermission], core.ArrayOut[Ec2InboundPermission]]
        ] = core.arg(default=None)

        ec2_instance_type: Union[str, core.StringOut] = core.arg()

        fleet_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metric_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        new_game_session_protection_policy: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        resource_creation_limit_policy: Optional[ResourceCreationLimitPolicy] = core.arg(
            default=None
        )

        runtime_configuration: Optional[RuntimeConfiguration] = core.arg(default=None)

        script_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
