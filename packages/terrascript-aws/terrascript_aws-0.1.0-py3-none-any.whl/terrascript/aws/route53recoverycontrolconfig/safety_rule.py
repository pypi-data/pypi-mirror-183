from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class RuleConfig(core.Schema):

    inverted: Union[bool, core.BoolOut] = core.attr(bool)

    threshold: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        inverted: Union[bool, core.BoolOut],
        threshold: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RuleConfig.Args(
                inverted=inverted,
                threshold=threshold,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        inverted: Union[bool, core.BoolOut] = core.arg()

        threshold: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(
    type="aws_route53recoverycontrolconfig_safety_rule",
    namespace="aws_route53recoverycontrolconfig",
)
class SafetyRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    asserted_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    control_panel_arn: Union[str, core.StringOut] = core.attr(str)

    gating_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rule_config: RuleConfig = core.attr(RuleConfig)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    wait_period_ms: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        control_panel_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        rule_config: RuleConfig,
        wait_period_ms: Union[int, core.IntOut],
        asserted_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        gating_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        target_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SafetyRule.Args(
                control_panel_arn=control_panel_arn,
                name=name,
                rule_config=rule_config,
                wait_period_ms=wait_period_ms,
                asserted_controls=asserted_controls,
                gating_controls=gating_controls,
                target_controls=target_controls,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        asserted_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        control_panel_arn: Union[str, core.StringOut] = core.arg()

        gating_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        rule_config: RuleConfig = core.arg()

        target_controls: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        wait_period_ms: Union[int, core.IntOut] = core.arg()
