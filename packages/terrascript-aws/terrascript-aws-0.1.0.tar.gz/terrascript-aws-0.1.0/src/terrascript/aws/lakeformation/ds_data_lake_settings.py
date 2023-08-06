from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CreateDatabaseDefaultPermissions(core.Schema):

    permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    principal: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        permissions: Union[List[str], core.ArrayOut[core.StringOut]],
        principal: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CreateDatabaseDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        principal: Union[str, core.StringOut] = core.arg()


@core.schema
class CreateTableDefaultPermissions(core.Schema):

    permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    principal: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        permissions: Union[List[str], core.ArrayOut[core.StringOut]],
        principal: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CreateTableDefaultPermissions.Args(
                permissions=permissions,
                principal=principal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        principal: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_lakeformation_data_lake_settings", namespace="aws_lakeformation")
class DsDataLakeSettings(core.Data):

    admins: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    create_database_default_permissions: Union[
        List[CreateDatabaseDefaultPermissions], core.ArrayOut[CreateDatabaseDefaultPermissions]
    ] = core.attr(CreateDatabaseDefaultPermissions, computed=True, kind=core.Kind.array)

    create_table_default_permissions: Union[
        List[CreateTableDefaultPermissions], core.ArrayOut[CreateTableDefaultPermissions]
    ] = core.attr(CreateTableDefaultPermissions, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    trusted_resource_owners: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        catalog_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDataLakeSettings.Args(
                catalog_id=catalog_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
