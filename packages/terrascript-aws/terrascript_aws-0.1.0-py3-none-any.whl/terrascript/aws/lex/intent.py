from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Message(core.Schema):

    content: Union[str, core.StringOut] = core.attr(str)

    content_type: Union[str, core.StringOut] = core.attr(str)

    group_number: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        content: Union[str, core.StringOut],
        content_type: Union[str, core.StringOut],
        group_number: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Message.Args(
                content=content,
                content_type=content_type,
                group_number=group_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        content: Union[str, core.StringOut] = core.arg()

        content_type: Union[str, core.StringOut] = core.arg()

        group_number: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ConfirmationPrompt(core.Schema):

    max_attempts: Union[int, core.IntOut] = core.attr(int)

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: Union[int, core.IntOut],
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConfirmationPrompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: Union[int, core.IntOut] = core.arg()

        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RejectionStatement(core.Schema):

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RejectionStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Prompt(core.Schema):

    max_attempts: Union[int, core.IntOut] = core.attr(int)

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: Union[int, core.IntOut],
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Prompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: Union[int, core.IntOut] = core.arg()

        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class FollowUpPrompt(core.Schema):

    prompt: Prompt = core.attr(Prompt)

    rejection_statement: RejectionStatement = core.attr(RejectionStatement)

    def __init__(
        self,
        *,
        prompt: Prompt,
        rejection_statement: RejectionStatement,
    ):
        super().__init__(
            args=FollowUpPrompt.Args(
                prompt=prompt,
                rejection_statement=rejection_statement,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prompt: Prompt = core.arg()

        rejection_statement: RejectionStatement = core.arg()


@core.schema
class DialogCodeHook(core.Schema):

    message_version: Union[str, core.StringOut] = core.attr(str)

    uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        message_version: Union[str, core.StringOut],
        uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DialogCodeHook.Args(
                message_version=message_version,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_version: Union[str, core.StringOut] = core.arg()

        uri: Union[str, core.StringOut] = core.arg()


@core.schema
class CodeHook(core.Schema):

    message_version: Union[str, core.StringOut] = core.attr(str)

    uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        message_version: Union[str, core.StringOut],
        uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CodeHook.Args(
                message_version=message_version,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_version: Union[str, core.StringOut] = core.arg()

        uri: Union[str, core.StringOut] = core.arg()


@core.schema
class FulfillmentActivity(core.Schema):

    code_hook: Optional[CodeHook] = core.attr(CodeHook, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        code_hook: Optional[CodeHook] = None,
    ):
        super().__init__(
            args=FulfillmentActivity.Args(
                type=type,
                code_hook=code_hook,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        code_hook: Optional[CodeHook] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class ValueElicitationPrompt(core.Schema):

    max_attempts: Union[int, core.IntOut] = core.attr(int)

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        max_attempts: Union[int, core.IntOut],
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ValueElicitationPrompt.Args(
                max_attempts=max_attempts,
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_attempts: Union[int, core.IntOut] = core.arg()

        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Slot(core.Schema):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    slot_constraint: Union[str, core.StringOut] = core.attr(str)

    slot_type: Union[str, core.StringOut] = core.attr(str)

    slot_type_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value_elicitation_prompt: Optional[ValueElicitationPrompt] = core.attr(
        ValueElicitationPrompt, default=None
    )

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        slot_constraint: Union[str, core.StringOut],
        slot_type: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[int, core.IntOut]] = None,
        response_card: Optional[Union[str, core.StringOut]] = None,
        sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        slot_type_version: Optional[Union[str, core.StringOut]] = None,
        value_elicitation_prompt: Optional[ValueElicitationPrompt] = None,
    ):
        super().__init__(
            args=Slot.Args(
                name=name,
                slot_constraint=slot_constraint,
                slot_type=slot_type,
                description=description,
                priority=priority,
                response_card=response_card,
                sample_utterances=sample_utterances,
                slot_type_version=slot_type_version,
                value_elicitation_prompt=value_elicitation_prompt,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        slot_constraint: Union[str, core.StringOut] = core.arg()

        slot_type: Union[str, core.StringOut] = core.arg()

        slot_type_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value_elicitation_prompt: Optional[ValueElicitationPrompt] = core.arg(default=None)


@core.schema
class ConclusionStatement(core.Schema):

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ConclusionStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_lex_intent", namespace="aws_lex")
class Intent(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    conclusion_statement: Optional[ConclusionStatement] = core.attr(
        ConclusionStatement, default=None
    )

    confirmation_prompt: Optional[ConfirmationPrompt] = core.attr(ConfirmationPrompt, default=None)

    create_version: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dialog_code_hook: Optional[DialogCodeHook] = core.attr(DialogCodeHook, default=None)

    follow_up_prompt: Optional[FollowUpPrompt] = core.attr(FollowUpPrompt, default=None)

    fulfillment_activity: FulfillmentActivity = core.attr(FulfillmentActivity)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parent_intent_signature: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rejection_statement: Optional[RejectionStatement] = core.attr(RejectionStatement, default=None)

    sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    slot: Optional[Union[List[Slot], core.ArrayOut[Slot]]] = core.attr(
        Slot, default=None, kind=core.Kind.array
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        fulfillment_activity: FulfillmentActivity,
        name: Union[str, core.StringOut],
        conclusion_statement: Optional[ConclusionStatement] = None,
        confirmation_prompt: Optional[ConfirmationPrompt] = None,
        create_version: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        dialog_code_hook: Optional[DialogCodeHook] = None,
        follow_up_prompt: Optional[FollowUpPrompt] = None,
        parent_intent_signature: Optional[Union[str, core.StringOut]] = None,
        rejection_statement: Optional[RejectionStatement] = None,
        sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        slot: Optional[Union[List[Slot], core.ArrayOut[Slot]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Intent.Args(
                fulfillment_activity=fulfillment_activity,
                name=name,
                conclusion_statement=conclusion_statement,
                confirmation_prompt=confirmation_prompt,
                create_version=create_version,
                description=description,
                dialog_code_hook=dialog_code_hook,
                follow_up_prompt=follow_up_prompt,
                parent_intent_signature=parent_intent_signature,
                rejection_statement=rejection_statement,
                sample_utterances=sample_utterances,
                slot=slot,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        conclusion_statement: Optional[ConclusionStatement] = core.arg(default=None)

        confirmation_prompt: Optional[ConfirmationPrompt] = core.arg(default=None)

        create_version: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dialog_code_hook: Optional[DialogCodeHook] = core.arg(default=None)

        follow_up_prompt: Optional[FollowUpPrompt] = core.arg(default=None)

        fulfillment_activity: FulfillmentActivity = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        parent_intent_signature: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rejection_statement: Optional[RejectionStatement] = core.arg(default=None)

        sample_utterances: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        slot: Optional[Union[List[Slot], core.ArrayOut[Slot]]] = core.arg(default=None)
