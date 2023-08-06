from typing import Optional, Union

import terrascript.core as core


@core.data(type="aws_servicecatalog_constraint", namespace="aws_servicecatalog")
class DsConstraint(core.Data):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    parameters: Union[str, core.StringOut] = core.attr(str, computed=True)

    portfolio_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    product_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsConstraint.Args(
                id=id,
                accept_language=accept_language,
                description=description,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()
