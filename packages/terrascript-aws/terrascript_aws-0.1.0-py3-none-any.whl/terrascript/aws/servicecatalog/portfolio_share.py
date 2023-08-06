from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicecatalog_portfolio_share", namespace="aws_servicecatalog")
class PortfolioShare(core.Resource):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    accepted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str)

    principal_id: Union[str, core.StringOut] = core.attr(str)

    share_tag_options: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    type: Union[str, core.StringOut] = core.attr(str)

    wait_for_acceptance: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        portfolio_id: Union[str, core.StringOut],
        principal_id: Union[str, core.StringOut],
        type: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        share_tag_options: Optional[Union[bool, core.BoolOut]] = None,
        wait_for_acceptance: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PortfolioShare.Args(
                portfolio_id=portfolio_id,
                principal_id=principal_id,
                type=type,
                accept_language=accept_language,
                share_tag_options=share_tag_options,
                wait_for_acceptance=wait_for_acceptance,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        portfolio_id: Union[str, core.StringOut] = core.arg()

        principal_id: Union[str, core.StringOut] = core.arg()

        share_tag_options: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()

        wait_for_acceptance: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
