from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_finding_aggregator", namespace="aws_securityhub")
class FindingAggregator(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    linking_mode: Union[str, core.StringOut] = core.attr(str)

    specified_regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        linking_mode: Union[str, core.StringOut],
        specified_regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FindingAggregator.Args(
                linking_mode=linking_mode,
                specified_regions=specified_regions,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        linking_mode: Union[str, core.StringOut] = core.arg()

        specified_regions: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
