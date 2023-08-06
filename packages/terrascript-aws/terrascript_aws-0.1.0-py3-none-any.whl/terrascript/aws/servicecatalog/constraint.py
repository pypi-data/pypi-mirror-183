from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicecatalog_constraint", namespace="aws_servicecatalog")
class Constraint(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Union[str, core.StringOut] = core.attr(str)

    portfolio_id: Union[str, core.StringOut] = core.attr(str)

    product_id: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        parameters: Union[str, core.StringOut],
        portfolio_id: Union[str, core.StringOut],
        product_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Constraint.Args(
                parameters=parameters,
                portfolio_id=portfolio_id,
                product_id=product_id,
                type=type,
                accept_language=accept_language,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        parameters: Union[str, core.StringOut] = core.arg()

        portfolio_id: Union[str, core.StringOut] = core.arg()

        product_id: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()
