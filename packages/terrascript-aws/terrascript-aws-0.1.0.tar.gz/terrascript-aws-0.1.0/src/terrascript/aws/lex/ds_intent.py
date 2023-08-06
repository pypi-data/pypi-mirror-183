from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_lex_intent", namespace="aws_lex")
class DsIntent(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parent_intent_signature: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIntent.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
