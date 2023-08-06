from typing import Union

import terrascript.core as core


@core.data(type="aws_connect_prompt", namespace="aws_connect")
class DsPrompt(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    prompt_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsPrompt.Args(
                instance_id=instance_id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
