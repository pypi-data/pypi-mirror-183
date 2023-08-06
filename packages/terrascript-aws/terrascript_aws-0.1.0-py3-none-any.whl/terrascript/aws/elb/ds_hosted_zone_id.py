from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_elb_hosted_zone_id", namespace="aws_elb")
class DsHostedZoneId(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        region: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsHostedZoneId.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)
