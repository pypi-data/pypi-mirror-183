from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RepositoryAuthConfig(core.Schema):

    repository_credentials_provider_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        repository_credentials_provider_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RepositoryAuthConfig.Args(
                repository_credentials_provider_arn=repository_credentials_provider_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_credentials_provider_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class ImageConfig(core.Schema):

    repository_access_mode: Union[str, core.StringOut] = core.attr(str)

    repository_auth_config: Optional[RepositoryAuthConfig] = core.attr(
        RepositoryAuthConfig, default=None
    )

    def __init__(
        self,
        *,
        repository_access_mode: Union[str, core.StringOut],
        repository_auth_config: Optional[RepositoryAuthConfig] = None,
    ):
        super().__init__(
            args=ImageConfig.Args(
                repository_access_mode=repository_access_mode,
                repository_auth_config=repository_auth_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        repository_access_mode: Union[str, core.StringOut] = core.arg()

        repository_auth_config: Optional[RepositoryAuthConfig] = core.arg(default=None)


@core.schema
class PrimaryContainer(core.Schema):

    container_hostname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: Union[str, core.StringOut] = core.attr(str)

    image_config: Optional[ImageConfig] = core.attr(ImageConfig, default=None)

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    model_data_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image: Union[str, core.StringOut],
        container_hostname: Optional[Union[str, core.StringOut]] = None,
        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        image_config: Optional[ImageConfig] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
        model_data_url: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PrimaryContainer.Args(
                image=image,
                container_hostname=container_hostname,
                environment=environment,
                image_config=image_config,
                mode=mode,
                model_data_url=model_data_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_hostname: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        image: Union[str, core.StringOut] = core.arg()

        image_config: Optional[ImageConfig] = core.arg(default=None)

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        model_data_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Container(core.Schema):

    container_hostname: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    image: Union[str, core.StringOut] = core.attr(str)

    image_config: Optional[ImageConfig] = core.attr(ImageConfig, default=None)

    mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    model_data_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image: Union[str, core.StringOut],
        container_hostname: Optional[Union[str, core.StringOut]] = None,
        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        image_config: Optional[ImageConfig] = None,
        mode: Optional[Union[str, core.StringOut]] = None,
        model_data_url: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Container.Args(
                image=image,
                container_hostname=container_hostname,
                environment=environment,
                image_config=image_config,
                mode=mode,
                model_data_url=model_data_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        container_hostname: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        image: Union[str, core.StringOut] = core.arg()

        image_config: Optional[ImageConfig] = core.arg(default=None)

        mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        model_data_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class InferenceExecutionConfig(core.Schema):

    mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=InferenceExecutionConfig.Args(
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_sagemaker_model", namespace="aws_sagemaker")
class Model(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container: Optional[Union[List[Container], core.ArrayOut[Container]]] = core.attr(
        Container, default=None, kind=core.Kind.array
    )

    enable_network_isolation: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    inference_execution_config: Optional[InferenceExecutionConfig] = core.attr(
        InferenceExecutionConfig, default=None, computed=True
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    primary_container: Optional[PrimaryContainer] = core.attr(PrimaryContainer, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        execution_role_arn: Union[str, core.StringOut],
        container: Optional[Union[List[Container], core.ArrayOut[Container]]] = None,
        enable_network_isolation: Optional[Union[bool, core.BoolOut]] = None,
        inference_execution_config: Optional[InferenceExecutionConfig] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        primary_container: Optional[PrimaryContainer] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Model.Args(
                execution_role_arn=execution_role_arn,
                container=container,
                enable_network_isolation=enable_network_isolation,
                inference_execution_config=inference_execution_config,
                name=name,
                primary_container=primary_container,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container: Optional[Union[List[Container], core.ArrayOut[Container]]] = core.arg(
            default=None
        )

        enable_network_isolation: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        execution_role_arn: Union[str, core.StringOut] = core.arg()

        inference_execution_config: Optional[InferenceExecutionConfig] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        primary_container: Optional[PrimaryContainer] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
