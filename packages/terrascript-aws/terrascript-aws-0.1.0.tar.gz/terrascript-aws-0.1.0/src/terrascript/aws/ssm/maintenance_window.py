from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssm_maintenance_window", namespace="aws_ssm")
class MaintenanceWindow(core.Resource):

    allow_unassociated_targets: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cutoff: Union[int, core.IntOut] = core.attr(int)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    duration: Union[int, core.IntOut] = core.attr(int)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    end_date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    schedule: Union[str, core.StringOut] = core.attr(str)

    schedule_offset: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    schedule_timezone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    start_date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        cutoff: Union[int, core.IntOut],
        duration: Union[int, core.IntOut],
        name: Union[str, core.StringOut],
        schedule: Union[str, core.StringOut],
        allow_unassociated_targets: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        end_date: Optional[Union[str, core.StringOut]] = None,
        schedule_offset: Optional[Union[int, core.IntOut]] = None,
        schedule_timezone: Optional[Union[str, core.StringOut]] = None,
        start_date: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindow.Args(
                cutoff=cutoff,
                duration=duration,
                name=name,
                schedule=schedule,
                allow_unassociated_targets=allow_unassociated_targets,
                description=description,
                enabled=enabled,
                end_date=end_date,
                schedule_offset=schedule_offset,
                schedule_timezone=schedule_timezone,
                start_date=start_date,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allow_unassociated_targets: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cutoff: Union[int, core.IntOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        duration: Union[int, core.IntOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        end_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        schedule: Union[str, core.StringOut] = core.arg()

        schedule_offset: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        schedule_timezone: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        start_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
