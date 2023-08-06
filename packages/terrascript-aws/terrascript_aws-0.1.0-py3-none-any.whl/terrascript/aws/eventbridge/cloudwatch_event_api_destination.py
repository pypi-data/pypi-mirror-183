from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_api_destination", namespace="aws_eventbridge")
class CloudwatchEventApiDestination(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_arn: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_method: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invocation_endpoint: Union[str, core.StringOut] = core.attr(str)

    invocation_rate_limit_per_second: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_arn: Union[str, core.StringOut],
        http_method: Union[str, core.StringOut],
        invocation_endpoint: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        invocation_rate_limit_per_second: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventApiDestination.Args(
                connection_arn=connection_arn,
                http_method=http_method,
                invocation_endpoint=invocation_endpoint,
                name=name,
                description=description,
                invocation_rate_limit_per_second=invocation_rate_limit_per_second,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_arn: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_method: Union[str, core.StringOut] = core.arg()

        invocation_endpoint: Union[str, core.StringOut] = core.arg()

        invocation_rate_limit_per_second: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
