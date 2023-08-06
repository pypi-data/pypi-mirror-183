from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_sfn_activity", namespace="aws_sfn")
class DsActivity(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsActivity.Args(
                arn=arn,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
