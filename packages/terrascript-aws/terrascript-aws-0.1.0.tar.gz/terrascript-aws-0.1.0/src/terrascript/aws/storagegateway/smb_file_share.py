from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.resource(type="aws_storagegateway_smb_file_share", namespace="aws_storagegateway")
class SmbFileShare(core.Resource):

    access_based_enumeration: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    admin_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    audit_destination_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    authentication: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cache_attributes: Optional[CacheAttributes] = core.attr(CacheAttributes, default=None)

    case_sensitivity: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    file_share_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    fileshare_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invalid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location_arn: Union[str, core.StringOut] = core.attr(str)

    notification_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    object_acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    oplocks_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    read_only: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    requester_pays: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    smb_acl_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    valid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: Union[str, core.StringOut],
        location_arn: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        access_based_enumeration: Optional[Union[bool, core.BoolOut]] = None,
        admin_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        audit_destination_arn: Optional[Union[str, core.StringOut]] = None,
        authentication: Optional[Union[str, core.StringOut]] = None,
        bucket_region: Optional[Union[str, core.StringOut]] = None,
        cache_attributes: Optional[CacheAttributes] = None,
        case_sensitivity: Optional[Union[str, core.StringOut]] = None,
        default_storage_class: Optional[Union[str, core.StringOut]] = None,
        file_share_name: Optional[Union[str, core.StringOut]] = None,
        guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = None,
        invalid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        kms_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        notification_policy: Optional[Union[str, core.StringOut]] = None,
        object_acl: Optional[Union[str, core.StringOut]] = None,
        oplocks_enabled: Optional[Union[bool, core.BoolOut]] = None,
        read_only: Optional[Union[bool, core.BoolOut]] = None,
        requester_pays: Optional[Union[bool, core.BoolOut]] = None,
        smb_acl_enabled: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        valid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SmbFileShare.Args(
                gateway_arn=gateway_arn,
                location_arn=location_arn,
                role_arn=role_arn,
                access_based_enumeration=access_based_enumeration,
                admin_user_list=admin_user_list,
                audit_destination_arn=audit_destination_arn,
                authentication=authentication,
                bucket_region=bucket_region,
                cache_attributes=cache_attributes,
                case_sensitivity=case_sensitivity,
                default_storage_class=default_storage_class,
                file_share_name=file_share_name,
                guess_mime_type_enabled=guess_mime_type_enabled,
                invalid_user_list=invalid_user_list,
                kms_encrypted=kms_encrypted,
                kms_key_arn=kms_key_arn,
                notification_policy=notification_policy,
                object_acl=object_acl,
                oplocks_enabled=oplocks_enabled,
                read_only=read_only,
                requester_pays=requester_pays,
                smb_acl_enabled=smb_acl_enabled,
                tags=tags,
                tags_all=tags_all,
                valid_user_list=valid_user_list,
                vpc_endpoint_dns_name=vpc_endpoint_dns_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_based_enumeration: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        admin_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        audit_destination_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        authentication: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cache_attributes: Optional[CacheAttributes] = core.arg(default=None)

        case_sensitivity: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_share_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        gateway_arn: Union[str, core.StringOut] = core.arg()

        guess_mime_type_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        invalid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location_arn: Union[str, core.StringOut] = core.arg()

        notification_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        object_acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        oplocks_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        read_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        requester_pays: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        smb_acl_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        valid_user_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_endpoint_dns_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
