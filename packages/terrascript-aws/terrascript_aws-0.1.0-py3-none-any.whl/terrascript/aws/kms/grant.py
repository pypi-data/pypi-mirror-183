from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Constraints(core.Schema):

    encryption_context_equals: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    encryption_context_subset: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    def __init__(
        self,
        *,
        encryption_context_equals: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        encryption_context_subset: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=Constraints.Args(
                encryption_context_equals=encryption_context_equals,
                encryption_context_subset=encryption_context_subset,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_context_equals: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        encryption_context_subset: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)


@core.resource(type="aws_kms_grant", namespace="aws_kms")
class Grant(core.Resource):

    constraints: Optional[Union[List[Constraints], core.ArrayOut[Constraints]]] = core.attr(
        Constraints, default=None, kind=core.Kind.array
    )

    grant_creation_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    grant_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    grant_token: Union[str, core.StringOut] = core.attr(str, computed=True)

    grantee_principal: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_id: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operations: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    retire_on_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    retiring_principal: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        grantee_principal: Union[str, core.StringOut],
        key_id: Union[str, core.StringOut],
        operations: Union[List[str], core.ArrayOut[core.StringOut]],
        constraints: Optional[Union[List[Constraints], core.ArrayOut[Constraints]]] = None,
        grant_creation_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        retire_on_delete: Optional[Union[bool, core.BoolOut]] = None,
        retiring_principal: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Grant.Args(
                grantee_principal=grantee_principal,
                key_id=key_id,
                operations=operations,
                constraints=constraints,
                grant_creation_tokens=grant_creation_tokens,
                name=name,
                retire_on_delete=retire_on_delete,
                retiring_principal=retiring_principal,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        constraints: Optional[Union[List[Constraints], core.ArrayOut[Constraints]]] = core.arg(
            default=None
        )

        grant_creation_tokens: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        grantee_principal: Union[str, core.StringOut] = core.arg()

        key_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operations: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        retire_on_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        retiring_principal: Optional[Union[str, core.StringOut]] = core.arg(default=None)
