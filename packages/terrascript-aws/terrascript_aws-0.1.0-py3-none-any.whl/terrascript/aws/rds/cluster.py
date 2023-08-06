from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RestoreToPointInTime(core.Schema):

    restore_to_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    restore_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        source_cluster_identifier: Union[str, core.StringOut],
        restore_to_time: Optional[Union[str, core.StringOut]] = None,
        restore_type: Optional[Union[str, core.StringOut]] = None,
        use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=RestoreToPointInTime.Args(
                source_cluster_identifier=source_cluster_identifier,
                restore_to_time=restore_to_time,
                restore_type=restore_type,
                use_latest_restorable_time=use_latest_restorable_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        restore_to_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restore_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_cluster_identifier: Union[str, core.StringOut] = core.arg()

        use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ScalingConfiguration(core.Schema):

    auto_pause: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    max_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    min_capacity: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    seconds_until_auto_pause: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    timeout_action: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        auto_pause: Optional[Union[bool, core.BoolOut]] = None,
        max_capacity: Optional[Union[int, core.IntOut]] = None,
        min_capacity: Optional[Union[int, core.IntOut]] = None,
        seconds_until_auto_pause: Optional[Union[int, core.IntOut]] = None,
        timeout_action: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ScalingConfiguration.Args(
                auto_pause=auto_pause,
                max_capacity=max_capacity,
                min_capacity=min_capacity,
                seconds_until_auto_pause=seconds_until_auto_pause,
                timeout_action=timeout_action,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auto_pause: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        max_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_capacity: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        seconds_until_auto_pause: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        timeout_action: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Serverlessv2ScalingConfiguration(core.Schema):

    max_capacity: Union[float, core.FloatOut] = core.attr(float)

    min_capacity: Union[float, core.FloatOut] = core.attr(float)

    def __init__(
        self,
        *,
        max_capacity: Union[float, core.FloatOut],
        min_capacity: Union[float, core.FloatOut],
    ):
        super().__init__(
            args=Serverlessv2ScalingConfiguration.Args(
                max_capacity=max_capacity,
                min_capacity=min_capacity,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_capacity: Union[float, core.FloatOut] = core.arg()

        min_capacity: Union[float, core.FloatOut] = core.arg()


@core.schema
class S3Import(core.Schema):

    bucket_name: Union[str, core.StringOut] = core.attr(str)

    bucket_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ingestion_role: Union[str, core.StringOut] = core.attr(str)

    source_engine: Union[str, core.StringOut] = core.attr(str)

    source_engine_version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        bucket_name: Union[str, core.StringOut],
        ingestion_role: Union[str, core.StringOut],
        source_engine: Union[str, core.StringOut],
        source_engine_version: Union[str, core.StringOut],
        bucket_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Import.Args(
                bucket_name=bucket_name,
                ingestion_role=ingestion_role,
                source_engine=source_engine,
                source_engine_version=source_engine_version,
                bucket_prefix=bucket_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_name: Union[str, core.StringOut] = core.arg()

        bucket_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ingestion_role: Union[str, core.StringOut] = core.arg()

        source_engine: Union[str, core.StringOut] = core.arg()

        source_engine_version: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_rds_cluster", namespace="aws_rds")
class Cluster(core.Resource):

    allocated_storage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    backtrack_window: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    backup_retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    cluster_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    database_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    db_cluster_instance_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    db_instance_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_global_write_forwarding: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    enable_http_endpoint: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enabled_cloudwatch_logs_exports: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    master_password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    master_username: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    preferred_backup_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    reader_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_source_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    restore_to_point_in_time: Optional[RestoreToPointInTime] = core.attr(
        RestoreToPointInTime, default=None
    )

    s3_import: Optional[S3Import] = core.attr(S3Import, default=None)

    scaling_configuration: Optional[ScalingConfiguration] = core.attr(
        ScalingConfiguration, default=None
    )

    serverlessv2_scaling_configuration: Optional[Serverlessv2ScalingConfiguration] = core.attr(
        Serverlessv2ScalingConfiguration, default=None
    )

    skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    storage_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        allocated_storage: Optional[Union[int, core.IntOut]] = None,
        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        backtrack_window: Optional[Union[int, core.IntOut]] = None,
        backup_retention_period: Optional[Union[int, core.IntOut]] = None,
        cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = None,
        cluster_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        database_name: Optional[Union[str, core.StringOut]] = None,
        db_cluster_instance_class: Optional[Union[str, core.StringOut]] = None,
        db_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        db_instance_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        db_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        enable_global_write_forwarding: Optional[Union[bool, core.BoolOut]] = None,
        enable_http_endpoint: Optional[Union[bool, core.BoolOut]] = None,
        enabled_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_mode: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        global_cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = None,
        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        master_password: Optional[Union[str, core.StringOut]] = None,
        master_username: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        preferred_backup_window: Optional[Union[str, core.StringOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        replication_source_identifier: Optional[Union[str, core.StringOut]] = None,
        restore_to_point_in_time: Optional[RestoreToPointInTime] = None,
        s3_import: Optional[S3Import] = None,
        scaling_configuration: Optional[ScalingConfiguration] = None,
        serverlessv2_scaling_configuration: Optional[Serverlessv2ScalingConfiguration] = None,
        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        source_region: Optional[Union[str, core.StringOut]] = None,
        storage_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        storage_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                availability_zones=availability_zones,
                backtrack_window=backtrack_window,
                backup_retention_period=backup_retention_period,
                cluster_identifier=cluster_identifier,
                cluster_identifier_prefix=cluster_identifier_prefix,
                cluster_members=cluster_members,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                database_name=database_name,
                db_cluster_instance_class=db_cluster_instance_class,
                db_cluster_parameter_group_name=db_cluster_parameter_group_name,
                db_instance_parameter_group_name=db_instance_parameter_group_name,
                db_subnet_group_name=db_subnet_group_name,
                deletion_protection=deletion_protection,
                enable_global_write_forwarding=enable_global_write_forwarding,
                enable_http_endpoint=enable_http_endpoint,
                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                engine=engine,
                engine_mode=engine_mode,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                global_cluster_identifier=global_cluster_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                iam_roles=iam_roles,
                iops=iops,
                kms_key_id=kms_key_id,
                master_password=master_password,
                master_username=master_username,
                port=port,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                replication_source_identifier=replication_source_identifier,
                restore_to_point_in_time=restore_to_point_in_time,
                s3_import=s3_import,
                scaling_configuration=scaling_configuration,
                serverlessv2_scaling_configuration=serverlessv2_scaling_configuration,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                source_region=source_region,
                storage_encrypted=storage_encrypted,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                vpc_security_group_ids=vpc_security_group_ids,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allocated_storage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zones: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        backtrack_window: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        backup_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_identifier_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_members: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        database_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_cluster_instance_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_cluster_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        db_instance_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_global_write_forwarding: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_http_endpoint: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enabled_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        iam_roles: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        master_username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replication_source_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restore_to_point_in_time: Optional[RestoreToPointInTime] = core.arg(default=None)

        s3_import: Optional[S3Import] = core.arg(default=None)

        scaling_configuration: Optional[ScalingConfiguration] = core.arg(default=None)

        serverlessv2_scaling_configuration: Optional[Serverlessv2ScalingConfiguration] = core.arg(
            default=None
        )

        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
