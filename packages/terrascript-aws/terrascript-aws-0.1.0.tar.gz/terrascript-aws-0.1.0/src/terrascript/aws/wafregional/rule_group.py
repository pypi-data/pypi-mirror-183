from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Action(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Action.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ActivatedRule(core.Schema):

    action: Action = core.attr(Action)

    priority: Union[int, core.IntOut] = core.attr(int)

    rule_id: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: Action,
        priority: Union[int, core.IntOut],
        rule_id: Union[str, core.StringOut],
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ActivatedRule.Args(
                action=action,
                priority=priority,
                rule_id=rule_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Action = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        rule_id: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_wafregional_rule_group", namespace="aws_wafregional")
class RuleGroup(core.Resource):

    activated_rule: Optional[Union[List[ActivatedRule], core.ArrayOut[ActivatedRule]]] = core.attr(
        ActivatedRule, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    metric_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        metric_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        activated_rule: Optional[Union[List[ActivatedRule], core.ArrayOut[ActivatedRule]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RuleGroup.Args(
                metric_name=metric_name,
                name=name,
                activated_rule=activated_rule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        activated_rule: Optional[
            Union[List[ActivatedRule], core.ArrayOut[ActivatedRule]]
        ] = core.arg(default=None)

        metric_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
