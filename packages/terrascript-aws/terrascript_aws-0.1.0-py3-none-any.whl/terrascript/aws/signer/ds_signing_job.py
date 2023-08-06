from typing import List, Union

import terrascript.core as core


@core.schema
class RevocationRecord(core.Schema):

    reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    revoked_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    revoked_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        reason: Union[str, core.StringOut],
        revoked_at: Union[str, core.StringOut],
        revoked_by: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RevocationRecord.Args(
                reason=reason,
                revoked_at=revoked_at,
                revoked_by=revoked_by,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        reason: Union[str, core.StringOut] = core.arg()

        revoked_at: Union[str, core.StringOut] = core.arg()

        revoked_by: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceS3(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SourceS3.Args(
                bucket=bucket,
                key=key,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        version: Union[str, core.StringOut] = core.arg()


@core.schema
class Source(core.Schema):

    s3: Union[List[SourceS3], core.ArrayOut[SourceS3]] = core.attr(
        SourceS3, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3: Union[List[SourceS3], core.ArrayOut[SourceS3]],
    ):
        super().__init__(
            args=Source.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: Union[List[SourceS3], core.ArrayOut[SourceS3]] = core.arg()


@core.schema
class SignedObjectS3(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SignedObjectS3.Args(
                bucket=bucket,
                key=key,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()


@core.schema
class SignedObject(core.Schema):

    s3: Union[List[SignedObjectS3], core.ArrayOut[SignedObjectS3]] = core.attr(
        SignedObjectS3, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        s3: Union[List[SignedObjectS3], core.ArrayOut[SignedObjectS3]],
    ):
        super().__init__(
            args=SignedObject.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: Union[List[SignedObjectS3], core.ArrayOut[SignedObjectS3]] = core.arg()


@core.data(type="aws_signer_signing_job", namespace="aws_signer")
class DsSigningJob(core.Data):

    completed_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_id: Union[str, core.StringOut] = core.attr(str)

    job_invoker: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_display_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    profile_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    profile_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    requested_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    revocation_record: Union[List[RevocationRecord], core.ArrayOut[RevocationRecord]] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_expires_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    signed_object: Union[List[SignedObject], core.ArrayOut[SignedObject]] = core.attr(
        SignedObject, computed=True, kind=core.Kind.array
    )

    source: Union[List[Source], core.ArrayOut[Source]] = core.attr(
        Source, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        job_id: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsSigningJob.Args(
                job_id=job_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        job_id: Union[str, core.StringOut] = core.arg()
