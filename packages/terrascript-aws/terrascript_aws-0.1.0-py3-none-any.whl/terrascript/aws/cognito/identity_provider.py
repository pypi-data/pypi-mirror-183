from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cognito_identity_provider", namespace="aws_cognito")
class IdentityProvider(core.Resource):

    attribute_mapping: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idp_identifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    provider_details: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.map
    )

    provider_name: Union[str, core.StringOut] = core.attr(str)

    provider_type: Union[str, core.StringOut] = core.attr(str)

    user_pool_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        provider_details: Union[Dict[str, str], core.MapOut[core.StringOut]],
        provider_name: Union[str, core.StringOut],
        provider_type: Union[str, core.StringOut],
        user_pool_id: Union[str, core.StringOut],
        attribute_mapping: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        idp_identifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=IdentityProvider.Args(
                provider_details=provider_details,
                provider_name=provider_name,
                provider_type=provider_type,
                user_pool_id=user_pool_id,
                attribute_mapping=attribute_mapping,
                idp_identifiers=idp_identifiers,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute_mapping: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        idp_identifiers: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        provider_details: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.arg()

        provider_name: Union[str, core.StringOut] = core.arg()

        provider_type: Union[str, core.StringOut] = core.arg()

        user_pool_id: Union[str, core.StringOut] = core.arg()
