from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_outposts_outpost", namespace="aws_outposts")
class DsOutpost(core.Data):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    site_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        owner_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutpost.Args(
                arn=arn,
                id=id,
                name=name,
                owner_id=owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
