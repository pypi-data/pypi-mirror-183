from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Excludes(core.Schema):

    filter_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        filter_type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Excludes.Args(
                filter_type=filter_type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Includes(core.Schema):

    filter_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        filter_type: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Includes.Args(
                filter_type=filter_type,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Schedule(core.Schema):

    schedule_expression: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        schedule_expression: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Schedule.Args(
                schedule_expression=schedule_expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        schedule_expression: Union[str, core.StringOut] = core.arg()


@core.schema
class Options(core.Schema):

    atime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bytes_per_second: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    gid: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mtime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    overwrite_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    posix_permissions: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    preserve_deleted_files: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    preserve_devices: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    task_queueing: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transfer_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    uid: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    verify_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        atime: Optional[Union[str, core.StringOut]] = None,
        bytes_per_second: Optional[Union[int, core.IntOut]] = None,
        gid: Optional[Union[str, core.StringOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
        mtime: Optional[Union[str, core.StringOut]] = None,
        overwrite_mode: Optional[Union[str, core.StringOut]] = None,
        posix_permissions: Optional[Union[str, core.StringOut]] = None,
        preserve_deleted_files: Optional[Union[str, core.StringOut]] = None,
        preserve_devices: Optional[Union[str, core.StringOut]] = None,
        task_queueing: Optional[Union[str, core.StringOut]] = None,
        transfer_mode: Optional[Union[str, core.StringOut]] = None,
        uid: Optional[Union[str, core.StringOut]] = None,
        verify_mode: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Options.Args(
                atime=atime,
                bytes_per_second=bytes_per_second,
                gid=gid,
                log_level=log_level,
                mtime=mtime,
                overwrite_mode=overwrite_mode,
                posix_permissions=posix_permissions,
                preserve_deleted_files=preserve_deleted_files,
                preserve_devices=preserve_devices,
                task_queueing=task_queueing,
                transfer_mode=transfer_mode,
                uid=uid,
                verify_mode=verify_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        atime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bytes_per_second: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        gid: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mtime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        overwrite_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        posix_permissions: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preserve_deleted_files: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        preserve_devices: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        task_queueing: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transfer_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        uid: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        verify_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_datasync_task", namespace="aws_datasync")
class Task(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    destination_location_arn: Union[str, core.StringOut] = core.attr(str)

    excludes: Optional[Excludes] = core.attr(Excludes, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    includes: Optional[Includes] = core.attr(Includes, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    options: Optional[Options] = core.attr(Options, default=None)

    schedule: Optional[Schedule] = core.attr(Schedule, default=None)

    source_location_arn: Union[str, core.StringOut] = core.attr(str)

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
        destination_location_arn: Union[str, core.StringOut],
        source_location_arn: Union[str, core.StringOut],
        cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = None,
        excludes: Optional[Excludes] = None,
        includes: Optional[Includes] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        options: Optional[Options] = None,
        schedule: Optional[Schedule] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Task.Args(
                destination_location_arn=destination_location_arn,
                source_location_arn=source_location_arn,
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                excludes=excludes,
                includes=includes,
                name=name,
                options=options,
                schedule=schedule,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_log_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        destination_location_arn: Union[str, core.StringOut] = core.arg()

        excludes: Optional[Excludes] = core.arg(default=None)

        includes: Optional[Includes] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        options: Optional[Options] = core.arg(default=None)

        schedule: Optional[Schedule] = core.arg(default=None)

        source_location_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
