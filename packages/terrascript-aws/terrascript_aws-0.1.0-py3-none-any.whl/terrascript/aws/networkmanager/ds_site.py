from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Location(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    latitude: Union[str, core.StringOut] = core.attr(str, computed=True)

    longitude: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        latitude: Union[str, core.StringOut],
        longitude: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Location.Args(
                address=address,
                latitude=latitude,
                longitude=longitude,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        latitude: Union[str, core.StringOut] = core.arg()

        longitude: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_networkmanager_site", namespace="aws_networkmanager")
class DsSite(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[List[Location], core.ArrayOut[Location]] = core.attr(
        Location, computed=True, kind=core.Kind.array
    )

    site_id: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        global_network_id: Union[str, core.StringOut],
        site_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsSite.Args(
                global_network_id=global_network_id,
                site_id=site_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        global_network_id: Union[str, core.StringOut] = core.arg()

        site_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
