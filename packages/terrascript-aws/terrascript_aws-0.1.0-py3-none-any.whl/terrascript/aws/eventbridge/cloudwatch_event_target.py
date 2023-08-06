from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RedshiftTarget(core.Schema):

    database: Union[str, core.StringOut] = core.attr(str)

    db_user: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sql: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    statement_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    with_event: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        database: Union[str, core.StringOut],
        db_user: Optional[Union[str, core.StringOut]] = None,
        secrets_manager_arn: Optional[Union[str, core.StringOut]] = None,
        sql: Optional[Union[str, core.StringOut]] = None,
        statement_name: Optional[Union[str, core.StringOut]] = None,
        with_event: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=RedshiftTarget.Args(
                database=database,
                db_user=db_user,
                secrets_manager_arn=secrets_manager_arn,
                sql=sql,
                statement_name=statement_name,
                with_event=with_event,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        database: Union[str, core.StringOut] = core.arg()

        db_user: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secrets_manager_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sql: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        statement_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        with_event: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class InputTransformer(core.Schema):

    input_paths: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    input_template: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        input_template: Union[str, core.StringOut],
        input_paths: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=InputTransformer.Args(
                input_template=input_template,
                input_paths=input_paths,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        input_paths: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        input_template: Union[str, core.StringOut] = core.arg()


@core.schema
class BatchTarget(core.Schema):

    array_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    job_attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    job_definition: Union[str, core.StringOut] = core.attr(str)

    job_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        job_definition: Union[str, core.StringOut],
        job_name: Union[str, core.StringOut],
        array_size: Optional[Union[int, core.IntOut]] = None,
        job_attempts: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=BatchTarget.Args(
                job_definition=job_definition,
                job_name=job_name,
                array_size=array_size,
                job_attempts=job_attempts,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        array_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        job_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        job_definition: Union[str, core.StringOut] = core.arg()

        job_name: Union[str, core.StringOut] = core.arg()


@core.schema
class KinesisTarget(core.Schema):

    partition_key_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        partition_key_path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=KinesisTarget.Args(
                partition_key_path=partition_key_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        partition_key_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RetryPolicy(core.Schema):

    maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = None,
        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=RetryPolicy.Args(
                maximum_event_age_in_seconds=maximum_event_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class DeadLetterConfig(core.Schema):

    arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeadLetterConfig.Args(
                arn=arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class HttpTarget(core.Schema):

    header_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    path_parameter_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    query_string_parameters: Optional[
        Union[Dict[str, str], core.MapOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.map)

    def __init__(
        self,
        *,
        header_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        path_parameter_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        query_string_parameters: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=HttpTarget.Args(
                header_parameters=header_parameters,
                path_parameter_values=path_parameter_values,
                query_string_parameters=query_string_parameters,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        header_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        path_parameter_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        query_string_parameters: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class SqsTarget(core.Schema):

    message_group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        message_group_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SqsTarget.Args(
                message_group_id=message_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        message_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RunCommandTargets(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=RunCommandTargets.Args(
                key=key,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class PlacementConstraint(core.Schema):

    expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        expression: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PlacementConstraint.Args(
                type=type,
                expression=expression,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class NetworkConfiguration(core.Schema):

    assign_public_ip: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        assign_public_ip: Optional[Union[bool, core.BoolOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=NetworkConfiguration.Args(
                subnets=subnets,
                assign_public_ip=assign_public_ip,
                security_groups=security_groups,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        assign_public_ip: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class EcsTarget(core.Schema):

    enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_execute_command: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    network_configuration: Optional[NetworkConfiguration] = core.attr(
        NetworkConfiguration, default=None
    )

    placement_constraint: Optional[
        Union[List[PlacementConstraint], core.ArrayOut[PlacementConstraint]]
    ] = core.attr(PlacementConstraint, default=None, kind=core.Kind.array)

    platform_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    propagate_tags: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    task_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    task_definition_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        task_definition_arn: Union[str, core.StringOut],
        enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = None,
        enable_execute_command: Optional[Union[bool, core.BoolOut]] = None,
        group: Optional[Union[str, core.StringOut]] = None,
        launch_type: Optional[Union[str, core.StringOut]] = None,
        network_configuration: Optional[NetworkConfiguration] = None,
        placement_constraint: Optional[
            Union[List[PlacementConstraint], core.ArrayOut[PlacementConstraint]]
        ] = None,
        platform_version: Optional[Union[str, core.StringOut]] = None,
        propagate_tags: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        task_count: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EcsTarget.Args(
                task_definition_arn=task_definition_arn,
                enable_ecs_managed_tags=enable_ecs_managed_tags,
                enable_execute_command=enable_execute_command,
                group=group,
                launch_type=launch_type,
                network_configuration=network_configuration,
                placement_constraint=placement_constraint,
                platform_version=platform_version,
                propagate_tags=propagate_tags,
                tags=tags,
                task_count=task_count,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enable_ecs_managed_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_execute_command: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_configuration: Optional[NetworkConfiguration] = core.arg(default=None)

        placement_constraint: Optional[
            Union[List[PlacementConstraint], core.ArrayOut[PlacementConstraint]]
        ] = core.arg(default=None)

        platform_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        propagate_tags: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        task_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        task_definition_arn: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_cloudwatch_event_target", namespace="aws_eventbridge")
class CloudwatchEventTarget(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str)

    batch_target: Optional[BatchTarget] = core.attr(BatchTarget, default=None)

    dead_letter_config: Optional[DeadLetterConfig] = core.attr(DeadLetterConfig, default=None)

    ecs_target: Optional[EcsTarget] = core.attr(EcsTarget, default=None)

    event_bus_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_target: Optional[HttpTarget] = core.attr(HttpTarget, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    input_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    input_transformer: Optional[InputTransformer] = core.attr(InputTransformer, default=None)

    kinesis_target: Optional[KinesisTarget] = core.attr(KinesisTarget, default=None)

    redshift_target: Optional[RedshiftTarget] = core.attr(RedshiftTarget, default=None)

    retry_policy: Optional[RetryPolicy] = core.attr(RetryPolicy, default=None)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule: Union[str, core.StringOut] = core.attr(str)

    run_command_targets: Optional[
        Union[List[RunCommandTargets], core.ArrayOut[RunCommandTargets]]
    ] = core.attr(RunCommandTargets, default=None, kind=core.Kind.array)

    sqs_target: Optional[SqsTarget] = core.attr(SqsTarget, default=None)

    target_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        arn: Union[str, core.StringOut],
        rule: Union[str, core.StringOut],
        batch_target: Optional[BatchTarget] = None,
        dead_letter_config: Optional[DeadLetterConfig] = None,
        ecs_target: Optional[EcsTarget] = None,
        event_bus_name: Optional[Union[str, core.StringOut]] = None,
        http_target: Optional[HttpTarget] = None,
        input: Optional[Union[str, core.StringOut]] = None,
        input_path: Optional[Union[str, core.StringOut]] = None,
        input_transformer: Optional[InputTransformer] = None,
        kinesis_target: Optional[KinesisTarget] = None,
        redshift_target: Optional[RedshiftTarget] = None,
        retry_policy: Optional[RetryPolicy] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        run_command_targets: Optional[
            Union[List[RunCommandTargets], core.ArrayOut[RunCommandTargets]]
        ] = None,
        sqs_target: Optional[SqsTarget] = None,
        target_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CloudwatchEventTarget.Args(
                arn=arn,
                rule=rule,
                batch_target=batch_target,
                dead_letter_config=dead_letter_config,
                ecs_target=ecs_target,
                event_bus_name=event_bus_name,
                http_target=http_target,
                input=input,
                input_path=input_path,
                input_transformer=input_transformer,
                kinesis_target=kinesis_target,
                redshift_target=redshift_target,
                retry_policy=retry_policy,
                role_arn=role_arn,
                run_command_targets=run_command_targets,
                sqs_target=sqs_target,
                target_id=target_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        arn: Union[str, core.StringOut] = core.arg()

        batch_target: Optional[BatchTarget] = core.arg(default=None)

        dead_letter_config: Optional[DeadLetterConfig] = core.arg(default=None)

        ecs_target: Optional[EcsTarget] = core.arg(default=None)

        event_bus_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_target: Optional[HttpTarget] = core.arg(default=None)

        input: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        input_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        input_transformer: Optional[InputTransformer] = core.arg(default=None)

        kinesis_target: Optional[KinesisTarget] = core.arg(default=None)

        redshift_target: Optional[RedshiftTarget] = core.arg(default=None)

        retry_policy: Optional[RetryPolicy] = core.arg(default=None)

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule: Union[str, core.StringOut] = core.arg()

        run_command_targets: Optional[
            Union[List[RunCommandTargets], core.ArrayOut[RunCommandTargets]]
        ] = core.arg(default=None)

        sqs_target: Optional[SqsTarget] = core.arg(default=None)

        target_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
