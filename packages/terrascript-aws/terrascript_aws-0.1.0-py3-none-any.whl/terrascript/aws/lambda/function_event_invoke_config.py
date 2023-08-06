from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class OnFailure(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnFailure.Args(
                destination=destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[str, core.StringOut] = core.arg()


@core.schema
class OnSuccess(core.Schema):

    destination: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        destination: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OnSuccess.Args(
                destination=destination,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        destination: Union[str, core.StringOut] = core.arg()


@core.schema
class DestinationConfig(core.Schema):

    on_failure: Optional[OnFailure] = core.attr(OnFailure, default=None)

    on_success: Optional[OnSuccess] = core.attr(OnSuccess, default=None)

    def __init__(
        self,
        *,
        on_failure: Optional[OnFailure] = None,
        on_success: Optional[OnSuccess] = None,
    ):
        super().__init__(
            args=DestinationConfig.Args(
                on_failure=on_failure,
                on_success=on_success,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        on_failure: Optional[OnFailure] = core.arg(default=None)

        on_success: Optional[OnSuccess] = core.arg(default=None)


@core.resource(type="aws_lambda_function_event_invoke_config", namespace="aws_lambda")
class FunctionEventInvokeConfig(core.Resource):

    destination_config: Optional[DestinationConfig] = core.attr(DestinationConfig, default=None)

    function_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    qualifier: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        destination_config: Optional[DestinationConfig] = None,
        maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = None,
        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = None,
        qualifier: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FunctionEventInvokeConfig.Args(
                function_name=function_name,
                destination_config=destination_config,
                maximum_event_age_in_seconds=maximum_event_age_in_seconds,
                maximum_retry_attempts=maximum_retry_attempts,
                qualifier=qualifier,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_config: Optional[DestinationConfig] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        maximum_event_age_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        maximum_retry_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        qualifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)
