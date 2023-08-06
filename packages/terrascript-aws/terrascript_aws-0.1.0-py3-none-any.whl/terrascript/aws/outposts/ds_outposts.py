from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_outposts_outposts", namespace="aws_outposts")
class DsOutposts(core.Data):

    arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    availability_zone_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    site_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        availability_zone_id: Optional[Union[str, core.StringOut]] = None,
        owner_id: Optional[Union[str, core.StringOut]] = None,
        site_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOutposts.Args(
                availability_zone=availability_zone,
                availability_zone_id=availability_zone_id,
                owner_id=owner_id,
                site_id=site_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        availability_zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        site_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
