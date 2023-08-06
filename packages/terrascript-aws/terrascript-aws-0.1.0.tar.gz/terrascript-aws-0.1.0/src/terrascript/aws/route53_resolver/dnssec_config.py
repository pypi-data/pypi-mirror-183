from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_resolver_dnssec_config", namespace="aws_route53_resolver")
class DnssecConfig(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resource_id: Union[str, core.StringOut] = core.attr(str)

    validation_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DnssecConfig.Args(
                resource_id=resource_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        resource_id: Union[str, core.StringOut] = core.arg()
