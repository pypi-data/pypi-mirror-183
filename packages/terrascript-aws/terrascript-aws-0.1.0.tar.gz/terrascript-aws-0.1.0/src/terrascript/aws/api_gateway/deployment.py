from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_deployment", namespace="aws_api_gateway")
class Deployment(core.Resource):

    created_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    execution_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    invoke_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    stage_description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    stage_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        rest_api_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        stage_description: Optional[Union[str, core.StringOut]] = None,
        stage_name: Optional[Union[str, core.StringOut]] = None,
        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Deployment.Args(
                rest_api_id=rest_api_id,
                description=description,
                stage_description=stage_description,
                stage_name=stage_name,
                triggers=triggers,
                variables=variables,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rest_api_id: Union[str, core.StringOut] = core.arg()

        stage_description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stage_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        triggers: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        variables: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
