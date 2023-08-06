from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RunConfig(core.Schema):

    active_tracing: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    memory_in_mb: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        active_tracing: Optional[Union[bool, core.BoolOut]] = None,
        environment_variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        memory_in_mb: Optional[Union[int, core.IntOut]] = None,
        timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=RunConfig.Args(
                active_tracing=active_tracing,
                environment_variables=environment_variables,
                memory_in_mb=memory_in_mb,
                timeout_in_seconds=timeout_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        active_tracing: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        environment_variables: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        memory_in_mb: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        vpc_id: Union[str, core.StringOut],
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                vpc_id=vpc_id,
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Schedule(core.Schema):

    duration_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    expression: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        expression: Union[str, core.StringOut],
        duration_in_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Schedule.Args(
                expression=expression,
                duration_in_seconds=duration_in_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        duration_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        expression: Union[str, core.StringOut] = core.arg()


@core.schema
class S3Encryption(core.Schema):

    encryption_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        encryption_mode: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Encryption.Args(
                encryption_mode=encryption_mode,
                kms_key_arn=kms_key_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ArtifactConfig(core.Schema):

    s3_encryption: Optional[S3Encryption] = core.attr(S3Encryption, default=None)

    def __init__(
        self,
        *,
        s3_encryption: Optional[S3Encryption] = None,
    ):
        super().__init__(
            args=ArtifactConfig.Args(
                s3_encryption=s3_encryption,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        s3_encryption: Optional[S3Encryption] = core.arg(default=None)


@core.schema
class Timeline(core.Schema):

    created: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_started: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_stopped: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        created: Union[str, core.StringOut],
        last_modified: Union[str, core.StringOut],
        last_started: Union[str, core.StringOut],
        last_stopped: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Timeline.Args(
                created=created,
                last_modified=last_modified,
                last_started=last_started,
                last_stopped=last_stopped,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        created: Union[str, core.StringOut] = core.arg()

        last_modified: Union[str, core.StringOut] = core.arg()

        last_started: Union[str, core.StringOut] = core.arg()

        last_stopped: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_synthetics_canary", namespace="aws_synthetics")
class Canary(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    artifact_config: Optional[ArtifactConfig] = core.attr(ArtifactConfig, default=None)

    artifact_s3_location: Union[str, core.StringOut] = core.attr(str)

    delete_lambda: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    engine_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    execution_role_arn: Union[str, core.StringOut] = core.attr(str)

    failure_retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    handler: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    run_config: Optional[RunConfig] = core.attr(RunConfig, default=None, computed=True)

    runtime_version: Union[str, core.StringOut] = core.attr(str)

    s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    schedule: Schedule = core.attr(Schedule)

    source_location_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    start_canary: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    success_retention_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeline: Union[List[Timeline], core.ArrayOut[Timeline]] = core.attr(
        Timeline, computed=True, kind=core.Kind.array
    )

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    zip_file: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        artifact_s3_location: Union[str, core.StringOut],
        execution_role_arn: Union[str, core.StringOut],
        handler: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        runtime_version: Union[str, core.StringOut],
        schedule: Schedule,
        artifact_config: Optional[ArtifactConfig] = None,
        delete_lambda: Optional[Union[bool, core.BoolOut]] = None,
        failure_retention_period: Optional[Union[int, core.IntOut]] = None,
        run_config: Optional[RunConfig] = None,
        s3_bucket: Optional[Union[str, core.StringOut]] = None,
        s3_key: Optional[Union[str, core.StringOut]] = None,
        s3_version: Optional[Union[str, core.StringOut]] = None,
        start_canary: Optional[Union[bool, core.BoolOut]] = None,
        success_retention_period: Optional[Union[int, core.IntOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_config: Optional[VpcConfig] = None,
        zip_file: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Canary.Args(
                artifact_s3_location=artifact_s3_location,
                execution_role_arn=execution_role_arn,
                handler=handler,
                name=name,
                runtime_version=runtime_version,
                schedule=schedule,
                artifact_config=artifact_config,
                delete_lambda=delete_lambda,
                failure_retention_period=failure_retention_period,
                run_config=run_config,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_version=s3_version,
                start_canary=start_canary,
                success_retention_period=success_retention_period,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                zip_file=zip_file,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifact_config: Optional[ArtifactConfig] = core.arg(default=None)

        artifact_s3_location: Union[str, core.StringOut] = core.arg()

        delete_lambda: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        execution_role_arn: Union[str, core.StringOut] = core.arg()

        failure_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        handler: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        run_config: Optional[RunConfig] = core.arg(default=None)

        runtime_version: Union[str, core.StringOut] = core.arg()

        s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        schedule: Schedule = core.arg()

        start_canary: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        success_retention_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Optional[VpcConfig] = core.arg(default=None)

        zip_file: Optional[Union[str, core.StringOut]] = core.arg(default=None)
