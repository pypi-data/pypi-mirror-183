from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SharingSettings(core.Schema):

    notebook_output_option: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_output_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notebook_output_option: Optional[Union[str, core.StringOut]] = None,
        s3_kms_key_id: Optional[Union[str, core.StringOut]] = None,
        s3_output_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SharingSettings.Args(
                notebook_output_option=notebook_output_option,
                s3_kms_key_id=s3_kms_key_id,
                s3_output_path=s3_output_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notebook_output_option: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_output_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DefaultResourceSpec(core.Schema):

    instance_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lifecycle_config_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemaker_image_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        instance_type: Optional[Union[str, core.StringOut]] = None,
        lifecycle_config_arn: Optional[Union[str, core.StringOut]] = None,
        sagemaker_image_arn: Optional[Union[str, core.StringOut]] = None,
        sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DefaultResourceSpec.Args(
                instance_type=instance_type,
                lifecycle_config_arn=lifecycle_config_arn,
                sagemaker_image_arn=sagemaker_image_arn,
                sagemaker_image_version_arn=sagemaker_image_version_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lifecycle_config_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemaker_image_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sagemaker_image_version_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TensorBoardAppSettings(core.Schema):

    default_resource_spec: DefaultResourceSpec = core.attr(DefaultResourceSpec)

    def __init__(
        self,
        *,
        default_resource_spec: DefaultResourceSpec,
    ):
        super().__init__(
            args=TensorBoardAppSettings.Args(
                default_resource_spec=default_resource_spec,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_resource_spec: DefaultResourceSpec = core.arg()


@core.schema
class JupyterServerAppSettings(core.Schema):

    default_resource_spec: DefaultResourceSpec = core.attr(DefaultResourceSpec)

    lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        default_resource_spec: DefaultResourceSpec,
        lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=JupyterServerAppSettings.Args(
                default_resource_spec=default_resource_spec,
                lifecycle_config_arns=lifecycle_config_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        default_resource_spec: DefaultResourceSpec = core.arg()

        lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class CustomImage(core.Schema):

    app_image_config_name: Union[str, core.StringOut] = core.attr(str)

    image_name: Union[str, core.StringOut] = core.attr(str)

    image_version_number: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        app_image_config_name: Union[str, core.StringOut],
        image_name: Union[str, core.StringOut],
        image_version_number: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CustomImage.Args(
                app_image_config_name=app_image_config_name,
                image_name=image_name,
                image_version_number=image_version_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        app_image_config_name: Union[str, core.StringOut] = core.arg()

        image_name: Union[str, core.StringOut] = core.arg()

        image_version_number: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class KernelGatewayAppSettings(core.Schema):

    custom_image: Optional[Union[List[CustomImage], core.ArrayOut[CustomImage]]] = core.attr(
        CustomImage, default=None, kind=core.Kind.array
    )

    default_resource_spec: DefaultResourceSpec = core.attr(DefaultResourceSpec)

    lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        default_resource_spec: DefaultResourceSpec,
        custom_image: Optional[Union[List[CustomImage], core.ArrayOut[CustomImage]]] = None,
        lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=KernelGatewayAppSettings.Args(
                default_resource_spec=default_resource_spec,
                custom_image=custom_image,
                lifecycle_config_arns=lifecycle_config_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_image: Optional[Union[List[CustomImage], core.ArrayOut[CustomImage]]] = core.arg(
            default=None
        )

        default_resource_spec: DefaultResourceSpec = core.arg()

        lifecycle_config_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class UserSettings(core.Schema):

    execution_role: Union[str, core.StringOut] = core.attr(str)

    jupyter_server_app_settings: Optional[JupyterServerAppSettings] = core.attr(
        JupyterServerAppSettings, default=None
    )

    kernel_gateway_app_settings: Optional[KernelGatewayAppSettings] = core.attr(
        KernelGatewayAppSettings, default=None
    )

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    sharing_settings: Optional[SharingSettings] = core.attr(SharingSettings, default=None)

    tensor_board_app_settings: Optional[TensorBoardAppSettings] = core.attr(
        TensorBoardAppSettings, default=None
    )

    def __init__(
        self,
        *,
        execution_role: Union[str, core.StringOut],
        jupyter_server_app_settings: Optional[JupyterServerAppSettings] = None,
        kernel_gateway_app_settings: Optional[KernelGatewayAppSettings] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        sharing_settings: Optional[SharingSettings] = None,
        tensor_board_app_settings: Optional[TensorBoardAppSettings] = None,
    ):
        super().__init__(
            args=UserSettings.Args(
                execution_role=execution_role,
                jupyter_server_app_settings=jupyter_server_app_settings,
                kernel_gateway_app_settings=kernel_gateway_app_settings,
                security_groups=security_groups,
                sharing_settings=sharing_settings,
                tensor_board_app_settings=tensor_board_app_settings,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execution_role: Union[str, core.StringOut] = core.arg()

        jupyter_server_app_settings: Optional[JupyterServerAppSettings] = core.arg(default=None)

        kernel_gateway_app_settings: Optional[KernelGatewayAppSettings] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        sharing_settings: Optional[SharingSettings] = core.arg(default=None)

        tensor_board_app_settings: Optional[TensorBoardAppSettings] = core.arg(default=None)


@core.resource(type="aws_sagemaker_user_profile", namespace="aws_sagemaker")
class UserProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_id: Union[str, core.StringOut] = core.attr(str)

    home_efs_file_system_uid: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    single_sign_on_user_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    single_sign_on_user_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_profile_name: Union[str, core.StringOut] = core.attr(str)

    user_settings: Optional[UserSettings] = core.attr(UserSettings, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        domain_id: Union[str, core.StringOut],
        user_profile_name: Union[str, core.StringOut],
        single_sign_on_user_identifier: Optional[Union[str, core.StringOut]] = None,
        single_sign_on_user_value: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_settings: Optional[UserSettings] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=UserProfile.Args(
                domain_id=domain_id,
                user_profile_name=user_profile_name,
                single_sign_on_user_identifier=single_sign_on_user_identifier,
                single_sign_on_user_value=single_sign_on_user_value,
                tags=tags,
                tags_all=tags_all,
                user_settings=user_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_id: Union[str, core.StringOut] = core.arg()

        single_sign_on_user_identifier: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        single_sign_on_user_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_profile_name: Union[str, core.StringOut] = core.arg()

        user_settings: Optional[UserSettings] = core.arg(default=None)
