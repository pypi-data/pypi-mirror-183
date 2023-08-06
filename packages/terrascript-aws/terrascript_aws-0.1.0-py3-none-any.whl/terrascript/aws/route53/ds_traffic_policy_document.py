from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Items(core.Schema):

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Items.Args(
                endpoint_reference=endpoint_reference,
                health_check=health_check,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Primary(core.Schema):

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
        rule_reference: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Primary.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Secondary(core.Schema):

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
        rule_reference: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Secondary.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Location(core.Schema):

    continent: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    country: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    is_default: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    rule_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subdivision: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        continent: Optional[Union[str, core.StringOut]] = None,
        country: Optional[Union[str, core.StringOut]] = None,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
        is_default: Optional[Union[bool, core.BoolOut]] = None,
        rule_reference: Optional[Union[str, core.StringOut]] = None,
        subdivision: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Location.Args(
                continent=continent,
                country=country,
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                is_default=is_default,
                rule_reference=rule_reference,
                subdivision=subdivision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        continent: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        is_default: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        rule_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subdivision: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class GeoProximityLocation(core.Schema):

    bias: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    latitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    longitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bias: Optional[Union[str, core.StringOut]] = None,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
        latitude: Optional[Union[str, core.StringOut]] = None,
        longitude: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        rule_reference: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=GeoProximityLocation.Args(
                bias=bias,
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                latitude=latitude,
                longitude=longitude,
                region=region,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bias: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        latitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        longitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Region(core.Schema):

    endpoint_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    health_check: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_reference: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        endpoint_reference: Optional[Union[str, core.StringOut]] = None,
        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = None,
        health_check: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        rule_reference: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Region.Args(
                endpoint_reference=endpoint_reference,
                evaluate_target_health=evaluate_target_health,
                health_check=health_check,
                region=region,
                rule_reference=rule_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        evaluate_target_health: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        health_check: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_reference: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    geo_proximity_location: Optional[
        Union[List[GeoProximityLocation], core.ArrayOut[GeoProximityLocation]]
    ] = core.attr(GeoProximityLocation, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str)

    items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.attr(
        Items, default=None, kind=core.Kind.array
    )

    location: Optional[Union[List[Location], core.ArrayOut[Location]]] = core.attr(
        Location, default=None, kind=core.Kind.array
    )

    primary: Optional[Primary] = core.attr(Primary, default=None)

    region: Optional[Union[List[Region], core.ArrayOut[Region]]] = core.attr(
        Region, default=None, kind=core.Kind.array
    )

    secondary: Optional[Secondary] = core.attr(Secondary, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        geo_proximity_location: Optional[
            Union[List[GeoProximityLocation], core.ArrayOut[GeoProximityLocation]]
        ] = None,
        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = None,
        location: Optional[Union[List[Location], core.ArrayOut[Location]]] = None,
        primary: Optional[Primary] = None,
        region: Optional[Union[List[Region], core.ArrayOut[Region]]] = None,
        secondary: Optional[Secondary] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                geo_proximity_location=geo_proximity_location,
                items=items,
                location=location,
                primary=primary,
                region=region,
                secondary=secondary,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        geo_proximity_location: Optional[
            Union[List[GeoProximityLocation], core.ArrayOut[GeoProximityLocation]]
        ] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        items: Optional[Union[List[Items], core.ArrayOut[Items]]] = core.arg(default=None)

        location: Optional[Union[List[Location], core.ArrayOut[Location]]] = core.arg(default=None)

        primary: Optional[Primary] = core.arg(default=None)

        region: Optional[Union[List[Region], core.ArrayOut[Region]]] = core.arg(default=None)

        secondary: Optional[Secondary] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Endpoint(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        region: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Endpoint.Args(
                id=id,
                region=region,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.data(type="aws_route53_traffic_policy_document", namespace="aws_route53")
class DsTrafficPolicyDocument(core.Data):

    endpoint: Optional[Union[List[Endpoint], core.ArrayOut[Endpoint]]] = core.attr(
        Endpoint, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    json: Union[str, core.StringOut] = core.attr(str, computed=True)

    record_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.attr(
        Rule, default=None, kind=core.Kind.array
    )

    start_endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start_rule: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        endpoint: Optional[Union[List[Endpoint], core.ArrayOut[Endpoint]]] = None,
        record_type: Optional[Union[str, core.StringOut]] = None,
        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = None,
        start_endpoint: Optional[Union[str, core.StringOut]] = None,
        start_rule: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsTrafficPolicyDocument.Args(
                endpoint=endpoint,
                record_type=record_type,
                rule=rule,
                start_endpoint=start_endpoint,
                start_rule=start_rule,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint: Optional[Union[List[Endpoint], core.ArrayOut[Endpoint]]] = core.arg(default=None)

        record_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Optional[Union[List[Rule], core.ArrayOut[Rule]]] = core.arg(default=None)

        start_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start_rule: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
