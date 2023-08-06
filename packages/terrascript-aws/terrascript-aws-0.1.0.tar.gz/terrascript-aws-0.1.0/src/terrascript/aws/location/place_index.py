from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DataSourceConfiguration(core.Schema):

    intended_use: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        intended_use: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DataSourceConfiguration.Args(
                intended_use=intended_use,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intended_use: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_location_place_index", namespace="aws_location")
class PlaceIndex(core.Resource):

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_source: Union[str, core.StringOut] = core.attr(str)

    data_source_configuration: Optional[DataSourceConfiguration] = core.attr(
        DataSourceConfiguration, default=None, computed=True
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_name: Union[str, core.StringOut] = core.attr(str)

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
        data_source: Union[str, core.StringOut],
        index_name: Union[str, core.StringOut],
        data_source_configuration: Optional[DataSourceConfiguration] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PlaceIndex.Args(
                data_source=data_source,
                index_name=index_name,
                data_source_configuration=data_source_configuration,
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
        data_source: Union[str, core.StringOut] = core.arg()

        data_source_configuration: Optional[DataSourceConfiguration] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
