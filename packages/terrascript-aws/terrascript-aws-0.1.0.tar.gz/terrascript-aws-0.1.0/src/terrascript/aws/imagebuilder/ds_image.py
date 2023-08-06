from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ImageTestsConfiguration(core.Schema):

    image_tests_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    timeout_minutes: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        image_tests_enabled: Union[bool, core.BoolOut],
        timeout_minutes: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ImageTestsConfiguration.Args(
                image_tests_enabled=image_tests_enabled,
                timeout_minutes=timeout_minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_tests_enabled: Union[bool, core.BoolOut] = core.arg()

        timeout_minutes: Union[int, core.IntOut] = core.arg()


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


@core.data(type="aws_imagebuilder_image", namespace="aws_imagebuilder")
class DsImage(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    build_version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container_recipe_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    distribution_configuration_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enhanced_image_metadata_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_recipe_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_tests_configuration: Union[
        List[ImageTestsConfiguration], core.ArrayOut[ImageTestsConfiguration]
    ] = core.attr(ImageTestsConfiguration, computed=True, kind=core.Kind.array)

    infrastructure_configuration_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    os_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    output_resources: Union[List[OutputResources], core.ArrayOut[OutputResources]] = core.attr(
        OutputResources, computed=True, kind=core.Kind.array
    )

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImage.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
