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


@core.data(type="aws_availability_zones", namespace="aws_ec2")
class DsAvailabilityZones(core.Data):

    all_availability_zones: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    exclude_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    exclude_zone_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    group_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    zone_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        all_availability_zones: Optional[Union[bool, core.BoolOut]] = None,
        exclude_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        exclude_zone_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAvailabilityZones.Args(
                all_availability_zones=all_availability_zones,
                exclude_names=exclude_names,
                exclude_zone_ids=exclude_zone_ids,
                filter=filter,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_availability_zones: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        exclude_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        exclude_zone_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)
