from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class MinimumHealthyHosts(core.Schema):

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=MinimumHealthyHosts.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class TimeBasedCanary(core.Schema):

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        interval: Optional[Union[int, core.IntOut]] = None,
        percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TimeBasedCanary.Args(
                interval=interval,
                percentage=percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class TimeBasedLinear(core.Schema):

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        interval: Optional[Union[int, core.IntOut]] = None,
        percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TimeBasedLinear.Args(
                interval=interval,
                percentage=percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class TrafficRoutingConfig(core.Schema):

    time_based_canary: Optional[TimeBasedCanary] = core.attr(TimeBasedCanary, default=None)

    time_based_linear: Optional[TimeBasedLinear] = core.attr(TimeBasedLinear, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        time_based_canary: Optional[TimeBasedCanary] = None,
        time_based_linear: Optional[TimeBasedLinear] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TrafficRoutingConfig.Args(
                time_based_canary=time_based_canary,
                time_based_linear=time_based_linear,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        time_based_canary: Optional[TimeBasedCanary] = core.arg(default=None)

        time_based_linear: Optional[TimeBasedLinear] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_codedeploy_deployment_config", namespace="aws_codedeploy")
class DeploymentConfig(core.Resource):

    compute_platform: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_config_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    deployment_config_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    minimum_healthy_hosts: Optional[MinimumHealthyHosts] = core.attr(
        MinimumHealthyHosts, default=None
    )

    traffic_routing_config: Optional[TrafficRoutingConfig] = core.attr(
        TrafficRoutingConfig, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        deployment_config_name: Union[str, core.StringOut],
        compute_platform: Optional[Union[str, core.StringOut]] = None,
        minimum_healthy_hosts: Optional[MinimumHealthyHosts] = None,
        traffic_routing_config: Optional[TrafficRoutingConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DeploymentConfig.Args(
                deployment_config_name=deployment_config_name,
                compute_platform=compute_platform,
                minimum_healthy_hosts=minimum_healthy_hosts,
                traffic_routing_config=traffic_routing_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_platform: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_config_name: Union[str, core.StringOut] = core.arg()

        minimum_healthy_hosts: Optional[MinimumHealthyHosts] = core.arg(default=None)

        traffic_routing_config: Optional[TrafficRoutingConfig] = core.arg(default=None)
