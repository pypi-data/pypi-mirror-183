from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apigatewayv2_integration_response", namespace="aws_apigatewayv2")
class IntegrationResponse(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    content_handling_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    integration_id: Union[str, core.StringOut] = core.attr(str)

    integration_response_key: Union[str, core.StringOut] = core.attr(str)

    response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    template_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        integration_id: Union[str, core.StringOut],
        integration_response_key: Union[str, core.StringOut],
        content_handling_strategy: Optional[Union[str, core.StringOut]] = None,
        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        template_selection_expression: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IntegrationResponse.Args(
                api_id=api_id,
                integration_id=integration_id,
                integration_response_key=integration_response_key,
                content_handling_strategy=content_handling_strategy,
                response_templates=response_templates,
                template_selection_expression=template_selection_expression,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        content_handling_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        integration_id: Union[str, core.StringOut] = core.arg()

        integration_response_key: Union[str, core.StringOut] = core.arg()

        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        template_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)
