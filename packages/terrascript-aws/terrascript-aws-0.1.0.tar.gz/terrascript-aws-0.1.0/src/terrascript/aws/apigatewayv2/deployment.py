from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apigatewayv2_deployment", namespace="aws_apigatewayv2")
class Deployment(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    auto_deployed: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                api_id=api_id,
                description=description,
                triggers=triggers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
