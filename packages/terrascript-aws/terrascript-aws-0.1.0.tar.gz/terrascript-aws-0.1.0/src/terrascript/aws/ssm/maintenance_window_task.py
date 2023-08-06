from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class StepFunctionsParameters(core.Schema):

    input: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        input: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StepFunctionsParameters.Args(
                input=input,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Parameter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class AutomationParameters(core.Schema):

    document_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        document_version: Optional[Union[str, core.StringOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
    ):
        super().__init__(
            args=AutomationParameters.Args(
                document_version=document_version,
                parameter=parameter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        document_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )


@core.schema
class LambdaParameters(core.Schema):

    client_context: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    payload: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        client_context: Optional[Union[str, core.StringOut]] = None,
        payload: Optional[Union[str, core.StringOut]] = None,
        qualifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaParameters.Args(
                client_context=client_context,
                payload=payload,
                qualifier=qualifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_context: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        payload: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CloudwatchConfig(core.Schema):

    cloudwatch_log_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cloudwatch_output_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        cloudwatch_log_group_name: Optional[Union[str, core.StringOut]] = None,
        cloudwatch_output_enabled: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=CloudwatchConfig.Args(
                cloudwatch_log_group_name=cloudwatch_log_group_name,
                cloudwatch_output_enabled=cloudwatch_output_enabled,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_log_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cloudwatch_output_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class NotificationConfig(core.Schema):

    notification_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    notification_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        notification_arn: Optional[Union[str, core.StringOut]] = None,
        notification_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        notification_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=NotificationConfig.Args(
                notification_arn=notification_arn,
                notification_events=notification_events,
                notification_type=notification_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        notification_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_events: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        notification_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RunCommandParameters(core.Schema):

    cloudwatch_config: Optional[CloudwatchConfig] = core.attr(CloudwatchConfig, default=None)

    comment: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_hash: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_hash_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    document_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    notification_config: Optional[NotificationConfig] = core.attr(NotificationConfig, default=None)

    output_s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    output_s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    service_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    timeout_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cloudwatch_config: Optional[CloudwatchConfig] = None,
        comment: Optional[Union[str, core.StringOut]] = None,
        document_hash: Optional[Union[str, core.StringOut]] = None,
        document_hash_type: Optional[Union[str, core.StringOut]] = None,
        document_version: Optional[Union[str, core.StringOut]] = None,
        notification_config: Optional[NotificationConfig] = None,
        output_s3_bucket: Optional[Union[str, core.StringOut]] = None,
        output_s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
        service_role_arn: Optional[Union[str, core.StringOut]] = None,
        timeout_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=RunCommandParameters.Args(
                cloudwatch_config=cloudwatch_config,
                comment=comment,
                document_hash=document_hash,
                document_hash_type=document_hash_type,
                document_version=document_version,
                notification_config=notification_config,
                output_s3_bucket=output_s3_bucket,
                output_s3_key_prefix=output_s3_key_prefix,
                parameter=parameter,
                service_role_arn=service_role_arn,
                timeout_seconds=timeout_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_config: Optional[CloudwatchConfig] = core.arg(default=None)

        comment: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_hash: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_hash_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        document_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_config: Optional[NotificationConfig] = core.arg(default=None)

        output_s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        output_s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        service_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        timeout_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class TaskInvocationParameters(core.Schema):

    automation_parameters: Optional[AutomationParameters] = core.attr(
        AutomationParameters, default=None
    )

    lambda_parameters: Optional[LambdaParameters] = core.attr(LambdaParameters, default=None)

    run_command_parameters: Optional[RunCommandParameters] = core.attr(
        RunCommandParameters, default=None
    )

    step_functions_parameters: Optional[StepFunctionsParameters] = core.attr(
        StepFunctionsParameters, default=None
    )

    def __init__(
        self,
        *,
        automation_parameters: Optional[AutomationParameters] = None,
        lambda_parameters: Optional[LambdaParameters] = None,
        run_command_parameters: Optional[RunCommandParameters] = None,
        step_functions_parameters: Optional[StepFunctionsParameters] = None,
    ):
        super().__init__(
            args=TaskInvocationParameters.Args(
                automation_parameters=automation_parameters,
                lambda_parameters=lambda_parameters,
                run_command_parameters=run_command_parameters,
                step_functions_parameters=step_functions_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        automation_parameters: Optional[AutomationParameters] = core.arg(default=None)

        lambda_parameters: Optional[LambdaParameters] = core.arg(default=None)

        run_command_parameters: Optional[RunCommandParameters] = core.arg(default=None)

        step_functions_parameters: Optional[StepFunctionsParameters] = core.arg(default=None)


@core.schema
class Targets(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Targets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.resource(type="aws_ssm_maintenance_window_task", namespace="aws_ssm")
class MaintenanceWindowTask(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cutoff_behavior: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_concurrency: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    max_errors: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    priority: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    service_role_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = core.attr(
        Targets, default=None, kind=core.Kind.array
    )

    task_arn: Union[str, core.StringOut] = core.attr(str)

    task_invocation_parameters: Optional[TaskInvocationParameters] = core.attr(
        TaskInvocationParameters, default=None
    )

    task_type: Union[str, core.StringOut] = core.attr(str)

    window_id: Union[str, core.StringOut] = core.attr(str)

    window_task_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        task_arn: Union[str, core.StringOut],
        task_type: Union[str, core.StringOut],
        window_id: Union[str, core.StringOut],
        cutoff_behavior: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        max_concurrency: Optional[Union[str, core.StringOut]] = None,
        max_errors: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        priority: Optional[Union[int, core.IntOut]] = None,
        service_role_arn: Optional[Union[str, core.StringOut]] = None,
        targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = None,
        task_invocation_parameters: Optional[TaskInvocationParameters] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MaintenanceWindowTask.Args(
                task_arn=task_arn,
                task_type=task_type,
                window_id=window_id,
                cutoff_behavior=cutoff_behavior,
                description=description,
                max_concurrency=max_concurrency,
                max_errors=max_errors,
                name=name,
                priority=priority,
                service_role_arn=service_role_arn,
                targets=targets,
                task_invocation_parameters=task_invocation_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cutoff_behavior: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_concurrency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_errors: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        priority: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        service_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        targets: Optional[Union[List[Targets], core.ArrayOut[Targets]]] = core.arg(default=None)

        task_arn: Union[str, core.StringOut] = core.arg()

        task_invocation_parameters: Optional[TaskInvocationParameters] = core.arg(default=None)

        task_type: Union[str, core.StringOut] = core.arg()

        window_id: Union[str, core.StringOut] = core.arg()
