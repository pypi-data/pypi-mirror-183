from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ssm_patch_group", namespace="aws_ssm")
class PatchGroup(core.Resource):

    baseline_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    patch_group: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        baseline_id: Union[str, core.StringOut],
        patch_group: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PatchGroup.Args(
                baseline_id=baseline_id,
                patch_group=patch_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        baseline_id: Union[str, core.StringOut] = core.arg()

        patch_group: Union[str, core.StringOut] = core.arg()
