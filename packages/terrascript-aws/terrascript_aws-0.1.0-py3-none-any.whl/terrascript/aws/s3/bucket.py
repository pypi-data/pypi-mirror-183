from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Website(core.Schema):

    error_document: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    index_document: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    redirect_all_requests_to: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    routing_rules: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        error_document: Optional[Union[str, core.StringOut]] = None,
        index_document: Optional[Union[str, core.StringOut]] = None,
        redirect_all_requests_to: Optional[Union[str, core.StringOut]] = None,
        routing_rules: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Website.Args(
                error_document=error_document,
                index_document=index_document,
                redirect_all_requests_to=redirect_all_requests_to,
                routing_rules=routing_rules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_document: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        index_document: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        redirect_all_requests_to: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        routing_rules: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Versioning(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    mfa_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        mfa_delete: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Versioning.Args(
                enabled=enabled,
                mfa_delete=mfa_delete,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        mfa_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


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
class AccessControlTranslation(core.Schema):

    owner: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        owner: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AccessControlTranslation.Args(
                owner=owner,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        owner: Union[str, core.StringOut] = core.arg()


@core.schema
class ReplicationTime(core.Schema):

    minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        minutes: Optional[Union[int, core.IntOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ReplicationTime.Args(
                minutes=minutes,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Metrics(core.Schema):

    minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        minutes: Optional[Union[int, core.IntOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Metrics.Args(
                minutes=minutes,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Destination(core.Schema):

    access_control_translation: Optional[AccessControlTranslation] = core.attr(
        AccessControlTranslation, default=None
    )

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    metrics: Optional[Metrics] = core.attr(Metrics, default=None)

    replica_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    replication_time: Optional[ReplicationTime] = core.attr(ReplicationTime, default=None)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        access_control_translation: Optional[AccessControlTranslation] = None,
        account_id: Optional[Union[str, core.StringOut]] = None,
        metrics: Optional[Metrics] = None,
        replica_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        replication_time: Optional[ReplicationTime] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
                access_control_translation=access_control_translation,
                account_id=account_id,
                metrics=metrics,
                replica_kms_key_id=replica_kms_key_id,
                replication_time=replication_time,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_translation: Optional[AccessControlTranslation] = core.arg(default=None)

        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        metrics: Optional[Metrics] = core.arg(default=None)

        replica_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_time: Optional[ReplicationTime] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SseKmsEncryptedObjects(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=SseKmsEncryptedObjects.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SourceSelectionCriteria(core.Schema):

    sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = core.attr(
        SseKmsEncryptedObjects, default=None
    )

    def __init__(
        self,
        *,
        sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = None,
    ):
        super().__init__(
            args=SourceSelectionCriteria.Args(
                sse_kms_encrypted_objects=sse_kms_encrypted_objects,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = core.arg(default=None)


@core.schema
class Rules(core.Schema):

    delete_marker_replication_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    destination: Destination = core.attr(Destination)

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    source_selection_criteria: Optional[SourceSelectionCriteria] = core.attr(
        SourceSelectionCriteria, default=None
    )

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination: Destination,
        status: Union[str, core.StringOut],
        delete_marker_replication_status: Optional[Union[str, core.StringOut]] = None,
        filter: Optional[Filter] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[int, core.IntOut]] = None,
        source_selection_criteria: Optional[SourceSelectionCriteria] = None,
    ):
        super().__init__(
            args=Rules.Args(
                destination=destination,
                status=status,
                delete_marker_replication_status=delete_marker_replication_status,
                filter=filter,
                id=id,
                prefix=prefix,
                priority=priority,
                source_selection_criteria=source_selection_criteria,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_marker_replication_status: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        destination: Destination = core.arg()

        filter: Optional[Filter] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        source_selection_criteria: Optional[SourceSelectionCriteria] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class ReplicationConfiguration(core.Schema):

    role: Union[str, core.StringOut] = core.attr(str)

    rules: Union[List[Rules], core.ArrayOut[Rules]] = core.attr(Rules, kind=core.Kind.array)

    def __init__(
        self,
        *,
        role: Union[str, core.StringOut],
        rules: Union[List[Rules], core.ArrayOut[Rules]],
    ):
        super().__init__(
            args=ReplicationConfiguration.Args(
                role=role,
                rules=rules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        role: Union[str, core.StringOut] = core.arg()

        rules: Union[List[Rules], core.ArrayOut[Rules]] = core.arg()


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
class NoncurrentVersionTransition(core.Schema):

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    storage_class: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        storage_class: Union[str, core.StringOut],
        days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NoncurrentVersionTransition.Args(
                storage_class=storage_class,
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_class: Union[str, core.StringOut] = core.arg()


@core.schema
class NoncurrentVersionExpiration(core.Schema):

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        days: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NoncurrentVersionExpiration.Args(
                days=days,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)


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
class LifecycleRule(core.Schema):

    abort_incomplete_multipart_upload_days: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    expiration: Optional[Expiration] = core.attr(Expiration, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = core.attr(
        NoncurrentVersionExpiration, default=None
    )

    noncurrent_version_transition: Optional[
        Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
    ] = core.attr(NoncurrentVersionTransition, default=None, kind=core.Kind.array)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = core.attr(
        Transition, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        abort_incomplete_multipart_upload_days: Optional[Union[int, core.IntOut]] = None,
        expiration: Optional[Expiration] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = None,
        noncurrent_version_transition: Optional[
            Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
        ] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = None,
    ):
        super().__init__(
            args=LifecycleRule.Args(
                enabled=enabled,
                abort_incomplete_multipart_upload_days=abort_incomplete_multipart_upload_days,
                expiration=expiration,
                id=id,
                noncurrent_version_expiration=noncurrent_version_expiration,
                noncurrent_version_transition=noncurrent_version_transition,
                prefix=prefix,
                tags=tags,
                transition=transition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        abort_incomplete_multipart_upload_days: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        enabled: Union[bool, core.BoolOut] = core.arg()

        expiration: Optional[Expiration] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        noncurrent_version_expiration: Optional[NoncurrentVersionExpiration] = core.arg(
            default=None
        )

        noncurrent_version_transition: Optional[
            Union[List[NoncurrentVersionTransition], core.ArrayOut[NoncurrentVersionTransition]]
        ] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        transition: Optional[Union[List[Transition], core.ArrayOut[Transition]]] = core.arg(
            default=None
        )


@core.schema
class Logging(core.Schema):

    target_bucket: Union[str, core.StringOut] = core.attr(str)

    target_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        target_bucket: Union[str, core.StringOut],
        target_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Logging.Args(
                target_bucket=target_bucket,
                target_prefix=target_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_bucket: Union[str, core.StringOut] = core.arg()

        target_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Grant(core.Schema):

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
        id: Optional[Union[str, core.StringOut]] = None,
        uri: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Grant.Args(
                permissions=permissions,
                type=type,
                id=id,
                uri=uri,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permissions: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DefaultRetention(core.Schema):

    days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    mode: Union[str, core.StringOut] = core.attr(str)

    years: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        mode: Union[str, core.StringOut],
        days: Optional[Union[int, core.IntOut]] = None,
        years: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DefaultRetention.Args(
                mode=mode,
                days=days,
                years=years,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        mode: Union[str, core.StringOut] = core.arg()

        years: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ObjectLockConfigurationRule(core.Schema):

    default_retention: DefaultRetention = core.attr(DefaultRetention)

    def __init__(
        self,
        *,
        default_retention: DefaultRetention,
    ):
        super().__init__(
            args=ObjectLockConfigurationRule.Args(
                default_retention=default_retention,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_retention: DefaultRetention = core.arg()


@core.schema
class ObjectLockConfiguration(core.Schema):

    object_lock_enabled: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule: Optional[ObjectLockConfigurationRule] = core.attr(
        ObjectLockConfigurationRule, default=None
    )

    def __init__(
        self,
        *,
        object_lock_enabled: Optional[Union[str, core.StringOut]] = None,
        rule: Optional[ObjectLockConfigurationRule] = None,
    ):
        super().__init__(
            args=ObjectLockConfiguration.Args(
                object_lock_enabled=object_lock_enabled,
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        object_lock_enabled: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Optional[ObjectLockConfigurationRule] = core.arg(default=None)


@core.schema
class ApplyServerSideEncryptionByDefault(core.Schema):

    kms_master_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sse_algorithm: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        sse_algorithm: Union[str, core.StringOut],
        kms_master_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ApplyServerSideEncryptionByDefault.Args(
                sse_algorithm=sse_algorithm,
                kms_master_key_id=kms_master_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_master_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sse_algorithm: Union[str, core.StringOut] = core.arg()


@core.schema
class ServerSideEncryptionConfigurationRule(core.Schema):

    apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = core.attr(
        ApplyServerSideEncryptionByDefault
    )

    bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault,
        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ServerSideEncryptionConfigurationRule.Args(
                apply_server_side_encryption_by_default=apply_server_side_encryption_by_default,
                bucket_key_enabled=bucket_key_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        apply_server_side_encryption_by_default: ApplyServerSideEncryptionByDefault = core.arg()

        bucket_key_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ServerSideEncryptionConfiguration(core.Schema):

    rule: ServerSideEncryptionConfigurationRule = core.attr(ServerSideEncryptionConfigurationRule)

    def __init__(
        self,
        *,
        rule: ServerSideEncryptionConfigurationRule,
    ):
        super().__init__(
            args=ServerSideEncryptionConfiguration.Args(
                rule=rule,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        rule: ServerSideEncryptionConfigurationRule = core.arg()


@core.schema
class CorsRule(core.Schema):

    allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    max_age_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]],
        allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]],
        allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        max_age_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CorsRule.Args(
                allowed_methods=allowed_methods,
                allowed_origins=allowed_origins,
                allowed_headers=allowed_headers,
                expose_headers=expose_headers,
                max_age_seconds=max_age_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allowed_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allowed_methods: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        allowed_origins: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        expose_headers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        max_age_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_s3_bucket", namespace="aws_s3")
class Bucket(core.Resource):

    acceleration_status: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    acl: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    bucket_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_regional_domain_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    cors_rule: Optional[Union[List[CorsRule], core.ArrayOut[CorsRule]]] = core.attr(
        CorsRule, default=None, computed=True, kind=core.Kind.array
    )

    force_destroy: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.attr(
        Grant, default=None, computed=True, kind=core.Kind.array
    )

    hosted_zone_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lifecycle_rule: Optional[Union[List[LifecycleRule], core.ArrayOut[LifecycleRule]]] = core.attr(
        LifecycleRule, default=None, computed=True, kind=core.Kind.array
    )

    logging: Optional[Logging] = core.attr(Logging, default=None, computed=True)

    object_lock_configuration: Optional[ObjectLockConfiguration] = core.attr(
        ObjectLockConfiguration, default=None, computed=True
    )

    object_lock_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_configuration: Optional[ReplicationConfiguration] = core.attr(
        ReplicationConfiguration, default=None, computed=True
    )

    request_payer: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    server_side_encryption_configuration: Optional[ServerSideEncryptionConfiguration] = core.attr(
        ServerSideEncryptionConfiguration, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    versioning: Optional[Versioning] = core.attr(Versioning, default=None, computed=True)

    website: Optional[Website] = core.attr(Website, default=None, computed=True)

    website_domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        acceleration_status: Optional[Union[str, core.StringOut]] = None,
        acl: Optional[Union[str, core.StringOut]] = None,
        arn: Optional[Union[str, core.StringOut]] = None,
        bucket: Optional[Union[str, core.StringOut]] = None,
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
        cors_rule: Optional[Union[List[CorsRule], core.ArrayOut[CorsRule]]] = None,
        force_destroy: Optional[Union[bool, core.BoolOut]] = None,
        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = None,
        hosted_zone_id: Optional[Union[str, core.StringOut]] = None,
        lifecycle_rule: Optional[Union[List[LifecycleRule], core.ArrayOut[LifecycleRule]]] = None,
        logging: Optional[Logging] = None,
        object_lock_configuration: Optional[ObjectLockConfiguration] = None,
        object_lock_enabled: Optional[Union[bool, core.BoolOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        replication_configuration: Optional[ReplicationConfiguration] = None,
        request_payer: Optional[Union[str, core.StringOut]] = None,
        server_side_encryption_configuration: Optional[ServerSideEncryptionConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        versioning: Optional[Versioning] = None,
        website: Optional[Website] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Bucket.Args(
                acceleration_status=acceleration_status,
                acl=acl,
                arn=arn,
                bucket=bucket,
                bucket_prefix=bucket_prefix,
                cors_rule=cors_rule,
                force_destroy=force_destroy,
                grant=grant,
                hosted_zone_id=hosted_zone_id,
                lifecycle_rule=lifecycle_rule,
                logging=logging,
                object_lock_configuration=object_lock_configuration,
                object_lock_enabled=object_lock_enabled,
                policy=policy,
                replication_configuration=replication_configuration,
                request_payer=request_payer,
                server_side_encryption_configuration=server_side_encryption_configuration,
                tags=tags,
                tags_all=tags_all,
                versioning=versioning,
                website=website,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        acceleration_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        acl: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cors_rule: Optional[Union[List[CorsRule], core.ArrayOut[CorsRule]]] = core.arg(default=None)

        force_destroy: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        grant: Optional[Union[List[Grant], core.ArrayOut[Grant]]] = core.arg(default=None)

        hosted_zone_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lifecycle_rule: Optional[
            Union[List[LifecycleRule], core.ArrayOut[LifecycleRule]]
        ] = core.arg(default=None)

        logging: Optional[Logging] = core.arg(default=None)

        object_lock_configuration: Optional[ObjectLockConfiguration] = core.arg(default=None)

        object_lock_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_configuration: Optional[ReplicationConfiguration] = core.arg(default=None)

        request_payer: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_side_encryption_configuration: Optional[
            ServerSideEncryptionConfiguration
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        versioning: Optional[Versioning] = core.arg(default=None)

        website: Optional[Website] = core.arg(default=None)
