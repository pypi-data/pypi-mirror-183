from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Principal(core.Schema):

    data_lake_principal_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        data_lake_principal_identifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Principal.Args(
                data_lake_principal_identifier=data_lake_principal_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        data_lake_principal_identifier: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class CreateTableDefaultPermission(core.Schema):

    permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    principal: Optional[Principal] = core.attr(Principal, default=None)

    def __init__(
        self,
        *,
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        principal: Optional[Principal] = None,
    ):
        super().__init__(
            args=CreateTableDefaultPermission.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        principal: Optional[Principal] = core.arg(default=None)


@core.schema
class TargetDatabase(core.Schema):

    catalog_id: Union[str, core.StringOut] = core.attr(str)

    database_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        catalog_id: Union[str, core.StringOut],
        database_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetDatabase.Args(
                catalog_id=catalog_id,
                database_name=database_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Union[str, core.StringOut] = core.arg()

        database_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_glue_catalog_database", namespace="aws_glue")
class CatalogDatabase(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    create_table_default_permission: Optional[
        Union[List[CreateTableDefaultPermission], core.ArrayOut[CreateTableDefaultPermission]]
    ] = core.attr(CreateTableDefaultPermission, default=None, computed=True, kind=core.Kind.array)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    target_database: Optional[TargetDatabase] = core.attr(TargetDatabase, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        create_table_default_permission: Optional[
            Union[List[CreateTableDefaultPermission], core.ArrayOut[CreateTableDefaultPermission]]
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        location_uri: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_database: Optional[TargetDatabase] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CatalogDatabase.Args(
                name=name,
                catalog_id=catalog_id,
                create_table_default_permission=create_table_default_permission,
                description=description,
                location_uri=location_uri,
                parameters=parameters,
                target_database=target_database,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        create_table_default_permission: Optional[
            Union[List[CreateTableDefaultPermission], core.ArrayOut[CreateTableDefaultPermission]]
        ] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_database: Optional[TargetDatabase] = core.arg(default=None)
