from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Alias(core.Schema):

    evaluate_target_health: Union[bool, core.BoolOut] = core.attr(bool)

    name: Union[str, core.StringOut] = core.attr(str)

    zone_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        evaluate_target_health: Union[bool, core.BoolOut],
        name: Union[str, core.StringOut],
        zone_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Alias.Args(
                evaluate_target_health=evaluate_target_health,
                name=name,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        evaluate_target_health: Union[bool, core.BoolOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        zone_id: Union[str, core.StringOut] = core.arg()


@core.schema
class LatencyRoutingPolicy(core.Schema):

    region: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LatencyRoutingPolicy.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: Union[str, core.StringOut] = core.arg()


@core.schema
class FailoverRoutingPolicy(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FailoverRoutingPolicy.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class GeolocationRoutingPolicy(core.Schema):

    continent: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    country: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subdivision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continent: Optional[Union[str, core.StringOut]] = None,
        country: Optional[Union[str, core.StringOut]] = None,
        subdivision: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GeolocationRoutingPolicy.Args(
                continent=continent,
                country=country,
                subdivision=subdivision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continent: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subdivision: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WeightedRoutingPolicy(core.Schema):

    weight: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        weight: Union[int, core.IntOut],
    ):
        super().__init__(
            args=WeightedRoutingPolicy.Args(
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        weight: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_route53_record", namespace="aws_route53")
class Record(core.Resource):

    alias: Optional[Union[List[Alias], core.ArrayOut[Alias]]] = core.attr(
        Alias, default=None, kind=core.Kind.array
    )

    allow_overwrite: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    failover_routing_policy: Optional[
        Union[List[FailoverRoutingPolicy], core.ArrayOut[FailoverRoutingPolicy]]
    ] = core.attr(FailoverRoutingPolicy, default=None, kind=core.Kind.array)

    fqdn: Union[str, core.StringOut] = core.attr(str, computed=True)

    geolocation_routing_policy: Optional[
        Union[List[GeolocationRoutingPolicy], core.ArrayOut[GeolocationRoutingPolicy]]
    ] = core.attr(GeolocationRoutingPolicy, default=None, kind=core.Kind.array)

    health_check_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    latency_routing_policy: Optional[
        Union[List[LatencyRoutingPolicy], core.ArrayOut[LatencyRoutingPolicy]]
    ] = core.attr(LatencyRoutingPolicy, default=None, kind=core.Kind.array)

    multivalue_answer_routing_policy: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    name: Union[str, core.StringOut] = core.attr(str)

    records: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    set_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    weighted_routing_policy: Optional[
        Union[List[WeightedRoutingPolicy], core.ArrayOut[WeightedRoutingPolicy]]
    ] = core.attr(WeightedRoutingPolicy, default=None, kind=core.Kind.array)

    zone_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        zone_id: Union[str, core.StringOut],
        alias: Optional[Union[List[Alias], core.ArrayOut[Alias]]] = None,
        allow_overwrite: Optional[Union[bool, core.BoolOut]] = None,
        failover_routing_policy: Optional[
            Union[List[FailoverRoutingPolicy], core.ArrayOut[FailoverRoutingPolicy]]
        ] = None,
        geolocation_routing_policy: Optional[
            Union[List[GeolocationRoutingPolicy], core.ArrayOut[GeolocationRoutingPolicy]]
        ] = None,
        health_check_id: Optional[Union[str, core.StringOut]] = None,
        latency_routing_policy: Optional[
            Union[List[LatencyRoutingPolicy], core.ArrayOut[LatencyRoutingPolicy]]
        ] = None,
        multivalue_answer_routing_policy: Optional[Union[bool, core.BoolOut]] = None,
        records: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        set_identifier: Optional[Union[str, core.StringOut]] = None,
        ttl: Optional[Union[int, core.IntOut]] = None,
        weighted_routing_policy: Optional[
            Union[List[WeightedRoutingPolicy], core.ArrayOut[WeightedRoutingPolicy]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Record.Args(
                name=name,
                type=type,
                zone_id=zone_id,
                alias=alias,
                allow_overwrite=allow_overwrite,
                failover_routing_policy=failover_routing_policy,
                geolocation_routing_policy=geolocation_routing_policy,
                health_check_id=health_check_id,
                latency_routing_policy=latency_routing_policy,
                multivalue_answer_routing_policy=multivalue_answer_routing_policy,
                records=records,
                set_identifier=set_identifier,
                ttl=ttl,
                weighted_routing_policy=weighted_routing_policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: Optional[Union[List[Alias], core.ArrayOut[Alias]]] = core.arg(default=None)

        allow_overwrite: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        failover_routing_policy: Optional[
            Union[List[FailoverRoutingPolicy], core.ArrayOut[FailoverRoutingPolicy]]
        ] = core.arg(default=None)

        geolocation_routing_policy: Optional[
            Union[List[GeolocationRoutingPolicy], core.ArrayOut[GeolocationRoutingPolicy]]
        ] = core.arg(default=None)

        health_check_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        latency_routing_policy: Optional[
            Union[List[LatencyRoutingPolicy], core.ArrayOut[LatencyRoutingPolicy]]
        ] = core.arg(default=None)

        multivalue_answer_routing_policy: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        records: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        set_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        weighted_routing_policy: Optional[
            Union[List[WeightedRoutingPolicy], core.ArrayOut[WeightedRoutingPolicy]]
        ] = core.arg(default=None)

        zone_id: Union[str, core.StringOut] = core.arg()
