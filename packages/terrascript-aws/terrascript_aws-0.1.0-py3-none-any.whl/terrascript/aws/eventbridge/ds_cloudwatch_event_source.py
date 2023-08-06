from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_cloudwatch_event_source", namespace="aws_eventbridge")
class DsCloudwatchEventSource(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCloudwatchEventSource.Args(
                name_prefix=name_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)
