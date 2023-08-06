from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_proxy_protocol_policy", namespace="aws_elb_classic")
class ProxyProtocolPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_ports: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    load_balancer: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        instance_ports: Union[List[str], core.ArrayOut[core.StringOut]],
        load_balancer: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ProxyProtocolPolicy.Args(
                instance_ports=instance_ports,
                load_balancer=load_balancer,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_ports: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        load_balancer: Union[str, core.StringOut] = core.arg()
