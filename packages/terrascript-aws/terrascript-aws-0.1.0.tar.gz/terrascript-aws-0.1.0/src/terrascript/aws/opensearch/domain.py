from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DomainEndpointOptions(core.Schema):

    custom_endpoint: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    custom_endpoint_certificate_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    custom_endpoint_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enforce_https: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tls_security_policy: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        custom_endpoint: Optional[Union[str, core.StringOut]] = None,
        custom_endpoint_certificate_arn: Optional[Union[str, core.StringOut]] = None,
        custom_endpoint_enabled: Optional[Union[bool, core.BoolOut]] = None,
        enforce_https: Optional[Union[bool, core.BoolOut]] = None,
        tls_security_policy: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DomainEndpointOptions.Args(
                custom_endpoint=custom_endpoint,
                custom_endpoint_certificate_arn=custom_endpoint_certificate_arn,
                custom_endpoint_enabled=custom_endpoint_enabled,
                enforce_https=enforce_https,
                tls_security_policy=tls_security_policy,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        custom_endpoint_certificate_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        custom_endpoint_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enforce_https: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tls_security_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class NodeToNodeEncryption(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

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
class ZoneAwarenessConfig(core.Schema):

    availability_zone_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        availability_zone_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ZoneAwarenessConfig.Args(
                availability_zone_count=availability_zone_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zone_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ColdStorageOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ColdStorageOptions.Args(
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ClusterConfig(core.Schema):

    cold_storage_options: Optional[ColdStorageOptions] = core.attr(
        ColdStorageOptions, default=None, computed=True
    )

    dedicated_master_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    dedicated_master_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    dedicated_master_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    warm_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    warm_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    warm_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    zone_awareness_config: Optional[ZoneAwarenessConfig] = core.attr(
        ZoneAwarenessConfig, default=None
    )

    zone_awareness_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cold_storage_options: Optional[ColdStorageOptions] = None,
        dedicated_master_count: Optional[Union[int, core.IntOut]] = None,
        dedicated_master_enabled: Optional[Union[bool, core.BoolOut]] = None,
        dedicated_master_type: Optional[Union[str, core.StringOut]] = None,
        instance_count: Optional[Union[int, core.IntOut]] = None,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        warm_count: Optional[Union[int, core.IntOut]] = None,
        warm_enabled: Optional[Union[bool, core.BoolOut]] = None,
        warm_type: Optional[Union[str, core.StringOut]] = None,
        zone_awareness_config: Optional[ZoneAwarenessConfig] = None,
        zone_awareness_enabled: Optional[Union[bool, core.BoolOut]] = None,
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
                warm_enabled=warm_enabled,
                warm_type=warm_type,
                zone_awareness_config=zone_awareness_config,
                zone_awareness_enabled=zone_awareness_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cold_storage_options: Optional[ColdStorageOptions] = core.arg(default=None)

        dedicated_master_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        dedicated_master_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        dedicated_master_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        warm_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        warm_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        warm_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zone_awareness_config: Optional[ZoneAwarenessConfig] = core.arg(default=None)

        zone_awareness_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class CognitoOptions(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    identity_pool_id: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        identity_pool_id: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CognitoOptions.Args(
                identity_pool_id=identity_pool_id,
                role_arn=role_arn,
                user_pool_id=user_pool_id,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        identity_pool_id: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        user_pool_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Duration(core.Schema):

    unit: Union[str, core.StringOut] = core.attr(str)

    value: Union[int, core.IntOut] = core.attr(int)

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

    cron_expression_for_recurrence: Union[str, core.StringOut] = core.attr(str)

    duration: Duration = core.attr(Duration)

    start_at: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cron_expression_for_recurrence: Union[str, core.StringOut],
        duration: Duration,
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

        duration: Duration = core.arg()

        start_at: Union[str, core.StringOut] = core.arg()


@core.schema
class AutoTuneOptions(core.Schema):

    desired_state: Union[str, core.StringOut] = core.attr(str)

    maintenance_schedule: Optional[
        Union[List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]]
    ] = core.attr(MaintenanceSchedule, default=None, computed=True, kind=core.Kind.array)

    rollback_on_disable: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        desired_state: Union[str, core.StringOut],
        maintenance_schedule: Optional[
            Union[List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]]
        ] = None,
        rollback_on_disable: Optional[Union[str, core.StringOut]] = None,
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

        maintenance_schedule: Optional[
            Union[List[MaintenanceSchedule], core.ArrayOut[MaintenanceSchedule]]
        ] = core.arg(default=None)

        rollback_on_disable: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SnapshotOptions(core.Schema):

    automated_snapshot_start_hour: Union[int, core.IntOut] = core.attr(int)

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
class LogPublishingOptions(core.Schema):

    cloudwatch_log_group_arn: Union[str, core.StringOut] = core.attr(str)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    log_type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cloudwatch_log_group_arn: Union[str, core.StringOut],
        log_type: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=LogPublishingOptions.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                log_type=log_type,
                enabled=enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_type: Union[str, core.StringOut] = core.arg()


@core.schema
class EncryptAtRest(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EncryptAtRest.Args(
                enabled=enabled,
                kms_key_id=kms_key_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class VpcOptions(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcOptions.Args(
                availability_zones=availability_zones,
                vpc_id=vpc_id,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class EbsOptions(core.Schema):

    ebs_enabled: Union[bool, core.BoolOut] = core.attr(bool)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        ebs_enabled: Union[bool, core.BoolOut],
        iops: Optional[Union[int, core.IntOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
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

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class MasterUserOptions(core.Schema):

    master_user_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_user_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        master_user_arn: Optional[Union[str, core.StringOut]] = None,
        master_user_name: Optional[Union[str, core.StringOut]] = None,
        master_user_password: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MasterUserOptions.Args(
                master_user_arn=master_user_arn,
                master_user_name=master_user_name,
                master_user_password=master_user_password,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        master_user_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_user_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AdvancedSecurityOptions(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    internal_user_database_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    master_user_options: Optional[MasterUserOptions] = core.attr(MasterUserOptions, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        internal_user_database_enabled: Optional[Union[bool, core.BoolOut]] = None,
        master_user_options: Optional[MasterUserOptions] = None,
    ):
        super().__init__(
            args=AdvancedSecurityOptions.Args(
                enabled=enabled,
                internal_user_database_enabled=internal_user_database_enabled,
                master_user_options=master_user_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        internal_user_database_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        master_user_options: Optional[MasterUserOptions] = core.arg(default=None)


@core.resource(type="aws_opensearch_domain", namespace="aws_opensearch")
class Domain(core.Resource):

    access_policies: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    advanced_options: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    advanced_security_options: Optional[AdvancedSecurityOptions] = core.attr(
        AdvancedSecurityOptions, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_tune_options: Optional[AutoTuneOptions] = core.attr(
        AutoTuneOptions, default=None, computed=True
    )

    cluster_config: Optional[ClusterConfig] = core.attr(ClusterConfig, default=None, computed=True)

    cognito_options: Optional[CognitoOptions] = core.attr(CognitoOptions, default=None)

    domain_endpoint_options: Optional[DomainEndpointOptions] = core.attr(
        DomainEndpointOptions, default=None, computed=True
    )

    domain_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    ebs_options: Optional[EbsOptions] = core.attr(EbsOptions, default=None, computed=True)

    encrypt_at_rest: Optional[EncryptAtRest] = core.attr(EncryptAtRest, default=None, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kibana_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_publishing_options: Optional[
        Union[List[LogPublishingOptions], core.ArrayOut[LogPublishingOptions]]
    ] = core.attr(LogPublishingOptions, default=None, kind=core.Kind.array)

    node_to_node_encryption: Optional[NodeToNodeEncryption] = core.attr(
        NodeToNodeEncryption, default=None, computed=True
    )

    snapshot_options: Optional[SnapshotOptions] = core.attr(SnapshotOptions, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_options: Optional[VpcOptions] = core.attr(VpcOptions, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        access_policies: Optional[Union[str, core.StringOut]] = None,
        advanced_options: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        advanced_security_options: Optional[AdvancedSecurityOptions] = None,
        auto_tune_options: Optional[AutoTuneOptions] = None,
        cluster_config: Optional[ClusterConfig] = None,
        cognito_options: Optional[CognitoOptions] = None,
        domain_endpoint_options: Optional[DomainEndpointOptions] = None,
        ebs_options: Optional[EbsOptions] = None,
        encrypt_at_rest: Optional[EncryptAtRest] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        log_publishing_options: Optional[
            Union[List[LogPublishingOptions], core.ArrayOut[LogPublishingOptions]]
        ] = None,
        node_to_node_encryption: Optional[NodeToNodeEncryption] = None,
        snapshot_options: Optional[SnapshotOptions] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_options: Optional[VpcOptions] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Domain.Args(
                domain_name=domain_name,
                access_policies=access_policies,
                advanced_options=advanced_options,
                advanced_security_options=advanced_security_options,
                auto_tune_options=auto_tune_options,
                cluster_config=cluster_config,
                cognito_options=cognito_options,
                domain_endpoint_options=domain_endpoint_options,
                ebs_options=ebs_options,
                encrypt_at_rest=encrypt_at_rest,
                engine_version=engine_version,
                log_publishing_options=log_publishing_options,
                node_to_node_encryption=node_to_node_encryption,
                snapshot_options=snapshot_options,
                tags=tags,
                tags_all=tags_all,
                vpc_options=vpc_options,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policies: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        advanced_options: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        advanced_security_options: Optional[AdvancedSecurityOptions] = core.arg(default=None)

        auto_tune_options: Optional[AutoTuneOptions] = core.arg(default=None)

        cluster_config: Optional[ClusterConfig] = core.arg(default=None)

        cognito_options: Optional[CognitoOptions] = core.arg(default=None)

        domain_endpoint_options: Optional[DomainEndpointOptions] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        ebs_options: Optional[EbsOptions] = core.arg(default=None)

        encrypt_at_rest: Optional[EncryptAtRest] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_publishing_options: Optional[
            Union[List[LogPublishingOptions], core.ArrayOut[LogPublishingOptions]]
        ] = core.arg(default=None)

        node_to_node_encryption: Optional[NodeToNodeEncryption] = core.arg(default=None)

        snapshot_options: Optional[SnapshotOptions] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_options: Optional[VpcOptions] = core.arg(default=None)
