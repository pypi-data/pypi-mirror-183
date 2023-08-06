from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class NotPrincipals(core.Schema):

    identifiers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        identifiers: Union[List[str], core.ArrayOut[core.StringOut]],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NotPrincipals.Args(
                identifiers=identifiers,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifiers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Principals(core.Schema):

    identifiers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        identifiers: Union[List[str], core.ArrayOut[core.StringOut]],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Principals.Args(
                identifiers=identifiers,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifiers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Condition(core.Schema):

    test: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    variable: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        test: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
        variable: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Condition.Args(
                test=test,
                values=values,
                variable=variable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        test: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        variable: Union[str, core.StringOut] = core.arg()


@core.schema
class Statement(core.Schema):

    actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = core.attr(
        Condition, default=None, kind=core.Kind.array
    )

    effect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    not_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    not_principals: Optional[Union[List[NotPrincipals], core.ArrayOut[NotPrincipals]]] = core.attr(
        NotPrincipals, default=None, kind=core.Kind.array
    )

    not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    principals: Optional[Union[List[Principals], core.ArrayOut[Principals]]] = core.attr(
        Principals, default=None, kind=core.Kind.array
    )

    resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    sid: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = None,
        effect: Optional[Union[str, core.StringOut]] = None,
        not_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        not_principals: Optional[Union[List[NotPrincipals], core.ArrayOut[NotPrincipals]]] = None,
        not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        principals: Optional[Union[List[Principals], core.ArrayOut[Principals]]] = None,
        resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        sid: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Statement.Args(
                actions=actions,
                condition=condition,
                effect=effect,
                not_actions=not_actions,
                not_principals=not_principals,
                not_resources=not_resources,
                principals=principals,
                resources=resources,
                sid=sid,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        condition: Optional[Union[List[Condition], core.ArrayOut[Condition]]] = core.arg(
            default=None
        )

        effect: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        not_actions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        not_principals: Optional[
            Union[List[NotPrincipals], core.ArrayOut[NotPrincipals]]
        ] = core.arg(default=None)

        not_resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        principals: Optional[Union[List[Principals], core.ArrayOut[Principals]]] = core.arg(
            default=None
        )

        resources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        sid: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.data(type="aws_iam_policy_document", namespace="aws_iam")
class DsPolicyDocument(core.Data):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    json: Union[str, core.StringOut] = core.attr(str, computed=True)

    override_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    override_policy_documents: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    policy_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_policy_documents: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    statement: Optional[Union[List[Statement], core.ArrayOut[Statement]]] = core.attr(
        Statement, default=None, kind=core.Kind.array
    )

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        override_json: Optional[Union[str, core.StringOut]] = None,
        override_policy_documents: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        policy_id: Optional[Union[str, core.StringOut]] = None,
        source_json: Optional[Union[str, core.StringOut]] = None,
        source_policy_documents: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        statement: Optional[Union[List[Statement], core.ArrayOut[Statement]]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPolicyDocument.Args(
                override_json=override_json,
                override_policy_documents=override_policy_documents,
                policy_id=policy_id,
                source_json=source_json,
                source_policy_documents=source_policy_documents,
                statement=statement,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        override_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        override_policy_documents: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        policy_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_policy_documents: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        statement: Optional[Union[List[Statement], core.ArrayOut[Statement]]] = core.arg(
            default=None
        )

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
