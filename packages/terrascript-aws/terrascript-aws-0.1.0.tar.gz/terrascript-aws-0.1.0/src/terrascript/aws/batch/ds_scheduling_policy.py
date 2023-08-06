from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ShareDistribution(core.Schema):

    share_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    weight_factor: Union[float, core.FloatOut] = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        share_identifier: Union[str, core.StringOut],
        weight_factor: Union[float, core.FloatOut],
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

        weight_factor: Union[float, core.FloatOut] = core.arg()


@core.schema
class FairSharePolicy(core.Schema):

    compute_reservation: Union[int, core.IntOut] = core.attr(int, computed=True)

    share_decay_seconds: Union[int, core.IntOut] = core.attr(int, computed=True)

    share_distribution: Union[
        List[ShareDistribution], core.ArrayOut[ShareDistribution]
    ] = core.attr(ShareDistribution, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        compute_reservation: Union[int, core.IntOut],
        share_decay_seconds: Union[int, core.IntOut],
        share_distribution: Union[List[ShareDistribution], core.ArrayOut[ShareDistribution]],
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
        compute_reservation: Union[int, core.IntOut] = core.arg()

        share_decay_seconds: Union[int, core.IntOut] = core.arg()

        share_distribution: Union[
            List[ShareDistribution], core.ArrayOut[ShareDistribution]
        ] = core.arg()


@core.data(type="aws_batch_scheduling_policy", namespace="aws_batch")
class DsSchedulingPolicy(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    fair_share_policy: Union[List[FairSharePolicy], core.ArrayOut[FairSharePolicy]] = core.attr(
        FairSharePolicy, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSchedulingPolicy.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
