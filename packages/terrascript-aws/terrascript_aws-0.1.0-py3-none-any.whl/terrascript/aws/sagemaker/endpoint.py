from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Alarms(core.Schema):

    alarm_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        alarm_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Alarms.Args(
                alarm_name=alarm_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarm_name: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoRollbackConfiguration(core.Schema):

    alarms: Optional[Union[List[Alarms], core.ArrayOut[Alarms]]] = core.attr(
        Alarms, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        alarms: Optional[Union[List[Alarms], core.ArrayOut[Alarms]]] = None,
    ):
        super().__init__(
            args=AutoRollbackConfiguration.Args(
                alarms=alarms,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        alarms: Optional[Union[List[Alarms], core.ArrayOut[Alarms]]] = core.arg(default=None)


@core.schema
class CanarySize(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=CanarySize.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class LinearStepSize(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=LinearStepSize.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class TrafficRoutingConfiguration(core.Schema):

    canary_size: Optional[CanarySize] = core.attr(CanarySize, default=None)

    linear_step_size: Optional[LinearStepSize] = core.attr(LinearStepSize, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    wait_interval_in_seconds: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        wait_interval_in_seconds: Union[int, core.IntOut],
        canary_size: Optional[CanarySize] = None,
        linear_step_size: Optional[LinearStepSize] = None,
    ):
        super().__init__(
            args=TrafficRoutingConfiguration.Args(
                type=type,
                wait_interval_in_seconds=wait_interval_in_seconds,
                canary_size=canary_size,
                linear_step_size=linear_step_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        canary_size: Optional[CanarySize] = core.arg(default=None)

        linear_step_size: Optional[LinearStepSize] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        wait_interval_in_seconds: Union[int, core.IntOut] = core.arg()


@core.schema
class BlueGreenUpdatePolicy(core.Schema):

    maximum_execution_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    termination_wait_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    traffic_routing_configuration: TrafficRoutingConfiguration = core.attr(
        TrafficRoutingConfiguration
    )

    def __init__(
        self,
        *,
        traffic_routing_configuration: TrafficRoutingConfiguration,
        maximum_execution_timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
        termination_wait_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=BlueGreenUpdatePolicy.Args(
                traffic_routing_configuration=traffic_routing_configuration,
                maximum_execution_timeout_in_seconds=maximum_execution_timeout_in_seconds,
                termination_wait_in_seconds=termination_wait_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_execution_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        termination_wait_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        traffic_routing_configuration: TrafficRoutingConfiguration = core.arg()


@core.schema
class DeploymentConfig(core.Schema):

    auto_rollback_configuration: Optional[AutoRollbackConfiguration] = core.attr(
        AutoRollbackConfiguration, default=None
    )

    blue_green_update_policy: BlueGreenUpdatePolicy = core.attr(BlueGreenUpdatePolicy)

    def __init__(
        self,
        *,
        blue_green_update_policy: BlueGreenUpdatePolicy,
        auto_rollback_configuration: Optional[AutoRollbackConfiguration] = None,
    ):
        super().__init__(
            args=DeploymentConfig.Args(
                blue_green_update_policy=blue_green_update_policy,
                auto_rollback_configuration=auto_rollback_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_rollback_configuration: Optional[AutoRollbackConfiguration] = core.arg(default=None)

        blue_green_update_policy: BlueGreenUpdatePolicy = core.arg()


@core.resource(type="aws_sagemaker_endpoint", namespace="aws_sagemaker")
class Endpoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_config: Optional[DeploymentConfig] = core.attr(DeploymentConfig, default=None)

    endpoint_config_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        endpoint_config_name: Union[str, core.StringOut],
        deployment_config: Optional[DeploymentConfig] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Endpoint.Args(
                endpoint_config_name=endpoint_config_name,
                deployment_config=deployment_config,
                name=name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deployment_config: Optional[DeploymentConfig] = core.arg(default=None)

        endpoint_config_name: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
