from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Amis(core.Schema):

    account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    image: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        account_id: Union[str, core.StringOut],
        description: Union[str, core.StringOut],
        image: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        region: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Amis.Args(
                account_id=account_id,
                description=description,
                image=image,
                name=name,
                region=region,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        account_id: Union[str, core.StringOut] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        image: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        region: Union[str, core.StringOut] = core.arg()


@core.schema
class OutputResources(core.Schema):

    amis: Union[List[Amis], core.ArrayOut[Amis]] = core.attr(
        Amis, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        amis: Union[List[Amis], core.ArrayOut[Amis]],
    ):
        super().__init__(
            args=OutputResources.Args(
                amis=amis,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        amis: Union[List[Amis], core.ArrayOut[Amis]] = core.arg()


@core.schema
class ImageTestsConfiguration(core.Schema):

    image_tests_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    timeout_minutes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        image_tests_enabled: Optional[Union[bool, core.BoolOut]] = None,
        timeout_minutes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ImageTestsConfiguration.Args(
                image_tests_enabled=image_tests_enabled,
                timeout_minutes=timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_tests_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        timeout_minutes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_imagebuilder_image", namespace="aws_imagebuilder")
class Image(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container_recipe_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    distribution_configuration_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    enhanced_image_metadata_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_recipe_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    image_tests_configuration: Optional[ImageTestsConfiguration] = core.attr(
        ImageTestsConfiguration, default=None, computed=True
    )

    infrastructure_configuration_arn: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    os_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    output_resources: Union[List[OutputResources], core.ArrayOut[OutputResources]] = core.attr(
        OutputResources, computed=True, kind=core.Kind.array
    )

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        infrastructure_configuration_arn: Union[str, core.StringOut],
        container_recipe_arn: Optional[Union[str, core.StringOut]] = None,
        distribution_configuration_arn: Optional[Union[str, core.StringOut]] = None,
        enhanced_image_metadata_enabled: Optional[Union[bool, core.BoolOut]] = None,
        image_recipe_arn: Optional[Union[str, core.StringOut]] = None,
        image_tests_configuration: Optional[ImageTestsConfiguration] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Image.Args(
                infrastructure_configuration_arn=infrastructure_configuration_arn,
                container_recipe_arn=container_recipe_arn,
                distribution_configuration_arn=distribution_configuration_arn,
                enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
                image_recipe_arn=image_recipe_arn,
                image_tests_configuration=image_tests_configuration,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_recipe_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        distribution_configuration_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        enhanced_image_metadata_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        image_recipe_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_tests_configuration: Optional[ImageTestsConfiguration] = core.arg(default=None)

        infrastructure_configuration_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
