from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_product_portfolio_association", namespace="aws_servicecatalog"
)
class ProductPortfolioAssociation(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str)

    product_id: Union[str, core.StringOut] = core.attr(str)

    source_portfolio_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: Union[str, core.StringOut],
        product_id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        source_portfolio_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProductPortfolioAssociation.Args(
                portfolio_id=portfolio_id,
                product_id=product_id,
                accept_language=accept_language,
                source_portfolio_id=source_portfolio_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        portfolio_id: Union[str, core.StringOut] = core.arg()

        product_id: Union[str, core.StringOut] = core.arg()

        source_portfolio_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
