from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class InstanceMetadataServiceConfiguration(core.Schema):

    minimum_instance_metadata_service_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        minimum_instance_metadata_service_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=InstanceMetadataServiceConfiguration.Args(
                minimum_instance_metadata_service_version=minimum_instance_metadata_service_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        minimum_instance_metadata_service_version: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_sagemaker_notebook_instance", namespace="aws_sagemaker")
class NotebookInstance(core.Resource):

    accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    additional_code_repositories: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_code_repository: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    direct_internet_access: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_metadata_service_configuration: Optional[
        InstanceMetadataServiceConfiguration
    ] = core.attr(InstanceMetadataServiceConfiguration, default=None)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lifecycle_config_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    role_arn: Union[str, core.StringOut] = core.attr(str)

    root_access: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    url: Union[str, core.StringOut] = core.attr(str, computed=True)

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        additional_code_repositories: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        default_code_repository: Optional[Union[str, core.StringOut]] = None,
        direct_internet_access: Optional[Union[str, core.StringOut]] = None,
        instance_metadata_service_configuration: Optional[
            InstanceMetadataServiceConfiguration
        ] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        lifecycle_config_name: Optional[Union[str, core.StringOut]] = None,
        platform_identifier: Optional[Union[str, core.StringOut]] = None,
        root_access: Optional[Union[str, core.StringOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NotebookInstance.Args(
                instance_type=instance_type,
                name=name,
                role_arn=role_arn,
                accelerator_types=accelerator_types,
                additional_code_repositories=additional_code_repositories,
                default_code_repository=default_code_repository,
                direct_internet_access=direct_internet_access,
                instance_metadata_service_configuration=instance_metadata_service_configuration,
                kms_key_id=kms_key_id,
                lifecycle_config_name=lifecycle_config_name,
                platform_identifier=platform_identifier,
                root_access=root_access,
                security_groups=security_groups,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                volume_size=volume_size,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accelerator_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        additional_code_repositories: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        default_code_repository: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        direct_internet_access: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_metadata_service_configuration: Optional[
            InstanceMetadataServiceConfiguration
        ] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lifecycle_config_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        platform_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        root_access: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)
