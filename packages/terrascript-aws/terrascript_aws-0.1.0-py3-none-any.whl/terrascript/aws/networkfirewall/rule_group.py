from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PortSet(core.Schema):

    definition: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        definition: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=PortSet.Args(
                definition=definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        definition: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PortSets(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    port_set: PortSet = core.attr(PortSet)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        port_set: PortSet,
    ):
        super().__init__(
            args=PortSets.Args(
                key=key,
                port_set=port_set,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        port_set: PortSet = core.arg()


@core.schema
class IpSet(core.Schema):

    definition: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        definition: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=IpSet.Args(
                definition=definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        definition: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class IpSets(core.Schema):

    ip_set: IpSet = core.attr(IpSet)

    key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        ip_set: IpSet,
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=IpSets.Args(
                ip_set=ip_set,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_set: IpSet = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.schema
class RuleVariables(core.Schema):

    ip_sets: Optional[Union[List[IpSets], core.ArrayOut[IpSets]]] = core.attr(
        IpSets, default=None, kind=core.Kind.array
    )

    port_sets: Optional[Union[List[PortSets], core.ArrayOut[PortSets]]] = core.attr(
        PortSets, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ip_sets: Optional[Union[List[IpSets], core.ArrayOut[IpSets]]] = None,
        port_sets: Optional[Union[List[PortSets], core.ArrayOut[PortSets]]] = None,
    ):
        super().__init__(
            args=RuleVariables.Args(
                ip_sets=ip_sets,
                port_sets=port_sets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip_sets: Optional[Union[List[IpSets], core.ArrayOut[IpSets]]] = core.arg(default=None)

        port_sets: Optional[Union[List[PortSets], core.ArrayOut[PortSets]]] = core.arg(default=None)


@core.schema
class RulesSourceList(core.Schema):

    generated_rules_type: Union[str, core.StringOut] = core.attr(str)

    target_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        generated_rules_type: Union[str, core.StringOut],
        target_types: Union[List[str], core.ArrayOut[core.StringOut]],
        targets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=RulesSourceList.Args(
                generated_rules_type=generated_rules_type,
                target_types=target_types,
                targets=targets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        generated_rules_type: Union[str, core.StringOut] = core.arg()

        target_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        targets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Header(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str)

    destination_port: Union[str, core.StringOut] = core.attr(str)

    direction: Union[str, core.StringOut] = core.attr(str)

    protocol: Union[str, core.StringOut] = core.attr(str)

    source: Union[str, core.StringOut] = core.attr(str)

    source_port: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination: Union[str, core.StringOut],
        destination_port: Union[str, core.StringOut],
        direction: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        source: Union[str, core.StringOut],
        source_port: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Header.Args(
                destination=destination,
                destination_port=destination_port,
                direction=direction,
                protocol=protocol,
                source=source,
                source_port=source_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[str, core.StringOut] = core.arg()

        destination_port: Union[str, core.StringOut] = core.arg()

        direction: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        source: Union[str, core.StringOut] = core.arg()

        source_port: Union[str, core.StringOut] = core.arg()


@core.schema
class RuleOption(core.Schema):

    keyword: Union[str, core.StringOut] = core.attr(str)

    settings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        keyword: Union[str, core.StringOut],
        settings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=RuleOption.Args(
                keyword=keyword,
                settings=settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        keyword: Union[str, core.StringOut] = core.arg()

        settings: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class StatefulRule(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    header: Header = core.attr(Header)

    rule_option: Union[List[RuleOption], core.ArrayOut[RuleOption]] = core.attr(
        RuleOption, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        header: Header,
        rule_option: Union[List[RuleOption], core.ArrayOut[RuleOption]],
    ):
        super().__init__(
            args=StatefulRule.Args(
                action=action,
                header=header,
                rule_option=rule_option,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        header: Header = core.arg()

        rule_option: Union[List[RuleOption], core.ArrayOut[RuleOption]] = core.arg()


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
class CustomAction(core.Schema):

    action_definition: ActionDefinition = core.attr(ActionDefinition)

    action_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action_definition: ActionDefinition,
        action_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CustomAction.Args(
                action_definition=action_definition,
                action_name=action_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action_definition: ActionDefinition = core.arg()

        action_name: Union[str, core.StringOut] = core.arg()


@core.schema
class TcpFlag(core.Schema):

    flags: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    masks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        flags: Union[List[str], core.ArrayOut[core.StringOut]],
        masks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=TcpFlag.Args(
                flags=flags,
                masks=masks,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        flags: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        masks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    address_definition: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        address_definition: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Destination.Args(
                address_definition=address_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_definition: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationPort(core.Schema):

    from_port: Union[int, core.IntOut] = core.attr(int)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        to_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DestinationPort.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Union[int, core.IntOut] = core.arg()

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Source(core.Schema):

    address_definition: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        address_definition: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Source.Args(
                address_definition=address_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address_definition: Union[str, core.StringOut] = core.arg()


@core.schema
class SourcePort(core.Schema):

    from_port: Union[int, core.IntOut] = core.attr(int)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        to_port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SourcePort.Args(
                from_port=from_port,
                to_port=to_port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        from_port: Union[int, core.IntOut] = core.arg()

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class MatchAttributes(core.Schema):

    destination: Optional[Union[List[Destination], core.ArrayOut[Destination]]] = core.attr(
        Destination, default=None, kind=core.Kind.array
    )

    destination_port: Optional[
        Union[List[DestinationPort], core.ArrayOut[DestinationPort]]
    ] = core.attr(DestinationPort, default=None, kind=core.Kind.array)

    protocols: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.attr(
        int, default=None, kind=core.Kind.array
    )

    source: Optional[Union[List[Source], core.ArrayOut[Source]]] = core.attr(
        Source, default=None, kind=core.Kind.array
    )

    source_port: Optional[Union[List[SourcePort], core.ArrayOut[SourcePort]]] = core.attr(
        SourcePort, default=None, kind=core.Kind.array
    )

    tcp_flag: Optional[Union[List[TcpFlag], core.ArrayOut[TcpFlag]]] = core.attr(
        TcpFlag, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        destination: Optional[Union[List[Destination], core.ArrayOut[Destination]]] = None,
        destination_port: Optional[
            Union[List[DestinationPort], core.ArrayOut[DestinationPort]]
        ] = None,
        protocols: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = None,
        source: Optional[Union[List[Source], core.ArrayOut[Source]]] = None,
        source_port: Optional[Union[List[SourcePort], core.ArrayOut[SourcePort]]] = None,
        tcp_flag: Optional[Union[List[TcpFlag], core.ArrayOut[TcpFlag]]] = None,
    ):
        super().__init__(
            args=MatchAttributes.Args(
                destination=destination,
                destination_port=destination_port,
                protocols=protocols,
                source=source,
                source_port=source_port,
                tcp_flag=tcp_flag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Optional[Union[List[Destination], core.ArrayOut[Destination]]] = core.arg(
            default=None
        )

        destination_port: Optional[
            Union[List[DestinationPort], core.ArrayOut[DestinationPort]]
        ] = core.arg(default=None)

        protocols: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.arg(default=None)

        source: Optional[Union[List[Source], core.ArrayOut[Source]]] = core.arg(default=None)

        source_port: Optional[Union[List[SourcePort], core.ArrayOut[SourcePort]]] = core.arg(
            default=None
        )

        tcp_flag: Optional[Union[List[TcpFlag], core.ArrayOut[TcpFlag]]] = core.arg(default=None)


@core.schema
class RuleDefinition(core.Schema):

    actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    match_attributes: MatchAttributes = core.attr(MatchAttributes)

    def __init__(
        self,
        *,
        actions: Union[List[str], core.ArrayOut[core.StringOut]],
        match_attributes: MatchAttributes,
    ):
        super().__init__(
            args=RuleDefinition.Args(
                actions=actions,
                match_attributes=match_attributes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        match_attributes: MatchAttributes = core.arg()


@core.schema
class StatelessRule(core.Schema):

    priority: Union[int, core.IntOut] = core.attr(int)

    rule_definition: RuleDefinition = core.attr(RuleDefinition)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        rule_definition: RuleDefinition,
    ):
        super().__init__(
            args=StatelessRule.Args(
                priority=priority,
                rule_definition=rule_definition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        priority: Union[int, core.IntOut] = core.arg()

        rule_definition: RuleDefinition = core.arg()


@core.schema
class StatelessRulesAndCustomActions(core.Schema):

    custom_action: Optional[Union[List[CustomAction], core.ArrayOut[CustomAction]]] = core.attr(
        CustomAction, default=None, kind=core.Kind.array
    )

    stateless_rule: Union[List[StatelessRule], core.ArrayOut[StatelessRule]] = core.attr(
        StatelessRule, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        stateless_rule: Union[List[StatelessRule], core.ArrayOut[StatelessRule]],
        custom_action: Optional[Union[List[CustomAction], core.ArrayOut[CustomAction]]] = None,
    ):
        super().__init__(
            args=StatelessRulesAndCustomActions.Args(
                stateless_rule=stateless_rule,
                custom_action=custom_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_action: Optional[Union[List[CustomAction], core.ArrayOut[CustomAction]]] = core.arg(
            default=None
        )

        stateless_rule: Union[List[StatelessRule], core.ArrayOut[StatelessRule]] = core.arg()


@core.schema
class RulesSource(core.Schema):

    rules_source_list: Optional[RulesSourceList] = core.attr(RulesSourceList, default=None)

    rules_string: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stateful_rule: Optional[Union[List[StatefulRule], core.ArrayOut[StatefulRule]]] = core.attr(
        StatefulRule, default=None, kind=core.Kind.array
    )

    stateless_rules_and_custom_actions: Optional[StatelessRulesAndCustomActions] = core.attr(
        StatelessRulesAndCustomActions, default=None
    )

    def __init__(
        self,
        *,
        rules_source_list: Optional[RulesSourceList] = None,
        rules_string: Optional[Union[str, core.StringOut]] = None,
        stateful_rule: Optional[Union[List[StatefulRule], core.ArrayOut[StatefulRule]]] = None,
        stateless_rules_and_custom_actions: Optional[StatelessRulesAndCustomActions] = None,
    ):
        super().__init__(
            args=RulesSource.Args(
                rules_source_list=rules_source_list,
                rules_string=rules_string,
                stateful_rule=stateful_rule,
                stateless_rules_and_custom_actions=stateless_rules_and_custom_actions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rules_source_list: Optional[RulesSourceList] = core.arg(default=None)

        rules_string: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stateful_rule: Optional[Union[List[StatefulRule], core.ArrayOut[StatefulRule]]] = core.arg(
            default=None
        )

        stateless_rules_and_custom_actions: Optional[StatelessRulesAndCustomActions] = core.arg(
            default=None
        )


@core.schema
class StatefulRuleOptions(core.Schema):

    rule_order: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        rule_order: Union[str, core.StringOut],
    ):
        super().__init__(
            args=StatefulRuleOptions.Args(
                rule_order=rule_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_order: Union[str, core.StringOut] = core.arg()


@core.schema
class RuleGroupBlk(core.Schema):

    rule_variables: Optional[RuleVariables] = core.attr(RuleVariables, default=None)

    rules_source: RulesSource = core.attr(RulesSource)

    stateful_rule_options: Optional[StatefulRuleOptions] = core.attr(
        StatefulRuleOptions, default=None
    )

    def __init__(
        self,
        *,
        rules_source: RulesSource,
        rule_variables: Optional[RuleVariables] = None,
        stateful_rule_options: Optional[StatefulRuleOptions] = None,
    ):
        super().__init__(
            args=RuleGroupBlk.Args(
                rules_source=rules_source,
                rule_variables=rule_variables,
                stateful_rule_options=stateful_rule_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule_variables: Optional[RuleVariables] = core.arg(default=None)

        rules_source: RulesSource = core.arg()

        stateful_rule_options: Optional[StatefulRuleOptions] = core.arg(default=None)


@core.resource(type="aws_networkfirewall_rule_group", namespace="aws_networkfirewall")
class RuleGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity: Union[int, core.IntOut] = core.attr(int)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule_group: Optional[RuleGroupBlk] = core.attr(RuleGroupBlk, default=None, computed=True)

    rules: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    update_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        capacity: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        rule_group: Optional[RuleGroupBlk] = None,
        rules: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RuleGroup.Args(
                capacity=capacity,
                name=name,
                type=type,
                description=description,
                rule_group=rule_group,
                rules=rules,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity: Union[int, core.IntOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        rule_group: Optional[RuleGroupBlk] = core.arg(default=None)

        rules: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
