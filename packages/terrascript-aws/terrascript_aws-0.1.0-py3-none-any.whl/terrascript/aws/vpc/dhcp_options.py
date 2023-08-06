from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_dhcp_options", namespace="aws_vpc")
class DhcpOptions(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    netbios_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    netbios_node_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ntp_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        domain_name: Optional[Union[str, core.StringOut]] = None,
        domain_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        netbios_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        netbios_node_type: Optional[Union[str, core.StringOut]] = None,
        ntp_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DhcpOptions.Args(
                domain_name=domain_name,
                domain_name_servers=domain_name_servers,
                netbios_name_servers=netbios_name_servers,
                netbios_node_type=netbios_node_type,
                ntp_servers=ntp_servers,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        netbios_name_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        netbios_node_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ntp_servers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
