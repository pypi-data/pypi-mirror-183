from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dms_replication_instance", namespace="aws_dms")
class ReplicationInstance(core.Resource):

    allocated_storage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    multi_az: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    replication_instance_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_instance_class: Union[str, core.StringOut] = core.attr(str)

    replication_instance_id: Union[str, core.StringOut] = core.attr(str)

    replication_instance_private_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replication_instance_public_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    replication_subnet_group_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

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
        replication_instance_class: Union[str, core.StringOut],
        replication_instance_id: Union[str, core.StringOut],
        allocated_storage: Optional[Union[int, core.IntOut]] = None,
        allow_major_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        apply_immediately: Optional[Union[bool, core.BoolOut]] = None,
        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = None,
        availability_zone: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        multi_az: Optional[Union[bool, core.BoolOut]] = None,
        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = None,
        publicly_accessible: Optional[Union[bool, core.BoolOut]] = None,
        replication_subnet_group_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationInstance.Args(
                replication_instance_class=replication_instance_class,
                replication_instance_id=replication_instance_id,
                allocated_storage=allocated_storage,
                allow_major_version_upgrade=allow_major_version_upgrade,
                apply_immediately=apply_immediately,
                auto_minor_version_upgrade=auto_minor_version_upgrade,
                availability_zone=availability_zone,
                engine_version=engine_version,
                kms_key_arn=kms_key_arn,
                multi_az=multi_az,
                preferred_maintenance_window=preferred_maintenance_window,
                publicly_accessible=publicly_accessible,
                replication_subnet_group_id=replication_subnet_group_id,
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

        auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        availability_zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_az: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        replication_instance_class: Union[str, core.StringOut] = core.arg()

        replication_instance_id: Union[str, core.StringOut] = core.arg()

        replication_subnet_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
