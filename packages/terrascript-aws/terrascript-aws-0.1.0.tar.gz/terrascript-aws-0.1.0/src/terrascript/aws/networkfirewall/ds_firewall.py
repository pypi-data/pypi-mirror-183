from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    endpoint_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint_id: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attachment.Args(
                endpoint_id=endpoint_id,
                status=status,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_id: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()


@core.schema
class SyncStates(core.Schema):

    attachment: Union[List[Attachment], core.ArrayOut[Attachment]] = core.attr(
        Attachment, computed=True, kind=core.Kind.array
    )

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment: Union[List[Attachment], core.ArrayOut[Attachment]],
        availability_zone: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SyncStates.Args(
                attachment=attachment,
                availability_zone=availability_zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment: Union[List[Attachment], core.ArrayOut[Attachment]] = core.arg()

        availability_zone: Union[str, core.StringOut] = core.arg()


@core.schema
class IpSetReferences(core.Schema):

    resolved_cidr_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        resolved_cidr_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=IpSetReferences.Args(
                resolved_cidr_count=resolved_cidr_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resolved_cidr_count: Union[int, core.IntOut] = core.arg()


@core.schema
class Cidrs(core.Schema):

    available_cidr_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    ip_set_references: Union[List[IpSetReferences], core.ArrayOut[IpSetReferences]] = core.attr(
        IpSetReferences, computed=True, kind=core.Kind.array
    )

    utilized_cidr_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        available_cidr_count: Union[int, core.IntOut],
        ip_set_references: Union[List[IpSetReferences], core.ArrayOut[IpSetReferences]],
        utilized_cidr_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Cidrs.Args(
                available_cidr_count=available_cidr_count,
                ip_set_references=ip_set_references,
                utilized_cidr_count=utilized_cidr_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        available_cidr_count: Union[int, core.IntOut] = core.arg()

        ip_set_references: Union[List[IpSetReferences], core.ArrayOut[IpSetReferences]] = core.arg()

        utilized_cidr_count: Union[int, core.IntOut] = core.arg()


@core.schema
class CapacityUsageSummary(core.Schema):

    cidrs: Union[List[Cidrs], core.ArrayOut[Cidrs]] = core.attr(
        Cidrs, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cidrs: Union[List[Cidrs], core.ArrayOut[Cidrs]],
    ):
        super().__init__(
            args=CapacityUsageSummary.Args(
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: Union[List[Cidrs], core.ArrayOut[Cidrs]] = core.arg()


@core.schema
class FirewallStatus(core.Schema):

    capacity_usage_summary: Union[
        List[CapacityUsageSummary], core.ArrayOut[CapacityUsageSummary]
    ] = core.attr(CapacityUsageSummary, computed=True, kind=core.Kind.array)

    configuration_sync_state_summary: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    sync_states: Union[List[SyncStates], core.ArrayOut[SyncStates]] = core.attr(
        SyncStates, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        capacity_usage_summary: Union[
            List[CapacityUsageSummary], core.ArrayOut[CapacityUsageSummary]
        ],
        configuration_sync_state_summary: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        sync_states: Union[List[SyncStates], core.ArrayOut[SyncStates]],
    ):
        super().__init__(
            args=FirewallStatus.Args(
                capacity_usage_summary=capacity_usage_summary,
                configuration_sync_state_summary=configuration_sync_state_summary,
                status=status,
                sync_states=sync_states,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        capacity_usage_summary: Union[
            List[CapacityUsageSummary], core.ArrayOut[CapacityUsageSummary]
        ] = core.arg()

        configuration_sync_state_summary: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        sync_states: Union[List[SyncStates], core.ArrayOut[SyncStates]] = core.arg()


@core.schema
class SubnetMapping(core.Schema):

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SubnetMapping.Args(
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_id: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptionConfiguration(core.Schema):

    key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        key_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                key_id=key_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_id: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_networkfirewall_firewall", namespace="aws_networkfirewall")
class DsFirewall(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    delete_protection: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_configuration: Union[
        List[EncryptionConfiguration], core.ArrayOut[EncryptionConfiguration]
    ] = core.attr(EncryptionConfiguration, computed=True, kind=core.Kind.array)

    firewall_policy_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    firewall_policy_change_protection: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    firewall_status: Union[List[FirewallStatus], core.ArrayOut[FirewallStatus]] = core.attr(
        FirewallStatus, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    subnet_change_protection: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    subnet_mapping: Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]] = core.attr(
        SubnetMapping, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFirewall.Args(
                arn=arn,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
