from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CidrBlockAssociations(core.Schema):

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        association_id: Union[str, core.StringOut],
        cidr_block: Union[str, core.StringOut],
        state: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CidrBlockAssociations.Args(
                association_id=association_id,
                cidr_block=cidr_block,
                state=state,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        association_id: Union[str, core.StringOut] = core.arg()

        cidr_block: Union[str, core.StringOut] = core.arg()

        state: Union[str, core.StringOut] = core.arg()


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


@core.data(type="aws_vpc", namespace="aws_vpc")
class DsMain(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cidr_block_associations: Union[
        List[CidrBlockAssociations], core.ArrayOut[CidrBlockAssociations]
    ] = core.attr(CidrBlockAssociations, computed=True, kind=core.Kind.array)

    default: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    dhcp_options_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    enable_dns_hostnames: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_dns_support: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    instance_tenancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    main_route_table_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        default: Optional[Union[bool, core.BoolOut]] = None,
        dhcp_options_id: Optional[Union[str, core.StringOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMain.Args(
                cidr_block=cidr_block,
                default=default,
                dhcp_options_id=dhcp_options_id,
                filter=filter,
                id=id,
                state=state,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        dhcp_options_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
