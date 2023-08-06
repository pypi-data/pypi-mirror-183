from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_request_validator", namespace="aws_api_gateway")
class RequestValidator(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    validate_request_body: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    validate_request_parameters: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        validate_request_body: Optional[Union[bool, core.BoolOut]] = None,
        validate_request_parameters: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RequestValidator.Args(
                name=name,
                rest_api_id=rest_api_id,
                validate_request_body=validate_request_body,
                validate_request_parameters=validate_request_parameters,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        rest_api_id: Union[str, core.StringOut] = core.arg()

        validate_request_body: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        validate_request_parameters: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
