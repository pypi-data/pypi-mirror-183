from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RoutingConfig(core.Schema):

    additional_version_weights: Optional[
        Union[Dict[str, float], core.MapOut[core.FloatOut]]
    ] = core.attr(float, default=None, kind=core.Kind.map)

    def __init__(
        self,
        *,
        additional_version_weights: Optional[
            Union[Dict[str, float], core.MapOut[core.FloatOut]]
        ] = None,
    ):
        super().__init__(
            args=RoutingConfig.Args(
                additional_version_weights=additional_version_weights,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        additional_version_weights: Optional[
            Union[Dict[str, float], core.MapOut[core.FloatOut]]
        ] = core.arg(default=None)


@core.resource(type="aws_lambda_alias", namespace="aws_lambda")
class Alias(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    function_name: Union[str, core.StringOut] = core.attr(str)

    function_version: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    routing_config: Optional[RoutingConfig] = core.attr(RoutingConfig, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        function_name: Union[str, core.StringOut],
        function_version: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        routing_config: Optional[RoutingConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Alias.Args(
                function_name=function_name,
                function_version=function_version,
                name=name,
                description=description,
                routing_config=routing_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        function_name: Union[str, core.StringOut] = core.arg()

        function_version: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        routing_config: Optional[RoutingConfig] = core.arg(default=None)
