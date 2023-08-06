from typing import Union

import terrascript.core as core


@core.data(type="aws_lex_bot_alias", namespace="aws_lex")
class DsBotAlias(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bot_name: Union[str, core.StringOut] = core.attr(str)

    bot_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        bot_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsBotAlias.Args(
                bot_name=bot_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bot_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
