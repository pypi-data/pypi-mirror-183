from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_apigatewayv2_api_mapping", namespace="aws_apigatewayv2")
class ApiMapping(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    api_mapping_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stage: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        stage: Union[str, core.StringOut],
        api_mapping_key: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ApiMapping.Args(
                api_id=api_id,
                domain_name=domain_name,
                stage=stage,
                api_mapping_key=api_mapping_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        api_mapping_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        stage: Union[str, core.StringOut] = core.arg()
