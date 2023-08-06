from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class EndpointConfiguration(core.Schema):

    types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_endpoint_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        types: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_endpoint_ids: Union[List[str], core.ArrayOut[core.StringOut]],
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

        vpc_endpoint_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.data(type="aws_api_gateway_rest_api", namespace="aws_api_gateway")
class DsRestApi(core.Data):

    api_key_source: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    binary_media_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoint_configuration: Union[
        List[EndpointConfiguration], core.ArrayOut[EndpointConfiguration]
    ] = core.attr(EndpointConfiguration, computed=True, kind=core.Kind.array)

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    minimum_compression_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    policy: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_resource_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRestApi.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
