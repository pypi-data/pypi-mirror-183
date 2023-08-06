from typing import List, Union

import terrascript.core as core


@core.data(type="aws_dx_locations", namespace="aws_direct_connect")
class DsDxLocations(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location_codes: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
    ):
        super().__init__(
            name=data_name,
            args=DsDxLocations.Args(),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ...
