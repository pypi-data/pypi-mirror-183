from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_neptune_cluster_instance", namespace="aws_neptune")
class ClusterInstance(core.Resource):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    apply_immediately: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_minor_version_upgrade: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    dbi_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    engine_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    identifier_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    instance_class: Union[str, core.StringOut] = core.attr(str)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    neptune_parameter_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

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
        engine: Optional[Union[str, core.StringOut]] = None,
        engine_version: Optional[Union[str, core.StringOut]] = None,
        identifier: Optional[Union[str, core.StringOut]] = None,
        identifier_prefix: Optional[Union[str, core.StringOut]] = None,
        neptune_parameter_group_name: Optional[Union[str, core.StringOut]] = None,
        neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = None,
        port: Optional[Union[int, core.IntOut]] = None,
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
                engine=engine,
                engine_version=engine_version,
                identifier=identifier,
                identifier_prefix=identifier_prefix,
                neptune_parameter_group_name=neptune_parameter_group_name,
                neptune_subnet_group_name=neptune_subnet_group_name,
                port=port,
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

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        engine: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        engine_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identifier_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_class: Union[str, core.StringOut] = core.arg()

        neptune_parameter_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        neptune_subnet_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        preferred_backup_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preferred_maintenance_window: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        promotion_tier: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        publicly_accessible: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
