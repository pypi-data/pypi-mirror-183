from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SystemsManagerAgent(core.Schema):

    uninstall_after_build: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        uninstall_after_build: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=SystemsManagerAgent.Args(
                uninstall_after_build=uninstall_after_build,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        uninstall_after_build: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Ebs(core.Schema):

    delete_on_termination: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    snapshot_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    volume_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        delete_on_termination: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[str, core.StringOut]] = None,
        iops: Optional[Union[int, core.IntOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        snapshot_id: Optional[Union[str, core.StringOut]] = None,
        throughput: Optional[Union[int, core.IntOut]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        volume_type: Optional[Union[str, core.StringOut]] = None,
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
        delete_on_termination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        snapshot_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        volume_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class BlockDeviceMapping(core.Schema):

    device_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs: Optional[Ebs] = core.attr(Ebs, default=None)

    no_device: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    virtual_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Optional[Union[str, core.StringOut]] = None,
        ebs: Optional[Ebs] = None,
        no_device: Optional[Union[bool, core.BoolOut]] = None,
        virtual_name: Optional[Union[str, core.StringOut]] = None,
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
        device_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs: Optional[Ebs] = core.arg(default=None)

        no_device: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        virtual_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Parameter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

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

    component_arn: Union[str, core.StringOut] = core.attr(str)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        component_arn: Union[str, core.StringOut],
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
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

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )


@core.resource(type="aws_imagebuilder_image_recipe", namespace="aws_imagebuilder")
class ImageRecipe(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    block_device_mapping: Optional[
        Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
    ] = core.attr(BlockDeviceMapping, default=None, kind=core.Kind.array)

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, kind=core.Kind.array
    )

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_image: Union[str, core.StringOut] = core.attr(str)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    systems_manager_agent: Optional[SystemsManagerAgent] = core.attr(
        SystemsManagerAgent, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_data_base64: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    version: Union[str, core.StringOut] = core.attr(str)

    working_directory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        component: Union[List[Component], core.ArrayOut[Component]],
        name: Union[str, core.StringOut],
        parent_image: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
        block_device_mapping: Optional[
            Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
        ] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        systems_manager_agent: Optional[SystemsManagerAgent] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_data_base64: Optional[Union[str, core.StringOut]] = None,
        working_directory: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImageRecipe.Args(
                component=component,
                name=name,
                parent_image=parent_image,
                version=version,
                block_device_mapping=block_device_mapping,
                description=description,
                systems_manager_agent=systems_manager_agent,
                tags=tags,
                tags_all=tags_all,
                user_data_base64=user_data_base64,
                working_directory=working_directory,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        block_device_mapping: Optional[
            Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
        ] = core.arg(default=None)

        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parent_image: Union[str, core.StringOut] = core.arg()

        systems_manager_agent: Optional[SystemsManagerAgent] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_data_base64: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()

        working_directory: Optional[Union[str, core.StringOut]] = core.arg(default=None)
