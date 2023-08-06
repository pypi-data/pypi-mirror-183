from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_archive", namespace="aws_eventbridge")
class CloudwatchEventArchive(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    event_source_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    retention_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        event_source_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        event_pattern: Optional[Union[str, core.StringOut]] = None,
        retention_days: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventArchive.Args(
                event_source_arn=event_source_arn,
                name=name,
                description=description,
                event_pattern=event_pattern,
                retention_days=retention_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        event_source_arn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        retention_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)
