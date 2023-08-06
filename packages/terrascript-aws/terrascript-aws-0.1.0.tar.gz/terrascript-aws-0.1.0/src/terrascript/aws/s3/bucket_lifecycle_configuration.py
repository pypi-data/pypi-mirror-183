from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Transition(core.Schema):

    date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    storage_class: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: Union[str, core.StringOut],
        date: Optional[Union[str, core.StringOut]] = None,
        days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Transition.Args(
                storage_class=storage_class,
                date=date,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_class: Union[str, core.StringOut] = core.arg()


@core.schema
class Tag(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Tag.Args(
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class And(core.Schema):

    object_size_greater_than: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    object_size_less_than: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        object_size_greater_than: Optional[Union[int, core.IntOut]] = None,
        object_size_less_than: Optional[Union[int, core.IntOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=And.Args(
                object_size_greater_than=object_size_greater_than,
                object_size_less_than=object_size_less_than,
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_size_greater_than: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        object_size_less_than: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Filter(core.Schema):

    and_: Optional[And] = core.attr(And, default=None, alias="and")

    object_size_greater_than: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_size_less_than: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag: Optional[Tag] = core.attr(Tag, default=None)

    def __init__(
        self,
        *,
        and_: Optional[And] = None,
        object_size_greater_than: Optional[Union[str, core.StringOut]] = None,
        object_size_less_than: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tag: Optional[Tag] = None,
    ):
        super().__init__(
            args=Filter.Args(
                and_=and_,
                object_size_greater_than=object_size_greater_than,
                object_size_less_than=object_size_less_than,
                prefix=prefix,
                tag=tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[And] = core.arg(default=None)

        object_size_greater_than: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_size_less_than: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag: Optional[Tag] = core.arg(default=None)


@core.schema
class Expiration(core.Schema):

    date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    expired_object_delete_marker: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    def __init__(
        self,
        *,
        date: Optional[Union[str, core.StringOut]] = None,
        days: Optional[Union[int, core.IntOut]] = None,
        expired_object_delete_marker: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Expiration.Args(
                date=date,
                days=days,
                expired_object_delete_marker=expired_object_delete_marker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        expired_object_delete_marker: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class NoncurrentVersionTransition(core.Schema):

    newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    noncurrent_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    storage_class: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: Union[str, core.StringOut],
        newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = None,
        noncurrent_days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NoncurrentVersionTransition.Args(
                storage_class=storage_class,
                newer_noncurrent_versions=newer_noncurrent_versions,
                noncurrent_days=noncurrent_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        noncurrent_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_class: Union[str, core.StringOut] = core.arg()


@core.schema
class AbortIncompleteMultipartUpload(core.Schema):

    days_after_initiation: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days_after_initiation: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=AbortIncompleteMultipartUpload.Args(
                days_after_initiation=days_after_initiation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days_after_initiation: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class NoncurrentVersionExpiration(core.Schema):

    newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    noncurrent_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = None,
        noncurrent_days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NoncurrentVersionExpiration.Args(
                newer_noncurrent_versions=newer_noncurrent_versions,
                noncurrent_days=noncurrent_days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        newer_noncurrent_versions: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        noncurrent_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = core.attr(
        AbortIncompleteMultipartUpload, default=None
    )

    expiration: Optional[Expiration] = core.attr(Expiration, default=None)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str)

    noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = core.attr(
        NoncurrentVersionExpiration, default=None
    )

    noncurrent_version_transition: Optional[
        Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
    ] = core.attr(NoncurrentVersionTransition, default=None, kind=core.Kind.array)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str)

    transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = core.attr(
        Transition, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        status: Union[str, core.StringOut],
        abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None,
        expiration: Optional[Expiration] = None,
        filter: Optional[Filter] = None,
        noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = None,
        noncurrent_version_transition: Optional[
            Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
        ] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                status=status,
                abort_incomplete_multipart_upload=abort_incomplete_multipart_upload,
                expiration=expiration,
                filter=filter,
                noncurrent_version_expiration=noncurrent_version_expiration,
                noncurrent_version_transition=noncurrent_version_transition,
                prefix=prefix,
                transition=transition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = core.arg(
            default=None
        )

        expiration: Optional[Expiration] = core.arg(default=None)

        filter: Optional[Filter] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = core.arg(
            default=None
        )

        noncurrent_version_transition: Optional[
            Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
        ] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()

        transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = core.arg(
            default=None
        )


@core.resource(type="aws_s3_bucket_lifecycle_configuration", namespace="aws_s3")
class BucketLifecycleConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketLifecycleConfiguration.Args(
                bucket=bucket,
                rule=rule,
                expected_bucket_owner=expected_bucket_owner,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()
