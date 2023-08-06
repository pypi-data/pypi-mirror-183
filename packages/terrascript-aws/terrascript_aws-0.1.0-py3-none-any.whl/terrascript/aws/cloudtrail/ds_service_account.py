from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_cloudtrail_service_account", namespace="aws_cloudtrail")
class DsServiceAccount(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

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
            args=DsServiceAccount.Args(
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)
