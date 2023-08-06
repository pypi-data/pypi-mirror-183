from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class DestinationPortRange(core.Schema):

    from_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: Optional[Union[int, core.IntOut]] = None,
        to_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DestinationPortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class SourcePortRange(core.Schema):

    from_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: Optional[Union[int, core.IntOut]] = None,
        to_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SourcePortRange.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_ec2_traffic_mirror_filter_rule", namespace="aws_vpc")
class Ec2TrafficMirrorFilterRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_cidr_block: Union[str, core.StringOut] = core.attr(str)

    destination_port_range: Optional[DestinationPortRange] = core.attr(
        DestinationPortRange, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    rule_action: Union[str, core.StringOut] = core.attr(str)

    rule_number: Union[int, core.IntOut] = core.attr(int)

    source_cidr_block: Union[str, core.StringOut] = core.attr(str)

    source_port_range: Optional[SourcePortRange] = core.attr(SourcePortRange, default=None)

    traffic_direction: Union[str, core.StringOut] = core.attr(str)

    traffic_mirror_filter_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_cidr_block: Union[str, core.StringOut],
        rule_action: Union[str, core.StringOut],
        rule_number: Union[int, core.IntOut],
        source_cidr_block: Union[str, core.StringOut],
        traffic_direction: Union[str, core.StringOut],
        traffic_mirror_filter_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        destination_port_range: Optional[DestinationPortRange] = None,
        protocol: Optional[Union[int, core.IntOut]] = None,
        source_port_range: Optional[SourcePortRange] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2TrafficMirrorFilterRule.Args(
                destination_cidr_block=destination_cidr_block,
                rule_action=rule_action,
                rule_number=rule_number,
                source_cidr_block=source_cidr_block,
                traffic_direction=traffic_direction,
                traffic_mirror_filter_id=traffic_mirror_filter_id,
                description=description,
                destination_port_range=destination_port_range,
                protocol=protocol,
                source_port_range=source_port_range,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_cidr_block: Union[str, core.StringOut] = core.arg()

        destination_port_range: Optional[DestinationPortRange] = core.arg(default=None)

        protocol: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        rule_action: Union[str, core.StringOut] = core.arg()

        rule_number: Union[int, core.IntOut] = core.arg()

        source_cidr_block: Union[str, core.StringOut] = core.arg()

        source_port_range: Optional[SourcePortRange] = core.arg(default=None)

        traffic_direction: Union[str, core.StringOut] = core.arg()

        traffic_mirror_filter_id: Union[str, core.StringOut] = core.arg()
