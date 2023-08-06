from typing import Union

import terrascript.core as core


@core.data(type="aws_lakeformation_resource", namespace="aws_lakeformation")
class DsResource(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsResource.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()
