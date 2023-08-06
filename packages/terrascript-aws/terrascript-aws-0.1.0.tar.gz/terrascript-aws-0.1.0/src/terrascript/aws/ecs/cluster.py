from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LogConfiguration(core.Schema):

    cloud_watch_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    cloud_watch_log_group_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_bucket_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    s3_bucket_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    s3_key_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        cloud_watch_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        cloud_watch_log_group_name: Optional[Union[str, core.StringOut]] = None,
        s3_bucket_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        s3_bucket_name: Optional[Union[str, core.StringOut]] = None,
        s3_key_prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LogConfiguration.Args(
                cloud_watch_encryption_enabled=cloud_watch_encryption_enabled,
                cloud_watch_log_group_name=cloud_watch_log_group_name,
                s3_bucket_encryption_enabled=s3_bucket_encryption_enabled,
                s3_bucket_name=s3_bucket_name,
                s3_key_prefix=s3_key_prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloud_watch_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cloud_watch_log_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_bucket_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        s3_bucket_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        s3_key_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ExecuteCommandConfiguration(core.Schema):

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_configuration: Optional[LogConfiguration] = core.attr(LogConfiguration, default=None)

    logging: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        log_configuration: Optional[LogConfiguration] = None,
        logging: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ExecuteCommandConfiguration.Args(
                kms_key_id=kms_key_id,
                log_configuration=log_configuration,
                logging=logging,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_configuration: Optional[LogConfiguration] = core.arg(default=None)

        logging: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Configuration(core.Schema):

    execute_command_configuration: Optional[ExecuteCommandConfiguration] = core.attr(
        ExecuteCommandConfiguration, default=None
    )

    def __init__(
        self,
        *,
        execute_command_configuration: Optional[ExecuteCommandConfiguration] = None,
    ):
        super().__init__(
            args=Configuration.Args(
                execute_command_configuration=execute_command_configuration,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        execute_command_configuration: Optional[ExecuteCommandConfiguration] = core.arg(
            default=None
        )


@core.schema
class DefaultCapacityProviderStrategy(core.Schema):

    base: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    capacity_provider: Union[str, core.StringOut] = core.attr(str)

    weight: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        capacity_provider: Union[str, core.StringOut],
        base: Optional[Union[int, core.IntOut]] = None,
        weight: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=DefaultCapacityProviderStrategy.Args(
                capacity_provider=capacity_provider,
                base=base,
                weight=weight,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        base: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        capacity_provider: Union[str, core.StringOut] = core.arg()

        weight: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class Setting(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_ecs_cluster", namespace="aws_ecs")
class Cluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    configuration: Optional[Configuration] = core.attr(Configuration, default=None)

    default_capacity_provider_strategy: Optional[
        Union[List[DefaultCapacityProviderStrategy], core.ArrayOut[DefaultCapacityProviderStrategy]]
    ] = core.attr(
        DefaultCapacityProviderStrategy, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.attr(
        Setting, default=None, computed=True, kind=core.Kind.array
    )

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
        name: Union[str, core.StringOut],
        capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        configuration: Optional[Configuration] = None,
        default_capacity_provider_strategy: Optional[
            Union[
                List[DefaultCapacityProviderStrategy],
                core.ArrayOut[DefaultCapacityProviderStrategy],
            ]
        ] = None,
        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Cluster.Args(
                name=name,
                capacity_providers=capacity_providers,
                configuration=configuration,
                default_capacity_provider_strategy=default_capacity_provider_strategy,
                setting=setting,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        capacity_providers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        configuration: Optional[Configuration] = core.arg(default=None)

        default_capacity_provider_strategy: Optional[
            Union[
                List[DefaultCapacityProviderStrategy],
                core.ArrayOut[DefaultCapacityProviderStrategy],
            ]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        setting: Optional[Union[List[Setting], core.ArrayOut[Setting]]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
