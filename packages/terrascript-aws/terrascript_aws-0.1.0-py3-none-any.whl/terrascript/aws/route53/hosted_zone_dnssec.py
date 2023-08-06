from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_hosted_zone_dnssec", namespace="aws_route53")
class HostedZoneDnssec(core.Resource):

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    signing_status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: Union[str, core.StringOut],
        signing_status: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=HostedZoneDnssec.Args(
                hosted_zone_id=hosted_zone_id,
                signing_status=signing_status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: Union[str, core.StringOut] = core.arg()

        signing_status: Optional[Union[str, core.StringOut]] = core.arg(default=None)
