from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DomainNameConfiguration(core.Schema):

    certificate_arn: Union[str, core.StringOut] = core.attr(str)

    endpoint_type: Union[str, core.StringOut] = core.attr(str)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    security_policy: Union[str, core.StringOut] = core.attr(str)

    target_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        certificate_arn: Union[str, core.StringOut],
        endpoint_type: Union[str, core.StringOut],
        hosted_zone_id: Union[str, core.StringOut],
        security_policy: Union[str, core.StringOut],
        target_domain_name: Union[str, core.StringOut],
        ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DomainNameConfiguration.Args(
                certificate_arn=certificate_arn,
                endpoint_type=endpoint_type,
                hosted_zone_id=hosted_zone_id,
                security_policy=security_policy,
                target_domain_name=target_domain_name,
                ownership_verification_certificate_arn=ownership_verification_certificate_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_arn: Union[str, core.StringOut] = core.arg()

        endpoint_type: Union[str, core.StringOut] = core.arg()

        hosted_zone_id: Union[str, core.StringOut] = core.arg()

        ownership_verification_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        security_policy: Union[str, core.StringOut] = core.arg()

        target_domain_name: Union[str, core.StringOut] = core.arg()


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


@core.resource(type="aws_apigatewayv2_domain_name", namespace="aws_apigatewayv2")
class DomainName(core.Resource):

    api_mapping_selection_expression: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    domain_name_configuration: DomainNameConfiguration = core.attr(DomainNameConfiguration)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    mutual_tls_authentication: Optional[MutualTlsAuthentication] = core.attr(
        MutualTlsAuthentication, default=None
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
        domain_name_configuration: DomainNameConfiguration,
        mutual_tls_authentication: Optional[MutualTlsAuthentication] = None,
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
                domain_name_configuration=domain_name_configuration,
                mutual_tls_authentication=mutual_tls_authentication,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Union[str, core.StringOut] = core.arg()

        domain_name_configuration: DomainNameConfiguration = core.arg()

        mutual_tls_authentication: Optional[MutualTlsAuthentication] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
