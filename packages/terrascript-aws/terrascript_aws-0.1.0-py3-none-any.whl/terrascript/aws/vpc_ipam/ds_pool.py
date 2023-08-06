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


@core.data(type="aws_vpc_ipam_pool", namespace="aws_vpc_ipam")
class DsPool(core.Data):

    address_family: Union[str, core.StringOut] = core.attr(str, computed=True)

    allocation_default_netmask_length: Union[int, core.IntOut] = core.attr(int, computed=True)

    allocation_max_netmask_length: Union[int, core.IntOut] = core.attr(int, computed=True)

    allocation_min_netmask_length: Union[int, core.IntOut] = core.attr(int, computed=True)

    allocation_resource_tags: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, computed=True, kind=core.Kind.map)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_import: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    aws_service: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipam_pool_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipam_scope_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipam_scope_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    locale: Union[str, core.StringOut] = core.attr(str, computed=True)

    pool_depth: Union[int, core.IntOut] = core.attr(int, computed=True)

    publicly_advertisable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    source_ipam_pool_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        allocation_resource_tags: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        ipam_pool_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPool.Args(
                allocation_resource_tags=allocation_resource_tags,
                filter=filter,
                id=id,
                ipam_pool_id=ipam_pool_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_resource_tags: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipam_pool_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
