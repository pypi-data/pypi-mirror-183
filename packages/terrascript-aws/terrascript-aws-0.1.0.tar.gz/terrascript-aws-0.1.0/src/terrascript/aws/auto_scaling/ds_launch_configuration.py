from typing import List, Union

import terrascript.core as core


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    http_put_response_hop_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    http_tokens: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: Union[str, core.StringOut],
        http_put_response_hop_limit: Union[int, core.IntOut],
        http_tokens: Union[str, core.StringOut],
    ):
        super().__init__(
            args=MetadataOptions.Args(
                http_endpoint=http_endpoint,
                http_put_response_hop_limit=http_put_response_hop_limit,
                http_tokens=http_tokens,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        http_endpoint: Union[str, core.StringOut] = core.arg()

        http_put_response_hop_limit: Union[int, core.IntOut] = core.arg()

        http_tokens: Union[str, core.StringOut] = core.arg()


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    no_device: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

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
        no_device: Union[bool, core.BoolOut],
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
                no_device=no_device,
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

        no_device: Union[bool, core.BoolOut] = core.arg()

        snapshot_id: Union[str, core.StringOut] = core.arg()

        throughput: Union[int, core.IntOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Union[bool, core.BoolOut],
        encrypted: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        throughput: Union[int, core.IntOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RootBlockDevice.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                throughput=throughput,
                volume_size=volume_size,
                volume_type=volume_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delete_on_termination: Union[bool, core.BoolOut] = core.arg()

        encrypted: Union[bool, core.BoolOut] = core.arg()

        iops: Union[int, core.IntOut] = core.arg()

        throughput: Union[int, core.IntOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


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


@core.data(type="aws_launch_configuration", namespace="aws_auto_scaling")
class DsLaunchConfiguration(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associate_public_ip_address: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ebs_block_device: Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]] = core.attr(
        EbsBlockDevice, computed=True, kind=core.Kind.array
    )

    ebs_optimized: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_monitoring: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ephemeral_block_device: Union[
        List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]
    ] = core.attr(EphemeralBlockDevice, computed=True, kind=core.Kind.array)

    iam_instance_profile: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    key_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    metadata_options: Union[List[MetadataOptions], core.ArrayOut[MetadataOptions]] = core.attr(
        MetadataOptions, computed=True, kind=core.Kind.array
    )

    name: Union[str, core.StringOut] = core.attr(str)

    placement_tenancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_block_device: Union[List[RootBlockDevice], core.ArrayOut[RootBlockDevice]] = core.attr(
        RootBlockDevice, computed=True, kind=core.Kind.array
    )

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    spot_price: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_data: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_classic_link_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_classic_link_security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsLaunchConfiguration.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
