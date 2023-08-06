from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Environment(core.Schema):

    variables: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        *,
        variables: Union[Dict[str, str], core.MapOut[core.StringOut]],
    ):
        super().__init__(
            args=Environment.Args(
                variables=variables,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        variables: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
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
class FileSystemConfig(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    local_mount_path: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.schema
class TracingConfig(core.Schema):

    mode: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    size: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        size: Union[int, core.IntOut],
    ):
        super().__init__(
            args=EphemeralStorage.Args(
                size=size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        size: Union[int, core.IntOut] = core.arg()


@core.schema
class DeadLetterConfig(core.Schema):

    target_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

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


@core.data(type="aws_lambda_function", namespace="aws_lambda")
class DsFunction(core.Data):

    architectures: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    code_signing_config_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    dead_letter_config: Union[List[DeadLetterConfig], core.ArrayOut[DeadLetterConfig]] = core.attr(
        DeadLetterConfig, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    environment: Union[List[Environment], core.ArrayOut[Environment]] = core.attr(
        Environment, computed=True, kind=core.Kind.array
    )

    ephemeral_storage: Union[List[EphemeralStorage], core.ArrayOut[EphemeralStorage]] = core.attr(
        EphemeralStorage, computed=True, kind=core.Kind.array
    )

    file_system_config: Union[List[FileSystemConfig], core.ArrayOut[FileSystemConfig]] = core.attr(
        FileSystemConfig, computed=True, kind=core.Kind.array
    )

    function_name: Union[str, core.StringOut] = core.attr(str)

    handler: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_uri: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_modified: Union[str, core.StringOut] = core.attr(str, computed=True)

    layers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    memory_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    qualified_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    reserved_concurrent_executions: Union[int, core.IntOut] = core.attr(int, computed=True)

    role: Union[str, core.StringOut] = core.attr(str, computed=True)

    runtime: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_job_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_profile_version_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_code_hash: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_code_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    tracing_config: Union[List[TracingConfig], core.ArrayOut[TracingConfig]] = core.attr(
        TracingConfig, computed=True, kind=core.Kind.array
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_config: Union[List[VpcConfig], core.ArrayOut[VpcConfig]] = core.attr(
        VpcConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        function_name: Union[str, core.StringOut],
        qualifier: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFunction.Args(
                function_name=function_name,
                qualifier=qualifier,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        function_name: Union[str, core.StringOut] = core.arg()

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
