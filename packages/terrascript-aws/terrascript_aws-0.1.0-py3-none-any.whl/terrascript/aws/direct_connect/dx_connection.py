from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_connection", namespace="aws_direct_connect")
class DxConnection(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    bandwidth: Union[str, core.StringOut] = core.attr(str)

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
        bandwidth: Union[str, core.StringOut],
        location: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        provider_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxConnection.Args(
                bandwidth=bandwidth,
                location=location,
                name=name,
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
        bandwidth: Union[str, core.StringOut] = core.arg()

        location: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        provider_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
