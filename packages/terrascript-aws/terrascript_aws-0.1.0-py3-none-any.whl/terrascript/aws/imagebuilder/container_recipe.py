from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TargetRepository(core.Schema):

    repository_name: Union[str, core.StringOut] = core.attr(str)

    service: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        repository_name: Union[str, core.StringOut],
        service: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TargetRepository.Args(
                repository_name=repository_name,
                service=service,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_name: Union[str, core.StringOut] = core.arg()

        service: Union[str, core.StringOut] = core.arg()


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
class InstanceConfiguration(core.Schema):

    block_device_mapping: Optional[
        Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
    ] = core.attr(BlockDeviceMapping, default=None, kind=core.Kind.array)

    image: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        block_device_mapping: Optional[
            Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
        ] = None,
        image: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstanceConfiguration.Args(
                block_device_mapping=block_device_mapping,
                image=image,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        block_device_mapping: Optional[
            Union[List[BlockDeviceMapping], core.ArrayOut[BlockDeviceMapping]]
        ] = core.arg(default=None)

        image: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_imagebuilder_container_recipe", namespace="aws_imagebuilder")
class ContainerRecipe(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    component: Union[List[Component], core.ArrayOut[Component]] = core.attr(
        Component, kind=core.Kind.array
    )

    container_type: Union[str, core.StringOut] = core.attr(str)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dockerfile_template_data: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    dockerfile_template_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_configuration: Optional[InstanceConfiguration] = core.attr(
        InstanceConfiguration, default=None
    )

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parent_image: Union[str, core.StringOut] = core.attr(str)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_repository: TargetRepository = core.attr(TargetRepository)

    version: Union[str, core.StringOut] = core.attr(str)

    working_directory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        component: Union[List[Component], core.ArrayOut[Component]],
        container_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        parent_image: Union[str, core.StringOut],
        target_repository: TargetRepository,
        version: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        dockerfile_template_data: Optional[Union[str, core.StringOut]] = None,
        dockerfile_template_uri: Optional[Union[str, core.StringOut]] = None,
        instance_configuration: Optional[InstanceConfiguration] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        working_directory: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContainerRecipe.Args(
                component=component,
                container_type=container_type,
                name=name,
                parent_image=parent_image,
                target_repository=target_repository,
                version=version,
                description=description,
                dockerfile_template_data=dockerfile_template_data,
                dockerfile_template_uri=dockerfile_template_uri,
                instance_configuration=instance_configuration,
                kms_key_id=kms_key_id,
                tags=tags,
                tags_all=tags_all,
                working_directory=working_directory,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        component: Union[List[Component], core.ArrayOut[Component]] = core.arg()

        container_type: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dockerfile_template_data: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dockerfile_template_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_configuration: Optional[InstanceConfiguration] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parent_image: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_repository: TargetRepository = core.arg()

        version: Union[str, core.StringOut] = core.arg()

        working_directory: Optional[Union[str, core.StringOut]] = core.arg(default=None)
