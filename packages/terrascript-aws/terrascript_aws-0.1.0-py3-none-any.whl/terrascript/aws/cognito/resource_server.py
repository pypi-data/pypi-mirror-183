from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Scope(core.Schema):

    scope_description: Union[str, core.StringOut] = core.attr(str)

    scope_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        scope_description: Union[str, core.StringOut],
        scope_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Scope.Args(
                scope_description=scope_description,
                scope_name=scope_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        scope_description: Union[str, core.StringOut] = core.arg()

        scope_name: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cognito_resource_server", namespace="aws_cognito")
class ResourceServer(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) An identifier for the resource server.
    """
    identifier: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) A name for the resource server.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) A list of [Authorization Scope](#authorization-scope).
    """
    scope: Optional[Union[List[Scope], core.ArrayOut[Scope]]] = core.attr(
        Scope, default=None, kind=core.Kind.array
    )

    """
    A list of all scopes configured for this resource server in the format identifier/scope_name.
    """
    scope_identifiers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        identifier: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        scope: Optional[Union[List[Scope], core.ArrayOut[Scope]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceServer.Args(
                identifier=identifier,
                name=name,
                user_pool_id=user_pool_id,
                scope=scope,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identifier: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        scope: Optional[Union[List[Scope], core.ArrayOut[Scope]]] = core.arg(default=None)

        user_pool_id: Union[str, core.StringOut] = core.arg()
