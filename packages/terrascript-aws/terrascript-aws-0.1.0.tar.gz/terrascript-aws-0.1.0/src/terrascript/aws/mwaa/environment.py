from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DagProcessingLogs(core.Schema):

    cloud_watch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DagProcessingLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SchedulerLogs(core.Schema):

    cloud_watch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SchedulerLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class TaskLogs(core.Schema):

    cloud_watch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=TaskLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WebserverLogs(core.Schema):

    cloud_watch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WebserverLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class WorkerLogs(core.Schema):

    cloud_watch_log_group_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    log_level: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        cloud_watch_log_group_arn: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        log_level: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WorkerLogs.Args(
                cloud_watch_log_group_arn=cloud_watch_log_group_arn,
                enabled=enabled,
                log_level=log_level,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_log_group_arn: Union[str, core.StringOut] = core.arg()

        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        log_level: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LoggingConfiguration(core.Schema):

    dag_processing_logs: Optional[DagProcessingLogs] = core.attr(
        DagProcessingLogs, default=None, computed=True
    )

    scheduler_logs: Optional[SchedulerLogs] = core.attr(SchedulerLogs, default=None, computed=True)

    task_logs: Optional[TaskLogs] = core.attr(TaskLogs, default=None, computed=True)

    webserver_logs: Optional[WebserverLogs] = core.attr(WebserverLogs, default=None, computed=True)

    worker_logs: Optional[WorkerLogs] = core.attr(WorkerLogs, default=None, computed=True)

    def __init__(
        self,
        *,
        dag_processing_logs: Optional[DagProcessingLogs] = None,
        scheduler_logs: Optional[SchedulerLogs] = None,
        task_logs: Optional[TaskLogs] = None,
        webserver_logs: Optional[WebserverLogs] = None,
        worker_logs: Optional[WorkerLogs] = None,
    ):
        super().__init__(
            args=LoggingConfiguration.Args(
                dag_processing_logs=dag_processing_logs,
                scheduler_logs=scheduler_logs,
                task_logs=task_logs,
                webserver_logs=webserver_logs,
                worker_logs=worker_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        dag_processing_logs: Optional[DagProcessingLogs] = core.arg(default=None)

        scheduler_logs: Optional[SchedulerLogs] = core.arg(default=None)

        task_logs: Optional[TaskLogs] = core.arg(default=None)

        webserver_logs: Optional[WebserverLogs] = core.arg(default=None)

        worker_logs: Optional[WorkerLogs] = core.arg(default=None)


@core.schema
class Error(core.Schema):

    error_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    error_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        error_code: Union[str, core.StringOut],
        error_message: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Error.Args(
                error_code=error_code,
                error_message=error_message,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        error_code: Union[str, core.StringOut] = core.arg()

        error_message: Union[str, core.StringOut] = core.arg()


@core.schema
class LastUpdated(core.Schema):

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    error: Union[List[Error], core.ArrayOut[Error]] = core.attr(
        Error, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        created_at: Union[str, core.StringOut],
        error: Union[List[Error], core.ArrayOut[Error]],
        status: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LastUpdated.Args(
                created_at=created_at,
                error=error,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        created_at: Union[str, core.StringOut] = core.arg()

        error: Union[List[Error], core.ArrayOut[Error]] = core.arg()

        status: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkConfiguration(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_mwaa_environment", namespace="aws_mwaa")
class Environment(core.Resource):

    airflow_configuration_options: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    airflow_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    dag_s3_path: Union[str, core.StringOut] = core.attr(str)

    environment_class: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    last_updated: Union[List[LastUpdated], core.ArrayOut[LastUpdated]] = core.attr(
        LastUpdated, computed=True, kind=core.Kind.array
    )

    logging_configuration: Optional[LoggingConfiguration] = core.attr(
        LoggingConfiguration, default=None, computed=True
    )

    max_workers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    min_workers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    network_configuration: NetworkConfiguration = core.attr(NetworkConfiguration)

    plugins_s3_object_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    plugins_s3_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    requirements_s3_object_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    requirements_s3_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedulers: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    service_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_bucket_arn: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    webserver_access_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    webserver_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    weekly_maintenance_window_start: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        dag_s3_path: Union[str, core.StringOut],
        execution_role_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        network_configuration: NetworkConfiguration,
        source_bucket_arn: Union[str, core.StringOut],
        airflow_configuration_options: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
        airflow_version: Optional[Union[str, core.StringOut]] = None,
        environment_class: Optional[Union[str, core.StringOut]] = None,
        kms_key: Optional[Union[str, core.StringOut]] = None,
        logging_configuration: Optional[LoggingConfiguration] = None,
        max_workers: Optional[Union[int, core.IntOut]] = None,
        min_workers: Optional[Union[int, core.IntOut]] = None,
        plugins_s3_object_version: Optional[Union[str, core.StringOut]] = None,
        plugins_s3_path: Optional[Union[str, core.StringOut]] = None,
        requirements_s3_object_version: Optional[Union[str, core.StringOut]] = None,
        requirements_s3_path: Optional[Union[str, core.StringOut]] = None,
        schedulers: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        webserver_access_mode: Optional[Union[str, core.StringOut]] = None,
        weekly_maintenance_window_start: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Environment.Args(
                dag_s3_path=dag_s3_path,
                execution_role_arn=execution_role_arn,
                name=name,
                network_configuration=network_configuration,
                source_bucket_arn=source_bucket_arn,
                airflow_configuration_options=airflow_configuration_options,
                airflow_version=airflow_version,
                environment_class=environment_class,
                kms_key=kms_key,
                logging_configuration=logging_configuration,
                max_workers=max_workers,
                min_workers=min_workers,
                plugins_s3_object_version=plugins_s3_object_version,
                plugins_s3_path=plugins_s3_path,
                requirements_s3_object_version=requirements_s3_object_version,
                requirements_s3_path=requirements_s3_path,
                schedulers=schedulers,
                tags=tags,
                tags_all=tags_all,
                webserver_access_mode=webserver_access_mode,
                weekly_maintenance_window_start=weekly_maintenance_window_start,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        airflow_configuration_options: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        airflow_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dag_s3_path: Union[str, core.StringOut] = core.arg()

        environment_class: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        execution_role_arn: Union[str, core.StringOut] = core.arg()

        kms_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        logging_configuration: Optional[LoggingConfiguration] = core.arg(default=None)

        max_workers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        min_workers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        network_configuration: NetworkConfiguration = core.arg()

        plugins_s3_object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        plugins_s3_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        requirements_s3_object_version: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        requirements_s3_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedulers: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        source_bucket_arn: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        webserver_access_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        weekly_maintenance_window_start: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )
