from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class S3Logs(core.Schema):

    bucket_owner_access: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        bucket_owner_access: Optional[Union[str, core.StringOut]] = None,
        encryption_disabled: Optional[Union[bool, core.BoolOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3Logs.Args(
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                status=status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket_owner_access: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class CloudwatchLogs(core.Schema):

    group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stream_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        group_name: Optional[Union[str, core.StringOut]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        stream_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                group_name=group_name,
                status=status,
                stream_name=stream_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stream_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class LogsConfig(core.Schema):

    cloudwatch_logs: Optional[CloudwatchLogs] = core.attr(CloudwatchLogs, default=None)

    s3_logs: Optional[S3Logs] = core.attr(S3Logs, default=None)

    def __init__(
        self,
        *,
        cloudwatch_logs: Optional[CloudwatchLogs] = None,
        s3_logs: Optional[S3Logs] = None,
    ):
        super().__init__(
            args=LogsConfig.Args(
                cloudwatch_logs=cloudwatch_logs,
                s3_logs=s3_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs: Optional[CloudwatchLogs] = core.arg(default=None)

        s3_logs: Optional[S3Logs] = core.arg(default=None)


@core.schema
class RegistryCredential(core.Schema):

    credential: Union[str, core.StringOut] = core.attr(str)

    credential_provider: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        credential: Union[str, core.StringOut],
        credential_provider: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RegistryCredential.Args(
                credential=credential,
                credential_provider=credential_provider,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        credential: Union[str, core.StringOut] = core.arg()

        credential_provider: Union[str, core.StringOut] = core.arg()


@core.schema
class EnvironmentVariable(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EnvironmentVariable.Args(
                name=name,
                value=value,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class Environment(core.Schema):

    certificate: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    compute_type: Union[str, core.StringOut] = core.attr(str)

    environment_variable: Optional[
        Union[List[EnvironmentVariable], core.ArrayOut[EnvironmentVariable]]
    ] = core.attr(EnvironmentVariable, default=None, kind=core.Kind.array)

    image: Union[str, core.StringOut] = core.attr(str)

    image_pull_credentials_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    privileged_mode: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    registry_credential: Optional[RegistryCredential] = core.attr(RegistryCredential, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        compute_type: Union[str, core.StringOut],
        image: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        certificate: Optional[Union[str, core.StringOut]] = None,
        environment_variable: Optional[
            Union[List[EnvironmentVariable], core.ArrayOut[EnvironmentVariable]]
        ] = None,
        image_pull_credentials_type: Optional[Union[str, core.StringOut]] = None,
        privileged_mode: Optional[Union[bool, core.BoolOut]] = None,
        registry_credential: Optional[RegistryCredential] = None,
    ):
        super().__init__(
            args=Environment.Args(
                compute_type=compute_type,
                image=image,
                type=type,
                certificate=certificate,
                environment_variable=environment_variable,
                image_pull_credentials_type=image_pull_credentials_type,
                privileged_mode=privileged_mode,
                registry_credential=registry_credential,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compute_type: Union[str, core.StringOut] = core.arg()

        environment_variable: Optional[
            Union[List[EnvironmentVariable], core.ArrayOut[EnvironmentVariable]]
        ] = core.arg(default=None)

        image: Union[str, core.StringOut] = core.arg()

        image_pull_credentials_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        privileged_mode: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        registry_credential: Optional[RegistryCredential] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class GitSubmodulesConfig(core.Schema):

    fetch_submodules: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        fetch_submodules: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=GitSubmodulesConfig.Args(
                fetch_submodules=fetch_submodules,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        fetch_submodules: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Auth(core.Schema):

    resource: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        resource: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Auth.Args(
                type=type,
                resource=resource,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        resource: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class BuildStatusConfig(core.Schema):

    context: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        context: Optional[Union[str, core.StringOut]] = None,
        target_url: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=BuildStatusConfig.Args(
                context=context,
                target_url=target_url,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        context: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SecondarySources(core.Schema):

    auth: Optional[Auth] = core.attr(Auth, default=None)

    build_status_config: Optional[BuildStatusConfig] = core.attr(BuildStatusConfig, default=None)

    buildspec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    git_clone_depth: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    git_submodules_config: Optional[GitSubmodulesConfig] = core.attr(
        GitSubmodulesConfig, default=None
    )

    insecure_ssl: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    report_build_status: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    source_identifier: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source_identifier: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        auth: Optional[Auth] = None,
        build_status_config: Optional[BuildStatusConfig] = None,
        buildspec: Optional[Union[str, core.StringOut]] = None,
        git_clone_depth: Optional[Union[int, core.IntOut]] = None,
        git_submodules_config: Optional[GitSubmodulesConfig] = None,
        insecure_ssl: Optional[Union[bool, core.BoolOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        report_build_status: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=SecondarySources.Args(
                source_identifier=source_identifier,
                type=type,
                auth=auth,
                build_status_config=build_status_config,
                buildspec=buildspec,
                git_clone_depth=git_clone_depth,
                git_submodules_config=git_submodules_config,
                insecure_ssl=insecure_ssl,
                location=location,
                report_build_status=report_build_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth: Optional[Auth] = core.arg(default=None)

        build_status_config: Optional[BuildStatusConfig] = core.arg(default=None)

        buildspec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        git_clone_depth: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        git_submodules_config: Optional[GitSubmodulesConfig] = core.arg(default=None)

        insecure_ssl: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        report_build_status: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_identifier: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Source(core.Schema):

    auth: Optional[Auth] = core.attr(Auth, default=None)

    build_status_config: Optional[BuildStatusConfig] = core.attr(BuildStatusConfig, default=None)

    buildspec: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    git_clone_depth: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    git_submodules_config: Optional[GitSubmodulesConfig] = core.attr(
        GitSubmodulesConfig, default=None
    )

    insecure_ssl: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    report_build_status: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        auth: Optional[Auth] = None,
        build_status_config: Optional[BuildStatusConfig] = None,
        buildspec: Optional[Union[str, core.StringOut]] = None,
        git_clone_depth: Optional[Union[int, core.IntOut]] = None,
        git_submodules_config: Optional[GitSubmodulesConfig] = None,
        insecure_ssl: Optional[Union[bool, core.BoolOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        report_build_status: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Source.Args(
                type=type,
                auth=auth,
                build_status_config=build_status_config,
                buildspec=buildspec,
                git_clone_depth=git_clone_depth,
                git_submodules_config=git_submodules_config,
                insecure_ssl=insecure_ssl,
                location=location,
                report_build_status=report_build_status,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        auth: Optional[Auth] = core.arg(default=None)

        build_status_config: Optional[BuildStatusConfig] = core.arg(default=None)

        buildspec: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        git_clone_depth: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        git_submodules_config: Optional[GitSubmodulesConfig] = core.arg(default=None)

        insecure_ssl: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        report_build_status: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class SecondaryArtifacts(core.Schema):

    artifact_identifier: Union[str, core.StringOut] = core.attr(str)

    bucket_owner_access: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    namespace_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    override_artifact_name: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    packaging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        artifact_identifier: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        bucket_owner_access: Optional[Union[str, core.StringOut]] = None,
        encryption_disabled: Optional[Union[bool, core.BoolOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        namespace_type: Optional[Union[str, core.StringOut]] = None,
        override_artifact_name: Optional[Union[bool, core.BoolOut]] = None,
        packaging: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=SecondaryArtifacts.Args(
                artifact_identifier=artifact_identifier,
                type=type,
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                name=name,
                namespace_type=namespace_type,
                override_artifact_name=override_artifact_name,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        artifact_identifier: Union[str, core.StringOut] = core.arg()

        bucket_owner_access: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        namespace_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        override_artifact_name: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        packaging: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnets=subnets,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Cache(core.Schema):

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    modes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        location: Optional[Union[str, core.StringOut]] = None,
        modes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Cache.Args(
                location=location,
                modes=modes,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        modes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SecondarySourceVersion(core.Schema):

    source_identifier: Union[str, core.StringOut] = core.attr(str)

    source_version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        source_identifier: Union[str, core.StringOut],
        source_version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=SecondarySourceVersion.Args(
                source_identifier=source_identifier,
                source_version=source_version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        source_identifier: Union[str, core.StringOut] = core.arg()

        source_version: Union[str, core.StringOut] = core.arg()


@core.schema
class Artifacts(core.Schema):

    artifact_identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bucket_owner_access: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    namespace_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    override_artifact_name: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    packaging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        type: Union[str, core.StringOut],
        artifact_identifier: Optional[Union[str, core.StringOut]] = None,
        bucket_owner_access: Optional[Union[str, core.StringOut]] = None,
        encryption_disabled: Optional[Union[bool, core.BoolOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        namespace_type: Optional[Union[str, core.StringOut]] = None,
        override_artifact_name: Optional[Union[bool, core.BoolOut]] = None,
        packaging: Optional[Union[str, core.StringOut]] = None,
        path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Artifacts.Args(
                type=type,
                artifact_identifier=artifact_identifier,
                bucket_owner_access=bucket_owner_access,
                encryption_disabled=encryption_disabled,
                location=location,
                name=name,
                namespace_type=namespace_type,
                override_artifact_name=override_artifact_name,
                packaging=packaging,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        artifact_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bucket_owner_access: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_disabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        namespace_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        override_artifact_name: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        packaging: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.schema
class Restrictions(core.Schema):

    compute_types_allowed: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    maximum_builds_allowed: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        compute_types_allowed: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        maximum_builds_allowed: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Restrictions.Args(
                compute_types_allowed=compute_types_allowed,
                maximum_builds_allowed=maximum_builds_allowed,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_types_allowed: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        maximum_builds_allowed: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class BuildBatchConfig(core.Schema):

    combine_artifacts: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    restrictions: Optional[Restrictions] = core.attr(Restrictions, default=None)

    service_role: Union[str, core.StringOut] = core.attr(str)

    timeout_in_mins: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        service_role: Union[str, core.StringOut],
        combine_artifacts: Optional[Union[bool, core.BoolOut]] = None,
        restrictions: Optional[Restrictions] = None,
        timeout_in_mins: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=BuildBatchConfig.Args(
                service_role=service_role,
                combine_artifacts=combine_artifacts,
                restrictions=restrictions,
                timeout_in_mins=timeout_in_mins,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        combine_artifacts: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        restrictions: Optional[Restrictions] = core.arg(default=None)

        service_role: Union[str, core.StringOut] = core.arg()

        timeout_in_mins: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class FileSystemLocations(core.Schema):

    identifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    location: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mount_options: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    mount_point: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        identifier: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Union[str, core.StringOut]] = None,
        mount_options: Optional[Union[str, core.StringOut]] = None,
        mount_point: Optional[Union[str, core.StringOut]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=FileSystemLocations.Args(
                identifier=identifier,
                location=location,
                mount_options=mount_options,
                mount_point=mount_point,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        location: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mount_options: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mount_point: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_codebuild_project", namespace="aws_codebuild")
class Project(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    artifacts: Artifacts = core.attr(Artifacts)

    badge_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    badge_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    build_batch_config: Optional[BuildBatchConfig] = core.attr(BuildBatchConfig, default=None)

    build_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    cache: Optional[Cache] = core.attr(Cache, default=None)

    concurrent_build_limit: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    encryption_key: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    environment: Environment = core.attr(Environment)

    file_system_locations: Optional[
        Union[List[FileSystemLocations], core.ArrayOut[FileSystemLocations]]
    ] = core.attr(FileSystemLocations, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    logs_config: Optional[LogsConfig] = core.attr(LogsConfig, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    project_visibility: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    public_project_alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    queued_timeout: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    resource_access_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    secondary_artifacts: Optional[
        Union[List[SecondaryArtifacts], core.ArrayOut[SecondaryArtifacts]]
    ] = core.attr(SecondaryArtifacts, default=None, kind=core.Kind.array)

    secondary_source_version: Optional[
        Union[List[SecondarySourceVersion], core.ArrayOut[SecondarySourceVersion]]
    ] = core.attr(SecondarySourceVersion, default=None, kind=core.Kind.array)

    secondary_sources: Optional[
        Union[List[SecondarySources], core.ArrayOut[SecondarySources]]
    ] = core.attr(SecondarySources, default=None, kind=core.Kind.array)

    service_role: Union[str, core.StringOut] = core.attr(str)

    source: Source = core.attr(Source)

    source_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        artifacts: Artifacts,
        environment: Environment,
        name: Union[str, core.StringOut],
        service_role: Union[str, core.StringOut],
        source: Source,
        badge_enabled: Optional[Union[bool, core.BoolOut]] = None,
        build_batch_config: Optional[BuildBatchConfig] = None,
        build_timeout: Optional[Union[int, core.IntOut]] = None,
        cache: Optional[Cache] = None,
        concurrent_build_limit: Optional[Union[int, core.IntOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        encryption_key: Optional[Union[str, core.StringOut]] = None,
        file_system_locations: Optional[
            Union[List[FileSystemLocations], core.ArrayOut[FileSystemLocations]]
        ] = None,
        logs_config: Optional[LogsConfig] = None,
        project_visibility: Optional[Union[str, core.StringOut]] = None,
        queued_timeout: Optional[Union[int, core.IntOut]] = None,
        resource_access_role: Optional[Union[str, core.StringOut]] = None,
        secondary_artifacts: Optional[
            Union[List[SecondaryArtifacts], core.ArrayOut[SecondaryArtifacts]]
        ] = None,
        secondary_source_version: Optional[
            Union[List[SecondarySourceVersion], core.ArrayOut[SecondarySourceVersion]]
        ] = None,
        secondary_sources: Optional[
            Union[List[SecondarySources], core.ArrayOut[SecondarySources]]
        ] = None,
        source_version: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Project.Args(
                artifacts=artifacts,
                environment=environment,
                name=name,
                service_role=service_role,
                source=source,
                badge_enabled=badge_enabled,
                build_batch_config=build_batch_config,
                build_timeout=build_timeout,
                cache=cache,
                concurrent_build_limit=concurrent_build_limit,
                description=description,
                encryption_key=encryption_key,
                file_system_locations=file_system_locations,
                logs_config=logs_config,
                project_visibility=project_visibility,
                queued_timeout=queued_timeout,
                resource_access_role=resource_access_role,
                secondary_artifacts=secondary_artifacts,
                secondary_source_version=secondary_source_version,
                secondary_sources=secondary_sources,
                source_version=source_version,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        artifacts: Artifacts = core.arg()

        badge_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        build_batch_config: Optional[BuildBatchConfig] = core.arg(default=None)

        build_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        cache: Optional[Cache] = core.arg(default=None)

        concurrent_build_limit: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encryption_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        environment: Environment = core.arg()

        file_system_locations: Optional[
            Union[List[FileSystemLocations], core.ArrayOut[FileSystemLocations]]
        ] = core.arg(default=None)

        logs_config: Optional[LogsConfig] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        project_visibility: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        queued_timeout: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        resource_access_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        secondary_artifacts: Optional[
            Union[List[SecondaryArtifacts], core.ArrayOut[SecondaryArtifacts]]
        ] = core.arg(default=None)

        secondary_source_version: Optional[
            Union[List[SecondarySourceVersion], core.ArrayOut[SecondarySourceVersion]]
        ] = core.arg(default=None)

        secondary_sources: Optional[
            Union[List[SecondarySources], core.ArrayOut[SecondarySources]]
        ] = core.arg(default=None)

        service_role: Union[str, core.StringOut] = core.arg()

        source: Source = core.arg()

        source_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
