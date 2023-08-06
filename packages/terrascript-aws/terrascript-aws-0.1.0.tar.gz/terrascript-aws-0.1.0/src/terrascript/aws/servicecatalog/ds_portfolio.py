from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_servicecatalog_portfolio", namespace="aws_servicecatalog")
class DsPortfolio(core.Data):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    provider_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        id: Union[str, core.StringOut],
        accept_language: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsPortfolio.Args(
                id=id,
                accept_language=accept_language,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        accept_language: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
