from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_base_path_mapping", namespace="aws_api_gateway")
class BasePathMapping(core.Resource):

    api_id: Union[str, core.StringOut] = core.attr(str)

    base_path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stage_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        api_id: Union[str, core.StringOut],
        domain_name: Union[str, core.StringOut],
        base_path: Optional[Union[str, core.StringOut]] = None,
        stage_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BasePathMapping.Args(
                api_id=api_id,
                domain_name=domain_name,
                base_path=base_path,
                stage_name=stage_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        api_id: Union[str, core.StringOut] = core.arg()

        base_path: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_name: Union[str, core.StringOut] = core.arg()

        stage_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
