from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Details(core.Schema):

    constraint_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    product_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        constraint_id: Union[str, core.StringOut],
        description: Union[str, core.StringOut],
        owner: Union[str, core.StringOut],
        portfolio_id: Union[str, core.StringOut],
        product_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Details.Args(
                constraint_id=constraint_id,
                description=description,
                owner=owner,
                portfolio_id=portfolio_id,
                product_id=product_id,
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        constraint_id: Union[str, core.StringOut] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        owner: Union[str, core.StringOut] = core.arg()

        portfolio_id: Union[str, core.StringOut] = core.arg()

        product_id: Union[str, core.StringOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_servicecatalog_portfolio_constraints", namespace="aws_servicecatalog")
class DsPortfolioConstraints(core.Data):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    details: Union[List[Details], core.ArrayOut[Details]] = core.attr(
        Details, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str)

    product_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        data_name: str,
        *,
        portfolio_id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        product_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPortfolioConstraints.Args(
                portfolio_id=portfolio_id,
                accept_language=accept_language,
                product_id=product_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        portfolio_id: Union[str, core.StringOut] = core.arg()

        product_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
