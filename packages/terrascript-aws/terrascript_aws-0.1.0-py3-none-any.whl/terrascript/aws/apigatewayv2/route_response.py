from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apigatewayv2_route_response", namespace="aws_apigatewayv2")
class RouteResponse(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    model_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    response_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    route_id: Union[str, core.StringOut] = core.attr(str)

    route_response_key: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        route_id: Union[str, core.StringOut],
        route_response_key: Union[str, core.StringOut],
        model_selection_expression: Optional[Union[str, core.StringOut]] = None,
        response_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RouteResponse.Args(
                api_id=api_id,
                route_id=route_id,
                route_response_key=route_response_key,
                model_selection_expression=model_selection_expression,
                response_models=response_models,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        model_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        response_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        route_id: Union[str, core.StringOut] = core.arg()

        route_response_key: Union[str, core.StringOut] = core.arg()
