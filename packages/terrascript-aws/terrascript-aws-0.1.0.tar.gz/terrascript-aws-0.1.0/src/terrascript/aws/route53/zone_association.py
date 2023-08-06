from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_zone_association", namespace="aws_route53")
class ZoneAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owning_account: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    vpc_region: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    zone_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: Union[str, core.StringOut],
        zone_id: Union[str, core.StringOut],
        vpc_region: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ZoneAssociation.Args(
                vpc_id=vpc_id,
                zone_id=zone_id,
                vpc_region=vpc_region,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        vpc_id: Union[str, core.StringOut] = core.arg()

        vpc_region: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zone_id: Union[str, core.StringOut] = core.arg()
