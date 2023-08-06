from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_api_gateway_documentation_version", namespace="aws_api_gateway")
class DocumentationVersion(core.Resource):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    rest_api_id: Union[str, core.StringOut] = core.attr(str)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        rest_api_id: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DocumentationVersion.Args(
                rest_api_id=rest_api_id,
                version=version,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rest_api_id: Union[str, core.StringOut] = core.arg()

        version: Union[str, core.StringOut] = core.arg()
