from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Configuration(core.Schema):

    style: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_location_map", namespace="aws_location")
class DsMap(core.Data):

    configuration: Union[List[Configuration], core.ArrayOut[Configuration]] = core.attr(
        Configuration, computed=True, kind=core.Kind.array
    )

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    map_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    map_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        map_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMap.Args(
                map_name=map_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        map_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
