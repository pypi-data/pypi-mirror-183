from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ImageConfig(core.Schema):

    command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    entry_point: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    working_directory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        entry_point: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        working_directory: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ImageConfig.Args(
                command=command,
                entry_point=entry_point,
                working_directory=working_directory,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        command: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        entry_point: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        working_directory: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class DeadLetterConfig(core.Schema):

    target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        target_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=DeadLetterConfig.Args(
                target_arn=target_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        target_arn: Union[str, core.StringOut] = core.arg()


@core.schema
class Environment(core.Schema):

    variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Environment.Args(
                variables=variables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class TracingConfig(core.Schema):

    mode: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        mode: Union[str, core.StringOut],
    ):
        super().__init__(
            args=TracingConfig.Args(
                mode=mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mode: Union[str, core.StringOut] = core.arg()


@core.schema
class EphemeralStorage(core.Schema):

    size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    def __init__(
        self,
        *,
        size: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size=size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class FileSystemConfig(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    local_mount_path: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        local_mount_path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=FileSystemConfig.Args(
                arn=arn,
                local_mount_path=local_mount_path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        local_mount_path: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lambda_function", namespace="aws_lambda")
class Function(core.Resource):

    architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    code_signing_config_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    dead_letter_config: Optional[DeadLetterConfig] = core.attr(DeadLetterConfig, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    environment: Optional[Environment] = core.attr(Environment, default=None)

    ephemeral_storage: Optional[EphemeralStorage] = core.attr(
        EphemeralStorage, default=None, computed=True
    )

    file_system_config: Optional[FileSystemConfig] = core.attr(FileSystemConfig, default=None)

    filename: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    function_name: Union[str, core.StringOut] = core.attr(str)

    handler: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_config: Optional[ImageConfig] = core.attr(ImageConfig, default=None)

    image_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    invoke_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    layers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    memory_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    package_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    publish: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    qualified_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    reserved_concurrent_executions: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    role: Union[str, core.StringOut] = core.attr(str)

    runtime: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_object_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    signing_job_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_profile_version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_code_hash: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    source_code_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    tracing_config: Optional[TracingConfig] = core.attr(TracingConfig, default=None, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        role: Union[str, core.StringOut],
        architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        code_signing_config_arn: Optional[Union[str, core.StringOut]] = None,
        dead_letter_config: Optional[DeadLetterConfig] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        environment: Optional[Environment] = None,
        ephemeral_storage: Optional[EphemeralStorage] = None,
        file_system_config: Optional[FileSystemConfig] = None,
        filename: Optional[Union[str, core.StringOut]] = None,
        handler: Optional[Union[str, core.StringOut]] = None,
        image_config: Optional[ImageConfig] = None,
        image_uri: Optional[Union[str, core.StringOut]] = None,
        kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        layers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        memory_size: Optional[Union[int, core.IntOut]] = None,
        package_type: Optional[Union[str, core.StringOut]] = None,
        publish: Optional[Union[bool, core.BoolOut]] = None,
        reserved_concurrent_executions: Optional[Union[int, core.IntOut]] = None,
        runtime: Optional[Union[str, core.StringOut]] = None,
        s3_bucket: Optional[Union[str, core.StringOut]] = None,
        s3_key: Optional[Union[str, core.StringOut]] = None,
        s3_object_version: Optional[Union[str, core.StringOut]] = None,
        source_code_hash: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout: Optional[Union[int, core.IntOut]] = None,
        tracing_config: Optional[TracingConfig] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                function_name=function_name,
                role=role,
                architectures=architectures,
                code_signing_config_arn=code_signing_config_arn,
                dead_letter_config=dead_letter_config,
                description=description,
                environment=environment,
                ephemeral_storage=ephemeral_storage,
                file_system_config=file_system_config,
                filename=filename,
                handler=handler,
                image_config=image_config,
                image_uri=image_uri,
                kms_key_arn=kms_key_arn,
                layers=layers,
                memory_size=memory_size,
                package_type=package_type,
                publish=publish,
                reserved_concurrent_executions=reserved_concurrent_executions,
                runtime=runtime,
                s3_bucket=s3_bucket,
                s3_key=s3_key,
                s3_object_version=s3_object_version,
                source_code_hash=source_code_hash,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                tracing_config=tracing_config,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        architectures: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        code_signing_config_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        dead_letter_config: Optional[DeadLetterConfig] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment: Optional[Environment] = core.arg(default=None)

        ephemeral_storage: Optional[EphemeralStorage] = core.arg(default=None)

        file_system_config: Optional[FileSystemConfig] = core.arg(default=None)

        filename: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        handler: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_config: Optional[ImageConfig] = core.arg(default=None)

        image_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        layers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        memory_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        package_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        publish: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        reserved_concurrent_executions: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        role: Union[str, core.StringOut] = core.arg()

        runtime: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_object_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_code_hash: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        tracing_config: Optional[TracingConfig] = core.arg(default=None)

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
