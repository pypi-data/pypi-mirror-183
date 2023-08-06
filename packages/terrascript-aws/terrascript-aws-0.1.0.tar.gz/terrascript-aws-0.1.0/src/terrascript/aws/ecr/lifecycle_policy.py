from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ecr_lifecycle_policy", namespace="aws_ecr")
class LifecyclePolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    registry_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    repository: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        policy: Union[str, core.StringOut],
        repository: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LifecyclePolicy.Args(
                policy=policy,
                repository=repository,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        policy: Union[str, core.StringOut] = core.arg()

        repository: Union[str, core.StringOut] = core.arg()
