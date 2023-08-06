from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CrlConfiguration(core.Schema):

    custom_cname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    expiration_in_days: Union[int, core.IntOut] = core.attr(int)

    s3_bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_object_acl: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        expiration_in_days: Union[int, core.IntOut],
        custom_cname: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        s3_bucket_name: Optional[Union[str, core.StringOut]] = None,
        s3_object_acl: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CrlConfiguration.Args(
                expiration_in_days=expiration_in_days,
                custom_cname=custom_cname,
                enabled=enabled,
                s3_bucket_name=s3_bucket_name,
                s3_object_acl=s3_object_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_cname: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        expiration_in_days: Union[int, core.IntOut] = core.arg()

        s3_bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_object_acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class OcspConfiguration(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    ocsp_custom_cname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        ocsp_custom_cname: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=OcspConfiguration.Args(
                enabled=enabled,
                ocsp_custom_cname=ocsp_custom_cname,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        ocsp_custom_cname: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RevocationConfiguration(core.Schema):

    crl_configuration: Optional[CrlConfiguration] = core.attr(CrlConfiguration, default=None)

    ocsp_configuration: Optional[OcspConfiguration] = core.attr(OcspConfiguration, default=None)

    def __init__(
        self,
        *,
        crl_configuration: Optional[CrlConfiguration] = None,
        ocsp_configuration: Optional[OcspConfiguration] = None,
    ):
        super().__init__(
            args=RevocationConfiguration.Args(
                crl_configuration=crl_configuration,
                ocsp_configuration=ocsp_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crl_configuration: Optional[CrlConfiguration] = core.arg(default=None)

        ocsp_configuration: Optional[OcspConfiguration] = core.arg(default=None)


@core.schema
class Subject(core.Schema):

    common_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    country: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    distinguished_name_qualifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    generation_qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    given_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    initials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    locality: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organization: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organizational_unit: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    pseudonym: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    surname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    title: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        common_name: Optional[Union[str, core.StringOut]] = None,
        country: Optional[Union[str, core.StringOut]] = None,
        distinguished_name_qualifier: Optional[Union[str, core.StringOut]] = None,
        generation_qualifier: Optional[Union[str, core.StringOut]] = None,
        given_name: Optional[Union[str, core.StringOut]] = None,
        initials: Optional[Union[str, core.StringOut]] = None,
        locality: Optional[Union[str, core.StringOut]] = None,
        organization: Optional[Union[str, core.StringOut]] = None,
        organizational_unit: Optional[Union[str, core.StringOut]] = None,
        pseudonym: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        surname: Optional[Union[str, core.StringOut]] = None,
        title: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Subject.Args(
                common_name=common_name,
                country=country,
                distinguished_name_qualifier=distinguished_name_qualifier,
                generation_qualifier=generation_qualifier,
                given_name=given_name,
                initials=initials,
                locality=locality,
                organization=organization,
                organizational_unit=organizational_unit,
                pseudonym=pseudonym,
                state=state,
                surname=surname,
                title=title,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        common_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        country: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        distinguished_name_qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        generation_qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        given_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        initials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        locality: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organization: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizational_unit: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        pseudonym: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        surname: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        title: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CertificateAuthorityConfiguration(core.Schema):

    key_algorithm: Union[str, core.StringOut] = core.attr(str)

    signing_algorithm: Union[str, core.StringOut] = core.attr(str)

    subject: Subject = core.attr(Subject)

    def __init__(
        self,
        *,
        key_algorithm: Union[str, core.StringOut],
        signing_algorithm: Union[str, core.StringOut],
        subject: Subject,
    ):
        super().__init__(
            args=CertificateAuthorityConfiguration.Args(
                key_algorithm=key_algorithm,
                signing_algorithm=signing_algorithm,
                subject=subject,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_algorithm: Union[str, core.StringOut] = core.arg()

        signing_algorithm: Union[str, core.StringOut] = core.arg()

        subject: Subject = core.arg()


@core.resource(type="aws_acmpca_certificate_authority", namespace="aws_acmpca")
class CertificateAuthority(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_authority_configuration: CertificateAuthorityConfiguration = core.attr(
        CertificateAuthorityConfiguration
    )

    certificate_chain: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_signing_request: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_after: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_before: Union[str, core.StringOut] = core.attr(str, computed=True)

    permanent_deletion_time_in_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    revocation_configuration: Optional[RevocationConfiguration] = core.attr(
        RevocationConfiguration, default=None
    )

    serial: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate_authority_configuration: CertificateAuthorityConfiguration,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        permanent_deletion_time_in_days: Optional[Union[int, core.IntOut]] = None,
        revocation_configuration: Optional[RevocationConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CertificateAuthority.Args(
                certificate_authority_configuration=certificate_authority_configuration,
                enabled=enabled,
                permanent_deletion_time_in_days=permanent_deletion_time_in_days,
                revocation_configuration=revocation_configuration,
                tags=tags,
                tags_all=tags_all,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate_authority_configuration: CertificateAuthorityConfiguration = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        permanent_deletion_time_in_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        revocation_configuration: Optional[RevocationConfiguration] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
