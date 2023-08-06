from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SegmentActions(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    segment: Union[str, core.StringOut] = core.attr(str)

    share_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    share_with_except: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        segment: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        destination_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
        share_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        share_with_except: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SegmentActions.Args(
                action=action,
                segment=segment,
                description=description,
                destination_cidr_blocks=destination_cidr_blocks,
                destinations=destinations,
                mode=mode,
                share_with=share_with,
                share_with_except=share_with_except,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_cidr_blocks: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        segment: Union[str, core.StringOut] = core.arg()

        share_with: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        share_with_except: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class Conditions(core.Schema):

    key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operator: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        key: Optional[Union[str, core.StringOut]] = None,
        operator: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Conditions.Args(
                type=type,
                key=key,
                operator=operator,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operator: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Action(core.Schema):

    association_method: Union[str, core.StringOut] = core.attr(str)

    require_acceptance: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    segment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag_value_of_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        association_method: Union[str, core.StringOut],
        require_acceptance: Optional[Union[bool, core.BoolOut]] = None,
        segment: Optional[Union[str, core.StringOut]] = None,
        tag_value_of_key: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Action.Args(
                association_method=association_method,
                require_acceptance=require_acceptance,
                segment=segment,
                tag_value_of_key=tag_value_of_key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        association_method: Union[str, core.StringOut] = core.arg()

        require_acceptance: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        segment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_value_of_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AttachmentPolicies(core.Schema):

    action: Action = core.attr(Action)

    condition_logic: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    conditions: Union[List[Conditions], core.ArrayOut[Conditions]] = core.attr(
        Conditions, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_number: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        action: Action,
        conditions: Union[List[Conditions], core.ArrayOut[Conditions]],
        rule_number: Union[int, core.IntOut],
        condition_logic: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AttachmentPolicies.Args(
                action=action,
                conditions=conditions,
                rule_number=rule_number,
                condition_logic=condition_logic,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        condition_logic: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        conditions: Union[List[Conditions], core.ArrayOut[Conditions]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_number: Union[int, core.IntOut] = core.arg()


@core.schema
class EdgeLocations(core.Schema):

    asn: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    location: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        location: Union[str, core.StringOut],
        asn: Optional[Union[int, core.IntOut]] = None,
        inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=EdgeLocations.Args(
                location=location,
                asn=asn,
                inside_cidr_blocks=inside_cidr_blocks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        asn: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        location: Union[str, core.StringOut] = core.arg()


@core.schema
class CoreNetworkConfiguration(core.Schema):

    asn_ranges: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    edge_locations: Union[List[EdgeLocations], core.ArrayOut[EdgeLocations]] = core.attr(
        EdgeLocations, kind=core.Kind.array
    )

    inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpn_ecmp_support: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        asn_ranges: Union[List[str], core.ArrayOut[core.StringOut]],
        edge_locations: Union[List[EdgeLocations], core.ArrayOut[EdgeLocations]],
        inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        vpn_ecmp_support: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CoreNetworkConfiguration.Args(
                asn_ranges=asn_ranges,
                edge_locations=edge_locations,
                inside_cidr_blocks=inside_cidr_blocks,
                vpn_ecmp_support=vpn_ecmp_support,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        asn_ranges: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        edge_locations: Union[List[EdgeLocations], core.ArrayOut[EdgeLocations]] = core.arg()

        inside_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpn_ecmp_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Segments(core.Schema):

    allow_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    deny_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    edge_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    isolate_attachments: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    require_attachment_acceptance: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        allow_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        deny_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        edge_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        isolate_attachments: Optional[Union[bool, core.BoolOut]] = None,
        require_attachment_acceptance: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Segments.Args(
                name=name,
                allow_filter=allow_filter,
                deny_filter=deny_filter,
                description=description,
                edge_locations=edge_locations,
                isolate_attachments=isolate_attachments,
                require_attachment_acceptance=require_attachment_acceptance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        deny_filter: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        edge_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        isolate_attachments: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        require_attachment_acceptance: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.data(type="aws_networkmanager_core_network_policy_document", namespace="aws_networkmanager")
class DsCoreNetworkPolicyDocument(core.Data):

    attachment_policies: Optional[
        Union[List[AttachmentPolicies], core.ArrayOut[AttachmentPolicies]]
    ] = core.attr(AttachmentPolicies, default=None, kind=core.Kind.array)

    core_network_configuration: Union[
        List[CoreNetworkConfiguration], core.ArrayOut[CoreNetworkConfiguration]
    ] = core.attr(CoreNetworkConfiguration, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    json: Union[str, core.StringOut] = core.attr(str, computed=True)

    segment_actions: Optional[
        Union[List[SegmentActions], core.ArrayOut[SegmentActions]]
    ] = core.attr(SegmentActions, default=None, kind=core.Kind.array)

    segments: Union[List[Segments], core.ArrayOut[Segments]] = core.attr(
        Segments, kind=core.Kind.array
    )

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        core_network_configuration: Union[
            List[CoreNetworkConfiguration], core.ArrayOut[CoreNetworkConfiguration]
        ],
        segments: Union[List[Segments], core.ArrayOut[Segments]],
        attachment_policies: Optional[
            Union[List[AttachmentPolicies], core.ArrayOut[AttachmentPolicies]]
        ] = None,
        segment_actions: Optional[
            Union[List[SegmentActions], core.ArrayOut[SegmentActions]]
        ] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCoreNetworkPolicyDocument.Args(
                core_network_configuration=core_network_configuration,
                segments=segments,
                attachment_policies=attachment_policies,
                segment_actions=segment_actions,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_policies: Optional[
            Union[List[AttachmentPolicies], core.ArrayOut[AttachmentPolicies]]
        ] = core.arg(default=None)

        core_network_configuration: Union[
            List[CoreNetworkConfiguration], core.ArrayOut[CoreNetworkConfiguration]
        ] = core.arg()

        segment_actions: Optional[
            Union[List[SegmentActions], core.ArrayOut[SegmentActions]]
        ] = core.arg(default=None)

        segments: Union[List[Segments], core.ArrayOut[Segments]] = core.arg()

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
