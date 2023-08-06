from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_inspector_resource_group", namespace="aws_inspector")
class ResourceGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(str, kind=core.Kind.map)

    def __init__(
        self,
        resource_name: str,
        *,
        tags: Union[Dict[str, str], core.MapOut[core.StringOut]],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceGroup.Args(
                tags=tags,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        tags: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()
