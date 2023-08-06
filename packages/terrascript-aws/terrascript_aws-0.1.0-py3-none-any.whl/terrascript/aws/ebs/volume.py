from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ebs_volume", namespace="aws_ebs")
class Volume(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    final_snapshot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    multi_attach_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: Union[str, core.StringOut],
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        final_snapshot: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        multi_attach_enabled: Optional[Union[bool, core.BoolOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        size: Optional[Union[int, core.IntOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Volume.Args(
                availability_zone=availability_zone,
                encrypted=encrypted,
                final_snapshot=final_snapshot,
                iops=iops,
                kms_key_id=kms_key_id,
                multi_attach_enabled=multi_attach_enabled,
                outpost_arn=outpost_arn,
                size=size,
                snapshot_id=snapshot_id,
                tags=tags,
                tags_all=tags_all,
                throughput=throughput,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: Union[str, core.StringOut] = core.arg()

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        final_snapshot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        multi_attach_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
