from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class JwtConfiguration(core.Schema):

    audience: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    issuer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        audience: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        issuer: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=JwtConfiguration.Args(
                audience=audience,
                issuer=issuer,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        audience: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        issuer: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_apigatewayv2_authorizer", namespace="aws_apigatewayv2")
class Authorizer(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    authorizer_credentials_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    authorizer_payload_format_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    authorizer_type: Union[str, core.StringOut] = core.attr(str)

    authorizer_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_simple_responses: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    jwt_configuration: Optional[JwtConfiguration] = core.attr(JwtConfiguration, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        authorizer_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        authorizer_credentials_arn: Optional[Union[str, core.StringOut]] = None,
        authorizer_payload_format_version: Optional[Union[str, core.StringOut]] = None,
        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = None,
        authorizer_uri: Optional[Union[str, core.StringOut]] = None,
        enable_simple_responses: Optional[Union[bool, core.BoolOut]] = None,
        identity_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        jwt_configuration: Optional[JwtConfiguration] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                api_id=api_id,
                authorizer_type=authorizer_type,
                name=name,
                authorizer_credentials_arn=authorizer_credentials_arn,
                authorizer_payload_format_version=authorizer_payload_format_version,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                authorizer_uri=authorizer_uri,
                enable_simple_responses=enable_simple_responses,
                identity_sources=identity_sources,
                jwt_configuration=jwt_configuration,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        authorizer_credentials_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        authorizer_payload_format_version: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        authorizer_type: Union[str, core.StringOut] = core.arg()

        authorizer_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_simple_responses: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        identity_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        jwt_configuration: Optional[JwtConfiguration] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()
