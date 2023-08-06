from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_gateway_response", namespace="aws_api_gateway")
class GatewayResponse(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) A map specifying the parameters (paths, query strings and headers) of the Gateway Respons
    e.
    """
    response_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Optional) A map specifying the templates used to transform the response body.
    """
    response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    (Required) The response type of the associated GatewayResponse.
    """
    response_type: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The string identifier of the associated REST API.
    """
    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) The HTTP status code of the Gateway Response.
    """
    status_code: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        response_type: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        response_parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        status_code: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GatewayResponse.Args(
                response_type=response_type,
                rest_api_id=rest_api_id,
                response_parameters=response_parameters,
                response_templates=response_templates,
                status_code=status_code,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        response_parameters: Optional[
            Union[Dict[str, str], core.MapOut[core.StringOut]]
        ] = core.arg(default=None)

        response_templates: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        response_type: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()

        status_code: Optional[Union[str, core.StringOut]] = core.arg(default=None)
