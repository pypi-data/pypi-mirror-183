from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_method", namespace="aws_api_gateway")
class Method(core.Resource):

    api_key_required: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    authorization: Union[str, core.StringOut] = core.attr(str)

    authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    authorizer_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    http_method: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    operation_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    request_parameters: Optional[Union[Dict[str, bool], core.MapOut[core.BoolOut]]] = core.attr(
        bool, default=None, kind=core.Kind.map
    )

    request_validator_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        authorization: Union[str, core.StringOut],
        http_method: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        api_key_required: Optional[Union[bool, core.BoolOut]] = None,
        authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        authorizer_id: Optional[Union[str, core.StringOut]] = None,
        operation_name: Optional[Union[str, core.StringOut]] = None,
        request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        request_parameters: Optional[Union[Dict[str, bool], core.MapOut[core.BoolOut]]] = None,
        request_validator_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Method.Args(
                authorization=authorization,
                http_method=http_method,
                resource_id=resource_id,
                rest_api_id=rest_api_id,
                api_key_required=api_key_required,
                authorization_scopes=authorization_scopes,
                authorizer_id=authorizer_id,
                operation_name=operation_name,
                request_models=request_models,
                request_parameters=request_parameters,
                request_validator_id=request_validator_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_required: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        authorization: Union[str, core.StringOut] = core.arg()

        authorization_scopes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        authorizer_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        http_method: Union[str, core.StringOut] = core.arg()

        operation_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        request_models: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        request_parameters: Optional[Union[Dict[str, bool], core.MapOut[core.BoolOut]]] = core.arg(
            default=None
        )

        request_validator_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_id: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()
