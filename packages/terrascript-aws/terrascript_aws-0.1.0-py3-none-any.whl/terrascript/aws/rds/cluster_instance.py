from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_rds_cluster_instance", namespace="aws_rds")
class ClusterInstance(core.Resource):

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ca_cert_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    db_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    dbi_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version_actual: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    identifier_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_class: Union[str, core.StringOut] = core.attr(str)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    monitoring_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    monitoring_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    performance_insights_retention_period: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    preferred_backup_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    promotion_tier: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    storage_encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    writer: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_identifier: Union[str, core.StringOut],
        instance_class: Union[str, core.StringOut],
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        ca_cert_identifier: Optional[Union[str, core.StringOut]] = None,
        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        db_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        db_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        identifier: Optional[Union[str, core.StringOut]] = None,
        identifier_prefix: Optional[Union[str, core.StringOut]] = None,
        monitoring_interval: Optional[Union[int, core.IntOut]] = None,
        monitoring_role_arn: Optional[Union[str, core.StringOut]] = None,
        performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = None,
        performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        performance_insights_retention_period: Optional[Union[int, core.IntOut]] = None,
        preferred_backup_window: Optional[Union[str, core.StringOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        promotion_tier: Optional[Union[int, core.IntOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ClusterInstance.Args(
                cluster_identifier=cluster_identifier,
                instance_class=instance_class,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                ca_cert_identifier=ca_cert_identifier,
                copy_tags_to_snapshot=copy_tags_to_snapshot,
                db_parameter_group_name=db_parameter_group_name,
                db_subnet_group_name=db_subnet_group_name,
                engine=engine,
                engine_version=engine_version,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                monitoring_interval=monitoring_interval,
                monitoring_role_arn=monitoring_role_arn,
                performance_insights_enabled=performance_insights_enabled,
                performance_insights_kms_key_id=performance_insights_kms_key_id,
                performance_insights_retention_period=performance_insights_retention_period,
                preferred_backup_window=preferred_backup_window,
                preferred_maintenance_window=preferred_maintenance_window,
                promotion_tier=promotion_tier,
                publicly_accessible=publicly_accessible,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        apply_immediately: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ca_cert_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        copy_tags_to_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        db_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identifier_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_class: Union[str, core.StringOut] = core.arg()

        monitoring_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        monitoring_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        performance_insights_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        performance_insights_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        performance_insights_retention_period: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        preferred_backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        promotion_tier: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
