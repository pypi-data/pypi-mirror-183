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
class AbortStatement(core.Schema):

    message: Union[List[Message], core.ArrayOut[Message]] = core.attr(Message, kind=core.Kind.array)

    response_card: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message: Union[List[Message], core.ArrayOut[Message]],
        response_card: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AbortStatement.Args(
                message=message,
                response_card=response_card,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message: Union[List[Message], core.ArrayOut[Message]] = core.arg()

        response_card: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ClarificationPrompt(core.Schema):

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
            args=ClarificationPrompt.Args(
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
class Intent(core.Schema):

    intent_name: Union[str, core.StringOut] = core.attr(str)

    intent_version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        intent_name: Union[str, core.StringOut],
        intent_version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Intent.Args(
                intent_name=intent_name,
                intent_version=intent_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intent_name: Union[str, core.StringOut] = core.arg()

        intent_version: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lex_bot", namespace="aws_lex")
class Bot(core.Resource):

    abort_statement: AbortStatement = core.attr(AbortStatement)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    child_directed: Union[bool, core.BoolOut] = core.attr(bool)

    clarification_prompt: Optional[ClarificationPrompt] = core.attr(
        ClarificationPrompt, default=None
    )

    create_version: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    detect_sentiment: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_model_improvements: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    failure_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_session_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    intent: Union[List[Intent], core.ArrayOut[Intent]] = core.attr(Intent, kind=core.Kind.array)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    locale: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    nlu_intent_confidence_threshold: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    process_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    voice_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        abort_statement: AbortStatement,
        child_directed: Union[bool, core.BoolOut],
        intent: Union[List[Intent], core.ArrayOut[Intent]],
        name: Union[str, core.StringOut],
        clarification_prompt: Optional[ClarificationPrompt] = None,
        create_version: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        detect_sentiment: Optional[Union[bool, core.BoolOut]] = None,
        enable_model_improvements: Optional[Union[bool, core.BoolOut]] = None,
        idle_session_ttl_in_seconds: Optional[Union[int, core.IntOut]] = None,
        locale: Optional[Union[str, core.StringOut]] = None,
        nlu_intent_confidence_threshold: Optional[Union[float, core.FloatOut]] = None,
        process_behavior: Optional[Union[str, core.StringOut]] = None,
        voice_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Bot.Args(
                abort_statement=abort_statement,
                child_directed=child_directed,
                intent=intent,
                name=name,
                clarification_prompt=clarification_prompt,
                create_version=create_version,
                description=description,
                detect_sentiment=detect_sentiment,
                enable_model_improvements=enable_model_improvements,
                idle_session_ttl_in_seconds=idle_session_ttl_in_seconds,
                locale=locale,
                nlu_intent_confidence_threshold=nlu_intent_confidence_threshold,
                process_behavior=process_behavior,
                voice_id=voice_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        abort_statement: AbortStatement = core.arg()

        child_directed: Union[bool, core.BoolOut] = core.arg()

        clarification_prompt: Optional[ClarificationPrompt] = core.arg(default=None)

        create_version: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        detect_sentiment: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_model_improvements: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        idle_session_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        intent: Union[List[Intent], core.ArrayOut[Intent]] = core.arg()

        locale: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        nlu_intent_confidence_threshold: Optional[Union[float, core.FloatOut]] = core.arg(
            default=None
        )

        process_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        voice_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
