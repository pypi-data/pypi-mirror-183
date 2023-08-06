from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Database(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Database.Args(
                name=name,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class LfTag(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LfTag.Args(
                key=key,
                value=value,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Table(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    wildcard: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        wildcard: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Table.Args(
                database_name=database_name,
                catalog_id=catalog_id,
                name=name,
                wildcard=wildcard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database_name: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        wildcard: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class TableWithColumns(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    database_name: Union[str, core.StringOut] = core.attr(str)

    excluded_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    wildcard: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        excluded_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        wildcard: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=TableWithColumns.Args(
                database_name=database_name,
                name=name,
                catalog_id=catalog_id,
                column_names=column_names,
                excluded_column_names=excluded_column_names,
                wildcard=wildcard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        database_name: Union[str, core.StringOut] = core.arg()

        excluded_column_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        wildcard: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_lakeformation_resource_lf_tags", namespace="aws_lakeformation")
class ResourceLfTags(core.Resource):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    database: Optional[Database] = core.attr(Database, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lf_tag: Union[List[LfTag], core.ArrayOut[LfTag]] = core.attr(LfTag, kind=core.Kind.array)

    table: Optional[Table] = core.attr(Table, default=None, computed=True)

    table_with_columns: Optional[TableWithColumns] = core.attr(
        TableWithColumns, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        lf_tag: Union[List[LfTag], core.ArrayOut[LfTag]],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        database: Optional[Database] = None,
        table: Optional[Table] = None,
        table_with_columns: Optional[TableWithColumns] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceLfTags.Args(
                lf_tag=lf_tag,
                catalog_id=catalog_id,
                database=database,
                table=table,
                table_with_columns=table_with_columns,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        database: Optional[Database] = core.arg(default=None)

        lf_tag: Union[List[LfTag], core.ArrayOut[LfTag]] = core.arg()

        table: Optional[Table] = core.arg(default=None)

        table_with_columns: Optional[TableWithColumns] = core.arg(default=None)
