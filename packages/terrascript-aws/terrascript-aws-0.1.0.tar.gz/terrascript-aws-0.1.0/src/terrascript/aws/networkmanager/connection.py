from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_networkmanager_connection", namespace="aws_networkmanager")
class Connection(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connected_device_id: Union[str, core.StringOut] = core.attr(str)

    connected_link_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_id: Union[str, core.StringOut] = core.attr(str)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    link_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        connected_device_id: Union[str, core.StringOut],
        device_id: Union[str, core.StringOut],
        global_network_id: Union[str, core.StringOut],
        connected_link_id: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        link_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Connection.Args(
                connected_device_id=connected_device_id,
                device_id=device_id,
                global_network_id=global_network_id,
                connected_link_id=connected_link_id,
                description=description,
                link_id=link_id,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        connected_device_id: Union[str, core.StringOut] = core.arg()

        connected_link_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_id: Union[str, core.StringOut] = core.arg()

        global_network_id: Union[str, core.StringOut] = core.arg()

        link_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
