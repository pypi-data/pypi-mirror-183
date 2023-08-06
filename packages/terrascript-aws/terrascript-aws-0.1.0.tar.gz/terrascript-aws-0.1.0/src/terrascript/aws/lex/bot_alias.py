from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class LogSettings(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_type: Union[str, core.StringOut] = core.attr(str)

    resource_arn: Union[str, core.StringOut] = core.attr(str)

    resource_prefix: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        destination: Union[str, core.StringOut],
        log_type: Union[str, core.StringOut],
        resource_arn: Union[str, core.StringOut],
        resource_prefix: Union[str, core.StringOut],
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LogSettings.Args(
                destination=destination,
                log_type=log_type,
                resource_arn=resource_arn,
                resource_prefix=resource_prefix,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[str, core.StringOut] = core.arg()

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_type: Union[str, core.StringOut] = core.arg()

        resource_arn: Union[str, core.StringOut] = core.arg()

        resource_prefix: Union[str, core.StringOut] = core.arg()


@core.schema
class ConversationLogs(core.Schema):

    iam_role_arn: Union[str, core.StringOut] = core.attr(str)

    log_settings: Optional[Union[List[LogSettings], core.ArrayOut[LogSettings]]] = core.attr(
        LogSettings, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        iam_role_arn: Union[str, core.StringOut],
        log_settings: Optional[Union[List[LogSettings], core.ArrayOut[LogSettings]]] = None,
    ):
        super().__init__(
            args=ConversationLogs.Args(
                iam_role_arn=iam_role_arn,
                log_settings=log_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam_role_arn: Union[str, core.StringOut] = core.arg()

        log_settings: Optional[Union[List[LogSettings], core.ArrayOut[LogSettings]]] = core.arg(
            default=None
        )


@core.resource(type="aws_lex_bot_alias", namespace="aws_lex")
class BotAlias(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bot_name: Union[str, core.StringOut] = core.attr(str)

    bot_version: Union[str, core.StringOut] = core.attr(str)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    conversation_logs: Optional[ConversationLogs] = core.attr(ConversationLogs, default=None)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        bot_name: Union[str, core.StringOut],
        bot_version: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        conversation_logs: Optional[ConversationLogs] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BotAlias.Args(
                bot_name=bot_name,
                bot_version=bot_version,
                name=name,
                conversation_logs=conversation_logs,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bot_name: Union[str, core.StringOut] = core.arg()

        bot_version: Union[str, core.StringOut] = core.arg()

        conversation_logs: Optional[ConversationLogs] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
