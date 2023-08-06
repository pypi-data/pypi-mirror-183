from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CertificateValidationRecords(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CertificateValidationRecords.Args(
                name=name,
                status=status,
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        status: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_apprunner_custom_domain_association", namespace="aws_apprunner")
class CustomDomainAssociation(core.Resource):

    certificate_validation_records: Union[
        List[CertificateValidationRecords], core.ArrayOut[CertificateValidationRecords]
    ] = core.attr(CertificateValidationRecords, computed=True, kind=core.Kind.array)

    dns_target: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    enable_www_subdomain: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_arn: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        service_arn: Union[str, core.StringOut],
        enable_www_subdomain: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CustomDomainAssociation.Args(
                domain_name=domain_name,
                service_arn=service_arn,
                enable_www_subdomain=enable_www_subdomain,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Union[str, core.StringOut] = core.arg()

        enable_www_subdomain: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        service_arn: Union[str, core.StringOut] = core.arg()
