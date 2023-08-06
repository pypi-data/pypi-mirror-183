from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    vpc_endpoint_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_endpoint_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=EndpointConfiguration.Args(
                types=types,
                vpc_endpoint_ids=vpc_endpoint_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        types: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_endpoint_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.resource(type="aws_api_gateway_rest_api", namespace="aws_api_gateway")
class RestApi(core.Resource):

    api_key_source: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    binary_media_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    body: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    endpoint_configuration: Optional[EndpointConfiguration] = core.attr(
        EndpointConfiguration, default=None, computed=True
    )

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    minimum_compression_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    put_rest_api_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        api_key_source: Optional[Union[str, core.StringOut]] = None,
        binary_media_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        body: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = None,
        endpoint_configuration: Optional[EndpointConfiguration] = None,
        minimum_compression_size: Optional[Union[int, core.IntOut]] = None,
        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        put_rest_api_mode: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RestApi.Args(
                name=name,
                api_key_source=api_key_source,
                binary_media_types=binary_media_types,
                body=body,
                description=description,
                disable_execute_api_endpoint=disable_execute_api_endpoint,
                endpoint_configuration=endpoint_configuration,
                minimum_compression_size=minimum_compression_size,
                parameters=parameters,
                policy=policy,
                put_rest_api_mode=put_rest_api_mode,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_key_source: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        binary_media_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        body: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disable_execute_api_endpoint: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        endpoint_configuration: Optional[EndpointConfiguration] = core.arg(default=None)

        minimum_compression_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        parameters: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        put_rest_api_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
