from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dynamodb_contributor_insights", namespace="aws_dynamodb")
class ContributorInsights(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    index_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    table_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        table_name: Union[str, core.StringOut],
        index_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ContributorInsights.Args(
                table_name=table_name,
                index_name=index_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        index_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        table_name: Union[str, core.StringOut] = core.arg()
