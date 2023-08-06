from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class MetadataOptions(core.Schema):

    http_endpoint: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    http_tokens: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        http_endpoint: Optional[Union[str, core.StringOut]] = None,
        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = None,
        http_tokens: Optional[Union[str, core.StringOut]] = None,
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
        http_endpoint: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_put_response_hop_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        http_tokens: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RootBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
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
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EphemeralBlockDevice(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str)

    no_device: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    virtual_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        no_device: Optional[Union[bool, core.BoolOut]] = None,
        virtual_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EphemeralBlockDevice.Args(
                device_name=device_name,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        no_device: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        virtual_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class EbsBlockDevice(core.Schema):

    delete_on_termination: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    no_device: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        delete_on_termination: Optional[Union[bool, core.BoolOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        no_device: Optional[Union[bool, core.BoolOut]] = None,
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
                no_device=no_device,
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

        no_device: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_launch_configuration", namespace="aws_auto_scaling")
class LaunchConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    ebs_block_device: Optional[
        Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
    ] = core.attr(EbsBlockDevice, default=None, computed=True, kind=core.Kind.array)

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    enable_monitoring: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    ephemeral_block_device: Optional[
        Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
    ] = core.attr(EphemeralBlockDevice, default=None, kind=core.Kind.array)

    iam_instance_profile: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Union[str, core.StringOut] = core.attr(str)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    key_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    metadata_options: Optional[MetadataOptions] = core.attr(
        MetadataOptions, default=None, computed=True
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    placement_tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_block_device: Optional[RootBlockDevice] = core.attr(
        RootBlockDevice, default=None, computed=True
    )

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    spot_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_data: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    user_data_base64: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_classic_link_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_classic_link_security_groups: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    def __init__(
        self,
        resource_name: str,
        *,
        image_id: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = None,
        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = None,
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        enable_monitoring: Optional[Union[bool, core.BoolOut]] = None,
        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = None,
        iam_instance_profile: Optional[Union[str, core.StringOut]] = None,
        key_name: Optional[Union[str, core.StringOut]] = None,
        metadata_options: Optional[MetadataOptions] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        placement_tenancy: Optional[Union[str, core.StringOut]] = None,
        root_block_device: Optional[RootBlockDevice] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        spot_price: Optional[Union[str, core.StringOut]] = None,
        user_data: Optional[Union[str, core.StringOut]] = None,
        user_data_base64: Optional[Union[str, core.StringOut]] = None,
        vpc_classic_link_id: Optional[Union[str, core.StringOut]] = None,
        vpc_classic_link_security_groups: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LaunchConfiguration.Args(
                image_id=image_id,
                instance_type=instance_type,
                associate_public_ip_address=associate_public_ip_address,
                ebs_block_device=ebs_block_device,
                ebs_optimized=ebs_optimized,
                enable_monitoring=enable_monitoring,
                ephemeral_block_device=ephemeral_block_device,
                iam_instance_profile=iam_instance_profile,
                key_name=key_name,
                metadata_options=metadata_options,
                name=name,
                name_prefix=name_prefix,
                placement_tenancy=placement_tenancy,
                root_block_device=root_block_device,
                security_groups=security_groups,
                spot_price=spot_price,
                user_data=user_data,
                user_data_base64=user_data_base64,
                vpc_classic_link_id=vpc_classic_link_id,
                vpc_classic_link_security_groups=vpc_classic_link_security_groups,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        associate_public_ip_address: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ebs_block_device: Optional[
            Union[List[EbsBlockDevice], core.ArrayOut[EbsBlockDevice]]
        ] = core.arg(default=None)

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_monitoring: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ephemeral_block_device: Optional[
            Union[List[EphemeralBlockDevice], core.ArrayOut[EphemeralBlockDevice]]
        ] = core.arg(default=None)

        iam_instance_profile: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_id: Union[str, core.StringOut] = core.arg()

        instance_type: Union[str, core.StringOut] = core.arg()

        key_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        metadata_options: Optional[MetadataOptions] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        placement_tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_block_device: Optional[RootBlockDevice] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        spot_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        user_data_base64: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_classic_link_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_classic_link_security_groups: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)
