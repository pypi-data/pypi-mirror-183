from typing import List, Optional, Union

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


@core.data(type="aws_ami_ids", namespace="aws_ec2")
class DsAmiIds(core.Data):

    executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    name_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owners: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    sort_ascending: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        owners: Union[List[str], core.ArrayOut[core.StringOut]],
        executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        name_regex: Optional[Union[str, core.StringOut]] = None,
        sort_ascending: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAmiIds.Args(
                owners=owners,
                executable_users=executable_users,
                filter=filter,
                name_regex=name_regex,
                sort_ascending=sort_ascending,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        name_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owners: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        sort_ascending: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
