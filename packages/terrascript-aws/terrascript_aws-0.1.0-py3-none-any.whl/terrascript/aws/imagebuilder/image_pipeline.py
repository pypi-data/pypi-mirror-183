from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Schedule(core.Schema):

    pipeline_execution_start_condition: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    schedule_expression: Union[str, core.StringOut] = core.attr(str)

    timezone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        schedule_expression: Union[str, core.StringOut],
        pipeline_execution_start_condition: Optional[Union[str, core.StringOut]] = None,
        timezone: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Schedule.Args(
                schedule_expression=schedule_expression,
                pipeline_execution_start_condition=pipeline_execution_start_condition,
                timezone=timezone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pipeline_execution_start_condition: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        schedule_expression: Union[str, core.StringOut] = core.arg()

        timezone: Optional[Union[str, core.StringOut]] = core.arg(default=None)


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


@core.resource(type="aws_imagebuilder_image_pipeline", namespace="aws_imagebuilder")
class ImagePipeline(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container_recipe_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_last_run: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_next_run: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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

    name: Union[str, core.StringOut] = core.attr(str)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    schedule: Optional[Schedule] = core.attr(Schedule, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        infrastructure_configuration_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        container_recipe_arn: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        distribution_configuration_arn: Optional[Union[str, core.StringOut]] = None,
        enhanced_image_metadata_enabled: Optional[Union[bool, core.BoolOut]] = None,
        image_recipe_arn: Optional[Union[str, core.StringOut]] = None,
        image_tests_configuration: Optional[ImageTestsConfiguration] = None,
        schedule: Optional[Schedule] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ImagePipeline.Args(
                infrastructure_configuration_arn=infrastructure_configuration_arn,
                name=name,
                container_recipe_arn=container_recipe_arn,
                description=description,
                distribution_configuration_arn=distribution_configuration_arn,
                enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
                image_recipe_arn=image_recipe_arn,
                image_tests_configuration=image_tests_configuration,
                schedule=schedule,
                status=status,
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

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        distribution_configuration_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        enhanced_image_metadata_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )

        image_recipe_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_tests_configuration: Optional[ImageTestsConfiguration] = core.arg(default=None)

        infrastructure_configuration_arn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        schedule: Optional[Schedule] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
