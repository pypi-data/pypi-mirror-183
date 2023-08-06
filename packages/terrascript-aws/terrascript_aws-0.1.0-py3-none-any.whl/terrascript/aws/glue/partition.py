from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SortColumns(core.Schema):

    column: Union[str, core.StringOut] = core.attr(str)

    sort_order: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        column: Union[str, core.StringOut],
        sort_order: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SortColumns.Args(
                column=column,
                sort_order=sort_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        column: Union[str, core.StringOut] = core.arg()

        sort_order: Union[int, core.IntOut] = core.arg()


@core.schema
class SkewedInfo(core.Schema):

    skewed_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skewed_column_value_location_maps: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    skewed_column_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        skewed_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        skewed_column_value_location_maps: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        skewed_column_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=SkewedInfo.Args(
                skewed_column_names=skewed_column_names,
                skewed_column_value_location_maps=skewed_column_value_location_maps,
                skewed_column_values=skewed_column_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        skewed_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        skewed_column_value_location_maps: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        skewed_column_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class SerDeInfo(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    serialization_library: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        serialization_library: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SerDeInfo.Args(
                name=name,
                parameters=parameters,
                serialization_library=serialization_library,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        serialization_library: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Columns(core.Schema):

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Columns.Args(
                name=name,
                comment=comment,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class StorageDescriptor(core.Schema):

    bucket_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    columns: Optional[Union[List[Columns], core.ArrayOut[Columns]]] = core.attr(
        Columns, default=None, kind=core.Kind.array
    )

    compressed: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    input_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    number_of_buckets: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    output_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    ser_de_info: Optional[SerDeInfo] = core.attr(SerDeInfo, default=None)

    skewed_info: Optional[SkewedInfo] = core.attr(SkewedInfo, default=None)

    sort_columns: Optional[Union[List[SortColumns], core.ArrayOut[SortColumns]]] = core.attr(
        SortColumns, default=None, kind=core.Kind.array
    )

    stored_as_sub_directories: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        bucket_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        columns: Optional[Union[List[Columns], core.ArrayOut[Columns]]] = None,
        compressed: Optional[Union[bool, core.BoolOut]] = None,
        input_format: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        number_of_buckets: Optional[Union[int, core.IntOut]] = None,
        output_format: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        ser_de_info: Optional[SerDeInfo] = None,
        skewed_info: Optional[SkewedInfo] = None,
        sort_columns: Optional[Union[List[SortColumns], core.ArrayOut[SortColumns]]] = None,
        stored_as_sub_directories: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=StorageDescriptor.Args(
                bucket_columns=bucket_columns,
                columns=columns,
                compressed=compressed,
                input_format=input_format,
                location=location,
                number_of_buckets=number_of_buckets,
                output_format=output_format,
                parameters=parameters,
                ser_de_info=ser_de_info,
                skewed_info=skewed_info,
                sort_columns=sort_columns,
                stored_as_sub_directories=stored_as_sub_directories,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        columns: Optional[Union[List[Columns], core.ArrayOut[Columns]]] = core.arg(default=None)

        compressed: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        input_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        number_of_buckets: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        output_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        ser_de_info: Optional[SerDeInfo] = core.arg(default=None)

        skewed_info: Optional[SkewedInfo] = core.arg(default=None)

        sort_columns: Optional[Union[List[SortColumns], core.ArrayOut[SortColumns]]] = core.arg(
            default=None
        )

        stored_as_sub_directories: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_glue_partition", namespace="aws_glue")
class Partition(core.Resource):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_accessed_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_analyzed_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    partition_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    storage_descriptor: Optional[StorageDescriptor] = core.attr(StorageDescriptor, default=None)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: Union[str, core.StringOut],
        partition_values: Union[List[str], core.ArrayOut[core.StringOut]],
        table_name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        storage_descriptor: Optional[StorageDescriptor] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Partition.Args(
                database_name=database_name,
                partition_values=partition_values,
                table_name=table_name,
                catalog_id=catalog_id,
                parameters=parameters,
                storage_descriptor=storage_descriptor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        partition_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        storage_descriptor: Optional[StorageDescriptor] = core.arg(default=None)

        table_name: Union[str, core.StringOut] = core.arg()
