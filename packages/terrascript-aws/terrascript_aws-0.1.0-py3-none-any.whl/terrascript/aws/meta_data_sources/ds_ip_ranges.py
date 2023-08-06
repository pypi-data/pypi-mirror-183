from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_ip_ranges", namespace="aws_meta_data_sources")
class DsIpRanges(core.Data):

    cidr_blocks: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    create_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_blocks: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    services: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    sync_token: Union[int, core.IntOut] = core.attr(int, computed=True)

    url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        services: Union[List[str], core.ArrayOut[core.StringOut]],
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        url: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsIpRanges.Args(
                services=services,
                regions=regions,
                url=url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        services: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        url: Optional[Union[str, core.StringOut]] = core.arg(default=None)
