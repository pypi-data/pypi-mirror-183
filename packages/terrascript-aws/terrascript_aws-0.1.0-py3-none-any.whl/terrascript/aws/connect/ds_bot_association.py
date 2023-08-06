from typing import Optional, Union

import terrascript.core as core


@core.schema
class LexBot(core.Schema):

    lex_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        lex_region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LexBot.Args(
                name=name,
                lex_region=lex_region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lex_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_connect_bot_association", namespace="aws_connect")
class DsBotAssociation(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The identifier of the Amazon Connect instance. You can find the instanceId in the ARN of
    the instance.
    """
    instance_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) Configuration information of an Amazon Lex (V1) bot. Detailed below.
    """
    lex_bot: LexBot = core.attr(LexBot)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        lex_bot: LexBot,
    ):
        super().__init__(
            name=data_name,
            args=DsBotAssociation.Args(
                instance_id=instance_id,
                lex_bot=lex_bot,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()

        lex_bot: LexBot = core.arg()
