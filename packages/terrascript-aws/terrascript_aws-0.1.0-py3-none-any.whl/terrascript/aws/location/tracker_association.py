from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_location_tracker_association", namespace="aws_location")
class TrackerAssociation(core.Resource):

    consumer_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tracker_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        consumer_arn: Union[str, core.StringOut],
        tracker_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrackerAssociation.Args(
                consumer_arn=consumer_arn,
                tracker_name=tracker_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        consumer_arn: Union[str, core.StringOut] = core.arg()

        tracker_name: Union[str, core.StringOut] = core.arg()
