from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AbortIncompleteMultipartUpload(core.Schema):

    days_after_initiation: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        days_after_initiation: Union[int, core.IntOut],
    ):
        super().__init__(
            args=AbortIncompleteMultipartUpload.Args(
                days_after_initiation=days_after_initiation,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days_after_initiation: Union[int, core.IntOut] = core.arg()


@core.schema
class Expiration(core.Schema):

    date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    expired_object_delete_marker: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
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
class Filter(core.Schema):

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Filter.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = core.attr(
        AbortIncompleteMultipartUpload, default=None
    )

    expiration: Optional[Expiration] = core.attr(Expiration, default=None)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Union[str, core.StringOut] = core.attr(str)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        abort_incomplete_multipart_upload: Optional[AbortIncompleteMultipartUpload] = None,
        expiration: Optional[Expiration] = None,
        filter: Optional[Filter] = None,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Rule.Args(
                id=id,
                abort_incomplete_multipart_upload=abort_incomplete_multipart_upload,
                expiration=expiration,
                filter=filter,
                status=status,
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

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_s3control_bucket_lifecycle_configuration", namespace="aws_s3control")
class BucketLifecycleConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketLifecycleConfiguration.Args(
                bucket=bucket,
                rule=rule,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()
