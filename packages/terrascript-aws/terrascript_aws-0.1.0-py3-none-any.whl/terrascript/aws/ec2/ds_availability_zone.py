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


@core.data(type="aws_availability_zone", namespace="aws_ec2")
class DsAvailabilityZone(core.Data):

    all_availability_zones: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_suffix: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_border_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    opt_in_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_zone_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zone_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zone_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        all_availability_zones: Optional[Union[bool, core.BoolOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        zone_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAvailabilityZone.Args(
                all_availability_zones=all_availability_zones,
                filter=filter,
                name=name,
                state=state,
                zone_id=zone_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        all_availability_zones: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
