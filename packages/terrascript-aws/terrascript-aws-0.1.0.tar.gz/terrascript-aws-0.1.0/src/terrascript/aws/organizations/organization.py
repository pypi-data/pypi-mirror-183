from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class NonMasterAccounts(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    email: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NonMasterAccounts.Args(
                arn=arn,
                email=email,
                id=id,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        email: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class Accounts(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    email: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        email: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Accounts.Args(
                arn=arn,
                email=email,
                id=id,
                name=name,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        email: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class PolicyTypes(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PolicyTypes.Args(
                status=status,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Roots(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy_types: Union[List[PolicyTypes], core.ArrayOut[PolicyTypes]] = core.attr(
        PolicyTypes, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        policy_types: Union[List[PolicyTypes], core.ArrayOut[PolicyTypes]],
    ):
        super().__init__(
            args=Roots.Args(
                arn=arn,
                id=id,
                name=name,
                policy_types=policy_types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        policy_types: Union[List[PolicyTypes], core.ArrayOut[PolicyTypes]] = core.arg()


@core.resource(type="aws_organizations_organization", namespace="aws_organizations")
class Organization(core.Resource):

    accounts: Union[List[Accounts], core.ArrayOut[Accounts]] = core.attr(
        Accounts, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_service_access_principals: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    enabled_policy_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    feature_set: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_account_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_account_email: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    non_master_accounts: Union[
        List[NonMasterAccounts], core.ArrayOut[NonMasterAccounts]
    ] = core.attr(NonMasterAccounts, computed=True, kind=core.Kind.array)

    roots: Union[List[Roots], core.ArrayOut[Roots]] = core.attr(
        Roots, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        aws_service_access_principals: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        enabled_policy_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        feature_set: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Organization.Args(
                aws_service_access_principals=aws_service_access_principals,
                enabled_policy_types=enabled_policy_types,
                feature_set=feature_set,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_service_access_principals: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        enabled_policy_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        feature_set: Optional[Union[str, core.StringOut]] = core.arg(default=None)
