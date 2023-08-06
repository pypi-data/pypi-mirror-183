from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Requester(core.Schema):

    allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = None,
        allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = None,
        allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Requester.Args(
                allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
                allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
                allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class Accepter(core.Schema):

    allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = None,
        allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = None,
        allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Accepter.Args(
                allow_classic_link_to_remote_vpc=allow_classic_link_to_remote_vpc,
                allow_remote_vpc_dns_resolution=allow_remote_vpc_dns_resolution,
                allow_vpc_to_remote_classic_link=allow_vpc_to_remote_classic_link,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allow_classic_link_to_remote_vpc: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        allow_remote_vpc_dns_resolution: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        allow_vpc_to_remote_classic_link: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_vpc_peering_connection_accepter", namespace="aws_vpc")
class PeeringConnectionAccepter(core.Resource):

    accept_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    accepter: Optional[Accepter] = core.attr(Accepter, default=None, computed=True)

    auto_accept: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    peer_vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    requester: Optional[Requester] = core.attr(Requester, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_peering_connection_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_peering_connection_id: Union[str, core.StringOut],
        accepter: Optional[Accepter] = None,
        auto_accept: Optional[Union[bool, core.BoolOut]] = None,
        requester: Optional[Requester] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PeeringConnectionAccepter.Args(
                vpc_peering_connection_id=vpc_peering_connection_id,
                accepter=accepter,
                auto_accept=auto_accept,
                requester=requester,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accepter: Optional[Accepter] = core.arg(default=None)

        auto_accept: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        requester: Optional[Requester] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_peering_connection_id: Union[str, core.StringOut] = core.arg()
