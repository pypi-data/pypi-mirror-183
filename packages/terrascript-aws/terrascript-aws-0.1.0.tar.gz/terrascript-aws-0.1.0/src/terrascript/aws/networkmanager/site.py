from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Location(core.Schema):

    address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    latitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    longitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: Optional[Union[str, core.StringOut]] = None,
        latitude: Optional[Union[str, core.StringOut]] = None,
        longitude: Optional[Union[str, core.StringOut]] = None,
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
        address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        latitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        longitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_networkmanager_site", namespace="aws_networkmanager")
class Site(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Optional[Location] = core.attr(Location, default=None)

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
        global_network_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Location] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Site.Args(
                global_network_id=global_network_id,
                description=description,
                location=location,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_network_id: Union[str, core.StringOut] = core.arg()

        location: Optional[Location] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
