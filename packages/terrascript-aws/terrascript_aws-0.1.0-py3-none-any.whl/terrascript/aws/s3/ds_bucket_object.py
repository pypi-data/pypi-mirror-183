from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_s3_bucket_object", namespace="aws_s3")
class DsBucketObject(core.Data):

    body: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket: Union[str, core.StringOut] = core.attr(str)

    bucket_key_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    cache_control: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_disposition: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_encoding: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_language: Union[str, core.StringOut] = core.attr(str, computed=True)

    content_length: Union[int, core.IntOut] = core.attr(int, computed=True)

    content_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    etag: Union[str, core.StringOut] = core.attr(str, computed=True)

    expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    expires: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    metadata: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    object_lock_legal_hold_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    object_lock_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    object_lock_retain_until_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    range: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_side_encryption: Union[str, core.StringOut] = core.attr(str, computed=True)

    sse_kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_class: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    website_redirect_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        bucket: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        range: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        version_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsBucketObject.Args(
                bucket=bucket,
                key=key,
                range=range,
                tags=tags,
                version_id=version_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        range: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        version_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
