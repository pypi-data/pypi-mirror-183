from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class StatefulRuleGroupReference(core.Schema):

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_arn: Union[str, core.StringOut],
        priority: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=StatefulRuleGroupReference.Args(
                resource_arn=resource_arn,
                priority=priority,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Dimension(core.Schema):

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Dimension.Args(
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: Union[str, core.StringOut] = core.arg()


@core.schema
class PublishMetricAction(core.Schema):

    dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.attr(
        Dimension, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]],
    ):
        super().__init__(
            args=PublishMetricAction.Args(
                dimension=dimension,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dimension: Union[List[Dimension], core.ArrayOut[Dimension]] = core.arg()


@core.schema
class ActionDefinition(core.Schema):

    publish_metric_action: PublishMetricAction = core.attr(PublishMetricAction)

    def __init__(
        self,
        *,
        publish_metric_action: PublishMetricAction,
    ):
        super().__init__(
            args=ActionDefinition.Args(
                publish_metric_action=publish_metric_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        publish_metric_action: PublishMetricAction = core.arg()


@core.schema
class StatelessCustomAction(core.Schema):

    action_definition: ActionDefinition = core.attr(ActionDefinition)

    action_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action_definition: ActionDefinition,
        action_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StatelessCustomAction.Args(
                action_definition=action_definition,
                action_name=action_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_definition: ActionDefinition = core.arg()

        action_name: Union[str, core.StringOut] = core.arg()


@core.schema
class StatelessRuleGroupReference(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StatelessRuleGroupReference.Args(
                priority=priority,
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Union[int, core.IntOut] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class StatefulEngineOptions(core.Schema):

    rule_order: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        rule_order: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StatefulEngineOptions.Args(
                rule_order=rule_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_order: Union[str, core.StringOut] = core.arg()


@core.schema
class FirewallPolicyBlk(core.Schema):

    stateful_default_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    stateful_engine_options: Optional[StatefulEngineOptions] = core.attr(
        StatefulEngineOptions, default=None
    )

    stateful_rule_group_reference: Optional[
        Union[List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]]
    ] = core.attr(StatefulRuleGroupReference, default=None, kind=core.Kind.array)

    stateless_custom_action: Optional[
        Union[List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]]
    ] = core.attr(StatelessCustomAction, default=None, kind=core.Kind.array)

    stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    stateless_fragment_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    stateless_rule_group_reference: Optional[
        Union[List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]]
    ] = core.attr(StatelessRuleGroupReference, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]],
        stateless_fragment_default_actions: Union[List[str], core.ArrayOut[core.StringOut]],
        stateful_default_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        stateful_engine_options: Optional[StatefulEngineOptions] = None,
        stateful_rule_group_reference: Optional[
            Union[List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]]
        ] = None,
        stateless_custom_action: Optional[
            Union[List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]]
        ] = None,
        stateless_rule_group_reference: Optional[
            Union[List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]]
        ] = None,
    ):
        super().__init__(
            args=FirewallPolicyBlk.Args(
                stateless_default_actions=stateless_default_actions,
                stateless_fragment_default_actions=stateless_fragment_default_actions,
                stateful_default_actions=stateful_default_actions,
                stateful_engine_options=stateful_engine_options,
                stateful_rule_group_reference=stateful_rule_group_reference,
                stateless_custom_action=stateless_custom_action,
                stateless_rule_group_reference=stateless_rule_group_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stateful_default_actions: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        stateful_engine_options: Optional[StatefulEngineOptions] = core.arg(default=None)

        stateful_rule_group_reference: Optional[
            Union[List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]]
        ] = core.arg(default=None)

        stateless_custom_action: Optional[
            Union[List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]]
        ] = core.arg(default=None)

        stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        stateless_fragment_default_actions: Union[
            List[str], core.ArrayOut[core.StringOut]
        ] = core.arg()

        stateless_rule_group_reference: Optional[
            Union[List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]]
        ] = core.arg(default=None)


@core.resource(type="aws_networkfirewall_firewall_policy", namespace="aws_networkfirewall")
class FirewallPolicy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    firewall_policy: FirewallPolicyBlk = core.attr(FirewallPolicyBlk)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_policy: FirewallPolicyBlk,
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallPolicy.Args(
                firewall_policy=firewall_policy,
                name=name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        firewall_policy: FirewallPolicyBlk = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
