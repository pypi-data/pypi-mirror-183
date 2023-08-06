from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ShareDistribution(core.Schema):

    share_identifier: Union[str, core.StringOut] = core.attr(str)

    weight_factor: Optional[Union[float, core.FloatOut]] = core.attr(float, default=None)

    def __init__(
        self,
        *,
        share_identifier: Union[str, core.StringOut],
        weight_factor: Optional[Union[float, core.FloatOut]] = None,
    ):
        super().__init__(
            args=ShareDistribution.Args(
                share_identifier=share_identifier,
                weight_factor=weight_factor,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        share_identifier: Union[str, core.StringOut] = core.arg()

        weight_factor: Optional[Union[float, core.FloatOut]] = core.arg(default=None)


@core.schema
class FairSharePolicy(core.Schema):

    compute_reservation: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    share_decay_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    share_distribution: Optional[
        Union[List[ShareDistribution], core.ArrayOut[ShareDistribution]]
    ] = core.attr(ShareDistribution, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        compute_reservation: Optional[Union[int, core.IntOut]] = None,
        share_decay_seconds: Optional[Union[int, core.IntOut]] = None,
        share_distribution: Optional[
            Union[List[ShareDistribution], core.ArrayOut[ShareDistribution]]
        ] = None,
    ):
        super().__init__(
            args=FairSharePolicy.Args(
                compute_reservation=compute_reservation,
                share_decay_seconds=share_decay_seconds,
                share_distribution=share_distribution,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_reservation: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        share_decay_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        share_distribution: Optional[
            Union[List[ShareDistribution], core.ArrayOut[ShareDistribution]]
        ] = core.arg(default=None)


@core.resource(type="aws_batch_scheduling_policy", namespace="aws_batch")
class SchedulingPolicy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    fair_share_policy: Optional[FairSharePolicy] = core.attr(FairSharePolicy, default=None)

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
        name: Union[str, core.StringOut],
        fair_share_policy: Optional[FairSharePolicy] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SchedulingPolicy.Args(
                name=name,
                fair_share_policy=fair_share_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fair_share_policy: Optional[FairSharePolicy] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
