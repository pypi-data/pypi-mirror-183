from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Oidc(core.Schema):

    client_id: Union[str, core.StringOut] = core.attr(str)

    groups_claim: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    groups_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    identity_provider_config_name: Union[str, core.StringOut] = core.attr(str)

    issuer_url: Union[str, core.StringOut] = core.attr(str)

    required_claims: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    username_claim: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    username_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        identity_provider_config_name: Union[str, core.StringOut],
        issuer_url: Union[str, core.StringOut],
        groups_claim: Optional[Union[str, core.StringOut]] = None,
        groups_prefix: Optional[Union[str, core.StringOut]] = None,
        required_claims: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        username_claim: Optional[Union[str, core.StringOut]] = None,
        username_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Oidc.Args(
                client_id=client_id,
                identity_provider_config_name=identity_provider_config_name,
                issuer_url=issuer_url,
                groups_claim=groups_claim,
                groups_prefix=groups_prefix,
                required_claims=required_claims,
                username_claim=username_claim,
                username_prefix=username_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: Union[str, core.StringOut] = core.arg()

        groups_claim: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        groups_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_provider_config_name: Union[str, core.StringOut] = core.arg()

        issuer_url: Union[str, core.StringOut] = core.arg()

        required_claims: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        username_claim: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_eks_identity_provider_config", namespace="aws_eks")
class IdentityProviderConfig(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    oidc: Oidc = core.attr(Oidc)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        oidc: Oidc,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityProviderConfig.Args(
                cluster_name=cluster_name,
                oidc=oidc,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cluster_name: Union[str, core.StringOut] = core.arg()

        oidc: Oidc = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
