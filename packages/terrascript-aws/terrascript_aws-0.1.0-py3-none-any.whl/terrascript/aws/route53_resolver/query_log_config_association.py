from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_route53_resolver_query_log_config_association", namespace="aws_route53_resolver"
)
class QueryLogConfigAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resolver_query_log_config_id: Union[str, core.StringOut] = core.attr(str)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resolver_query_log_config_id: Union[str, core.StringOut],
        resource_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryLogConfigAssociation.Args(
                resolver_query_log_config_id=resolver_query_log_config_id,
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resolver_query_log_config_id: Union[str, core.StringOut] = core.arg()

        resource_id: Union[str, core.StringOut] = core.arg()
