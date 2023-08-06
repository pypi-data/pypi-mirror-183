from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_event_bus_policy", namespace="aws_eventbridge")
class CloudwatchEventBusPolicy(core.Resource):

    event_bus_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        event_bus_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventBusPolicy.Args(
                policy=policy,
                event_bus_name=event_bus_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        event_bus_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Union[str, core.StringOut] = core.arg()
