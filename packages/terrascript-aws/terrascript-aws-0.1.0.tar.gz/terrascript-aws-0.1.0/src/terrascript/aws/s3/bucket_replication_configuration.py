from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DeleteMarkerReplication(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DeleteMarkerReplication.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.schema
class ReplicaModifications(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ReplicaModifications.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.schema
class SseKmsEncryptedObjects(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SseKmsEncryptedObjects.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.schema
class SourceSelectionCriteria(core.Schema):

    replica_modifications: Optional[ReplicaModifications] = core.attr(
        ReplicaModifications, default=None
    )

    sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = core.attr(
        SseKmsEncryptedObjects, default=None
    )

    def __init__(
        self,
        *,
        replica_modifications: Optional[ReplicaModifications] = None,
        sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = None,
    ):
        super().__init__(
            args=SourceSelectionCriteria.Args(
                replica_modifications=replica_modifications,
                sse_kms_encrypted_objects=sse_kms_encrypted_objects,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replica_modifications: Optional[ReplicaModifications] = core.arg(default=None)

        sse_kms_encrypted_objects: Optional[SseKmsEncryptedObjects] = core.arg(default=None)


@core.schema
class ExistingObjectReplication(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ExistingObjectReplication.Args(
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()


@core.schema
class And(core.Schema):

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
            args=And.Args(
                prefix=prefix,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)


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
class Filter(core.Schema):

    and_: Optional[And] = core.attr(And, default=None, alias="and")

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag: Optional[Tag] = core.attr(Tag, default=None)

    def __init__(
        self,
        *,
        and_: Optional[And] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        tag: Optional[Tag] = None,
    ):
        super().__init__(
            args=Filter.Args(
                and_=and_,
                prefix=prefix,
                tag=tag,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        and_: Optional[And] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag: Optional[Tag] = core.arg(default=None)


@core.schema
class Time(core.Schema):

    minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        minutes: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Time.Args(
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class ReplicationTime(core.Schema):

    status: Union[str, core.StringOut] = core.attr(str)

    time: Time = core.attr(Time)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
        time: Time,
    ):
        super().__init__(
            args=ReplicationTime.Args(
                status=status,
                time=time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        status: Union[str, core.StringOut] = core.arg()

        time: Time = core.arg()


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
class EncryptionConfiguration(core.Schema):

    replica_kms_key_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        replica_kms_key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionConfiguration.Args(
                replica_kms_key_id=replica_kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        replica_kms_key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class EventThreshold(core.Schema):

    minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        minutes: Union[int, core.IntOut],
    ):
        super().__init__(
            args=EventThreshold.Args(
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class Metrics(core.Schema):

    event_threshold: Optional[EventThreshold] = core.attr(EventThreshold, default=None)

    status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        status: Union[str, core.StringOut],
        event_threshold: Optional[EventThreshold] = None,
    ):
        super().__init__(
            args=Metrics.Args(
                status=status,
                event_threshold=event_threshold,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        event_threshold: Optional[EventThreshold] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class Destination(core.Schema):

    access_control_translation: Optional[AccessControlTranslation] = core.attr(
        AccessControlTranslation, default=None
    )

    account: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket: Union[str, core.StringOut] = core.attr(str)

    encryption_configuration: Optional[EncryptionConfiguration] = core.attr(
        EncryptionConfiguration, default=None
    )

    metrics: Optional[Metrics] = core.attr(Metrics, default=None)

    replication_time: Optional[ReplicationTime] = core.attr(ReplicationTime, default=None)

    storage_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket: Union[str, core.StringOut],
        access_control_translation: Optional[AccessControlTranslation] = None,
        account: Optional[Union[str, core.StringOut]] = None,
        encryption_configuration: Optional[EncryptionConfiguration] = None,
        metrics: Optional[Metrics] = None,
        replication_time: Optional[ReplicationTime] = None,
        storage_class: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Destination.Args(
                bucket=bucket,
                access_control_translation=access_control_translation,
                account=account,
                encryption_configuration=encryption_configuration,
                metrics=metrics,
                replication_time=replication_time,
                storage_class=storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_control_translation: Optional[AccessControlTranslation] = core.arg(default=None)

        account: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket: Union[str, core.StringOut] = core.arg()

        encryption_configuration: Optional[EncryptionConfiguration] = core.arg(default=None)

        metrics: Optional[Metrics] = core.arg(default=None)

        replication_time: Optional[ReplicationTime] = core.arg(default=None)

        storage_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Rule(core.Schema):

    delete_marker_replication: Optional[DeleteMarkerReplication] = core.attr(
        DeleteMarkerReplication, default=None
    )

    destination: Destination = core.attr(Destination)

    existing_object_replication: Optional[ExistingObjectReplication] = core.attr(
        ExistingObjectReplication, default=None
    )

    filter: Optional[Filter] = core.attr(Filter, default=None)

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        delete_marker_replication: Optional[DeleteMarkerReplication] = None,
        existing_object_replication: Optional[ExistingObjectReplication] = None,
        filter: Optional[Filter] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[int, core.IntOut]] = None,
        source_selection_criteria: Optional[SourceSelectionCriteria] = None,
    ):
        super().__init__(
            args=Rule.Args(
                destination=destination,
                status=status,
                delete_marker_replication=delete_marker_replication,
                existing_object_replication=existing_object_replication,
                filter=filter,
                id=id,
                prefix=prefix,
                priority=priority,
                source_selection_criteria=source_selection_criteria,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_marker_replication: Optional[DeleteMarkerReplication] = core.arg(default=None)

        destination: Destination = core.arg()

        existing_object_replication: Optional[ExistingObjectReplication] = core.arg(default=None)

        filter: Optional[Filter] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        source_selection_criteria: Optional[SourceSelectionCriteria] = core.arg(default=None)

        status: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_s3_bucket_replication_configuration", namespace="aws_s3")
class BucketReplicationConfiguration(core.Resource):

    bucket: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role: Union[str, core.StringOut] = core.attr(str)

    rule: Union[List[Rule], core.ArrayOut[Rule]] = core.attr(Rule, kind=core.Kind.array)

    token: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        bucket: Union[str, core.StringOut],
        role: Union[str, core.StringOut],
        rule: Union[List[Rule], core.ArrayOut[Rule]],
        token: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BucketReplicationConfiguration.Args(
                bucket=bucket,
                role=role,
                rule=rule,
                token=token,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bucket: Union[str, core.StringOut] = core.arg()

        role: Union[str, core.StringOut] = core.arg()

        rule: Union[List[Rule], core.ArrayOut[Rule]] = core.arg()

        token: Optional[Union[str, core.StringOut]] = core.arg(default=None)
