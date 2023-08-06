from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_snapshot_copy", namespace="aws_rds")
class DbSnapshotCopy(core.Resource):

    allocated_storage: Union[int, core.IntOut] = core.attr(int, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    copy_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    db_snapshot_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    engine: Union[str, core.StringOut] = core.attr(str, computed=True)

    engine_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    license_model: Union[str, core.StringOut] = core.attr(str, computed=True)

    option_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    port: Union[int, core.IntOut] = core.attr(int, computed=True)

    presigned_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_db_snapshot_identifier: Union[str, core.StringOut] = core.attr(str)

    source_region: Union[str, core.StringOut] = core.attr(str, computed=True)

    storage_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_custom_availability_zone: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    target_db_snapshot_identifier: Union[str, core.StringOut] = core.attr(str)

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_db_snapshot_identifier: Union[str, core.StringOut],
        target_db_snapshot_identifier: Union[str, core.StringOut],
        copy_tags: Optional[Union[bool, core.BoolOut]] = None,
        destination_region: Optional[Union[str, core.StringOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        option_group_name: Optional[Union[str, core.StringOut]] = None,
        presigned_url: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_custom_availability_zone: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbSnapshotCopy.Args(
                source_db_snapshot_identifier=source_db_snapshot_identifier,
                target_db_snapshot_identifier=target_db_snapshot_identifier,
                copy_tags=copy_tags,
                destination_region=destination_region,
                kms_key_id=kms_key_id,
                option_group_name=option_group_name,
                presigned_url=presigned_url,
                tags=tags,
                tags_all=tags_all,
                target_custom_availability_zone=target_custom_availability_zone,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        copy_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        destination_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        option_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        presigned_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_db_snapshot_identifier: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_custom_availability_zone: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        target_db_snapshot_identifier: Union[str, core.StringOut] = core.arg()
