from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_traffic_policy_instance", namespace="aws_route53")
class TrafficPolicyInstance(core.Resource):

    hosted_zone_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    traffic_policy_id: Union[str, core.StringOut] = core.attr(str)

    traffic_policy_version: Union[int, core.IntOut] = core.attr(int)

    ttl: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        hosted_zone_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        traffic_policy_id: Union[str, core.StringOut],
        traffic_policy_version: Union[int, core.IntOut],
        ttl: Union[int, core.IntOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=TrafficPolicyInstance.Args(
                hosted_zone_id=hosted_zone_id,
                name=name,
                traffic_policy_id=traffic_policy_id,
                traffic_policy_version=traffic_policy_version,
                ttl=ttl,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        hosted_zone_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        traffic_policy_id: Union[str, core.StringOut] = core.arg()

        traffic_policy_version: Union[int, core.IntOut] = core.arg()

        ttl: Union[int, core.IntOut] = core.arg()
