from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class NfsFileShareDefaults(core.Schema):

    directory_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        directory_mode: Optional[Union[str, core.StringOut]] = None,
        file_mode: Optional[Union[str, core.StringOut]] = None,
        group_id: Optional[Union[str, core.StringOut]] = None,
        owner_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NfsFileShareDefaults.Args(
                directory_mode=directory_mode,
                file_mode=file_mode,
                group_id=group_id,
                owner_id=owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owner_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CacheAttributes(core.Schema):

    cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CacheAttributes.Args(
                cache_stale_timeout_in_seconds=cache_stale_timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cache_stale_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_storagegateway_nfs_file_share", namespace="aws_storagegateway")
class NfsFileShare(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audit_destination_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cache_attributes: Optional[CacheAttributes] = core.attr(CacheAttributes, default=None)

    client_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    default_storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file_share_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    fileshare_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location_arn: Union[str, core.StringOut] = core.attr(str)

    nfs_file_share_defaults: Optional[NfsFileShareDefaults] = core.attr(
        NfsFileShareDefaults, default=None
    )

    notification_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    read_only: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    requester_pays: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    squash: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        client_list: Union[List[str], core.ArrayOut[core.StringOut]],
        gateway_arn: Union[str, core.StringOut],
        location_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        audit_destination_arn: Optional[Union[str, core.StringOut]] = None,
        bucket_region: Optional[Union[str, core.StringOut]] = None,
        cache_attributes: Optional[CacheAttributes] = None,
        default_storage_class: Optional[Union[str, core.StringOut]] = None,
        file_share_name: Optional[Union[str, core.StringOut]] = None,
        guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = None,
        kms_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        nfs_file_share_defaults: Optional[NfsFileShareDefaults] = None,
        notification_policy: Optional[Union[str, core.StringOut]] = None,
        object_acl: Optional[Union[str, core.StringOut]] = None,
        read_only: Optional[Union[bool, core.BoolOut]] = None,
        requester_pays: Optional[Union[bool, core.BoolOut]] = None,
        squash: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NfsFileShare.Args(
                client_list=client_list,
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                role_arn=role_arn,
                audit_destination_arn=audit_destination_arn,
                bucket_region=bucket_region,
                cache_attributes=cache_attributes,
                default_storage_class=default_storage_class,
                file_share_name=file_share_name,
                guess_mime_type_enabled=guess_mime_type_enabled,
                kms_encrypted=kms_encrypted,
                kms_key_arn=kms_key_arn,
                nfs_file_share_defaults=nfs_file_share_defaults,
                notification_policy=notification_policy,
                object_acl=object_acl,
                read_only=read_only,
                requester_pays=requester_pays,
                squash=squash,
                tags=tags,
                tags_all=tags_all,
                vpc_endpoint_dns_name=vpc_endpoint_dns_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        audit_destination_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cache_attributes: Optional[CacheAttributes] = core.arg(default=None)

        client_list: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        default_storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_share_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_arn: Union[str, core.StringOut] = core.arg()

        guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location_arn: Union[str, core.StringOut] = core.arg()

        nfs_file_share_defaults: Optional[NfsFileShareDefaults] = core.arg(default=None)

        notification_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        read_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        requester_pays: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        squash: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
