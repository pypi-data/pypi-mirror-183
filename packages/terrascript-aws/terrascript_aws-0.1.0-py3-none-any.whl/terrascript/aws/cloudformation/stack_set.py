from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AutoDeployment(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    retain_stacks_on_account_removal: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        retain_stacks_on_account_removal: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=AutoDeployment.Args(
                enabled=enabled,
                retain_stacks_on_account_removal=retain_stacks_on_account_removal,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        retain_stacks_on_account_removal: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


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


@core.resource(type="aws_cloudformation_stack_set", namespace="aws_cloudformation")
class StackSet(core.Resource):

    administration_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    auto_deployment: Optional[AutoDeployment] = core.attr(AutoDeployment, default=None)

    call_as: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_role_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    operation_preferences: Optional[OperationPreferences] = core.attr(
        OperationPreferences, default=None
    )

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    permission_model: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stack_set_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    template_body: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    template_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        administration_role_arn: Optional[Union[str, core.StringOut]] = None,
        auto_deployment: Optional[AutoDeployment] = None,
        call_as: Optional[Union[str, core.StringOut]] = None,
        capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        execution_role_name: Optional[Union[str, core.StringOut]] = None,
        operation_preferences: Optional[OperationPreferences] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        permission_model: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        template_body: Optional[Union[str, core.StringOut]] = None,
        template_url: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StackSet.Args(
                name=name,
                administration_role_arn=administration_role_arn,
                auto_deployment=auto_deployment,
                call_as=call_as,
                capabilities=capabilities,
                description=description,
                execution_role_name=execution_role_name,
                operation_preferences=operation_preferences,
                parameters=parameters,
                permission_model=permission_model,
                tags=tags,
                tags_all=tags_all,
                template_body=template_body,
                template_url=template_url,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        administration_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        auto_deployment: Optional[AutoDeployment] = core.arg(default=None)

        call_as: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        capabilities: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        execution_role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        operation_preferences: Optional[OperationPreferences] = core.arg(default=None)

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        permission_model: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        template_body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        template_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)
