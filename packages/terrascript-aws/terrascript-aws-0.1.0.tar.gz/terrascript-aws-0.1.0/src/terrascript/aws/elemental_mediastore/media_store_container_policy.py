from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_media_store_container_policy", namespace="aws_elemental_mediastore")
class MediaStoreContainerPolicy(core.Resource):

    container_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        container_name: Union[str, core.StringOut],
        policy: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MediaStoreContainerPolicy.Args(
                container_name=container_name,
                policy=policy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        container_name: Union[str, core.StringOut] = core.arg()

        policy: Union[str, core.StringOut] = core.arg()
