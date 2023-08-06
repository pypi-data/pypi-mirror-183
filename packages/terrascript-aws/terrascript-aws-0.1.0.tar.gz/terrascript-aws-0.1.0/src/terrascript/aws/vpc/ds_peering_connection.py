from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CidrBlockSet(core.Schema):

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr_block: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CidrBlockSet.Args(
                cidr_block=cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: Union[str, core.StringOut] = core.arg()


@core.schema
class PeerCidrBlockSet(core.Schema):

    cidr_block: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cidr_block: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PeerCidrBlockSet.Args(
                cidr_block=cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: Union[str, core.StringOut] = core.arg()


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


@core.data(type="aws_vpc_peering_connection", namespace="aws_vpc")
class DsPeeringConnection(core.Data):

    accepter: Union[Dict[str, bool], core.MapOut[core.BoolOut]] = core.attr(
        bool, computed=True, kind=core.Kind.map
    )

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    cidr_block_set: Union[List[CidrBlockSet], core.ArrayOut[CidrBlockSet]] = core.attr(
        CidrBlockSet, computed=True, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    peer_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    peer_cidr_block_set: Union[List[PeerCidrBlockSet], core.ArrayOut[PeerCidrBlockSet]] = core.attr(
        PeerCidrBlockSet, computed=True, kind=core.Kind.array
    )

    peer_owner_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    peer_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    peer_vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    requester: Union[Dict[str, bool], core.MapOut[core.BoolOut]] = core.attr(
        bool, computed=True, kind=core.Kind.map
    )

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        owner_id: Optional[Union[str, core.StringOut]] = None,
        peer_cidr_block: Optional[Union[str, core.StringOut]] = None,
        peer_owner_id: Optional[Union[str, core.StringOut]] = None,
        peer_region: Optional[Union[str, core.StringOut]] = None,
        peer_vpc_id: Optional[Union[str, core.StringOut]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPeeringConnection.Args(
                cidr_block=cidr_block,
                filter=filter,
                id=id,
                owner_id=owner_id,
                peer_cidr_block=peer_cidr_block,
                peer_owner_id=peer_owner_id,
                peer_region=peer_region,
                peer_vpc_id=peer_vpc_id,
                region=region,
                status=status,
                tags=tags,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        peer_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        peer_owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        peer_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        peer_vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
