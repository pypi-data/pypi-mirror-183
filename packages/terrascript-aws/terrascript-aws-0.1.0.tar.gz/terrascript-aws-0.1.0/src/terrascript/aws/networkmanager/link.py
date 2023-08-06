from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Bandwidth(core.Schema):

    download_speed: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    upload_speed: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        download_speed: Optional[Union[int, core.IntOut]] = None,
        upload_speed: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Bandwidth.Args(
                download_speed=download_speed,
                upload_speed=upload_speed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        download_speed: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        upload_speed: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_networkmanager_link", namespace="aws_networkmanager")
class Link(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bandwidth: Bandwidth = core.attr(Bandwidth)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    provider_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    site_id: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: Bandwidth,
        global_network_id: Union[str, core.StringOut],
        site_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        provider_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Link.Args(
                bandwidth=bandwidth,
                global_network_id=global_network_id,
                site_id=site_id,
                description=description,
                provider_name=provider_name,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: Bandwidth = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_network_id: Union[str, core.StringOut] = core.arg()

        provider_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        site_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
