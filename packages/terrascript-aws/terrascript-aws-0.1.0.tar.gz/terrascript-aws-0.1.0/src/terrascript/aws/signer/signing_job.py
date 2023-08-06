from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class SourceS3(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    version: Union[str, core.StringOut] = core.attr(str)

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

    s3: SourceS3 = core.attr(SourceS3)

    def __init__(
        self,
        *,
        s3: SourceS3,
    ):
        super().__init__(
            args=Source.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: SourceS3 = core.arg()


@core.schema
class DestinationS3(core.Schema):

    bucket: Union[str, core.StringOut] = core.attr(str)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DestinationS3.Args(
                bucket=bucket,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    s3: DestinationS3 = core.attr(DestinationS3)

    def __init__(
        self,
        *,
        s3: DestinationS3,
    ):
        super().__init__(
            args=Destination.Args(
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3: DestinationS3 = core.arg()


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


@core.resource(type="aws_signer_signing_job", namespace="aws_signer")
class SigningJob(core.Resource):

    completed_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination: Destination = core.attr(Destination)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_signing_job_failure: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    job_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_invoker: Union[str, core.StringOut] = core.attr(str, computed=True)

    job_owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_display_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    profile_name: Union[str, core.StringOut] = core.attr(str)

    profile_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    requested_by: Union[str, core.StringOut] = core.attr(str, computed=True)

    revocation_record: Union[List[RevocationRecord], core.ArrayOut[RevocationRecord]] = core.attr(
        RevocationRecord, computed=True, kind=core.Kind.array
    )

    signature_expires_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    signed_object: Union[List[SignedObject], core.ArrayOut[SignedObject]] = core.attr(
        SignedObject, computed=True, kind=core.Kind.array
    )

    source: Source = core.attr(Source)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination: Destination,
        profile_name: Union[str, core.StringOut],
        source: Source,
        ignore_signing_job_failure: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SigningJob.Args(
                destination=destination,
                profile_name=profile_name,
                source=source,
                ignore_signing_job_failure=ignore_signing_job_failure,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination: Destination = core.arg()

        ignore_signing_job_failure: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        profile_name: Union[str, core.StringOut] = core.arg()

        source: Source = core.arg()
