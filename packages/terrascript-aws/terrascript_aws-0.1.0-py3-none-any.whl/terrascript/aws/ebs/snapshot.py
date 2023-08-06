from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ebs_snapshot", namespace="aws_ebs")
class Snapshot(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_encryption_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    permanent_restore: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    storage_tier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    temporary_restore_days: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    volume_id: Union[str, core.StringOut] = core.attr(str)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        volume_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
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
            args=Snapshot.Args(
                volume_id=volume_id,
                description=description,
                outpost_arn=outpost_arn,
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

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        permanent_restore: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        storage_tier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        temporary_restore_days: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_id: Union[str, core.StringOut] = core.arg()
