from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Parameter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    resource_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    static_value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    static_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        resource_value: Optional[Union[str, core.StringOut]] = None,
        static_value: Optional[Union[str, core.StringOut]] = None,
        static_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=Parameter.Args(
                name=name,
                resource_value=resource_value,
                static_value=static_value,
                static_values=static_values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        resource_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        static_value: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        static_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class SsmControls(core.Schema):

    concurrent_execution_rate_percentage: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    error_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        concurrent_execution_rate_percentage: Optional[Union[int, core.IntOut]] = None,
        error_percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=SsmControls.Args(
                concurrent_execution_rate_percentage=concurrent_execution_rate_percentage,
                error_percentage=error_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        concurrent_execution_rate_percentage: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        error_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ExecutionControls(core.Schema):

    ssm_controls: Optional[SsmControls] = core.attr(SsmControls, default=None)

    def __init__(
        self,
        *,
        ssm_controls: Optional[SsmControls] = None,
    ):
        super().__init__(
            args=ExecutionControls.Args(
                ssm_controls=ssm_controls,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ssm_controls: Optional[SsmControls] = core.arg(default=None)


@core.resource(type="aws_config_remediation_configuration", namespace="aws_config")
class RemediationConfiguration(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    automatic: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    config_rule_name: Union[str, core.StringOut] = core.attr(str)

    execution_controls: Optional[ExecutionControls] = core.attr(ExecutionControls, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    maximum_automatic_attempts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.attr(
        Parameter, default=None, kind=core.Kind.array
    )

    resource_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    retry_attempt_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    target_id: Union[str, core.StringOut] = core.attr(str)

    target_type: Union[str, core.StringOut] = core.attr(str)

    target_version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        config_rule_name: Union[str, core.StringOut],
        target_id: Union[str, core.StringOut],
        target_type: Union[str, core.StringOut],
        automatic: Optional[Union[bool, core.BoolOut]] = None,
        execution_controls: Optional[ExecutionControls] = None,
        maximum_automatic_attempts: Optional[Union[int, core.IntOut]] = None,
        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = None,
        resource_type: Optional[Union[str, core.StringOut]] = None,
        retry_attempt_seconds: Optional[Union[int, core.IntOut]] = None,
        target_version: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RemediationConfiguration.Args(
                config_rule_name=config_rule_name,
                target_id=target_id,
                target_type=target_type,
                automatic=automatic,
                execution_controls=execution_controls,
                maximum_automatic_attempts=maximum_automatic_attempts,
                parameter=parameter,
                resource_type=resource_type,
                retry_attempt_seconds=retry_attempt_seconds,
                target_version=target_version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        automatic: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        config_rule_name: Union[str, core.StringOut] = core.arg()

        execution_controls: Optional[ExecutionControls] = core.arg(default=None)

        maximum_automatic_attempts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        parameter: Optional[Union[List[Parameter], core.ArrayOut[Parameter]]] = core.arg(
            default=None
        )

        resource_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        retry_attempt_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        target_id: Union[str, core.StringOut] = core.arg()

        target_type: Union[str, core.StringOut] = core.arg()

        target_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
