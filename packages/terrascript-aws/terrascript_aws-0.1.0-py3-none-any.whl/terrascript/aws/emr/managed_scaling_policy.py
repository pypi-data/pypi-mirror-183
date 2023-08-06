from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ComputeLimits(core.Schema):

    maximum_capacity_units: Union[int, core.IntOut] = core.attr(int)

    maximum_core_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    maximum_ondemand_capacity_units: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    minimum_capacity_units: Union[int, core.IntOut] = core.attr(int)

    unit_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        maximum_capacity_units: Union[int, core.IntOut],
        minimum_capacity_units: Union[int, core.IntOut],
        unit_type: Union[str, core.StringOut],
        maximum_core_capacity_units: Optional[Union[int, core.IntOut]] = None,
        maximum_ondemand_capacity_units: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ComputeLimits.Args(
                maximum_capacity_units=maximum_capacity_units,
                minimum_capacity_units=minimum_capacity_units,
                unit_type=unit_type,
                maximum_core_capacity_units=maximum_core_capacity_units,
                maximum_ondemand_capacity_units=maximum_ondemand_capacity_units,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_capacity_units: Union[int, core.IntOut] = core.arg()

        maximum_core_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maximum_ondemand_capacity_units: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        minimum_capacity_units: Union[int, core.IntOut] = core.arg()

        unit_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_emr_managed_scaling_policy", namespace="aws_emr")
class ManagedScalingPolicy(core.Resource):

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    compute_limits: Union[List[ComputeLimits], core.ArrayOut[ComputeLimits]] = core.attr(
        ComputeLimits, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        compute_limits: Union[List[ComputeLimits], core.ArrayOut[ComputeLimits]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ManagedScalingPolicy.Args(
                cluster_id=cluster_id,
                compute_limits=compute_limits,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_id: Union[str, core.StringOut] = core.arg()

        compute_limits: Union[List[ComputeLimits], core.ArrayOut[ComputeLimits]] = core.arg()
