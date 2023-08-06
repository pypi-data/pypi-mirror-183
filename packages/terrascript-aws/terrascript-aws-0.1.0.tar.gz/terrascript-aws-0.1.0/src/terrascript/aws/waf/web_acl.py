from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DefaultAction(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DefaultAction.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


@core.schema
class FieldToMatch(core.Schema):

    data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        data: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FieldToMatch.Args(
                type=type,
                data=data,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class RedactedFields(core.Schema):

    field_to_match: Union[List[FieldToMatch], core.ArrayOut[FieldToMatch]] = core.attr(
        FieldToMatch, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        field_to_match: Union[List[FieldToMatch], core.ArrayOut[FieldToMatch]],
    ):
        super().__init__(
            args=RedactedFields.Args(
                field_to_match=field_to_match,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        field_to_match: Union[List[FieldToMatch], core.ArrayOut[FieldToMatch]] = core.arg()


@core.schema
class LoggingConfiguration(core.Schema):

    log_destination: Union[str, core.StringOut] = core.attr(str)

    redacted_fields: Optional[RedactedFields] = core.attr(RedactedFields, default=None)

    def __init__(
        self,
        *,
        log_destination: Union[str, core.StringOut],
        redacted_fields: Optional[RedactedFields] = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                log_destination=log_destination,
                redacted_fields=redacted_fields,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        log_destination: Union[str, core.StringOut] = core.arg()

        redacted_fields: Optional[RedactedFields] = core.arg(default=None)


@core.schema
class OverrideAction(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OverrideAction.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()


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
class Rules(core.Schema):

    action: Optional[Action] = core.attr(Action, default=None)

    override_action: Optional[OverrideAction] = core.attr(OverrideAction, default=None)

    priority: Union[int, core.IntOut] = core.attr(int)

    rule_id: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        priority: Union[int, core.IntOut],
        rule_id: Union[str, core.StringOut],
        action: Optional[Action] = None,
        override_action: Optional[OverrideAction] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rules.Args(
                priority=priority,
                rule_id=rule_id,
                action=action,
                override_action=override_action,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Optional[Action] = core.arg(default=None)

        override_action: Optional[OverrideAction] = core.arg(default=None)

        priority: Union[int, core.IntOut] = core.arg()

        rule_id: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_waf_web_acl", namespace="aws_waf")
class WebAcl(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_action: DefaultAction = core.attr(DefaultAction)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    logging_configuration: Optional[LoggingConfiguration] = core.attr(
        LoggingConfiguration, default=None
    )

    metric_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = core.attr(
        Rules, default=None, kind=core.Kind.array
    )

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
        default_action: DefaultAction,
        metric_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        logging_configuration: Optional[LoggingConfiguration] = None,
        rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WebAcl.Args(
                default_action=default_action,
                metric_name=metric_name,
                name=name,
                logging_configuration=logging_configuration,
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
        default_action: DefaultAction = core.arg()

        logging_configuration: Optional[LoggingConfiguration] = core.arg(default=None)

        metric_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        rules: Optional[Union[List[Rules], core.ArrayOut[Rules]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
