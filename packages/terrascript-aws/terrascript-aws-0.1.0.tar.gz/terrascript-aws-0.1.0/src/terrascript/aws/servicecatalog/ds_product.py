from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_servicecatalog_product", namespace="aws_servicecatalog")
class DsProduct(core.Data):

    accept_language: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    distributor: Union[str, core.StringOut] = core.attr(str, computed=True)

    has_default_path: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    support_description: Union[str, core.StringOut] = core.attr(str, computed=True)

    support_email: Union[str, core.StringOut] = core.attr(str, computed=True)

    support_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

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
            args=DsProduct.Args(
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
