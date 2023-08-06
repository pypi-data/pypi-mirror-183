from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        types: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class MutualTlsAuthentication(core.Schema):

    truststore_uri: Union[str, core.StringOut] = core.attr(str)

    truststore_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        truststore_uri: Union[str, core.StringOut],
        truststore_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MutualTlsAuthentication.Args(
                truststore_uri=truststore_uri,
                truststore_version=truststore_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        truststore_uri: Union[str, core.StringOut] = core.arg()

        truststore_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_api_gateway_domain_name", namespace="aws_api_gateway")
class DomainName(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_chain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_private_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_upload_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudfront_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    endpoint_configuration: Optional[EndpointConfiguration] = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    mutual_tls_authentication: Optional[MutualTlsAuthentication] = core.attr(
        MutualTlsAuthentication, default=None
    )

    ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    regional_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    regional_certificate_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    regional_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    regional_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

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
        domain_name: Union[str, core.StringOut],
        certificate_arn: Optional[Union[str, core.StringOut]] = None,
        certificate_body: Optional[Union[str, core.StringOut]] = None,
        certificate_chain: Optional[Union[str, core.StringOut]] = None,
        certificate_name: Optional[Union[str, core.StringOut]] = None,
        certificate_private_key: Optional[Union[str, core.StringOut]] = None,
        endpoint_configuration: Optional[EndpointConfiguration] = None,
        mutual_tls_authentication: Optional[MutualTlsAuthentication] = None,
        ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        regional_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        regional_certificate_name: Optional[Union[str, core.StringOut]] = None,
        security_policy: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DomainName.Args(
                domain_name=domain_name,
                certificate_arn=certificate_arn,
                certificate_body=certificate_body,
                certificate_chain=certificate_chain,
                certificate_name=certificate_name,
                certificate_private_key=certificate_private_key,
                endpoint_configuration=endpoint_configuration,
                mutual_tls_authentication=mutual_tls_authentication,
                ownership_verification_certificate_arn=ownership_verification_certificate_arn,
                regional_certificate_arn=regional_certificate_arn,
                regional_certificate_name=regional_certificate_name,
                security_policy=security_policy,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_chain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_private_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        endpoint_configuration: Optional[EndpointConfiguration] = core.arg(default=None)

        mutual_tls_authentication: Optional[MutualTlsAuthentication] = core.arg(default=None)

        ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        regional_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        regional_certificate_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
