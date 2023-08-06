from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class MappingRule(core.Schema):

    claim: Union[str, core.StringOut] = core.attr(str)

    match_type: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        claim: Union[str, core.StringOut],
        match_type: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MappingRule.Args(
                claim=claim,
                match_type=match_type,
                role_arn=role_arn,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        claim: Union[str, core.StringOut] = core.arg()

        match_type: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RoleMapping(core.Schema):

    ambiguous_role_resolution: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    identity_provider: Union[str, core.StringOut] = core.attr(str)

    mapping_rule: Optional[Union[List[MappingRule], core.ArrayOut[MappingRule]]] = core.attr(
        MappingRule, default=None, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        identity_provider: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        ambiguous_role_resolution: Optional[Union[str, core.StringOut]] = None,
        mapping_rule: Optional[Union[List[MappingRule], core.ArrayOut[MappingRule]]] = None,
    ):
        super().__init__(
            args=RoleMapping.Args(
                identity_provider=identity_provider,
                type=type,
                ambiguous_role_resolution=ambiguous_role_resolution,
                mapping_rule=mapping_rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ambiguous_role_resolution: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_provider: Union[str, core.StringOut] = core.arg()

        mapping_rule: Optional[Union[List[MappingRule], core.ArrayOut[MappingRule]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cognito_identity_pool_roles_attachment", namespace="aws_cognito_identity")
class PoolRolesAttachment(core.Resource):
    """
    The identity pool ID.
    """

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_pool_id: Union[str, core.StringOut] = core.attr(str)

    role_mapping: Optional[Union[List[RoleMapping], core.ArrayOut[RoleMapping]]] = core.attr(
        RoleMapping, default=None, kind=core.Kind.array
    )

    roles: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_pool_id: Union[str, core.StringOut],
        roles: Union[Dict[str, str], core.MapOut[core.StringOut]],
        role_mapping: Optional[Union[List[RoleMapping], core.ArrayOut[RoleMapping]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolRolesAttachment.Args(
                identity_pool_id=identity_pool_id,
                roles=roles,
                role_mapping=role_mapping,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_pool_id: Union[str, core.StringOut] = core.arg()

        role_mapping: Optional[Union[List[RoleMapping], core.ArrayOut[RoleMapping]]] = core.arg(
            default=None
        )

        roles: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()
