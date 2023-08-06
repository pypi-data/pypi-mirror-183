from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RequestParameter(core.Schema):

    request_parameter_key: Union[str, core.StringOut] = core.attr(str)

    required: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        request_parameter_key: Union[str, core.StringOut],
        required: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=RequestParameter.Args(
                request_parameter_key=request_parameter_key,
                required=required,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        request_parameter_key: Union[str, core.StringOut] = core.arg()

        required: Union[bool, core.BoolOut] = core.arg()


@core.resource(type="aws_apigatewayv2_route", namespace="aws_apigatewayv2")
class Route(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    api_key_required: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    authorization_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    authorizer_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    model_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    operation_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_parameter: Optional[
        Union[List[RequestParameter], core.ArrayOut[RequestParameter]]
    ] = core.attr(RequestParameter, default=None, kind=core.Kind.array)

    route_key: Union[str, core.StringOut] = core.attr(str)

    route_response_selection_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        route_key: Union[str, core.StringOut],
        api_key_required: Optional[Union[bool, core.BoolOut]] = None,
        authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        authorization_type: Optional[Union[str, core.StringOut]] = None,
        authorizer_id: Optional[Union[str, core.StringOut]] = None,
        model_selection_expression: Optional[Union[str, core.StringOut]] = None,
        operation_name: Optional[Union[str, core.StringOut]] = None,
        request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        request_parameter: Optional[
            Union[List[RequestParameter], core.ArrayOut[RequestParameter]]
        ] = None,
        route_response_selection_expression: Optional[Union[str, core.StringOut]] = None,
        target: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Route.Args(
                api_id=api_id,
                route_key=route_key,
                api_key_required=api_key_required,
                authorization_scopes=authorization_scopes,
                authorization_type=authorization_type,
                authorizer_id=authorizer_id,
                model_selection_expression=model_selection_expression,
                operation_name=operation_name,
                request_models=request_models,
                request_parameter=request_parameter,
                route_response_selection_expression=route_response_selection_expression,
                target=target,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        api_key_required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        authorization_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        authorizer_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        model_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        operation_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        request_parameter: Optional[
            Union[List[RequestParameter], core.ArrayOut[RequestParameter]]
        ] = core.arg(default=None)

        route_key: Union[str, core.StringOut] = core.arg()

        route_response_selection_expression: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        target: Optional[Union[str, core.StringOut]] = core.arg(default=None)
