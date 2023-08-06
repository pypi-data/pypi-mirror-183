from typing import List, Optional, Union

import terrascript.core as core


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


@core.resource(type="aws_appsync_function", namespace="aws_appsync")
class Function(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    data_source: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    function_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    function_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    max_batch_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    request_mapping_template: Union[str, core.StringOut] = core.attr(str)

    response_mapping_template: Union[str, core.StringOut] = core.attr(str)

    sync_config: Optional[SyncConfig] = core.attr(SyncConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        data_source: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        request_mapping_template: Union[str, core.StringOut],
        response_mapping_template: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        function_version: Optional[Union[str, core.StringOut]] = None,
        max_batch_size: Optional[Union[int, core.IntOut]] = None,
        sync_config: Optional[SyncConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Function.Args(
                api_id=api_id,
                data_source=data_source,
                name=name,
                request_mapping_template=request_mapping_template,
                response_mapping_template=response_mapping_template,
                description=description,
                function_version=function_version,
                max_batch_size=max_batch_size,
                sync_config=sync_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        data_source: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        function_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_batch_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        request_mapping_template: Union[str, core.StringOut] = core.arg()

        response_mapping_template: Union[str, core.StringOut] = core.arg()

        sync_config: Optional[SyncConfig] = core.arg(default=None)
