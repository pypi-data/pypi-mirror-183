from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    virtual_name: Union[str, core.StringOut] = core.attr(str)

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

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EbsBlockDevice.Args(
                device_name=device_name,
                delete_on_termination=delete_on_termination,
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
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        device_name: Union[str, core.StringOut] = core.arg()

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_ami", namespace="aws_ec2")
class Ami(core.Resource):

    architecture: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    boot_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deprecation_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ena_support: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, computed=True, kind=core.Kind.array)

    hypervisor: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_location: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    image_owner_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    kernel_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    manage_ebs_snapshots: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_details: Union[str, core.StringOut] = core.attr(str, computed=True)

    public: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ramdisk_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_device_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    sriov_net_support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tpm_support: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    usage_operation: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtualization_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        architecture: Optional[Union[str, core.StringOut]] = None,
        boot_mode: Optional[Union[str, core.StringOut]] = None,
        deprecation_time: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ena_support: Optional[Union[bool, core.BoolOut]] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        image_location: Optional[Union[str, core.StringOut]] = None,
        kernel_id: Optional[Union[str, core.StringOut]] = None,
        ramdisk_id: Optional[Union[str, core.StringOut]] = None,
        root_device_name: Optional[Union[str, core.StringOut]] = None,
        sriov_net_support: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tpm_support: Optional[Union[str, core.StringOut]] = None,
        virtualization_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ami.Args(
                name=name,
                architecture=architecture,
                boot_mode=boot_mode,
                deprecation_time=deprecation_time,
                description=description,
                ebs_block_device=ebs_block_device,
                ena_support=ena_support,
                ephemeral_block_device=ephemeral_block_device,
                image_location=image_location,
                kernel_id=kernel_id,
                ramdisk_id=ramdisk_id,
                root_device_name=root_device_name,
                sriov_net_support=sriov_net_support,
                tags=tags,
                tags_all=tags_all,
                tpm_support=tpm_support,
                virtualization_type=virtualization_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        architecture: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        boot_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deprecation_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ena_support: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        image_location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kernel_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        ramdisk_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_device_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sriov_net_support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tpm_support: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        virtualization_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
