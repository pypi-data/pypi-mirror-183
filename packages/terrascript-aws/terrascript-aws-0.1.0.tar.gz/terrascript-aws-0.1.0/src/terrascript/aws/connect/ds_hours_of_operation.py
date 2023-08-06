from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndTime(core.Schema):

    hours: Union[int, core.IntOut] = core.attr(int, computed=True)

    minutes: Union[int, core.IntOut] = core.attr(int, computed=True)

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

    hours: Union[int, core.IntOut] = core.attr(int, computed=True)

    minutes: Union[int, core.IntOut] = core.attr(int, computed=True)

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

    day: Union[str, core.StringOut] = core.attr(str, computed=True)

    end_time: Union[List[EndTime], core.ArrayOut[EndTime]] = core.attr(
        EndTime, computed=True, kind=core.Kind.array
    )

    start_time: Union[List[StartTime], core.ArrayOut[StartTime]] = core.attr(
        StartTime, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        day: Union[str, core.StringOut],
        end_time: Union[List[EndTime], core.ArrayOut[EndTime]],
        start_time: Union[List[StartTime], core.ArrayOut[StartTime]],
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

        end_time: Union[List[EndTime], core.ArrayOut[EndTime]] = core.arg()

        start_time: Union[List[StartTime], core.ArrayOut[StartTime]] = core.arg()


@core.data(type="aws_connect_hours_of_operation", namespace="aws_connect")
class DsHoursOfOperation(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    config: Union[List[Config], core.ArrayOut[Config]] = core.attr(
        Config, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    hours_of_operation_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    hours_of_operation_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    time_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        hours_of_operation_id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsHoursOfOperation.Args(
                instance_id=instance_id,
                hours_of_operation_id=hours_of_operation_id,
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        hours_of_operation_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
