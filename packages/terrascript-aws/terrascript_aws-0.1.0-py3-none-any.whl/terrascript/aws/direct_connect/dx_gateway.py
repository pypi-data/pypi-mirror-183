from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_gateway", namespace="aws_direct_connect")
class DxGateway(core.Resource):

    amazon_side_asn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        amazon_side_asn: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxGateway.Args(
                amazon_side_asn=amazon_side_asn,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        amazon_side_asn: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
