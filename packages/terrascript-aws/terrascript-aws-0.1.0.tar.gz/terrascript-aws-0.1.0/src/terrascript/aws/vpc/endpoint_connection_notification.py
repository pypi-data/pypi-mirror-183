from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_endpoint_connection_notification", namespace="aws_vpc")
class EndpointConnectionNotification(core.Resource):

    connection_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    connection_notification_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    notification_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_endpoint_service_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        connection_events: Union[List[str], core.ArrayOut[core.StringOut]],
        connection_notification_arn: Union[str, core.StringOut],
        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        vpc_endpoint_service_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=EndpointConnectionNotification.Args(
                connection_events=connection_events,
                connection_notification_arn=connection_notification_arn,
                vpc_endpoint_id=vpc_endpoint_id,
                vpc_endpoint_service_id=vpc_endpoint_service_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        connection_notification_arn: Union[str, core.StringOut] = core.arg()

        vpc_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_endpoint_service_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
