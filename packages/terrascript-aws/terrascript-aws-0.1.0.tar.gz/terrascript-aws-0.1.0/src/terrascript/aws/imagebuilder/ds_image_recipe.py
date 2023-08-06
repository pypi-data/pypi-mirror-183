from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Ebs(core.Schema):

    delete_on_termination: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    iops: Union[int, core.IntOut] = core.attr(int, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    snapshot_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    throughput: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    volume_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        delete_on_termination: Union[bool, core.BoolOut],
        encrypted: Union[bool, core.BoolOut],
        iops: Union[int, core.IntOut],
        kms_key_id: Union[str, core.StringOut],
        snapshot_id: Union[str, core.StringOut],
        throughput: Union[int, core.IntOut],
        volume_size: Union[int, core.IntOut],
        volume_type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Ebs.Args(
                delete_on_termination=delete_on_termination,
                encrypted=encrypted,
                iops=iops,
                kms_key_id=kms_key_id,
                snapshot_id=snapshot_id,
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

        kms_key_id: Union[str, core.StringOut] = core.arg()

        snapshot_id: Union[str, core.StringOut] = core.arg()

        throughput: Union[int, core.IntOut] = core.arg()

        volume_size: Union[int, core.IntOut] = core.arg()

        volume_type: Union[str, core.StringOut] = core.arg()


@core.schema
class BlockDeviceMapping(core.Schema):

    device_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    ebs: Union[List[Ebs], core.ArrayOut[Ebs]] = core.attr(Ebs, computed=True, kind=core.Kind.array)

    no_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    virtual_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        ebs: Union[List[Ebs], core.ArrayOut[Ebs]],
        no_device: Union[str, core.StringOut],
        virtual_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=BlockDeviceMapping.Args(
                device_name=device_name,
                ebs=ebs,
                no_device=no_device,
                virtual_name=virtual_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_name: Union[str, core.StringOut] = core.arg()

        ebs: Union[List[Ebs], core.ArrayOut[Ebs]] = core.arg()

        no_device: Union[str, core.StringOut] = core.arg()

        virtual_name: Union[str, core.StringOut] = core.arg()


@core.schema
class Parameter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Component(core.Schema):

    component_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter: Union[List[Parameter], core.ArrayOut[Parameter]] = core.attr(
        Parameter, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        component_arn: Union[str, core.StringOut],
        parameter: Union[List[Parameter], core.ArrayOut[Parameter]],
    ):
        super().__init__(
            args=Component.Args(
                component_arn=component_arn,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        component_arn: Union[str, core.StringOut] = core.arg()

        parameter: Union[List[Parameter], core.ArrayOut[Parameter]] = core.arg()


@core.data(type="aws_imagebuilder_image_recipe", namespace="aws_imagebuilder")
class DsImageRecipe(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    block_device_mapping: Union[
        List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]
    ] = core.attr(BlockDeviceMapping, computed=True, kind=core.Kind.array)

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, computed=True, kind=core.Kind.array
    )

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_image: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    user_data_base64: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    working_directory: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImageRecipe.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
