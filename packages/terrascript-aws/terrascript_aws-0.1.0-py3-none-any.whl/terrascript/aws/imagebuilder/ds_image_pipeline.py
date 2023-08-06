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
class Schedule(core.Schema):

    pipeline_execution_start_condition: Union[str, core.StringOut] = core.attr(str, computed=True)

    schedule_expression: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        pipeline_execution_start_condition: Union[str, core.StringOut],
        schedule_expression: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Schedule.Args(
                pipeline_execution_start_condition=pipeline_execution_start_condition,
                schedule_expression=schedule_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pipeline_execution_start_condition: Union[str, core.StringOut] = core.arg()

        schedule_expression: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_imagebuilder_image_pipeline", namespace="aws_imagebuilder")
class DsImagePipeline(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str)

    container_recipe_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_created: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_last_run: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_next_run: Union[str, core.StringOut] = core.attr(str, computed=True)

    date_updated: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    distribution_configuration_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enhanced_image_metadata_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_recipe_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_tests_configuration: Union[
        List[ImageTestsConfiguration], core.ArrayOut[ImageTestsConfiguration]
    ] = core.attr(ImageTestsConfiguration, computed=True, kind=core.Kind.array)

    infrastructure_configuration_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    platform: Union[str, core.StringOut] = core.attr(str, computed=True)

    schedule: Union[List[Schedule], core.ArrayOut[Schedule]] = core.attr(
        Schedule, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        arn: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsImagePipeline.Args(
                arn=arn,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
