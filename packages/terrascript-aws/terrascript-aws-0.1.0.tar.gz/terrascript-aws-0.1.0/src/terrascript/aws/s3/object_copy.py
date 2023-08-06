from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Grant(core.Schema):

    email: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    type: Union[str, core.StringOut] = core.attr(str)

    uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        permissions: Union[List[str], core.ArrayOut[core.StringOut]],
        type: Union[str, core.StringOut],
        email: Optional[Union[str, core.StringOut]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Grant.Args(
                permissions=permissions,
                type=type,
                email=email,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        email: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_s3_object_copy", namespace="aws_s3")
class ObjectCopy(core.Resource):

    acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    cache_control: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    content_disposition: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    content_encoding: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    content_language: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    content_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    copy_if_match: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_if_modified_since: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_if_none_match: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    copy_if_unmodified_since: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    customer_algorithm: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    customer_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    customer_key_md5: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    expected_source_bucket_owner: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    expires: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.attr(
        Grant, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    kms_encryption_context: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    metadata_directive: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    object_lock_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    request_charged: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    request_payer: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_side_encryption: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source: Union[str, core.StringOut] = core.attr(str)

    source_customer_algorithm: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_customer_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_customer_key_md5: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tagging_directive: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_redirect: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        source: Union[str, core.StringOut],
        acl: Optional[Union[str, core.StringOut]] = None,
        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = None,
        cache_control: Optional[Union[str, core.StringOut]] = None,
        content_disposition: Optional[Union[str, core.StringOut]] = None,
        content_encoding: Optional[Union[str, core.StringOut]] = None,
        content_language: Optional[Union[str, core.StringOut]] = None,
        content_type: Optional[Union[str, core.StringOut]] = None,
        copy_if_match: Optional[Union[str, core.StringOut]] = None,
        copy_if_modified_since: Optional[Union[str, core.StringOut]] = None,
        copy_if_none_match: Optional[Union[str, core.StringOut]] = None,
        copy_if_unmodified_since: Optional[Union[str, core.StringOut]] = None,
        customer_algorithm: Optional[Union[str, core.StringOut]] = None,
        customer_key: Optional[Union[str, core.StringOut]] = None,
        customer_key_md5: Optional[Union[str, core.StringOut]] = None,
        expected_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        expected_source_bucket_owner: Optional[Union[str, core.StringOut]] = None,
        expires: Optional[Union[str, core.StringOut]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = None,
        kms_encryption_context: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        metadata_directive: Optional[Union[str, core.StringOut]] = None,
        object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = None,
        object_lock_mode: Optional[Union[str, core.StringOut]] = None,
        object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = None,
        request_payer: Optional[Union[str, core.StringOut]] = None,
        server_side_encryption: Optional[Union[str, core.StringOut]] = None,
        source_customer_algorithm: Optional[Union[str, core.StringOut]] = None,
        source_customer_key: Optional[Union[str, core.StringOut]] = None,
        source_customer_key_md5: Optional[Union[str, core.StringOut]] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
        tagging_directive: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        website_redirect: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ObjectCopy.Args(
                bucket=bucket,
                key=key,
                source=source,
                acl=acl,
                bucket_key_enabled=bucket_key_enabled,
                cache_control=cache_control,
                content_disposition=content_disposition,
                content_encoding=content_encoding,
                content_language=content_language,
                content_type=content_type,
                copy_if_match=copy_if_match,
                copy_if_modified_since=copy_if_modified_since,
                copy_if_none_match=copy_if_none_match,
                copy_if_unmodified_since=copy_if_unmodified_since,
                customer_algorithm=customer_algorithm,
                customer_key=customer_key,
                customer_key_md5=customer_key_md5,
                expected_bucket_owner=expected_bucket_owner,
                expected_source_bucket_owner=expected_source_bucket_owner,
                expires=expires,
                force_destroy=force_destroy,
                grant=grant,
                kms_encryption_context=kms_encryption_context,
                kms_key_id=kms_key_id,
                metadata=metadata,
                metadata_directive=metadata_directive,
                object_lock_legal_hold_status=object_lock_legal_hold_status,
                object_lock_mode=object_lock_mode,
                object_lock_retain_until_date=object_lock_retain_until_date,
                request_payer=request_payer,
                server_side_encryption=server_side_encryption,
                source_customer_algorithm=source_customer_algorithm,
                source_customer_key=source_customer_key,
                source_customer_key_md5=source_customer_key_md5,
                storage_class=storage_class,
                tagging_directive=tagging_directive,
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

        content_disposition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_encoding: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        content_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_if_match: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_if_modified_since: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_if_none_match: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_if_unmodified_since: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customer_algorithm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customer_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customer_key_md5: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expected_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expected_source_bucket_owner: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        expires: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.arg(default=None)

        key: Union[str, core.StringOut] = core.arg()

        kms_encryption_context: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metadata: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        metadata_directive: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_legal_hold_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_lock_retain_until_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        request_payer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_side_encryption: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source: Union[str, core.StringOut] = core.arg()

        source_customer_algorithm: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_customer_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_customer_key_md5: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tagging_directive: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        website_redirect: Optional[Union[str, core.StringOut]] = core.arg(default=None)
