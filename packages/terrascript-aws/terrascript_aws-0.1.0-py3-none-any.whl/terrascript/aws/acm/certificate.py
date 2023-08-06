from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Options(core.Schema):

    certificate_transparency_logging_preference: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        certificate_transparency_logging_preference: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Options.Args(
                certificate_transparency_logging_preference=certificate_transparency_logging_preference,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_transparency_logging_preference: Optional[
            Union[str, core.StringOut]
        ] = core.arg(default=None)


@core.schema
class DomainValidationOptions(core.Schema):

    domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_record_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_record_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_record_value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        domain_name: Union[str, core.StringOut],
        resource_record_name: Union[str, core.StringOut],
        resource_record_type: Union[str, core.StringOut],
        resource_record_value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DomainValidationOptions.Args(
                domain_name=domain_name,
                resource_record_name=resource_record_name,
                resource_record_type=resource_record_type,
                resource_record_value=resource_record_value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        resource_record_name: Union[str, core.StringOut] = core.arg()

        resource_record_type: Union[str, core.StringOut] = core.arg()

        resource_record_value: Union[str, core.StringOut] = core.arg()


@core.schema
class ValidationOption(core.Schema):

    domain_name: Union[str, core.StringOut] = core.attr(str)

    validation_domain: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        domain_name: Union[str, core.StringOut],
        validation_domain: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ValidationOption.Args(
                domain_name=domain_name,
                validation_domain=validation_domain,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        validation_domain: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_acm_certificate", namespace="aws_acm")
class Certificate(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_authority_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    certificate_chain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    domain_validation_options: Union[
        List[DomainValidationOptions], core.ArrayOut[DomainValidationOptions]
    ] = core.attr(DomainValidationOptions, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_after: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_before: Union[str, core.StringOut] = core.attr(str, computed=True)

    options: Optional[Options] = core.attr(Options, default=None)

    private_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subject_alternative_names: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, computed=True, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    validation_emails: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    validation_method: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    validation_option: Optional[
        Union[List[ValidationOption], core.ArrayOut[ValidationOption]]
    ] = core.attr(ValidationOption, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_arn: Optional[Union[str, core.StringOut]] = None,
        certificate_body: Optional[Union[str, core.StringOut]] = None,
        certificate_chain: Optional[Union[str, core.StringOut]] = None,
        domain_name: Optional[Union[str, core.StringOut]] = None,
        options: Optional[Options] = None,
        private_key: Optional[Union[str, core.StringOut]] = None,
        subject_alternative_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        validation_method: Optional[Union[str, core.StringOut]] = None,
        validation_option: Optional[
            Union[List[ValidationOption], core.ArrayOut[ValidationOption]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Certificate.Args(
                certificate_authority_arn=certificate_authority_arn,
                certificate_body=certificate_body,
                certificate_chain=certificate_chain,
                domain_name=domain_name,
                options=options,
                private_key=private_key,
                subject_alternative_names=subject_alternative_names,
                tags=tags,
                tags_all=tags_all,
                validation_method=validation_method,
                validation_option=validation_option,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        certificate_chain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        options: Optional[Options] = core.arg(default=None)

        private_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subject_alternative_names: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        validation_method: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        validation_option: Optional[
            Union[List[ValidationOption], core.ArrayOut[ValidationOption]]
        ] = core.arg(default=None)
