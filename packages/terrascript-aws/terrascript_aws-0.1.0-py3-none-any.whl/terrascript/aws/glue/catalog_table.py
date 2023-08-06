from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TargetTable(core.Schema):

    catalog_id: Union[str, core.StringOut] = core.attr(str)

    database_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        catalog_id: Union[str, core.StringOut],
        database_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetTable.Args(
                catalog_id=catalog_id,
                database_name=database_name,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Union[str, core.StringOut] = core.arg()

        database_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class PartitionIndex(core.Schema):

    index_name: Union[str, core.StringOut] = core.attr(str)

    index_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    keys: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        index_name: Union[str, core.StringOut],
        index_status: Union[str, core.StringOut],
        keys: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=PartitionIndex.Args(
                index_name=index_name,
                index_status=index_status,
                keys=keys,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        index_name: Union[str, core.StringOut] = core.arg()

        index_status: Union[str, core.StringOut] = core.arg()

        keys: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PartitionKeys(core.Schema):

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
            args=PartitionKeys.Args(
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
class SchemaId(core.Schema):

    registry_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schema_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schema_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        registry_name: Optional[Union[str, core.StringOut]] = None,
        schema_arn: Optional[Union[str, core.StringOut]] = None,
        schema_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SchemaId.Args(
                registry_name=registry_name,
                schema_arn=schema_arn,
                schema_name=schema_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        registry_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SchemaReference(core.Schema):

    schema_id: Optional[SchemaId] = core.attr(SchemaId, default=None)

    schema_version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schema_version_number: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        schema_version_number: Union[int, core.IntOut],
        schema_id: Optional[SchemaId] = None,
        schema_version_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SchemaReference.Args(
                schema_version_number=schema_version_number,
                schema_id=schema_id,
                schema_version_id=schema_version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        schema_id: Optional[SchemaId] = core.arg(default=None)

        schema_version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schema_version_number: Union[int, core.IntOut] = core.arg()


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

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        comment: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Columns.Args(
                name=name,
                comment=comment,
                parameters=parameters,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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
class StorageDescriptor(core.Schema):

    bucket_columns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    columns: Optional[Union[List[Columns], core.ArrayOut[Columns]]] = core.attr(
        Columns, default=None, computed=True, kind=core.Kind.array
    )

    compressed: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    input_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    number_of_buckets: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    output_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    schema_reference: Optional[SchemaReference] = core.attr(SchemaReference, default=None)

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
        schema_reference: Optional[SchemaReference] = None,
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
                schema_reference=schema_reference,
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

        schema_reference: Optional[SchemaReference] = core.arg(default=None)

        ser_de_info: Optional[SerDeInfo] = core.arg(default=None)

        skewed_info: Optional[SkewedInfo] = core.arg(default=None)

        sort_columns: Optional[Union[List[SortColumns], core.ArrayOut[SortColumns]]] = core.arg(
            default=None
        )

        stored_as_sub_directories: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_glue_catalog_table", namespace="aws_glue")
class CatalogTable(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    partition_index: Optional[
        Union[List[PartitionIndex], core.ArrayOut[PartitionIndex]]
    ] = core.attr(PartitionIndex, default=None, computed=True, kind=core.Kind.array)

    partition_keys: Optional[Union[List[PartitionKeys], core.ArrayOut[PartitionKeys]]] = core.attr(
        PartitionKeys, default=None, kind=core.Kind.array
    )

    retention: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    storage_descriptor: Optional[StorageDescriptor] = core.attr(StorageDescriptor, default=None)

    table_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_table: Optional[TargetTable] = core.attr(TargetTable, default=None)

    view_expanded_text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    view_original_text: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        database_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        owner: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        partition_index: Optional[
            Union[List[PartitionIndex], core.ArrayOut[PartitionIndex]]
        ] = None,
        partition_keys: Optional[Union[List[PartitionKeys], core.ArrayOut[PartitionKeys]]] = None,
        retention: Optional[Union[int, core.IntOut]] = None,
        storage_descriptor: Optional[StorageDescriptor] = None,
        table_type: Optional[Union[str, core.StringOut]] = None,
        target_table: Optional[TargetTable] = None,
        view_expanded_text: Optional[Union[str, core.StringOut]] = None,
        view_original_text: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CatalogTable.Args(
                database_name=database_name,
                name=name,
                catalog_id=catalog_id,
                description=description,
                owner=owner,
                parameters=parameters,
                partition_index=partition_index,
                partition_keys=partition_keys,
                retention=retention,
                storage_descriptor=storage_descriptor,
                table_type=table_type,
                target_table=target_table,
                view_expanded_text=view_expanded_text,
                view_original_text=view_original_text,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        partition_index: Optional[
            Union[List[PartitionIndex], core.ArrayOut[PartitionIndex]]
        ] = core.arg(default=None)

        partition_keys: Optional[
            Union[List[PartitionKeys], core.ArrayOut[PartitionKeys]]
        ] = core.arg(default=None)

        retention: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_descriptor: Optional[StorageDescriptor] = core.arg(default=None)

        table_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_table: Optional[TargetTable] = core.arg(default=None)

        view_expanded_text: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        view_original_text: Optional[Union[str, core.StringOut]] = core.arg(default=None)
