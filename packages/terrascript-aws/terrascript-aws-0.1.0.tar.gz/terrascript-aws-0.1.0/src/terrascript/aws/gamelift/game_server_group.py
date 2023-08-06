from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InstanceDefinition(core.Schema):

    instance_type: Union[str, core.StringOut] = core.attr(str)

    weighted_capacity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_type: Union[str, core.StringOut],
        weighted_capacity: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstanceDefinition.Args(
                instance_type=instance_type,
                weighted_capacity=weighted_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: Union[str, core.StringOut] = core.arg()

        weighted_capacity: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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
class TargetTrackingConfiguration(core.Schema):

    target_value: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        target_value: Union[float, core.FloatOut],
    ):
        super().__init__(
            args=TargetTrackingConfiguration.Args(
                target_value=target_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_value: Union[float, core.FloatOut] = core.arg()


@core.schema
class AutoScalingPolicy(core.Schema):

    estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    target_tracking_configuration: TargetTrackingConfiguration = core.attr(
        TargetTrackingConfiguration
    )

    def __init__(
        self,
        *,
        target_tracking_configuration: TargetTrackingConfiguration,
        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AutoScalingPolicy.Args(
                target_tracking_configuration=target_tracking_configuration,
                estimated_instance_warmup=estimated_instance_warmup,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        estimated_instance_warmup: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_tracking_configuration: TargetTrackingConfiguration = core.arg()


@core.resource(type="aws_gamelift_game_server_group", namespace="aws_gamelift")
class GameServerGroup(core.Resource):
    """
    The ARN of the GameLift Game Server Group.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The ARN of the created EC2 Auto Scaling group.
    """
    auto_scaling_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_scaling_policy: Optional[AutoScalingPolicy] = core.attr(AutoScalingPolicy, default=None)

    """
    (Optional) Indicates how GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances
    .
    """
    balancing_strategy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) Name of the game server group.
    """
    game_server_group_name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Indicates whether instances in the game server group are protected from early termination
    .
    """
    game_server_protection_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) A unique identifier for an existing EC2 launch template.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_definition: Union[
        List[InstanceDefinition], core.ArrayOut[InstanceDefinition]
    ] = core.attr(InstanceDefinition, kind=core.Kind.array)

    launch_template: LaunchTemplate = core.attr(LaunchTemplate)

    """
    (Required) The maximum number of instances allowed in the EC2 Auto Scaling group.
    """
    max_size: Union[int, core.IntOut] = core.attr(int)

    """
    (Required) The minimum number of instances allowed in the EC2 Auto Scaling group.
    """
    min_size: Union[int, core.IntOut] = core.attr(int)

    """
    (Required) ARN for an IAM role that allows Amazon GameLift to access your EC2 Auto Scaling groups.
    """
    role_arn: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Key-value map of resource tags
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Optional) A list of VPC subnets to use with instances in the game server group.
    """
    vpc_subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        game_server_group_name: Union[str, core.StringOut],
        instance_definition: Union[List[InstanceDefinition], core.ArrayOut[InstanceDefinition]],
        launch_template: LaunchTemplate,
        max_size: Union[int, core.IntOut],
        min_size: Union[int, core.IntOut],
        role_arn: Union[str, core.StringOut],
        auto_scaling_policy: Optional[AutoScalingPolicy] = None,
        balancing_strategy: Optional[Union[str, core.StringOut]] = None,
        game_server_protection_policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GameServerGroup.Args(
                game_server_group_name=game_server_group_name,
                instance_definition=instance_definition,
                launch_template=launch_template,
                max_size=max_size,
                min_size=min_size,
                role_arn=role_arn,
                auto_scaling_policy=auto_scaling_policy,
                balancing_strategy=balancing_strategy,
                game_server_protection_policy=game_server_protection_policy,
                tags=tags,
                tags_all=tags_all,
                vpc_subnets=vpc_subnets,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_scaling_policy: Optional[AutoScalingPolicy] = core.arg(default=None)

        balancing_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        game_server_group_name: Union[str, core.StringOut] = core.arg()

        game_server_protection_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_definition: Union[
            List[InstanceDefinition], core.ArrayOut[InstanceDefinition]
        ] = core.arg()

        launch_template: LaunchTemplate = core.arg()

        max_size: Union[int, core.IntOut] = core.arg()

        min_size: Union[int, core.IntOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_subnets: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
