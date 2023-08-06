from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Configuration(core.Schema):

    style: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        style: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Configuration.Args(
                style=style,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        style: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_location_map", namespace="aws_location")
class Map(core.Resource):

    configuration: Configuration = core.attr(Configuration)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    map_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    map_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        configuration: Configuration,
        map_name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Map.Args(
                configuration=configuration,
                map_name=map_name,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        configuration: Configuration = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        map_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
