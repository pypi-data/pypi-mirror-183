from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_lex_bot", namespace="aws_lex")
class DsBot(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    checksum: Union[str, core.StringOut] = core.attr(str, computed=True)

    child_directed: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    detect_sentiment: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_model_improvements: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    failure_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_session_ttl_in_seconds: Union[int, core.IntOut] = core.attr(int, computed=True)

    last_updated_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    locale: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    nlu_intent_confidence_threshold: Union[float, core.FloatOut] = core.attr(float, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    voice_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBot.Args(
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
