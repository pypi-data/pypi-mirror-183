from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ManagedScaling(core.Schema):

    instance_warmup_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    maximum_scaling_step_size: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    minimum_scaling_step_size: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    target_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        instance_warmup_period: Optional[Union[int, core.IntOut]] = None,
        maximum_scaling_step_size: Optional[Union[int, core.IntOut]] = None,
        minimum_scaling_step_size: Optional[Union[int, core.IntOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        target_capacity: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ManagedScaling.Args(
                instance_warmup_period=instance_warmup_period,
                maximum_scaling_step_size=maximum_scaling_step_size,
                minimum_scaling_step_size=minimum_scaling_step_size,
                status=status,
                target_capacity=target_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_warmup_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maximum_scaling_step_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        minimum_scaling_step_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class AutoScalingGroupProvider(core.Schema):

    auto_scaling_group_arn: Union[str, core.StringOut] = core.attr(str)

    managed_scaling: Optional[ManagedScaling] = core.attr(
        ManagedScaling, default=None, computed=True
    )

    managed_termination_protection: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        auto_scaling_group_arn: Union[str, core.StringOut],
        managed_scaling: Optional[ManagedScaling] = None,
        managed_termination_protection: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AutoScalingGroupProvider.Args(
                auto_scaling_group_arn=auto_scaling_group_arn,
                managed_scaling=managed_scaling,
                managed_termination_protection=managed_termination_protection,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_scaling_group_arn: Union[str, core.StringOut] = core.arg()

        managed_scaling: Optional[ManagedScaling] = core.arg(default=None)

        managed_termination_protection: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_ecs_capacity_provider", namespace="aws_ecs")
class CapacityProvider(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_scaling_group_provider: AutoScalingGroupProvider = core.attr(AutoScalingGroupProvider)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

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
        auto_scaling_group_provider: AutoScalingGroupProvider,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CapacityProvider.Args(
                auto_scaling_group_provider=auto_scaling_group_provider,
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
        auto_scaling_group_provider: AutoScalingGroupProvider = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
