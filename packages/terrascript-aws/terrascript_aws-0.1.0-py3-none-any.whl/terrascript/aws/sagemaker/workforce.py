from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class OidcConfig(core.Schema):

    authorization_endpoint: Union[str, core.StringOut] = core.attr(str)

    client_id: Union[str, core.StringOut] = core.attr(str)

    client_secret: Union[str, core.StringOut] = core.attr(str)

    issuer: Union[str, core.StringOut] = core.attr(str)

    jwks_uri: Union[str, core.StringOut] = core.attr(str)

    logout_endpoint: Union[str, core.StringOut] = core.attr(str)

    token_endpoint: Union[str, core.StringOut] = core.attr(str)

    user_info_endpoint: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        authorization_endpoint: Union[str, core.StringOut],
        client_id: Union[str, core.StringOut],
        client_secret: Union[str, core.StringOut],
        issuer: Union[str, core.StringOut],
        jwks_uri: Union[str, core.StringOut],
        logout_endpoint: Union[str, core.StringOut],
        token_endpoint: Union[str, core.StringOut],
        user_info_endpoint: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OidcConfig.Args(
                authorization_endpoint=authorization_endpoint,
                client_id=client_id,
                client_secret=client_secret,
                issuer=issuer,
                jwks_uri=jwks_uri,
                logout_endpoint=logout_endpoint,
                token_endpoint=token_endpoint,
                user_info_endpoint=user_info_endpoint,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authorization_endpoint: Union[str, core.StringOut] = core.arg()

        client_id: Union[str, core.StringOut] = core.arg()

        client_secret: Union[str, core.StringOut] = core.arg()

        issuer: Union[str, core.StringOut] = core.arg()

        jwks_uri: Union[str, core.StringOut] = core.arg()

        logout_endpoint: Union[str, core.StringOut] = core.arg()

        token_endpoint: Union[str, core.StringOut] = core.arg()

        user_info_endpoint: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceIpConfig(core.Schema):

    cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        cidrs: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=SourceIpConfig.Args(
                cidrs=cidrs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidrs: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class CognitoConfig(core.Schema):

    client_id: Union[str, core.StringOut] = core.attr(str)

    user_pool: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        client_id: Union[str, core.StringOut],
        user_pool: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CognitoConfig.Args(
                client_id=client_id,
                user_pool=user_pool,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_id: Union[str, core.StringOut] = core.arg()

        user_pool: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_workforce", namespace="aws_sagemaker")
class Workforce(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cognito_config: Optional[CognitoConfig] = core.attr(CognitoConfig, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    oidc_config: Optional[OidcConfig] = core.attr(OidcConfig, default=None)

    source_ip_config: Optional[SourceIpConfig] = core.attr(
        SourceIpConfig, default=None, computed=True
    )

    subdomain: Union[str, core.StringOut] = core.attr(str, computed=True)

    workforce_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        workforce_name: Union[str, core.StringOut],
        cognito_config: Optional[CognitoConfig] = None,
        oidc_config: Optional[OidcConfig] = None,
        source_ip_config: Optional[SourceIpConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workforce.Args(
                workforce_name=workforce_name,
                cognito_config=cognito_config,
                oidc_config=oidc_config,
                source_ip_config=source_ip_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cognito_config: Optional[CognitoConfig] = core.arg(default=None)

        oidc_config: Optional[OidcConfig] = core.arg(default=None)

        source_ip_config: Optional[SourceIpConfig] = core.arg(default=None)

        workforce_name: Union[str, core.StringOut] = core.arg()
