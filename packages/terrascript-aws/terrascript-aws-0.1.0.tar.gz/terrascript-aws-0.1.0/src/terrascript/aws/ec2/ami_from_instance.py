from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtual_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        virtual_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        virtual_name: Union[str, core.StringOut] = core.arg()


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Union[bool, core.BoolOut],
        device_name: Union[str, core.StringOut],
        encrypted: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        outpost_arn: Union[str, core.StringOut],
        snapshot_id: Union[str, core.StringOut],
        throughput: Union[int, core.IntOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                device_name=device_name,
                encrypted=encrypted,
                iops=iops,
                outpost_arn=outpost_arn,
                snapshot_id=snapshot_id,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Union[bool, core.BoolOut] = core.arg()

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Union[bool, core.BoolOut] = core.arg()

        iops: Union[int, core.IntOut] = core.arg()

        outpost_arn: Union[str, core.StringOut] = core.arg()

        snapshot_id: Union[str, core.StringOut] = core.arg()

        throughput: Union[int, core.IntOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ami_from_instance", namespace="aws_ec2")
class AmiFromInstance(core.Resource):

    architecture: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    boot_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    deprecation_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ena_support: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    hypervisor: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_owner_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    kernel_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    manage_ebs_snapshots: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_details: Union[str, core.StringOut] = core.attr(str, computed=True)

    public: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ramdisk_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_without_reboot: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_instance_id: Union[str, core.StringOut] = core.attr(str)

    sriov_net_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tpm_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    usage_operation: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtualization_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        source_instance_id: Union[str, core.StringOut],
        deprecation_time: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        snapshot_without_reboot: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AmiFromInstance.Args(
                name=name,
                source_instance_id=source_instance_id,
                deprecation_time=deprecation_time,
                description=description,
                ebs_block_device=ebs_block_device,
                ephemeral_block_device=ephemeral_block_device,
                snapshot_without_reboot=snapshot_without_reboot,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        deprecation_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        snapshot_without_reboot: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_instance_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
