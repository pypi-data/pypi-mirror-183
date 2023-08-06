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


@core.schema
class DataLocation(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DataLocation.Args(
                arn=arn,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Expression(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Expression.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class LfTagPolicy(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    expression: Union[List[Expression], core.ArrayOut[Expression]] = core.attr(
        Expression, kind=core.Kind.array
    )

    resource_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        expression: Union[List[Expression], core.ArrayOut[Expression]],
        resource_type: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LfTagPolicy.Args(
                expression=expression,
                resource_type=resource_type,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expression: Union[List[Expression], core.ArrayOut[Expression]] = core.arg()

        resource_type: Union[str, core.StringOut] = core.arg()


@core.schema
class LfTag(core.Schema):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LfTag.Args(
                key=key,
                values=values,
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_lakeformation_permissions", namespace="aws_lakeformation")
class Permissions(core.Resource):

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    catalog_resource: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    data_location: Optional[DataLocation] = core.attr(DataLocation, default=None, computed=True)

    database: Optional[Database] = core.attr(Database, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lf_tag: Optional[LfTag] = core.attr(LfTag, default=None, computed=True)

    lf_tag_policy: Optional[LfTagPolicy] = core.attr(LfTagPolicy, default=None, computed=True)

    permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    permissions_with_grant_option: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, computed=True, kind=core.Kind.array)

    principal: Union[str, core.StringOut] = core.attr(str)

    table: Optional[Table] = core.attr(Table, default=None, computed=True)

    table_with_columns: Optional[TableWithColumns] = core.attr(
        TableWithColumns, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        permissions: Union[List[str], core.ArrayOut[core.StringOut]],
        principal: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        catalog_resource: Optional[Union[bool, core.BoolOut]] = None,
        data_location: Optional[DataLocation] = None,
        database: Optional[Database] = None,
        lf_tag: Optional[LfTag] = None,
        lf_tag_policy: Optional[LfTagPolicy] = None,
        permissions_with_grant_option: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        table: Optional[Table] = None,
        table_with_columns: Optional[TableWithColumns] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Permissions.Args(
                permissions=permissions,
                principal=principal,
                catalog_id=catalog_id,
                catalog_resource=catalog_resource,
                data_location=data_location,
                database=database,
                lf_tag=lf_tag,
                lf_tag_policy=lf_tag_policy,
                permissions_with_grant_option=permissions_with_grant_option,
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

        catalog_resource: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        data_location: Optional[DataLocation] = core.arg(default=None)

        database: Optional[Database] = core.arg(default=None)

        lf_tag: Optional[LfTag] = core.arg(default=None)

        lf_tag_policy: Optional[LfTagPolicy] = core.arg(default=None)

        permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        permissions_with_grant_option: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        principal: Union[str, core.StringOut] = core.arg()

        table: Optional[Table] = core.arg(default=None)

        table_with_columns: Optional[TableWithColumns] = core.arg(default=None)
