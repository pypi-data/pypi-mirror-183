from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_db_snapshot", namespace="aws_rds")
class DsDbSnapshot(core.Data):

    allocated_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_instance_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    db_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    db_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_public: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    include_shared: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    option_group_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_create_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_db_snapshot_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        db_instance_identifier: Optional[Union[str, core.StringOut]] = None,
        db_snapshot_identifier: Optional[Union[str, core.StringOut]] = None,
        include_public: Optional[Union[bool, core.BoolOut]] = None,
        include_shared: Optional[Union[bool, core.BoolOut]] = None,
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
        snapshot_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDbSnapshot.Args(
                db_instance_identifier=db_instance_identifier,
                db_snapshot_identifier=db_snapshot_identifier,
                include_public=include_public,
                include_shared=include_shared,
                most_recent=most_recent,
                snapshot_type=snapshot_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        db_instance_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        db_snapshot_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        include_public: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        include_shared: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
