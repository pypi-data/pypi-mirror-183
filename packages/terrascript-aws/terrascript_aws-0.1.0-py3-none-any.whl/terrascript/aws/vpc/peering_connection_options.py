from typing import List, Optional, Union

import terrascript.core as core


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


@core.resource(type="aws_vpc_peering_connection_options", namespace="aws_vpc")
class PeeringConnectionOptions(core.Resource):

    accepter: Optional[Accepter] = core.attr(Accepter, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    requester: Optional[Requester] = core.attr(Requester, default=None, computed=True)

    vpc_peering_connection_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_peering_connection_id: Union[str, core.StringOut],
        accepter: Optional[Accepter] = None,
        requester: Optional[Requester] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PeeringConnectionOptions.Args(
                vpc_peering_connection_id=vpc_peering_connection_id,
                accepter=accepter,
                requester=requester,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accepter: Optional[Accepter] = core.arg(default=None)

        requester: Optional[Requester] = core.arg(default=None)

        vpc_peering_connection_id: Union[str, core.StringOut] = core.arg()
