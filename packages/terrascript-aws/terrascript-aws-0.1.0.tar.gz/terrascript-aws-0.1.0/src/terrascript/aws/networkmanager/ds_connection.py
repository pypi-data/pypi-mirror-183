from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_networkmanager_connection", namespace="aws_networkmanager")
class DsConnection(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    connected_device_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    connected_link_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    connection_id: Union[str, core.StringOut] = core.attr(str)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    link_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        connection_id: Union[str, core.StringOut],
        global_network_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConnection.Args(
                connection_id=connection_id,
                global_network_id=global_network_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connection_id: Union[str, core.StringOut] = core.arg()

        global_network_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
