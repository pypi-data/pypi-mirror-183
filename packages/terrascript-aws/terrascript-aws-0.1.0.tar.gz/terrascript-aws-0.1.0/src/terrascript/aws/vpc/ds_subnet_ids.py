from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_subnet_ids", namespace="aws_vpc")
class DsSubnetIds(core.Data):

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        data_name: str,
        *,
        vpc_id: Union[str, core.StringOut],
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSubnetIds.Args(
                vpc_id=vpc_id,
                filter=filter,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Union[str, core.StringOut] = core.arg()
