from typing import List, Union

import terrascript.core as core


@core.data(type="aws_outposts_assets", namespace="aws_outposts")
class DsAssets(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    asset_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsAssets.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()
