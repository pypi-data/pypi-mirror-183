from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TriggerConfiguration(core.Schema):

    trigger_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    trigger_name: Union[str, core.StringOut] = core.attr(str)

    trigger_target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        trigger_events: Union[List[str], core.ArrayOut[core.StringOut]],
        trigger_name: Union[str, core.StringOut],
        trigger_target_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TriggerConfiguration.Args(
                trigger_events=trigger_events,
                trigger_name=trigger_name,
                trigger_target_arn=trigger_target_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        trigger_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        trigger_name: Union[str, core.StringOut] = core.arg()

        trigger_target_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ElbInfo(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ElbInfo.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TargetGroupInfo(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TargetGroupInfo.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TestTrafficRoute(core.Schema):

    listener_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        listener_arns: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=TestTrafficRoute.Args(
                listener_arns=listener_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class ProdTrafficRoute(core.Schema):

    listener_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        listener_arns: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ProdTrafficRoute.Args(
                listener_arns=listener_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        listener_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class TargetGroup(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class TargetGroupPairInfo(core.Schema):

    prod_traffic_route: ProdTrafficRoute = core.attr(ProdTrafficRoute)

    target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.attr(
        TargetGroup, kind=core.Kind.array
    )

    test_traffic_route: Optional[TestTrafficRoute] = core.attr(TestTrafficRoute, default=None)

    def __init__(
        self,
        *,
        prod_traffic_route: ProdTrafficRoute,
        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]],
        test_traffic_route: Optional[TestTrafficRoute] = None,
    ):
        super().__init__(
            args=TargetGroupPairInfo.Args(
                prod_traffic_route=prod_traffic_route,
                target_group=target_group,
                test_traffic_route=test_traffic_route,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prod_traffic_route: ProdTrafficRoute = core.arg()

        target_group: Union[List[TargetGroup], core.ArrayOut[TargetGroup]] = core.arg()

        test_traffic_route: Optional[TestTrafficRoute] = core.arg(default=None)


@core.schema
class LoadBalancerInfo(core.Schema):

    elb_info: Optional[Union[List[ElbInfo], core.ArrayOut[ElbInfo]]] = core.attr(
        ElbInfo, default=None, kind=core.Kind.array
    )

    target_group_info: Optional[
        Union[List[TargetGroupInfo], core.ArrayOut[TargetGroupInfo]]
    ] = core.attr(TargetGroupInfo, default=None, kind=core.Kind.array)

    target_group_pair_info: Optional[TargetGroupPairInfo] = core.attr(
        TargetGroupPairInfo, default=None
    )

    def __init__(
        self,
        *,
        elb_info: Optional[Union[List[ElbInfo], core.ArrayOut[ElbInfo]]] = None,
        target_group_info: Optional[
            Union[List[TargetGroupInfo], core.ArrayOut[TargetGroupInfo]]
        ] = None,
        target_group_pair_info: Optional[TargetGroupPairInfo] = None,
    ):
        super().__init__(
            args=LoadBalancerInfo.Args(
                elb_info=elb_info,
                target_group_info=target_group_info,
                target_group_pair_info=target_group_pair_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        elb_info: Optional[Union[List[ElbInfo], core.ArrayOut[ElbInfo]]] = core.arg(default=None)

        target_group_info: Optional[
            Union[List[TargetGroupInfo], core.ArrayOut[TargetGroupInfo]]
        ] = core.arg(default=None)

        target_group_pair_info: Optional[TargetGroupPairInfo] = core.arg(default=None)


@core.schema
class Ec2TagFilter(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Ec2TagFilter.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Ec2TagSet(core.Schema):

    ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = core.attr(
        Ec2TagFilter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = None,
    ):
        super().__init__(
            args=Ec2TagSet.Args(
                ec2_tag_filter=ec2_tag_filter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = core.arg(
            default=None
        )


@core.schema
class AutoRollbackConfiguration(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=AutoRollbackConfiguration.Args(
                enabled=enabled,
                events=events,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class DeploymentStyle(core.Schema):

    deployment_option: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        deployment_option: Optional[Union[str, core.StringOut]] = None,
        deployment_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeploymentStyle.Args(
                deployment_option=deployment_option,
                deployment_type=deployment_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deployment_option: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OnPremisesInstanceTagFilter(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OnPremisesInstanceTagFilter.Args(
                key=key,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AlarmConfiguration(core.Schema):

    alarms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ignore_poll_alarm_failure: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        alarms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        ignore_poll_alarm_failure: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=AlarmConfiguration.Args(
                alarms=alarms,
                enabled=enabled,
                ignore_poll_alarm_failure=ignore_poll_alarm_failure,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarms: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ignore_poll_alarm_failure: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class DeploymentReadyOption(core.Schema):

    action_on_timeout: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    wait_time_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        action_on_timeout: Optional[Union[str, core.StringOut]] = None,
        wait_time_in_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DeploymentReadyOption.Args(
                action_on_timeout=action_on_timeout,
                wait_time_in_minutes=wait_time_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_on_timeout: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wait_time_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class GreenFleetProvisioningOption(core.Schema):

    action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GreenFleetProvisioningOption.Args(
                action=action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TerminateBlueInstancesOnDeploymentSuccess(core.Schema):

    action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    termination_wait_time_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    def __init__(
        self,
        *,
        action: Optional[Union[str, core.StringOut]] = None,
        termination_wait_time_in_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TerminateBlueInstancesOnDeploymentSuccess.Args(
                action=action,
                termination_wait_time_in_minutes=termination_wait_time_in_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        termination_wait_time_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class BlueGreenDeploymentConfig(core.Schema):

    deployment_ready_option: Optional[DeploymentReadyOption] = core.attr(
        DeploymentReadyOption, default=None
    )

    green_fleet_provisioning_option: Optional[GreenFleetProvisioningOption] = core.attr(
        GreenFleetProvisioningOption, default=None, computed=True
    )

    terminate_blue_instances_on_deployment_success: Optional[
        TerminateBlueInstancesOnDeploymentSuccess
    ] = core.attr(TerminateBlueInstancesOnDeploymentSuccess, default=None)

    def __init__(
        self,
        *,
        deployment_ready_option: Optional[DeploymentReadyOption] = None,
        green_fleet_provisioning_option: Optional[GreenFleetProvisioningOption] = None,
        terminate_blue_instances_on_deployment_success: Optional[
            TerminateBlueInstancesOnDeploymentSuccess
        ] = None,
    ):
        super().__init__(
            args=BlueGreenDeploymentConfig.Args(
                deployment_ready_option=deployment_ready_option,
                green_fleet_provisioning_option=green_fleet_provisioning_option,
                terminate_blue_instances_on_deployment_success=terminate_blue_instances_on_deployment_success,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        deployment_ready_option: Optional[DeploymentReadyOption] = core.arg(default=None)

        green_fleet_provisioning_option: Optional[GreenFleetProvisioningOption] = core.arg(
            default=None
        )

        terminate_blue_instances_on_deployment_success: Optional[
            TerminateBlueInstancesOnDeploymentSuccess
        ] = core.arg(default=None)


@core.schema
class EcsService(core.Schema):

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    service_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cluster_name: Union[str, core.StringOut],
        service_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EcsService.Args(
                cluster_name=cluster_name,
                service_name=service_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: Union[str, core.StringOut] = core.arg()

        service_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_codedeploy_deployment_group", namespace="aws_codedeploy")
class DeploymentGroup(core.Resource):

    alarm_configuration: Optional[AlarmConfiguration] = core.attr(AlarmConfiguration, default=None)

    app_name: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_rollback_configuration: Optional[AutoRollbackConfiguration] = core.attr(
        AutoRollbackConfiguration, default=None
    )

    autoscaling_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    blue_green_deployment_config: Optional[BlueGreenDeploymentConfig] = core.attr(
        BlueGreenDeploymentConfig, default=None, computed=True
    )

    compute_platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_config_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_group_name: Union[str, core.StringOut] = core.attr(str)

    deployment_style: Optional[DeploymentStyle] = core.attr(DeploymentStyle, default=None)

    ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = core.attr(
        Ec2TagFilter, default=None, kind=core.Kind.array
    )

    ec2_tag_set: Optional[Union[List[Ec2TagSet], core.ArrayOut[Ec2TagSet]]] = core.attr(
        Ec2TagSet, default=None, kind=core.Kind.array
    )

    ecs_service: Optional[EcsService] = core.attr(EcsService, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_info: Optional[LoadBalancerInfo] = core.attr(LoadBalancerInfo, default=None)

    on_premises_instance_tag_filter: Optional[
        Union[List[OnPremisesInstanceTagFilter], core.ArrayOut[OnPremisesInstanceTagFilter]]
    ] = core.attr(OnPremisesInstanceTagFilter, default=None, kind=core.Kind.array)

    service_role_arn: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    trigger_configuration: Optional[
        Union[List[TriggerConfiguration], core.ArrayOut[TriggerConfiguration]]
    ] = core.attr(TriggerConfiguration, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        app_name: Union[str, core.StringOut],
        deployment_group_name: Union[str, core.StringOut],
        service_role_arn: Union[str, core.StringOut],
        alarm_configuration: Optional[AlarmConfiguration] = None,
        auto_rollback_configuration: Optional[AutoRollbackConfiguration] = None,
        autoscaling_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        blue_green_deployment_config: Optional[BlueGreenDeploymentConfig] = None,
        deployment_config_name: Optional[Union[str, core.StringOut]] = None,
        deployment_style: Optional[DeploymentStyle] = None,
        ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = None,
        ec2_tag_set: Optional[Union[List[Ec2TagSet], core.ArrayOut[Ec2TagSet]]] = None,
        ecs_service: Optional[EcsService] = None,
        load_balancer_info: Optional[LoadBalancerInfo] = None,
        on_premises_instance_tag_filter: Optional[
            Union[List[OnPremisesInstanceTagFilter], core.ArrayOut[OnPremisesInstanceTagFilter]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        trigger_configuration: Optional[
            Union[List[TriggerConfiguration], core.ArrayOut[TriggerConfiguration]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentGroup.Args(
                app_name=app_name,
                deployment_group_name=deployment_group_name,
                service_role_arn=service_role_arn,
                alarm_configuration=alarm_configuration,
                auto_rollback_configuration=auto_rollback_configuration,
                autoscaling_groups=autoscaling_groups,
                blue_green_deployment_config=blue_green_deployment_config,
                deployment_config_name=deployment_config_name,
                deployment_style=deployment_style,
                ec2_tag_filter=ec2_tag_filter,
                ec2_tag_set=ec2_tag_set,
                ecs_service=ecs_service,
                load_balancer_info=load_balancer_info,
                on_premises_instance_tag_filter=on_premises_instance_tag_filter,
                tags=tags,
                tags_all=tags_all,
                trigger_configuration=trigger_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alarm_configuration: Optional[AlarmConfiguration] = core.arg(default=None)

        app_name: Union[str, core.StringOut] = core.arg()

        auto_rollback_configuration: Optional[AutoRollbackConfiguration] = core.arg(default=None)

        autoscaling_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        blue_green_deployment_config: Optional[BlueGreenDeploymentConfig] = core.arg(default=None)

        deployment_config_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_group_name: Union[str, core.StringOut] = core.arg()

        deployment_style: Optional[DeploymentStyle] = core.arg(default=None)

        ec2_tag_filter: Optional[Union[List[Ec2TagFilter], core.ArrayOut[Ec2TagFilter]]] = core.arg(
            default=None
        )

        ec2_tag_set: Optional[Union[List[Ec2TagSet], core.ArrayOut[Ec2TagSet]]] = core.arg(
            default=None
        )

        ecs_service: Optional[EcsService] = core.arg(default=None)

        load_balancer_info: Optional[LoadBalancerInfo] = core.arg(default=None)

        on_premises_instance_tag_filter: Optional[
            Union[List[OnPremisesInstanceTagFilter], core.ArrayOut[OnPremisesInstanceTagFilter]]
        ] = core.arg(default=None)

        service_role_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        trigger_configuration: Optional[
            Union[List[TriggerConfiguration], core.ArrayOut[TriggerConfiguration]]
        ] = core.arg(default=None)
