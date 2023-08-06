from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class BlockDeviceMappings(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ebs: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    no_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtual_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        ebs: Union[Dict[str, str], core.MapOut[core.StringOut]],
        no_device: Union[str, core.StringOut],
        virtual_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=BlockDeviceMappings.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        ebs: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        no_device: Union[str, core.StringOut] = core.arg()

        virtual_name: Union[str, core.StringOut] = core.arg()


@core.schema
class ProductCodes(core.Schema):

    product_code_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    product_code_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        product_code_id: Union[str, core.StringOut],
        product_code_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ProductCodes.Args(
                product_code_id=product_code_id,
                product_code_type=product_code_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        product_code_id: Union[str, core.StringOut] = core.arg()

        product_code_type: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_ami", namespace="aws_ec2")
class DsAmi(core.Data):

    architecture: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    block_device_mappings: Union[
        List[BlockDeviceMappings], core.ArrayOut[BlockDeviceMappings]
    ] = core.attr(BlockDeviceMappings, computed=True, kind=core.Kind.array)

    boot_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    deprecation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    ena_support: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    hypervisor: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_location: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_owner_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    include_deprecated: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    kernel_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    most_recent: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    name_regex: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owners: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_details: Union[str, core.StringOut] = core.attr(str, computed=True)

    product_codes: Union[List[ProductCodes], core.ArrayOut[ProductCodes]] = core.attr(
        ProductCodes, computed=True, kind=core.Kind.array
    )

    public: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    ramdisk_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_device_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    sriov_net_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    state_reason: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tpm_support: Union[str, core.StringOut] = core.attr(str, computed=True)

    usage_operation: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtualization_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        include_deprecated: Optional[Union[bool, core.BoolOut]] = None,
        most_recent: Optional[Union[bool, core.BoolOut]] = None,
        name_regex: Optional[Union[str, core.StringOut]] = None,
        owners: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAmi.Args(
                executable_users=executable_users,
                filter=filter,
                include_deprecated=include_deprecated,
                most_recent=most_recent,
                name_regex=name_regex,
                owners=owners,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        executable_users: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        include_deprecated: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        most_recent: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name_regex: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        owners: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
