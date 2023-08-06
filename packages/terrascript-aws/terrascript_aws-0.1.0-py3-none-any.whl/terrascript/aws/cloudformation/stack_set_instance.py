from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DeploymentTargets(core.Schema):

    organizational_unit_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        organizational_unit_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=DeploymentTargets.Args(
                organizational_unit_ids=organizational_unit_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        organizational_unit_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class OperationPreferences(core.Schema):

    failure_tolerance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_concurrent_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_concurrent_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    region_concurrency_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    region_order: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        failure_tolerance_count: Optional[Union[int, core.IntOut]] = None,
        failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = None,
        max_concurrent_count: Optional[Union[int, core.IntOut]] = None,
        max_concurrent_percentage: Optional[Union[int, core.IntOut]] = None,
        region_concurrency_type: Optional[Union[str, core.StringOut]] = None,
        region_order: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=OperationPreferences.Args(
                failure_tolerance_count=failure_tolerance_count,
                failure_tolerance_percentage=failure_tolerance_percentage,
                max_concurrent_count=max_concurrent_count,
                max_concurrent_percentage=max_concurrent_percentage,
                region_concurrency_type=region_concurrency_type,
                region_order=region_order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        failure_tolerance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_concurrent_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_concurrent_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        region_concurrency_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        region_order: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_cloudformation_stack_set_instance", namespace="aws_cloudformation")
class StackSetInstance(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    call_as: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    deployment_targets: Optional[DeploymentTargets] = core.attr(DeploymentTargets, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    operation_preferences: Optional[OperationPreferences] = core.attr(
        OperationPreferences, default=None
    )

    organizational_unit_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameter_overrides: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    retain_stack: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stack_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stack_set_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        stack_set_name: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        call_as: Optional[Union[str, core.StringOut]] = None,
        deployment_targets: Optional[DeploymentTargets] = None,
        operation_preferences: Optional[OperationPreferences] = None,
        parameter_overrides: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        region: Optional[Union[str, core.StringOut]] = None,
        retain_stack: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StackSetInstance.Args(
                stack_set_name=stack_set_name,
                account_id=account_id,
                call_as=call_as,
                deployment_targets=deployment_targets,
                operation_preferences=operation_preferences,
                parameter_overrides=parameter_overrides,
                region=region,
                retain_stack=retain_stack,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        call_as: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        deployment_targets: Optional[DeploymentTargets] = core.arg(default=None)

        operation_preferences: Optional[OperationPreferences] = core.arg(default=None)

        parameter_overrides: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        retain_stack: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stack_set_name: Union[str, core.StringOut] = core.arg()
