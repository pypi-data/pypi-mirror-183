from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DataSourceConfiguration(core.Schema):

    intended_use: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        intended_use: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DataSourceConfiguration.Args(
                intended_use=intended_use,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        intended_use: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_location_place_index", namespace="aws_location")
class DsPlaceIndex(core.Data):

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_source: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_source_configuration: Union[
        List[DataSourceConfiguration], core.ArrayOut[DataSourceConfiguration]
    ] = core.attr(DataSourceConfiguration, computed=True, kind=core.Kind.array)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    update_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        index_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPlaceIndex.Args(
                index_name=index_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
