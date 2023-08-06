from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_default_vpc_dhcp_options", namespace="aws_vpc")
class DefaultVpcDhcpOptions(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name_servers: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    netbios_name_servers: Union[str, core.StringOut] = core.attr(str, computed=True)

    netbios_node_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    ntp_servers: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        owner_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultVpcDhcpOptions.Args(
                owner_id=owner_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
