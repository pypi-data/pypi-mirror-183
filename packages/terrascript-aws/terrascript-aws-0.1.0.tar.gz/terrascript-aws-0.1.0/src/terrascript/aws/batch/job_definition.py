from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Timeout(core.Schema):

    attempt_duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        attempt_duration_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=Timeout.Args(
                attempt_duration_seconds=attempt_duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attempt_duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class EvaluateOnExit(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    on_exit_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    on_reason: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    on_status_reason: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        on_exit_code: Optional[Union[str, core.StringOut]] = None,
        on_reason: Optional[Union[str, core.StringOut]] = None,
        on_status_reason: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=EvaluateOnExit.Args(
                action=action,
                on_exit_code=on_exit_code,
                on_reason=on_reason,
                on_status_reason=on_status_reason,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        on_exit_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_reason: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        on_status_reason: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class RetryStrategy(core.Schema):

    attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    evaluate_on_exit: Optional[
        Union[List[EvaluateOnExit], core.ArrayOut[EvaluateOnExit]]
    ] = core.attr(EvaluateOnExit, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        attempts: Optional[Union[int, core.IntOut]] = None,
        evaluate_on_exit: Optional[
            Union[List[EvaluateOnExit], core.ArrayOut[EvaluateOnExit]]
        ] = None,
    ):
        super().__init__(
            args=RetryStrategy.Args(
                attempts=attempts,
                evaluate_on_exit=evaluate_on_exit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        evaluate_on_exit: Optional[
            Union[List[EvaluateOnExit], core.ArrayOut[EvaluateOnExit]]
        ] = core.arg(default=None)


@core.resource(type="aws_batch_job_definition", namespace="aws_batch")
class JobDefinition(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    container_properties: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    platform_capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    propagate_tags: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    retry_strategy: Optional[RetryStrategy] = core.attr(RetryStrategy, default=None)

    revision: Union[int, core.IntOut] = core.attr(int, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout: Optional[Timeout] = core.attr(Timeout, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        container_properties: Optional[Union[str, core.StringOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        platform_capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        propagate_tags: Optional[Union[bool, core.BoolOut]] = None,
        retry_strategy: Optional[RetryStrategy] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout: Optional[Timeout] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=JobDefinition.Args(
                name=name,
                type=type,
                container_properties=container_properties,
                parameters=parameters,
                platform_capabilities=platform_capabilities,
                propagate_tags=propagate_tags,
                retry_strategy=retry_strategy,
                tags=tags,
                tags_all=tags_all,
                timeout=timeout,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_properties: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        platform_capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        propagate_tags: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        retry_strategy: Optional[RetryStrategy] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timeout: Optional[Timeout] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()
