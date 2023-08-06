from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_authorizer", namespace="aws_api_gateway")
class Authorizer(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authorizer_credentials: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    authorizer_uri: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_source: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    identity_validation_expression: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    name: Union[str, core.StringOut] = core.attr(str)

    provider_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        rest_api_id: Union[str, core.StringOut],
        authorizer_credentials: Optional[Union[str, core.StringOut]] = None,
        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = None,
        authorizer_uri: Optional[Union[str, core.StringOut]] = None,
        identity_source: Optional[Union[str, core.StringOut]] = None,
        identity_validation_expression: Optional[Union[str, core.StringOut]] = None,
        provider_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Authorizer.Args(
                name=name,
                rest_api_id=rest_api_id,
                authorizer_credentials=authorizer_credentials,
                authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
                authorizer_uri=authorizer_uri,
                identity_source=identity_source,
                identity_validation_expression=identity_validation_expression,
                provider_arns=provider_arns,
                type=type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authorizer_credentials: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        authorizer_result_ttl_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        authorizer_uri: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        identity_validation_expression: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        provider_arns: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        rest_api_id: Union[str, core.StringOut] = core.arg()

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
