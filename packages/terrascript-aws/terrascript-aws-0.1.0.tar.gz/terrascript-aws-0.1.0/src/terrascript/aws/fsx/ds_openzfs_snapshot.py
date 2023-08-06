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


@core.data(type="aws_fsx_openzfs_snapshot", namespace="aws_fsx")
class DsOpenzfsSnapshot(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        snapshot_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsOpenzfsSnapshot.Args(
                filter=filter,
                most_recent=most_recent,
                name=name,
                snapshot_ids=snapshot_ids,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
