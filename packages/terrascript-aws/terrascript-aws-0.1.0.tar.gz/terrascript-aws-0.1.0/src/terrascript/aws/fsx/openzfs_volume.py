from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ClientConfigurations(core.Schema):

    clients: Union[str, core.StringOut] = core.attr(str)

    options: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        clients: Union[str, core.StringOut],
        options: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=ClientConfigurations.Args(
                clients=clients,
                options=options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        clients: Union[str, core.StringOut] = core.arg()

        options: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class NfsExports(core.Schema):

    client_configurations: Union[
        List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
    ] = core.attr(ClientConfigurations, kind=core.Kind.array)

    def __init__(
        self,
        *,
        client_configurations: Union[
            List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
        ],
    ):
        super().__init__(
            args=NfsExports.Args(
                client_configurations=client_configurations,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_configurations: Union[
            List[ClientConfigurations], core.ArrayOut[ClientConfigurations]
        ] = core.arg()


@core.schema
class OriginSnapshot(core.Schema):

    copy_strategy: Union[str, core.StringOut] = core.attr(str)

    snapshot_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        copy_strategy: Union[str, core.StringOut],
        snapshot_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OriginSnapshot.Args(
                copy_strategy=copy_strategy,
                snapshot_arn=snapshot_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        copy_strategy: Union[str, core.StringOut] = core.arg()

        snapshot_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class UserAndGroupQuotas(core.Schema):

    id: Union[int, core.IntOut] = core.attr(int)

    storage_capacity_quota_gib: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        id: Union[int, core.IntOut],
        storage_capacity_quota_gib: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserAndGroupQuotas.Args(
                id=id,
                storage_capacity_quota_gib=storage_capacity_quota_gib,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[int, core.IntOut] = core.arg()

        storage_capacity_quota_gib: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_fsx_openzfs_volume", namespace="aws_fsx")
class OpenzfsVolume(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    data_compression_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    nfs_exports: Optional[NfsExports] = core.attr(NfsExports, default=None)

    origin_snapshot: Optional[OriginSnapshot] = core.attr(OriginSnapshot, default=None)

    parent_volume_id: Union[str, core.StringOut] = core.attr(str)

    read_only: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    record_size_kib: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    storage_capacity_quota_gib: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    storage_capacity_reservation_gib: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_and_group_quotas: Optional[
        Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
    ] = core.attr(UserAndGroupQuotas, default=None, computed=True, kind=core.Kind.array)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        parent_volume_id: Union[str, core.StringOut],
        copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = None,
        data_compression_type: Optional[Union[str, core.StringOut]] = None,
        nfs_exports: Optional[NfsExports] = None,
        origin_snapshot: Optional[OriginSnapshot] = None,
        read_only: Optional[Union[bool, core.BoolOut]] = None,
        record_size_kib: Optional[Union[int, core.IntOut]] = None,
        storage_capacity_quota_gib: Optional[Union[int, core.IntOut]] = None,
        storage_capacity_reservation_gib: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_and_group_quotas: Optional[
            Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
        ] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OpenzfsVolume.Args(
                name=name,
                parent_volume_id=parent_volume_id,
                copy_tags_to_snapshots=copy_tags_to_snapshots,
                data_compression_type=data_compression_type,
                nfs_exports=nfs_exports,
                origin_snapshot=origin_snapshot,
                read_only=read_only,
                record_size_kib=record_size_kib,
                storage_capacity_quota_gib=storage_capacity_quota_gib,
                storage_capacity_reservation_gib=storage_capacity_reservation_gib,
                tags=tags,
                tags_all=tags_all,
                user_and_group_quotas=user_and_group_quotas,
                volume_type=volume_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        copy_tags_to_snapshots: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        data_compression_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        nfs_exports: Optional[NfsExports] = core.arg(default=None)

        origin_snapshot: Optional[OriginSnapshot] = core.arg(default=None)

        parent_volume_id: Union[str, core.StringOut] = core.arg()

        read_only: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        record_size_kib: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_capacity_quota_gib: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        storage_capacity_reservation_gib: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_and_group_quotas: Optional[
            Union[List[UserAndGroupQuotas], core.ArrayOut[UserAndGroupQuotas]]
        ] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
