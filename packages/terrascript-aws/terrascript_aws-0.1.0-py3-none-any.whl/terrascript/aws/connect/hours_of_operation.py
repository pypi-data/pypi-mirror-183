from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndTime(core.Schema):

    hours: Union[int, core.IntOut] = core.attr(int)

    minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        hours: Union[int, core.IntOut],
        minutes: Union[int, core.IntOut],
    ):
        super().__init__(
            args=EndTime.Args(
                hours=hours,
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours: Union[int, core.IntOut] = core.arg()

        minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class StartTime(core.Schema):

    hours: Union[int, core.IntOut] = core.attr(int)

    minutes: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        hours: Union[int, core.IntOut],
        minutes: Union[int, core.IntOut],
    ):
        super().__init__(
            args=StartTime.Args(
                hours=hours,
                minutes=minutes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours: Union[int, core.IntOut] = core.arg()

        minutes: Union[int, core.IntOut] = core.arg()


@core.schema
class Config(core.Schema):

    day: Union[str, core.StringOut] = core.attr(str)

    end_time: EndTime = core.attr(EndTime)

    start_time: StartTime = core.attr(StartTime)

    def __init__(
        self,
        *,
        day: Union[str, core.StringOut],
        end_time: EndTime,
        start_time: StartTime,
    ):
        super().__init__(
            args=Config.Args(
                day=day,
                end_time=end_time,
                start_time=start_time,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        day: Union[str, core.StringOut] = core.arg()

        end_time: EndTime = core.arg()

        start_time: StartTime = core.arg()


@core.resource(type="aws_connect_hours_of_operation", namespace="aws_connect")
class HoursOfOperation(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    config: Union[List[Config], core.ArrayOut[Config]] = core.attr(Config, kind=core.Kind.array)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hours_of_operation_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    hours_of_operation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    time_zone: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        config: Union[List[Config], core.ArrayOut[Config]],
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        time_zone: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HoursOfOperation.Args(
                config=config,
                instance_id=instance_id,
                name=name,
                time_zone=time_zone,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        config: Union[List[Config], core.ArrayOut[Config]] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        time_zone: Union[str, core.StringOut] = core.arg()
