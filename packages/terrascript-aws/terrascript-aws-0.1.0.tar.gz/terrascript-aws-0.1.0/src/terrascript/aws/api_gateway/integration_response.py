from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_integration_response", namespace="aws_api_gateway")
class IntegrationResponse(core.Resource):

    content_handling: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_method: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    response_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    selection_pattern: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status_code: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        http_method: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        status_code: Union[str, core.StringOut],
        content_handling: Optional[Union[str, core.StringOut]] = None,
        response_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        selection_pattern: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IntegrationResponse.Args(
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                status_code=status_code,
                content_handling=content_handling,
                response_parameters=response_parameters,
                response_templates=response_templates,
                selection_pattern=selection_pattern,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        content_handling: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_method: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()

        response_parameters: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        rest_api_id: Union[str, core.StringOut] = core.arg()

        selection_pattern: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        status_code: Union[str, core.StringOut] = core.arg()
