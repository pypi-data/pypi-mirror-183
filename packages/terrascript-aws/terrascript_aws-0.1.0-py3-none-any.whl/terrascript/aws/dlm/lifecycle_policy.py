from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EncryptionConfiguration(core.Schema):

    cmk_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cmk_arn: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                cmk_arn=cmk_arn,
                encrypted=encrypted,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cmk_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class CrossRegionCopyRetainRule(core.Schema):

    interval: Union[int, core.IntOut] = core.attr(int)

    interval_unit: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        interval: Union[int, core.IntOut],
        interval_unit: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CrossRegionCopyRetainRule.Args(
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: Union[int, core.IntOut] = core.arg()

        interval_unit: Union[str, core.StringOut] = core.arg()


@core.schema
class CrossRegionCopy(core.Schema):

    encryption_configuration: EncryptionConfiguration = core.attr(EncryptionConfiguration)

    retain_rule: Optional[CrossRegionCopyRetainRule] = core.attr(
        CrossRegionCopyRetainRule, default=None
    )

    target: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        encryption_configuration: EncryptionConfiguration,
        target: Union[str, core.StringOut],
        retain_rule: Optional[CrossRegionCopyRetainRule] = None,
    ):
        super().__init__(
            args=CrossRegionCopy.Args(
                encryption_configuration=encryption_configuration,
                target=target,
                retain_rule=retain_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_configuration: EncryptionConfiguration = core.arg()

        retain_rule: Optional[CrossRegionCopyRetainRule] = core.arg(default=None)

        target: Union[str, core.StringOut] = core.arg()


@core.schema
class Action(core.Schema):

    cross_region_copy: Union[List[CrossRegionCopy], core.ArrayOut[CrossRegionCopy]] = core.attr(
        CrossRegionCopy, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cross_region_copy: Union[List[CrossRegionCopy], core.ArrayOut[CrossRegionCopy]],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Action.Args(
                cross_region_copy=cross_region_copy,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cross_region_copy: Union[List[CrossRegionCopy], core.ArrayOut[CrossRegionCopy]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class EventSourceParameters(core.Schema):

    description_regex: Union[str, core.StringOut] = core.attr(str)

    event_type: Union[str, core.StringOut] = core.attr(str)

    snapshot_owner: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        description_regex: Union[str, core.StringOut],
        event_type: Union[str, core.StringOut],
        snapshot_owner: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=EventSourceParameters.Args(
                description_regex=description_regex,
                event_type=event_type,
                snapshot_owner=snapshot_owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description_regex: Union[str, core.StringOut] = core.arg()

        event_type: Union[str, core.StringOut] = core.arg()

        snapshot_owner: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class EventSource(core.Schema):

    parameters: EventSourceParameters = core.attr(EventSourceParameters)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        parameters: EventSourceParameters,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EventSource.Args(
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        parameters: EventSourceParameters = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class PolicyDetailsParameters(core.Schema):

    exclude_boot_volume: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    no_reboot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        exclude_boot_volume: Optional[Union[bool, core.BoolOut]] = None,
        no_reboot: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=PolicyDetailsParameters.Args(
                exclude_boot_volume=exclude_boot_volume,
                no_reboot=no_reboot,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        exclude_boot_volume: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        no_reboot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class CreateRule(core.Schema):

    cron_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval_unit: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    times: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        cron_expression: Optional[Union[str, core.StringOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        interval_unit: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        times: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=CreateRule.Args(
                cron_expression=cron_expression,
                interval=interval,
                interval_unit=interval_unit,
                location=location,
                times=times,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cron_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        times: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class FastRestoreRule(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        count: Optional[Union[int, core.IntOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        interval_unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FastRestoreRule.Args(
                availability_zones=availability_zones,
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ShareRule(core.Schema):

    target_accounts: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    unshare_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    unshare_interval_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        target_accounts: Union[List[str], core.ArrayOut[core.StringOut]],
        unshare_interval: Optional[Union[int, core.IntOut]] = None,
        unshare_interval_unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ShareRule.Args(
                target_accounts=target_accounts,
                unshare_interval=unshare_interval,
                unshare_interval_unit=unshare_interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_accounts: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        unshare_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        unshare_interval_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ScheduleRetainRule(core.Schema):

    count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        count: Optional[Union[int, core.IntOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        interval_unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScheduleRetainRule.Args(
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CrossRegionCopyRuleDeprecateRule(core.Schema):

    interval: Union[int, core.IntOut] = core.attr(int)

    interval_unit: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        interval: Union[int, core.IntOut],
        interval_unit: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CrossRegionCopyRuleDeprecateRule.Args(
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        interval: Union[int, core.IntOut] = core.arg()

        interval_unit: Union[str, core.StringOut] = core.arg()


@core.schema
class CrossRegionCopyRule(core.Schema):

    cmk_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    deprecate_rule: Optional[CrossRegionCopyRuleDeprecateRule] = core.attr(
        CrossRegionCopyRuleDeprecateRule, default=None
    )

    encrypted: Union[bool, core.BoolOut] = core.attr(bool)

    retain_rule: Optional[CrossRegionCopyRetainRule] = core.attr(
        CrossRegionCopyRetainRule, default=None
    )

    target: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        encrypted: Union[bool, core.BoolOut],
        target: Union[str, core.StringOut],
        cmk_arn: Optional[Union[str, core.StringOut]] = None,
        copy_tags: Optional[Union[bool, core.BoolOut]] = None,
        deprecate_rule: Optional[CrossRegionCopyRuleDeprecateRule] = None,
        retain_rule: Optional[CrossRegionCopyRetainRule] = None,
    ):
        super().__init__(
            args=CrossRegionCopyRule.Args(
                encrypted=encrypted,
                target=target,
                cmk_arn=cmk_arn,
                copy_tags=copy_tags,
                deprecate_rule=deprecate_rule,
                retain_rule=retain_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cmk_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        deprecate_rule: Optional[CrossRegionCopyRuleDeprecateRule] = core.arg(default=None)

        encrypted: Union[bool, core.BoolOut] = core.arg()

        retain_rule: Optional[CrossRegionCopyRetainRule] = core.arg(default=None)

        target: Union[str, core.StringOut] = core.arg()


@core.schema
class ScheduleDeprecateRule(core.Schema):

    count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    interval_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        count: Optional[Union[int, core.IntOut]] = None,
        interval: Optional[Union[int, core.IntOut]] = None,
        interval_unit: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScheduleDeprecateRule.Args(
                count=count,
                interval=interval,
                interval_unit=interval_unit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        interval_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Schedule(core.Schema):

    copy_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    create_rule: CreateRule = core.attr(CreateRule)

    cross_region_copy_rule: Optional[
        Union[List[CrossRegionCopyRule], core.ArrayOut[CrossRegionCopyRule]]
    ] = core.attr(CrossRegionCopyRule, default=None, kind=core.Kind.array)

    deprecate_rule: Optional[ScheduleDeprecateRule] = core.attr(ScheduleDeprecateRule, default=None)

    fast_restore_rule: Optional[FastRestoreRule] = core.attr(FastRestoreRule, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    retain_rule: ScheduleRetainRule = core.attr(ScheduleRetainRule)

    share_rule: Optional[ShareRule] = core.attr(ShareRule, default=None)

    tags_to_add: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    variable_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        create_rule: CreateRule,
        name: Union[str, core.StringOut],
        retain_rule: ScheduleRetainRule,
        copy_tags: Optional[Union[bool, core.BoolOut]] = None,
        cross_region_copy_rule: Optional[
            Union[List[CrossRegionCopyRule], core.ArrayOut[CrossRegionCopyRule]]
        ] = None,
        deprecate_rule: Optional[ScheduleDeprecateRule] = None,
        fast_restore_rule: Optional[FastRestoreRule] = None,
        share_rule: Optional[ShareRule] = None,
        tags_to_add: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        variable_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Schedule.Args(
                create_rule=create_rule,
                name=name,
                retain_rule=retain_rule,
                copy_tags=copy_tags,
                cross_region_copy_rule=cross_region_copy_rule,
                deprecate_rule=deprecate_rule,
                fast_restore_rule=fast_restore_rule,
                share_rule=share_rule,
                tags_to_add=tags_to_add,
                variable_tags=variable_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        create_rule: CreateRule = core.arg()

        cross_region_copy_rule: Optional[
            Union[List[CrossRegionCopyRule], core.ArrayOut[CrossRegionCopyRule]]
        ] = core.arg(default=None)

        deprecate_rule: Optional[ScheduleDeprecateRule] = core.arg(default=None)

        fast_restore_rule: Optional[FastRestoreRule] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        retain_rule: ScheduleRetainRule = core.arg()

        share_rule: Optional[ShareRule] = core.arg(default=None)

        tags_to_add: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        variable_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class PolicyDetails(core.Schema):

    action: Optional[Action] = core.attr(Action, default=None)

    event_source: Optional[EventSource] = core.attr(EventSource, default=None)

    parameters: Optional[PolicyDetailsParameters] = core.attr(PolicyDetailsParameters, default=None)

    policy_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    schedule: Optional[Union[List[Schedule], core.ArrayOut[Schedule]]] = core.attr(
        Schedule, default=None, kind=core.Kind.array
    )

    target_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        action: Optional[Action] = None,
        event_source: Optional[EventSource] = None,
        parameters: Optional[PolicyDetailsParameters] = None,
        policy_type: Optional[Union[str, core.StringOut]] = None,
        resource_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        schedule: Optional[Union[List[Schedule], core.ArrayOut[Schedule]]] = None,
        target_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=PolicyDetails.Args(
                action=action,
                event_source=event_source,
                parameters=parameters,
                policy_type=policy_type,
                resource_locations=resource_locations,
                resource_types=resource_types,
                schedule=schedule,
                target_tags=target_tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Optional[Action] = core.arg(default=None)

        event_source: Optional[EventSource] = core.arg(default=None)

        parameters: Optional[PolicyDetailsParameters] = core.arg(default=None)

        policy_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_locations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        resource_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        schedule: Optional[Union[List[Schedule], core.ArrayOut[Schedule]]] = core.arg(default=None)

        target_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_dlm_lifecycle_policy", namespace="aws_dlm")
class LifecyclePolicy(core.Resource):
    """
    Amazon Resource Name (ARN) of the DLM Lifecycle Policy.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) A description for the DLM lifecycle policy.
    """
    description: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The ARN of an IAM role that is able to be assumed by the DLM service.
    """
    execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    """
    Identifier of the DLM Lifecycle Policy.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) See the [`policy_details` configuration](#policy-details-arguments) block. Max of 1.
    """
    policy_details: PolicyDetails = core.attr(PolicyDetails)

    """
    (Optional) Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are v
    alid values. Defaults to `ENABLED`.
    """
    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        description: Union[str, core.StringOut],
        execution_role_arn: Union[str, core.StringOut],
        policy_details: PolicyDetails,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LifecyclePolicy.Args(
                description=description,
                execution_role_arn=execution_role_arn,
                policy_details=policy_details,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Union[str, core.StringOut] = core.arg()

        execution_role_arn: Union[str, core.StringOut] = core.arg()

        policy_details: PolicyDetails = core.arg()

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
