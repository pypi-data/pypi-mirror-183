from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_db_instance", namespace="aws_rds")
class DsDbInstance(core.Data):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    allocated_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    auto_minor_version_upgrade: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    backup_retention_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    ca_cert_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_cluster_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_instance_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_instance_class: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_instance_identifier: Union[str, core.StringOut] = core.attr(str)

    db_instance_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    db_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_parameter_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_subnet_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled_cloudwatch_logs_exports: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    master_username: Union[str, core.StringOut] = core.attr(str, computed=True)

    monitoring_interval: Union[int, core.IntOut] = core.attr(int, computed=True)

    monitoring_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    multi_az: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    network_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    option_group_memberships: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    preferred_backup_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    preferred_maintenance_window: Union[str, core.StringOut] = core.attr(str, computed=True)

    publicly_accessible: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    replicate_source_db: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timezone: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        db_instance_identifier: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbInstance.Args(
                db_instance_identifier=db_instance_identifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_instance_identifier: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
