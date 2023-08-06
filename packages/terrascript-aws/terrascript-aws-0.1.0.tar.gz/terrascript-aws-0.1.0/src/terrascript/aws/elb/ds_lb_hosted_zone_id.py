from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_lb_hosted_zone_id", namespace="aws_elb")
class DsLbHostedZoneId(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        load_balancer_type: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLbHostedZoneId.Args(
                load_balancer_type=load_balancer_type,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        load_balancer_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)
