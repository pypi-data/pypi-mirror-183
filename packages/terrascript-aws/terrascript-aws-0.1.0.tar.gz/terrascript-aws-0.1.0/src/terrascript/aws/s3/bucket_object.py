from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_s3_bucket_object", namespace="aws_s3")
class BucketObject(core.Resource):

    acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    cache_control: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_base64: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_disposition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_encoding: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    content_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    etag: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    object_lock_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    server_side_encryption: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_hash: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_redirect: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        acl: Optional[Union[str, core.StringOut]] = None,
        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = None,
        cache_control: Optional[Union[str, core.StringOut]] = None,
        content: Optional[Union[str, core.StringOut]] = None,
        content_base64: Optional[Union[str, core.StringOut]] = None,
        content_disposition: Optional[Union[str, core.StringOut]] = None,
        content_encoding: Optional[Union[str, core.StringOut]] = None,
        content_language: Optional[Union[str, core.StringOut]] = None,
        content_type: Optional[Union[str, core.StringOut]] = None,
        etag: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = None,
        object_lock_mode: Optional[Union[str, core.StringOut]] = None,
        object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = None,
        server_side_encryption: Optional[Union[str, core.StringOut]] = None,
        source: Optional[Union[str, core.StringOut]] = None,
        source_hash: Optional[Union[str, core.StringOut]] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        website_redirect: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketObject.Args(
                bucket=bucket,
                key=key,
                acl=acl,
                bucket_key_enabled=bucket_key_enabled,
                cache_control=cache_control,
                content=content,
                content_base64=content_base64,
                content_disposition=content_disposition,
                content_encoding=content_encoding,
                content_language=content_language,
                content_type=content_type,
                etag=etag,
                force_destroy=force_destroy,
                kms_key_id=kms_key_id,
                metadata=metadata,
                object_lock_legal_hold_status=object_lock_legal_hold_status,
                object_lock_mode=object_lock_mode,
                object_lock_retain_until_date=object_lock_retain_until_date,
                server_side_encryption=server_side_encryption,
                source=source,
                source_hash=source_hash,
                storage_class=storage_class,
                tags=tags,
                tags_all=tags_all,
                website_redirect=website_redirect,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cache_control: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_base64: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_disposition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        etag: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_side_encryption: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_hash: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        website_redirect: Optional[Union[str, core.StringOut]] = core.arg(default=None)
