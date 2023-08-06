from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RevocationRecord(core.Schema):

    revocation_effective_from: Union[str, core.StringOut] = core.attr(str, computed=True)

    revoked_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    revoked_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        revocation_effective_from: Union[str, core.StringOut],
        revoked_at: Union[str, core.StringOut],
        revoked_by: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RevocationRecord.Args(
                revocation_effective_from=revocation_effective_from,
                revoked_at=revoked_at,
                revoked_by=revoked_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        revocation_effective_from: Union[str, core.StringOut] = core.arg()

        revoked_at: Union[str, core.StringOut] = core.arg()

        revoked_by: Union[str, core.StringOut] = core.arg()


@core.schema
class SignatureValidityPeriod(core.Schema):

    type: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SignatureValidityPeriod.Args(
                type=type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_signer_signing_profile", namespace="aws_signer")
class SigningProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    platform_display_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_id: Union[str, core.StringOut] = core.attr(str)

    revocation_record: Union[List[RevocationRecord], core.ArrayOut[RevocationRecord]] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_validity_period: Optional[SignatureValidityPeriod] = core.attr(
        SignatureValidityPeriod, default=None, computed=True
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        platform_id: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        signature_validity_period: Optional[SignatureValidityPeriod] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningProfile.Args(
                platform_id=platform_id,
                name=name,
                name_prefix=name_prefix,
                signature_validity_period=signature_validity_period,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        platform_id: Union[str, core.StringOut] = core.arg()

        signature_validity_period: Optional[SignatureValidityPeriod] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
