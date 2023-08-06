from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class CrlConfiguration(core.Schema):

    custom_cname: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    expiration_in_days: Union[int, core.IntOut] = core.attr(int, computed=True)

    s3_bucket_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    s3_object_acl: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        custom_cname: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        expiration_in_days: Union[int, core.IntOut],
        s3_bucket_name: Union[str, core.StringOut],
        s3_object_acl: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CrlConfiguration.Args(
                custom_cname=custom_cname,
                enabled=enabled,
                expiration_in_days=expiration_in_days,
                s3_bucket_name=s3_bucket_name,
                s3_object_acl=s3_object_acl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_cname: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()

        expiration_in_days: Union[int, core.IntOut] = core.arg()

        s3_bucket_name: Union[str, core.StringOut] = core.arg()

        s3_object_acl: Union[str, core.StringOut] = core.arg()


@core.schema
class OcspConfiguration(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ocsp_custom_cname: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        ocsp_custom_cname: Union[str, core.StringOut],
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

        ocsp_custom_cname: Union[str, core.StringOut] = core.arg()


@core.schema
class RevocationConfiguration(core.Schema):

    crl_configuration: Optional[
        Union[List[CrlConfiguration], core.ArrayOut[CrlConfiguration]]
    ] = core.attr(CrlConfiguration, default=None, computed=True, kind=core.Kind.array)

    ocsp_configuration: Optional[
        Union[List[OcspConfiguration], core.ArrayOut[OcspConfiguration]]
    ] = core.attr(OcspConfiguration, default=None, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        *,
        crl_configuration: Optional[
            Union[List[CrlConfiguration], core.ArrayOut[CrlConfiguration]]
        ] = None,
        ocsp_configuration: Optional[
            Union[List[OcspConfiguration], core.ArrayOut[OcspConfiguration]]
        ] = None,
    ):
        super().__init__(
            args=RevocationConfiguration.Args(
                crl_configuration=crl_configuration,
                ocsp_configuration=ocsp_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        crl_configuration: Optional[
            Union[List[CrlConfiguration], core.ArrayOut[CrlConfiguration]]
        ] = core.arg(default=None)

        ocsp_configuration: Optional[
            Union[List[OcspConfiguration], core.ArrayOut[OcspConfiguration]]
        ] = core.arg(default=None)


@core.data(type="aws_acmpca_certificate_authority", namespace="aws_acmpca")
class DsCertificateAuthority(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    certificate: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_chain: Union[str, core.StringOut] = core.attr(str, computed=True)

    certificate_signing_request: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_after: Union[str, core.StringOut] = core.attr(str, computed=True)

    not_before: Union[str, core.StringOut] = core.attr(str, computed=True)

    revocation_configuration: Optional[
        Union[List[RevocationConfiguration], core.ArrayOut[RevocationConfiguration]]
    ] = core.attr(RevocationConfiguration, default=None, computed=True, kind=core.Kind.array)

    serial: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        revocation_configuration: Optional[
            Union[List[RevocationConfiguration], core.ArrayOut[RevocationConfiguration]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsCertificateAuthority.Args(
                arn=arn,
                revocation_configuration=revocation_configuration,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        revocation_configuration: Optional[
            Union[List[RevocationConfiguration], core.ArrayOut[RevocationConfiguration]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
