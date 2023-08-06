from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ce_cost_allocation_tag", namespace="aws_ce")
class CostAllocationTag(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str)

    tag_key: Union[str, core.StringOut] = core.attr(str)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        status: Union[str, core.StringOut],
        tag_key: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CostAllocationTag.Args(
                status=status,
                tag_key=tag_key,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        status: Union[str, core.StringOut] = core.arg()

        tag_key: Union[str, core.StringOut] = core.arg()
