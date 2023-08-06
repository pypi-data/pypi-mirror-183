from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_cognito_identity_pool_provider_principal_tag", namespace="aws_cognito_identity"
)
class PoolProviderPrincipalTag(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identity_pool_id: Union[str, core.StringOut] = core.attr(str)

    identity_provider_name: Union[str, core.StringOut] = core.attr(str)

    principal_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    use_defaults: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        identity_pool_id: Union[str, core.StringOut],
        identity_provider_name: Union[str, core.StringOut],
        principal_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        use_defaults: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PoolProviderPrincipalTag.Args(
                identity_pool_id=identity_pool_id,
                identity_provider_name=identity_provider_name,
                principal_tags=principal_tags,
                use_defaults=use_defaults,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        identity_pool_id: Union[str, core.StringOut] = core.arg()

        identity_provider_name: Union[str, core.StringOut] = core.arg()

        principal_tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        use_defaults: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
