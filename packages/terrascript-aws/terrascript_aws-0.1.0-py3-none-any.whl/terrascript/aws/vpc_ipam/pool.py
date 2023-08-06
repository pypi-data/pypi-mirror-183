from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_ipam_pool", namespace="aws_vpc_ipam")
class Pool(core.Resource):

    address_family: Union[str, core.StringOut] = core.attr(str)

    allocation_default_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    allocation_max_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    allocation_min_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    allocation_resource_tags: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_import: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    aws_service: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipam_scope_id: Union[str, core.StringOut] = core.attr(str)

    ipam_scope_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    locale: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pool_depth: Union[int, core.IntOut] = core.attr(int, computed=True)

    publicly_advertisable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        address_family: Union[str, core.StringOut],
        ipam_scope_id: Union[str, core.StringOut],
        allocation_default_netmask_length: Optional[Union[int, core.IntOut]] = None,
        allocation_max_netmask_length: Optional[Union[int, core.IntOut]] = None,
        allocation_min_netmask_length: Optional[Union[int, core.IntOut]] = None,
        allocation_resource_tags: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        auto_import: Optional[Union[bool, core.BoolOut]] = None,
        aws_service: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        locale: Optional[Union[str, core.StringOut]] = None,
        publicly_advertisable: Optional[Union[bool, core.BoolOut]] = None,
        source_ipam_pool_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Pool.Args(
                address_family=address_family,
                ipam_scope_id=ipam_scope_id,
                allocation_default_netmask_length=allocation_default_netmask_length,
                allocation_max_netmask_length=allocation_max_netmask_length,
                allocation_min_netmask_length=allocation_min_netmask_length,
                allocation_resource_tags=allocation_resource_tags,
                auto_import=auto_import,
                aws_service=aws_service,
                description=description,
                locale=locale,
                publicly_advertisable=publicly_advertisable,
                source_ipam_pool_id=source_ipam_pool_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address_family: Union[str, core.StringOut] = core.arg()

        allocation_default_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        allocation_max_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        allocation_min_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        allocation_resource_tags: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        auto_import: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        aws_service: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipam_scope_id: Union[str, core.StringOut] = core.arg()

        locale: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        publicly_advertisable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
