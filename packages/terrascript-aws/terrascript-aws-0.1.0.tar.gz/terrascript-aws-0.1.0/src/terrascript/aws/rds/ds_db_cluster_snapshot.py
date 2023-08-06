from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.data(type="aws_db_cluster_snapshot", namespace="aws_rds")
class DsDbClusterSnapshot(core.Data):

    allocated_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_cluster_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_cluster_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_public: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_shared: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_db_cluster_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        db_cluster_identifier: Optional[Union[str, core.StringOut]] = None,
        db_cluster_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        include_public: Optional[Union[bool, core.BoolOut]] = None,
        include_shared: Optional[Union[bool, core.BoolOut]] = None,
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbClusterSnapshot.Args(
                db_cluster_identifier=db_cluster_identifier,
                db_cluster_snapshot_identifier=db_cluster_snapshot_identifier,
                include_public=include_public,
                include_shared=include_shared,
                most_recent=most_recent,
                snapshot_type=snapshot_type,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_cluster_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_cluster_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        include_public: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_shared: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
