from typing import Union

import terrascript.core as core


@core.data(type="aws_outposts_asset", namespace="aws_outposts")
class DsAsset(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    asset_id: Union[str, core.StringOut] = core.attr(str)

    asset_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    host_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rack_elevation: Union[int, core.IntOut] = core.attr(int, computed=True)

    rack_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        asset_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsAsset.Args(
                arn=arn,
                asset_id=asset_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        asset_id: Union[str, core.StringOut] = core.arg()
