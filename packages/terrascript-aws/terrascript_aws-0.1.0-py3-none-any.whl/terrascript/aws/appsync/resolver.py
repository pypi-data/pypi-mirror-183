from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class CachingConfig(core.Schema):

    caching_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        caching_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ttl: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=CachingConfig.Args(
                caching_keys=caching_keys,
                ttl=ttl,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        caching_keys: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class PipelineConfig(core.Schema):

    functions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        functions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=PipelineConfig.Args(
                functions=functions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        functions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class LambdaConflictHandlerConfig(core.Schema):

    lambda_conflict_handler_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        lambda_conflict_handler_arn: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LambdaConflictHandlerConfig.Args(
                lambda_conflict_handler_arn=lambda_conflict_handler_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        lambda_conflict_handler_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class SyncConfig(core.Schema):

    conflict_detection: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    conflict_handler: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lambda_conflict_handler_config: Optional[LambdaConflictHandlerConfig] = core.attr(
        LambdaConflictHandlerConfig, default=None
    )

    def __init__(
        self,
        *,
        conflict_detection: Optional[Union[str, core.StringOut]] = None,
        conflict_handler: Optional[Union[str, core.StringOut]] = None,
        lambda_conflict_handler_config: Optional[LambdaConflictHandlerConfig] = None,
    ):
        super().__init__(
            args=SyncConfig.Args(
                conflict_detection=conflict_detection,
                conflict_handler=conflict_handler,
                lambda_conflict_handler_config=lambda_conflict_handler_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        conflict_detection: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        conflict_handler: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_conflict_handler_config: Optional[LambdaConflictHandlerConfig] = core.arg(
            default=None
        )


@core.resource(type="aws_appsync_resolver", namespace="aws_appsync")
class Resolver(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    caching_config: Optional[CachingConfig] = core.attr(CachingConfig, default=None)

    data_source: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    field: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kind: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    max_batch_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    pipeline_config: Optional[PipelineConfig] = core.attr(PipelineConfig, default=None)

    request_template: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    response_template: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    sync_config: Optional[SyncConfig] = core.attr(SyncConfig, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        field: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        caching_config: Optional[CachingConfig] = None,
        data_source: Optional[Union[str, core.StringOut]] = None,
        kind: Optional[Union[str, core.StringOut]] = None,
        max_batch_size: Optional[Union[int, core.IntOut]] = None,
        pipeline_config: Optional[PipelineConfig] = None,
        request_template: Optional[Union[str, core.StringOut]] = None,
        response_template: Optional[Union[str, core.StringOut]] = None,
        sync_config: Optional[SyncConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Resolver.Args(
                api_id=api_id,
                field=field,
                type=type,
                caching_config=caching_config,
                data_source=data_source,
                kind=kind,
                max_batch_size=max_batch_size,
                pipeline_config=pipeline_config,
                request_template=request_template,
                response_template=response_template,
                sync_config=sync_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        caching_config: Optional[CachingConfig] = core.arg(default=None)

        data_source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        field: Union[str, core.StringOut] = core.arg()

        kind: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_batch_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        pipeline_config: Optional[PipelineConfig] = core.arg(default=None)

        request_template: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        response_template: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sync_config: Optional[SyncConfig] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()
