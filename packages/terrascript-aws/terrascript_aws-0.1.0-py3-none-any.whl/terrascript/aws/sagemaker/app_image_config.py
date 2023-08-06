from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class FileSystemConfig(core.Schema):

    default_gid: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    default_uid: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    mount_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        default_gid: Optional[Union[int, core.IntOut]] = None,
        default_uid: Optional[Union[int, core.IntOut]] = None,
        mount_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FileSystemConfig.Args(
                default_gid=default_gid,
                default_uid=default_uid,
                mount_path=mount_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_gid: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        default_uid: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        mount_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class KernelSpec(core.Schema):

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        display_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KernelSpec.Args(
                name=name,
                display_name=display_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()


@core.schema
class KernelGatewayImageConfig(core.Schema):

    file_system_config: Optional[FileSystemConfig] = core.attr(FileSystemConfig, default=None)

    kernel_spec: KernelSpec = core.attr(KernelSpec)

    def __init__(
        self,
        *,
        kernel_spec: KernelSpec,
        file_system_config: Optional[FileSystemConfig] = None,
    ):
        super().__init__(
            args=KernelGatewayImageConfig.Args(
                kernel_spec=kernel_spec,
                file_system_config=file_system_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_system_config: Optional[FileSystemConfig] = core.arg(default=None)

        kernel_spec: KernelSpec = core.arg()


@core.resource(type="aws_sagemaker_app_image_config", namespace="aws_sagemaker")
class AppImageConfig(core.Resource):

    app_image_config_name: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kernel_gateway_image_config: Optional[KernelGatewayImageConfig] = core.attr(
        KernelGatewayImageConfig, default=None
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        app_image_config_name: Union[str, core.StringOut],
        kernel_gateway_image_config: Optional[KernelGatewayImageConfig] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AppImageConfig.Args(
                app_image_config_name=app_image_config_name,
                kernel_gateway_image_config=kernel_gateway_image_config,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        app_image_config_name: Union[str, core.StringOut] = core.arg()

        kernel_gateway_image_config: Optional[KernelGatewayImageConfig] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
