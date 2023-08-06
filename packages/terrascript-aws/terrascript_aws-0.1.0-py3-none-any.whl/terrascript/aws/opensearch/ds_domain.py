from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Duration(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        unit: Union[str, core.StringOut],
        value: Union[int, core.IntOut],
    ):
        super().__init__(
            args=Duration.Args(
                unit=unit,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        unit: Union[str, core.StringOut] = core.arg()

        value: Union[int, core.IntOut] = core.arg()


@core.schema
class MaintenanceSchedule(core.Schema):

    cron_expression_for_recurrence: Union[str, core.StringOut] = core.attr(str, computed=True)

    duration: Union[List[Duration], core.ArrayOut[Duration]] = core.attr(
        Duration, computed=True, kind=core.Kind.array
    )

    start_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cron_expression_for_recurrence: Union[str, core.StringOut],
        duration: Union[List[Duration], core.ArrayOut[Duration]],
        start_at: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MaintenanceSchedule.Args(
                cron_expression_for_recurrence=cron_expression_for_recurrence,
                duration=duration,
                start_at=start_at,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cron_expression_for_recurrence: Union[str, core.StringOut] = core.arg()

        duration: Union[List[Duration], core.ArrayOut[Duration]] = core.arg()

        start_at: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoTuneOptions(core.Schema):

    desired_state: Union[str, core.StringOut] = core.attr(str, computed=True)

    maintenance_schedule: Union[
        List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]
    ] = core.attr(MaintenanceSchedule, computed=True, kind=core.Kind.array)

    rollback_on_disable: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        desired_state: Union[str, core.StringOut],
        maintenance_schedule: Union[List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]],
        rollback_on_disable: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AutoTuneOptions.Args(
                desired_state=desired_state,
                maintenance_schedule=maintenance_schedule,
                rollback_on_disable=rollback_on_disable,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_state: Union[str, core.StringOut] = core.arg()

        maintenance_schedule: Union[
            List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]
        ] = core.arg()

        rollback_on_disable: Union[str, core.StringOut] = core.arg()


@core.schema
class SnapshotOptions(core.Schema):

    automated_snapshot_start_hour: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        automated_snapshot_start_hour: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SnapshotOptions.Args(
                automated_snapshot_start_hour=automated_snapshot_start_hour,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automated_snapshot_start_hour: Union[int, core.IntOut] = core.arg()


@core.schema
class EbsOptions(core.Schema):

    ebs_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        ebs_enabled: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        throughput: Union[int, core.IntOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EbsOptions.Args(
                ebs_enabled=ebs_enabled,
                iops=iops,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_enabled: Union[bool, core.BoolOut] = core.arg()

        iops: Union[int, core.IntOut] = core.arg()

        throughput: Union[int, core.IntOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.schema
class CognitoOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    identity_pool_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_pool_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        identity_pool_id: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CognitoOptions.Args(
                enabled=enabled,
                identity_pool_id=identity_pool_id,
                role_arn=role_arn,
                user_pool_id=user_pool_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        identity_pool_id: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        user_pool_id: Union[str, core.StringOut] = core.arg()


@core.schema
class ZoneAwarenessConfig(core.Schema):

    availability_zone_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        availability_zone_count: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ZoneAwarenessConfig.Args(
                availability_zone_count=availability_zone_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_count: Union[int, core.IntOut] = core.arg()


@core.schema
class ColdStorageOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=ColdStorageOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class ClusterConfig(core.Schema):

    cold_storage_options: Union[
        List[ColdStorageOptions], core.ArrayOut[ColdStorageOptions]
    ] = core.attr(ColdStorageOptions, computed=True, kind=core.Kind.array)

    dedicated_master_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    dedicated_master_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    dedicated_master_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    warm_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    warm_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    warm_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    zone_awareness_config: Union[
        List[ZoneAwarenessConfig], core.ArrayOut[ZoneAwarenessConfig]
    ] = core.attr(ZoneAwarenessConfig, computed=True, kind=core.Kind.array)

    zone_awareness_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        cold_storage_options: Union[List[ColdStorageOptions], core.ArrayOut[ColdStorageOptions]],
        dedicated_master_count: Union[int, core.IntOut],
        dedicated_master_enabled: Union[bool, core.BoolOut],
        dedicated_master_type: Union[str, core.StringOut],
        instance_count: Union[int, core.IntOut],
        instance_type: Union[str, core.StringOut],
        warm_count: Union[int, core.IntOut],
        warm_type: Union[str, core.StringOut],
        zone_awareness_config: Union[List[ZoneAwarenessConfig], core.ArrayOut[ZoneAwarenessConfig]],
        zone_awareness_enabled: Union[bool, core.BoolOut],
        warm_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ClusterConfig.Args(
                cold_storage_options=cold_storage_options,
                dedicated_master_count=dedicated_master_count,
                dedicated_master_enabled=dedicated_master_enabled,
                dedicated_master_type=dedicated_master_type,
                instance_count=instance_count,
                instance_type=instance_type,
                warm_count=warm_count,
                warm_type=warm_type,
                zone_awareness_config=zone_awareness_config,
                zone_awareness_enabled=zone_awareness_enabled,
                warm_enabled=warm_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cold_storage_options: Union[
            List[ColdStorageOptions], core.ArrayOut[ColdStorageOptions]
        ] = core.arg()

        dedicated_master_count: Union[int, core.IntOut] = core.arg()

        dedicated_master_enabled: Union[bool, core.BoolOut] = core.arg()

        dedicated_master_type: Union[str, core.StringOut] = core.arg()

        instance_count: Union[int, core.IntOut] = core.arg()

        instance_type: Union[str, core.StringOut] = core.arg()

        warm_count: Union[int, core.IntOut] = core.arg()

        warm_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        warm_type: Union[str, core.StringOut] = core.arg()

        zone_awareness_config: Union[
            List[ZoneAwarenessConfig], core.ArrayOut[ZoneAwarenessConfig]
        ] = core.arg()

        zone_awareness_enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class EncryptionAtRest(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        kms_key_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EncryptionAtRest.Args(
                enabled=enabled,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        kms_key_id: Union[str, core.StringOut] = core.arg()


@core.schema
class LogPublishingOptions(core.Schema):

    cloudwatch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    log_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: Union[str, core.StringOut],
        enabled: Union[bool, core.BoolOut],
        log_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LogPublishingOptions.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                enabled=enabled,
                log_type=log_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Union[bool, core.BoolOut] = core.arg()

        log_type: Union[str, core.StringOut] = core.arg()


@core.schema
class NodeToNodeEncryption(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=NodeToNodeEncryption.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class AdvancedSecurityOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    internal_user_database_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        internal_user_database_enabled: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=AdvancedSecurityOptions.Args(
                enabled=enabled,
                internal_user_database_enabled=internal_user_database_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        internal_user_database_enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class VpcOptions(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcOptions.Args(
                availability_zones=availability_zones,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_opensearch_domain", namespace="aws_opensearch")
class DsDomain(core.Data):

    access_policies: Union[str, core.StringOut] = core.attr(str, computed=True)

    advanced_options: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    advanced_security_options: Union[
        List[AdvancedSecurityOptions], core.ArrayOut[AdvancedSecurityOptions]
    ] = core.attr(AdvancedSecurityOptions, computed=True, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_tune_options: Union[List[AutoTuneOptions], core.ArrayOut[AutoTuneOptions]] = core.attr(
        AutoTuneOptions, computed=True, kind=core.Kind.array
    )

    cluster_config: Union[List[ClusterConfig], core.ArrayOut[ClusterConfig]] = core.attr(
        ClusterConfig, computed=True, kind=core.Kind.array
    )

    cognito_options: Union[List[CognitoOptions], core.ArrayOut[CognitoOptions]] = core.attr(
        CognitoOptions, computed=True, kind=core.Kind.array
    )

    created: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    deleted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    domain_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    ebs_options: Union[List[EbsOptions], core.ArrayOut[EbsOptions]] = core.attr(
        EbsOptions, computed=True, kind=core.Kind.array
    )

    encryption_at_rest: Union[List[EncryptionAtRest], core.ArrayOut[EncryptionAtRest]] = core.attr(
        EncryptionAtRest, computed=True, kind=core.Kind.array
    )

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kibana_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_publishing_options: Union[
        List[LogPublishingOptions], core.ArrayOut[LogPublishingOptions]
    ] = core.attr(LogPublishingOptions, computed=True, kind=core.Kind.array)

    node_to_node_encryption: Union[
        List[NodeToNodeEncryption], core.ArrayOut[NodeToNodeEncryption]
    ] = core.attr(NodeToNodeEncryption, computed=True, kind=core.Kind.array)

    processing: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    snapshot_options: Union[List[SnapshotOptions], core.ArrayOut[SnapshotOptions]] = core.attr(
        SnapshotOptions, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_options: Union[List[VpcOptions], core.ArrayOut[VpcOptions]] = core.attr(
        VpcOptions, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDomain.Args(
                domain_name=domain_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        domain_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
