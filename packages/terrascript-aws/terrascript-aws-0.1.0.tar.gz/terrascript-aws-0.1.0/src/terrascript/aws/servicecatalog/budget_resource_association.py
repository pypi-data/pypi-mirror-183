from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_budget_resource_association", namespace="aws_servicecatalog"
)
class BudgetResourceAssociation(core.Resource):

    budget_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        budget_name: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=BudgetResourceAssociation.Args(
                budget_name=budget_name,
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        budget_name: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()
