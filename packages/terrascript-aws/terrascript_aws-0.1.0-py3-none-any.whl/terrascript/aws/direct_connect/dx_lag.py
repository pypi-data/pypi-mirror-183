from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_lag", namespace="aws_direct_connect")
class DxLag(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    connections_bandwidth: Union[str, core.StringOut] = core.attr(str)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    has_logical_redundancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    jumbo_frame_capable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    location: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    provider_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

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
        connections_bandwidth: Union[str, core.StringOut],
        location: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        connection_id: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        provider_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxLag.Args(
                connections_bandwidth=connections_bandwidth,
                location=location,
                name=name,
                connection_id=connection_id,
                force_destroy=force_destroy,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connection_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connections_bandwidth: Union[str, core.StringOut] = core.arg()

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        provider_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
