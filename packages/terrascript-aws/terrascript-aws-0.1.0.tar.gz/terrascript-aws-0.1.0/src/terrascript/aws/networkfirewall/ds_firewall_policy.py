from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class StatelessRuleGroupReference(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    rule_order: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class StatefulRuleGroupReference(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int, computed=True)

    resource_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        resource_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StatefulRuleGroupReference.Args(
                priority=priority,
                resource_arn=resource_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Union[int, core.IntOut] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Dimension(core.Schema):

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        Dimension, computed=True, kind=core.Kind.array
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

    publish_metric_action: Union[
        List[PublishMetricAction], core.ArrayOut[PublishMetricAction]
    ] = core.attr(PublishMetricAction, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        publish_metric_action: Union[List[PublishMetricAction], core.ArrayOut[PublishMetricAction]],
    ):
        super().__init__(
            args=ActionDefinition.Args(
                publish_metric_action=publish_metric_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        publish_metric_action: Union[
            List[PublishMetricAction], core.ArrayOut[PublishMetricAction]
        ] = core.arg()


@core.schema
class StatelessCustomAction(core.Schema):

    action_definition: Union[List[ActionDefinition], core.ArrayOut[ActionDefinition]] = core.attr(
        ActionDefinition, computed=True, kind=core.Kind.array
    )

    action_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        action_definition: Union[List[ActionDefinition], core.ArrayOut[ActionDefinition]],
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
        action_definition: Union[
            List[ActionDefinition], core.ArrayOut[ActionDefinition]
        ] = core.arg()

        action_name: Union[str, core.StringOut] = core.arg()


@core.schema
class FirewallPolicyBlk(core.Schema):

    stateful_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateful_engine_options: Union[
        List[StatefulEngineOptions], core.ArrayOut[StatefulEngineOptions]
    ] = core.attr(StatefulEngineOptions, computed=True, kind=core.Kind.array)

    stateful_rule_group_reference: Union[
        List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]
    ] = core.attr(StatefulRuleGroupReference, computed=True, kind=core.Kind.array)

    stateless_custom_action: Union[
        List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]
    ] = core.attr(StatelessCustomAction, computed=True, kind=core.Kind.array)

    stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateless_fragment_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    stateless_rule_group_reference: Union[
        List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]
    ] = core.attr(StatelessRuleGroupReference, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        stateful_default_actions: Union[List[str], core.ArrayOut[core.StringOut]],
        stateful_engine_options: Union[
            List[StatefulEngineOptions], core.ArrayOut[StatefulEngineOptions]
        ],
        stateful_rule_group_reference: Union[
            List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]
        ],
        stateless_custom_action: Union[
            List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]
        ],
        stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]],
        stateless_fragment_default_actions: Union[List[str], core.ArrayOut[core.StringOut]],
        stateless_rule_group_reference: Union[
            List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]
        ],
    ):
        super().__init__(
            args=FirewallPolicyBlk.Args(
                stateful_default_actions=stateful_default_actions,
                stateful_engine_options=stateful_engine_options,
                stateful_rule_group_reference=stateful_rule_group_reference,
                stateless_custom_action=stateless_custom_action,
                stateless_default_actions=stateless_default_actions,
                stateless_fragment_default_actions=stateless_fragment_default_actions,
                stateless_rule_group_reference=stateless_rule_group_reference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        stateful_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        stateful_engine_options: Union[
            List[StatefulEngineOptions], core.ArrayOut[StatefulEngineOptions]
        ] = core.arg()

        stateful_rule_group_reference: Union[
            List[StatefulRuleGroupReference], core.ArrayOut[StatefulRuleGroupReference]
        ] = core.arg()

        stateless_custom_action: Union[
            List[StatelessCustomAction], core.ArrayOut[StatelessCustomAction]
        ] = core.arg()

        stateless_default_actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        stateless_fragment_default_actions: Union[
            List[str], core.ArrayOut[core.StringOut]
        ] = core.arg()

        stateless_rule_group_reference: Union[
            List[StatelessRuleGroupReference], core.ArrayOut[StatelessRuleGroupReference]
        ] = core.arg()


@core.data(type="aws_networkfirewall_firewall_policy", namespace="aws_networkfirewall")
class DsFirewallPolicy(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    firewall_policy: Union[List[FirewallPolicyBlk], core.ArrayOut[FirewallPolicyBlk]] = core.attr(
        FirewallPolicyBlk, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

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
            args=DsFirewallPolicy.Args(
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
