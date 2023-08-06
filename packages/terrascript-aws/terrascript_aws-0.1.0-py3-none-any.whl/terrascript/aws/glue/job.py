from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ExecutionProperty(core.Schema):

    max_concurrent_runs: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_concurrent_runs: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ExecutionProperty.Args(
                max_concurrent_runs=max_concurrent_runs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_concurrent_runs: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Command(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    python_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    script_location: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        script_location: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        python_version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Command.Args(
                script_location=script_location,
                name=name,
                python_version=python_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        python_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        script_location: Union[str, core.StringOut] = core.arg()


@core.schema
class NotificationProperty(core.Schema):

    notify_delay_after: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        notify_delay_after: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=NotificationProperty.Args(
                notify_delay_after=notify_delay_after,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notify_delay_after: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_glue_job", namespace="aws_glue")
class Job(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    command: Command = core.attr(Command)

    connections: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    default_arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_class: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_property: Optional[ExecutionProperty] = core.attr(
        ExecutionProperty, default=None, computed=True
    )

    glue_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_capacity: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None, computed=True
    )

    max_retries: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    non_overridable_arguments: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    notification_property: Optional[NotificationProperty] = core.attr(
        NotificationProperty, default=None, computed=True
    )

    number_of_workers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    security_configuration: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    worker_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        command: Command,
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        connections: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        default_arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        execution_class: Optional[Union[str, core.StringOut]] = None,
        execution_property: Optional[ExecutionProperty] = None,
        glue_version: Optional[Union[str, core.StringOut]] = None,
        max_capacity: Optional[Union[float, core.FloatOut]] = None,
        max_retries: Optional[Union[int, core.IntOut]] = None,
        non_overridable_arguments: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        notification_property: Optional[NotificationProperty] = None,
        number_of_workers: Optional[Union[int, core.IntOut]] = None,
        security_configuration: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
        worker_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Job.Args(
                command=command,
                name=name,
                role_arn=role_arn,
                connections=connections,
                default_arguments=default_arguments,
                description=description,
                execution_class=execution_class,
                execution_property=execution_property,
                glue_version=glue_version,
                max_capacity=max_capacity,
                max_retries=max_retries,
                non_overridable_arguments=non_overridable_arguments,
                notification_property=notification_property,
                number_of_workers=number_of_workers,
                security_configuration=security_configuration,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                worker_type=worker_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        command: Command = core.arg()

        connections: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        default_arguments: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        execution_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        execution_property: Optional[ExecutionProperty] = core.arg(default=None)

        glue_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_capacity: Optional[Union[float, core.FloatOut]] = core.arg(default=None)

        max_retries: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        non_overridable_arguments: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        notification_property: Optional[NotificationProperty] = core.arg(default=None)

        number_of_workers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()

        security_configuration: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        worker_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
