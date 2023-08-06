from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_glue_resource_policy", namespace="aws_glue")
class ResourcePolicy(core.Resource):

    enable_hybrid: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        enable_hybrid: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourcePolicy.Args(
                policy=policy,
                enable_hybrid=enable_hybrid,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enable_hybrid: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Union[str, core.StringOut] = core.arg()
