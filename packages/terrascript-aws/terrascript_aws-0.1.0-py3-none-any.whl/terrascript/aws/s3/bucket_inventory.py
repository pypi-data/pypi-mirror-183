from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Schedule(core.Schema):

    frequency: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        frequency: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Schedule.Args(
                frequency=frequency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        frequency: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SseKms(core.Schema):

    key_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SseKms.Args(
                key_id=key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class SseS3(core.Schema):
    ...

    @core.schema_args
    class Args(core.SchemaArgs):
        ...


@core.schema
class Encryption(core.Schema):

    sse_kms: Optional[SseKms] = core.attr(SseKms, default=None)

    sse_s3: Optional[SseS3] = core.attr(SseS3, default=None)

    def __init__(
        self,
        *,
        sse_kms: Optional[SseKms] = None,
        sse_s3: Optional[SseS3] = None,
    ):
        super().__init__(
            args=Encryption.Args(
                sse_kms=sse_kms,
                sse_s3=sse_s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sse_kms: Optional[SseKms] = core.arg(default=None)

        sse_s3: Optional[SseS3] = core.arg(default=None)


@core.schema
class Bucket(core.Schema):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_arn: Union[str, core.StringOut] = core.attr(str)

    encryption: Optional[Encryption] = core.attr(Encryption, default=None)

    format: Union[str, core.StringOut] = core.attr(str)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_arn: Union[str, core.StringOut],
        format: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        encryption: Optional[Encryption] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Bucket.Args(
                bucket_arn=bucket_arn,
                format=format,
                account_id=account_id,
                encryption=encryption,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_arn: Union[str, core.StringOut] = core.arg()

        encryption: Optional[Encryption] = core.arg(default=None)

        format: Union[str, core.StringOut] = core.arg()

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    bucket: Bucket = core.attr(Bucket)

    def __init__(
        self,
        *,
        bucket: Bucket,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Bucket = core.arg()


@core.resource(type="aws_s3_bucket_inventory", namespace="aws_s3")
class BucketInventory(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    destination: Destination = core.attr(Destination)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    included_object_versions: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    optional_fields: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    schedule: Schedule = core.attr(Schedule)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        destination: Destination,
        included_object_versions: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        schedule: Schedule,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        filter: Optional[Filter] = None,
        optional_fields: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketInventory.Args(
                bucket=bucket,
                destination=destination,
                included_object_versions=included_object_versions,
                name=name,
                schedule=schedule,
                enabled=enabled,
                filter=filter,
                optional_fields=optional_fields,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        destination: Destination = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        filter: Optional[Filter] = core.arg(default=None)

        included_object_versions: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        optional_fields: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        schedule: Schedule = core.arg()
