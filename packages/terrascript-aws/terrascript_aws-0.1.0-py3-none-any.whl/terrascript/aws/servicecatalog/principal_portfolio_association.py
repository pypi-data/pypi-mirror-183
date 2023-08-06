from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_servicecatalog_principal_portfolio_association", namespace="aws_servicecatalog"
)
class PrincipalPortfolioAssociation(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str)

    principal_arn: Union[str, core.StringOut] = core.attr(str)

    principal_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: Union[str, core.StringOut],
        principal_arn: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        principal_type: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrincipalPortfolioAssociation.Args(
                portfolio_id=portfolio_id,
                principal_arn=principal_arn,
                accept_language=accept_language,
                principal_type=principal_type,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        portfolio_id: Union[str, core.StringOut] = core.arg()

        principal_arn: Union[str, core.StringOut] = core.arg()

        principal_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)
