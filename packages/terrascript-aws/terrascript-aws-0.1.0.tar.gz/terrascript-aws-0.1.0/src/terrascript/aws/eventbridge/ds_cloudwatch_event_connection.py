from typing import Union

import terrascript.core as core


@core.data(type="aws_cloudwatch_event_connection", namespace="aws_eventbridge")
class DsCloudwatchEventConnection(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authorization_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    secret_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsCloudwatchEventConnection.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
