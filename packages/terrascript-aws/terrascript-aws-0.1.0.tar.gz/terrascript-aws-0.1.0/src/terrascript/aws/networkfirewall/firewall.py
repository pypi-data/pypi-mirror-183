from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    endpoint_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        endpoint_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attachment.Args(
                endpoint_id=endpoint_id,
                subnet_id=subnet_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_id: Union[str, core.StringOut] = core.arg()

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
class FirewallStatus(core.Schema):

    sync_states: Union[List[SyncStates], core.ArrayOut[SyncStates]] = core.attr(
        SyncStates, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        sync_states: Union[List[SyncStates], core.ArrayOut[SyncStates]],
    ):
        super().__init__(
            args=FirewallStatus.Args(
                sync_states=sync_states,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
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


@core.resource(type="aws_networkfirewall_firewall", namespace="aws_networkfirewall")
class Firewall(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delete_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    firewall_policy_arn: Union[str, core.StringOut] = core.attr(str)

    firewall_policy_change_protection: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    firewall_status: Union[List[FirewallStatus], core.ArrayOut[FirewallStatus]] = core.attr(
        FirewallStatus, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    subnet_change_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    subnet_mapping: Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]] = core.attr(
        SubnetMapping, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_policy_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        subnet_mapping: Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]],
        vpc_id: Union[str, core.StringOut],
        delete_protection: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        firewall_policy_change_protection: Optional[Union[bool, core.BoolOut]] = None,
        subnet_change_protection: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Firewall.Args(
                firewall_policy_arn=firewall_policy_arn,
                name=name,
                subnet_mapping=subnet_mapping,
                vpc_id=vpc_id,
                delete_protection=delete_protection,
                description=description,
                firewall_policy_change_protection=firewall_policy_change_protection,
                subnet_change_protection=subnet_change_protection,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delete_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        firewall_policy_arn: Union[str, core.StringOut] = core.arg()

        firewall_policy_change_protection: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        subnet_change_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        subnet_mapping: Union[List[SubnetMapping], core.ArrayOut[SubnetMapping]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Union[str, core.StringOut] = core.arg()
