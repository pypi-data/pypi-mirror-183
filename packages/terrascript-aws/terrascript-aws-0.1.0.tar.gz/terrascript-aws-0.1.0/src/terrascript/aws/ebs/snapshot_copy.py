from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ebs_snapshot_copy", namespace="aws_ebs")
class SnapshotCopy(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_encryption_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    permanent_restore: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_region: Union[str, core.StringOut] = core.attr(str)

    source_snapshot_id: Union[str, core.StringOut] = core.attr(str)

    storage_tier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    temporary_restore_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        source_region: Union[str, core.StringOut],
        source_snapshot_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        permanent_restore: Optional[Union[bool, core.BoolOut]] = None,
        storage_tier: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        temporary_restore_days: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SnapshotCopy.Args(
                source_region=source_region,
                source_snapshot_id=source_snapshot_id,
                description=description,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                permanent_restore=permanent_restore,
                storage_tier=storage_tier,
                tags=tags,
                tags_all=tags_all,
                temporary_restore_days=temporary_restore_days,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permanent_restore: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_region: Union[str, core.StringOut] = core.arg()

        source_snapshot_id: Union[str, core.StringOut] = core.arg()

        storage_tier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        temporary_restore_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)
