from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Bandwidth(core.Schema):

    download_speed: Union[int, core.IntOut] = core.attr(int, computed=True)

    upload_speed: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        download_speed: Union[int, core.IntOut],
        upload_speed: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Bandwidth.Args(
                download_speed=download_speed,
                upload_speed=upload_speed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        download_speed: Union[int, core.IntOut] = core.arg()

        upload_speed: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_networkmanager_link", namespace="aws_networkmanager")
class DsLink(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bandwidth: Union[List[Bandwidth], core.ArrayOut[Bandwidth]] = core.attr(
        Bandwidth, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    link_id: Union[str, core.StringOut] = core.attr(str)

    provider_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    site_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: Union[str, core.StringOut],
        link_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsLink.Args(
                global_network_id=global_network_id,
                link_id=link_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: Union[str, core.StringOut] = core.arg()

        link_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
