from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Outputs(core.Schema):

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        description: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Outputs.Args(
                description=description,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class StackSetProvisioningPreferences(core.Schema):

    accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    failure_tolerance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_concurrency_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_concurrency_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        failure_tolerance_count: Optional[Union[int, core.IntOut]] = None,
        failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = None,
        max_concurrency_count: Optional[Union[int, core.IntOut]] = None,
        max_concurrency_percentage: Optional[Union[int, core.IntOut]] = None,
        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=StackSetProvisioningPreferences.Args(
                accounts=accounts,
                failure_tolerance_count=failure_tolerance_count,
                failure_tolerance_percentage=failure_tolerance_percentage,
                max_concurrency_count=max_concurrency_count,
                max_concurrency_percentage=max_concurrency_percentage,
                regions=regions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        failure_tolerance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        failure_tolerance_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_concurrency_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_concurrency_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)


@core.schema
class ProvisioningParameters(core.Schema):

    key: Union[str, core.StringOut] = core.attr(str)

    use_previous_value: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        key: Union[str, core.StringOut],
        use_previous_value: Optional[Union[bool, core.BoolOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ProvisioningParameters.Args(
                key=key,
                use_previous_value=use_previous_value,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        key: Union[str, core.StringOut] = core.arg()

        use_previous_value: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_servicecatalog_provisioned_product", namespace="aws_servicecatalog")
class ProvisionedProduct(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_dashboard_names: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ignore_errors: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    last_provisioning_record_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_record_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    last_successful_provisioning_record_id: Union[str, core.StringOut] = core.attr(
        str, computed=True
    )

    launch_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    outputs: Union[List[Outputs], core.ArrayOut[Outputs]] = core.attr(
        Outputs, computed=True, kind=core.Kind.array
    )

    path_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    path_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    product_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    product_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    provisioning_artifact_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    provisioning_artifact_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    provisioning_parameters: Optional[
        Union[List[ProvisioningParameters], core.ArrayOut[ProvisioningParameters]]
    ] = core.attr(ProvisioningParameters, default=None, kind=core.Kind.array)

    retain_physical_resources: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    stack_set_provisioning_preferences: Optional[StackSetProvisioningPreferences] = core.attr(
        StackSetProvisioningPreferences, default=None
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_message: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        ignore_errors: Optional[Union[bool, core.BoolOut]] = None,
        notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        path_id: Optional[Union[str, core.StringOut]] = None,
        path_name: Optional[Union[str, core.StringOut]] = None,
        product_id: Optional[Union[str, core.StringOut]] = None,
        product_name: Optional[Union[str, core.StringOut]] = None,
        provisioning_artifact_id: Optional[Union[str, core.StringOut]] = None,
        provisioning_artifact_name: Optional[Union[str, core.StringOut]] = None,
        provisioning_parameters: Optional[
            Union[List[ProvisioningParameters], core.ArrayOut[ProvisioningParameters]]
        ] = None,
        retain_physical_resources: Optional[Union[bool, core.BoolOut]] = None,
        stack_set_provisioning_preferences: Optional[StackSetProvisioningPreferences] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProvisionedProduct.Args(
                name=name,
                accept_language=accept_language,
                ignore_errors=ignore_errors,
                notification_arns=notification_arns,
                path_id=path_id,
                path_name=path_name,
                product_id=product_id,
                product_name=product_name,
                provisioning_artifact_id=provisioning_artifact_id,
                provisioning_artifact_name=provisioning_artifact_name,
                provisioning_parameters=provisioning_parameters,
                retain_physical_resources=retain_physical_resources,
                stack_set_provisioning_preferences=stack_set_provisioning_preferences,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ignore_errors: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        notification_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        path_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        path_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        product_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        product_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioning_artifact_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioning_artifact_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioning_parameters: Optional[
            Union[List[ProvisioningParameters], core.ArrayOut[ProvisioningParameters]]
        ] = core.arg(default=None)

        retain_physical_resources: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        stack_set_provisioning_preferences: Optional[StackSetProvisioningPreferences] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
