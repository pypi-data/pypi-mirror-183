from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ResourceUris(core.Schema):

    resource_type: Union[str, core.StringOut] = core.attr(str)

    uri: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        resource_type: Union[str, core.StringOut],
        uri: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResourceUris.Args(
                resource_type=resource_type,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource_type: Union[str, core.StringOut] = core.arg()

        uri: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_glue_user_defined_function", namespace="aws_glue")
class UserDefinedFunction(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    catalog_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    class_name: Union[str, core.StringOut] = core.attr(str)

    create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    database_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_name: Union[str, core.StringOut] = core.attr(str)

    owner_type: Union[str, core.StringOut] = core.attr(str)

    resource_uris: Optional[Union[List[ResourceUris], core.ArrayOut[ResourceUris]]] = core.attr(
        ResourceUris, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        class_name: Union[str, core.StringOut],
        database_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        owner_name: Union[str, core.StringOut],
        owner_type: Union[str, core.StringOut],
        catalog_id: Optional[Union[str, core.StringOut]] = None,
        resource_uris: Optional[Union[List[ResourceUris], core.ArrayOut[ResourceUris]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserDefinedFunction.Args(
                class_name=class_name,
                database_name=database_name,
                name=name,
                owner_name=owner_name,
                owner_type=owner_type,
                catalog_id=catalog_id,
                resource_uris=resource_uris,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        catalog_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        class_name: Union[str, core.StringOut] = core.arg()

        database_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        owner_name: Union[str, core.StringOut] = core.arg()

        owner_type: Union[str, core.StringOut] = core.arg()

        resource_uris: Optional[Union[List[ResourceUris], core.ArrayOut[ResourceUris]]] = core.arg(
            default=None
        )
