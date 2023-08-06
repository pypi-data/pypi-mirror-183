from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_guardduty_detector", namespace="aws_guardduty")
class DsDetector(core.Data):

    finding_publishing_frequency: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    service_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDetector.Args(
                id=id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
