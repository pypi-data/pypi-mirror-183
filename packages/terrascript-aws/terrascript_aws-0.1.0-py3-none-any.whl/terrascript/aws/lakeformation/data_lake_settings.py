from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CreateDatabaseDefaultPermissions(core.Schema):

    permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        principal: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CreateDatabaseDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CreateTableDefaultPermissions(core.Schema):

    permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        principal: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CreateTableDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_lakeformation_data_lake_settings", namespace="aws_lakeformation")
class DataLakeSettings(core.Resource):

    admins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    create_database_default_permissions: Optional[
        Union[
            List[CreateDatabaseDefaultPermissions], core.ArrayOut[CreateDatabaseDefaultPermissions]
        ]
    ] = core.attr(
        CreateDatabaseDefaultPermissions, default=None, computed=True, kind=core.Kind.array
    )

    create_table_default_permissions: Optional[
        Union[List[CreateTableDefaultPermissions], core.ArrayOut[CreateTableDefaultPermissions]]
    ] = core.attr(CreateTableDefaultPermissions, default=None, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    trusted_resource_owners: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        admins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        create_database_default_permissions: Optional[
            Union[
                List[CreateDatabaseDefaultPermissions],
                core.ArrayOut[CreateDatabaseDefaultPermissions],
            ]
        ] = None,
        create_table_default_permissions: Optional[
            Union[List[CreateTableDefaultPermissions], core.ArrayOut[CreateTableDefaultPermissions]]
        ] = None,
        trusted_resource_owners: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DataLakeSettings.Args(
                admins=admins,
                catalog_id=catalog_id,
                create_database_default_permissions=create_database_default_permissions,
                create_table_default_permissions=create_table_default_permissions,
                trusted_resource_owners=trusted_resource_owners,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admins: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        create_database_default_permissions: Optional[
            Union[
                List[CreateDatabaseDefaultPermissions],
                core.ArrayOut[CreateDatabaseDefaultPermissions],
            ]
        ] = core.arg(default=None)

        create_table_default_permissions: Optional[
            Union[List[CreateTableDefaultPermissions], core.ArrayOut[CreateTableDefaultPermissions]]
        ] = core.arg(default=None)

        trusted_resource_owners: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
