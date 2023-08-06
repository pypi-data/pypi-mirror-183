from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_storagegateway_cached_iscsi_volume", namespace="aws_storagegateway")
class CachedIscsiVolume(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    chap_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    gateway_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kms_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lun_number: Union[int, core.IntOut] = core.attr(int, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    network_interface_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_volume_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_name: Union[str, core.StringOut] = core.attr(str)

    volume_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size_in_bytes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        gateway_arn: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        target_name: Union[str, core.StringOut],
        volume_size_in_bytes: Union[int, core.IntOut],
        kms_encrypted: Optional[Union[bool, core.BoolOut]] = None,
        kms_key: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        source_volume_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CachedIscsiVolume.Args(
                gateway_arn=gateway_arn,
                network_interface_id=network_interface_id,
                target_name=target_name,
                volume_size_in_bytes=volume_size_in_bytes,
                kms_encrypted=kms_encrypted,
                kms_key=kms_key,
                snapshot_id=snapshot_id,
                source_volume_arn=source_volume_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        gateway_arn: Union[str, core.StringOut] = core.arg()

        kms_encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interface_id: Union[str, core.StringOut] = core.arg()

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_volume_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_name: Union[str, core.StringOut] = core.arg()

        volume_size_in_bytes: Union[int, core.IntOut] = core.arg()
