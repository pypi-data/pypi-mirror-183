from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_config_organization_custom_rule", namespace="aws_config")
class OrganizationCustomRule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    input_parameters: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    lambda_function_arn: Union[str, core.StringOut] = core.attr(str)

    maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_id_scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_types_scope: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tag_key_scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tag_value_scope: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    trigger_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        lambda_function_arn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        trigger_types: Union[List[str], core.ArrayOut[core.StringOut]],
        description: Optional[Union[str, core.StringOut]] = None,
        excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        input_parameters: Optional[Union[str, core.StringOut]] = None,
        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = None,
        resource_id_scope: Optional[Union[str, core.StringOut]] = None,
        resource_types_scope: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tag_key_scope: Optional[Union[str, core.StringOut]] = None,
        tag_value_scope: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationCustomRule.Args(
                lambda_function_arn=lambda_function_arn,
                name=name,
                trigger_types=trigger_types,
                description=description,
                excluded_accounts=excluded_accounts,
                input_parameters=input_parameters,
                maximum_execution_frequency=maximum_execution_frequency,
                resource_id_scope=resource_id_scope,
                resource_types_scope=resource_types_scope,
                tag_key_scope=tag_key_scope,
                tag_value_scope=tag_value_scope,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        excluded_accounts: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        input_parameters: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lambda_function_arn: Union[str, core.StringOut] = core.arg()

        maximum_execution_frequency: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        resource_id_scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_types_scope: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tag_key_scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tag_value_scope: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        trigger_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()
