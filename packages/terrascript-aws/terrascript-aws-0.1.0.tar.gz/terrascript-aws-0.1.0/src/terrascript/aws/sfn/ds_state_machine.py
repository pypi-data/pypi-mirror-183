from typing import Union

import terrascript.core as core


@core.data(type="aws_sfn_state_machine", namespace="aws_sfn")
class DsStateMachine(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    definition: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsStateMachine.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
