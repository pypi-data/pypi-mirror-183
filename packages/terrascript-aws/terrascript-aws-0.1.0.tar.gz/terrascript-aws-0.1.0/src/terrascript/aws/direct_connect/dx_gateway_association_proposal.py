from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_gateway_association_proposal", namespace="aws_direct_connect")
class DxGatewayAssociationProposal(core.Resource):

    allowed_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    associated_gateway_id: Union[str, core.StringOut] = core.attr(str)

    associated_gateway_owner_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    associated_gateway_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    dx_gateway_id: Union[str, core.StringOut] = core.attr(str)

    dx_gateway_owner_account_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        associated_gateway_id: Union[str, core.StringOut],
        dx_gateway_id: Union[str, core.StringOut],
        dx_gateway_owner_account_id: Union[str, core.StringOut],
        allowed_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxGatewayAssociationProposal.Args(
                associated_gateway_id=associated_gateway_id,
                dx_gateway_id=dx_gateway_id,
                dx_gateway_owner_account_id=dx_gateway_owner_account_id,
                allowed_prefixes=allowed_prefixes,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        allowed_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        associated_gateway_id: Union[str, core.StringOut] = core.arg()

        dx_gateway_id: Union[str, core.StringOut] = core.arg()

        dx_gateway_owner_account_id: Union[str, core.StringOut] = core.arg()
