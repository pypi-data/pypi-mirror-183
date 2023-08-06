from typing import Dict, List, Optional, Union

import terrascript.core as core


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


@core.schema
class RestoreToPointInTime(core.Schema):

    restore_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_db_instance_automated_backups_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    source_db_instance_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    source_dbi_resource_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        restore_time: Optional[Union[str, core.StringOut]] = None,
        source_db_instance_automated_backups_arn: Optional[Union[str, core.StringOut]] = None,
        source_db_instance_identifier: Optional[Union[str, core.StringOut]] = None,
        source_dbi_resource_id: Optional[Union[str, core.StringOut]] = None,
        use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=RestoreToPointInTime.Args(
                restore_time=restore_time,
                source_db_instance_automated_backups_arn=source_db_instance_automated_backups_arn,
                source_db_instance_identifier=source_db_instance_identifier,
                source_dbi_resource_id=source_dbi_resource_id,
                use_latest_restorable_time=use_latest_restorable_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        restore_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_db_instance_automated_backups_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        source_db_instance_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_dbi_resource_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        use_latest_restorable_time: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_db_instance", namespace="aws_rds")
class DbInstance(core.Resource):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    allocated_storage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    backup_retention_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    backup_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ca_cert_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    character_set_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    customer_owned_ip_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    db_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    delete_automated_backups: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    deletion_protection: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_iam_role_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled_cloudwatch_logs_exports: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    identifier_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_class: Union[str, core.StringOut] = core.attr(str)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    latest_restorable_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_model: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    max_allocated_storage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    monitoring_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    monitoring_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    multi_az: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    nchar_character_set_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    network_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    option_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    password: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    performance_insights_retention_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    replica_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    replicas: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replicate_source_db: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    restore_to_point_in_time: Optional[RestoreToPointInTime] = core.attr(
        RestoreToPointInTime, default=None
    )

    s3_import: Optional[S3Import] = core.attr(S3Import, default=None)

    security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    storage_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timezone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    username: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_class: Union[str, core.StringOut],
        allocated_storage: Optional[Union[int, core.IntOut]] = None,
        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        backup_retention_period: Optional[Union[int, core.IntOut]] = None,
        backup_window: Optional[Union[str, core.StringOut]] = None,
        ca_cert_identifier: Optional[Union[str, core.StringOut]] = None,
        character_set_name: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        customer_owned_ip_enabled: Optional[Union[bool, core.BoolOut]] = None,
        db_name: Optional[Union[str, core.StringOut]] = None,
        db_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        delete_automated_backups: Optional[Union[bool, core.BoolOut]] = None,
        deletion_protection: Optional[Union[bool, core.BoolOut]] = None,
        domain: Optional[Union[str, core.StringOut]] = None,
        domain_iam_role_name: Optional[Union[str, core.StringOut]] = None,
        enabled_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = None,
        identifier: Optional[Union[str, core.StringOut]] = None,
        identifier_prefix: Optional[Union[str, core.StringOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        license_model: Optional[Union[str, core.StringOut]] = None,
        maintenance_window: Optional[Union[str, core.StringOut]] = None,
        max_allocated_storage: Optional[Union[int, core.IntOut]] = None,
        monitoring_interval: Optional[Union[int, core.IntOut]] = None,
        monitoring_role_arn: Optional[Union[str, core.StringOut]] = None,
        multi_az: Optional[Union[bool, core.BoolOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        nchar_character_set_name: Optional[Union[str, core.StringOut]] = None,
        network_type: Optional[Union[str, core.StringOut]] = None,
        option_group_name: Optional[Union[str, core.StringOut]] = None,
        parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        password: Optional[Union[str, core.StringOut]] = None,
        performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = None,
        performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        performance_insights_retention_period: Optional[Union[int, core.IntOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        replica_mode: Optional[Union[str, core.StringOut]] = None,
        replicate_source_db: Optional[Union[str, core.StringOut]] = None,
        restore_to_point_in_time: Optional[RestoreToPointInTime] = None,
        s3_import: Optional[S3Import] = None,
        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        storage_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        storage_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timezone: Optional[Union[str, core.StringOut]] = None,
        username: Optional[Union[str, core.StringOut]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbInstance.Args(
                instance_class=instance_class,
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                backup_retention_period=backup_retention_period,
                backup_window=backup_window,
                ca_cert_identifier=ca_cert_identifier,
                character_set_name=character_set_name,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                customer_owned_ip_enabled=customer_owned_ip_enabled,
                db_name=db_name,
                db_subnet_group_name=db_subnet_group_name,
                delete_automated_backups=delete_automated_backups,
                deletion_protection=deletion_protection,
                domain=domain,
                domain_iam_role_name=domain_iam_role_name,
                enabled_cloudwatch_logs_exports=enabled_cloudwatch_logs_exports,
                engine=engine,
                engine_version=engine_version,
                final_snapshot_identifier=final_snapshot_identifier,
                iam_database_authentication_enabled=iam_database_authentication_enabled,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                iops=iops,
                kms_key_id=kms_key_id,
                license_model=license_model,
                maintenance_window=maintenance_window,
                max_allocated_storage=max_allocated_storage,
                monitoring_interval=monitoring_interval,
                monitoring_role_arn=monitoring_role_arn,
                multi_az=multi_az,
                name=name,
                nchar_character_set_name=nchar_character_set_name,
                network_type=network_type,
                option_group_name=option_group_name,
                parameter_group_name=parameter_group_name,
                password=password,
                performance_insights_enabled=performance_insights_enabled,
                performance_insights_kms_key_id=performance_insights_kms_key_id,
                performance_insights_retention_period=performance_insights_retention_period,
                port=port,
                publicly_accessible=publicly_accessible,
                replica_mode=replica_mode,
                replicate_source_db=replicate_source_db,
                restore_to_point_in_time=restore_to_point_in_time,
                s3_import=s3_import,
                security_group_names=security_group_names,
                skip_final_snapshot=skip_final_snapshot,
                snapshot_identifier=snapshot_identifier,
                storage_encrypted=storage_encrypted,
                storage_type=storage_type,
                tags=tags,
                tags_all=tags_all,
                timezone=timezone,
                username=username,
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

        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        backup_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ca_cert_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        character_set_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        customer_owned_ip_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        db_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        delete_automated_backups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        deletion_protection: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_iam_role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled_cloudwatch_logs_exports: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        final_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_database_authentication_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identifier_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_class: Union[str, core.StringOut] = core.arg()

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        license_model: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_allocated_storage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        monitoring_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        monitoring_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_az: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        nchar_character_set_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        option_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        password: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        performance_insights_retention_period: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        replica_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        replicate_source_db: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        restore_to_point_in_time: Optional[RestoreToPointInTime] = core.arg(default=None)

        s3_import: Optional[S3Import] = core.arg(default=None)

        security_group_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        skip_final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        storage_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timezone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        username: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
