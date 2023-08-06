from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_load_balancer_backend_server_policy", namespace="aws_elb_classic")
class LoadBalancerBackendServerPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_port: Union[int, core.IntOut] = core.attr(int)

    load_balancer_name: Union[str, core.StringOut] = core.attr(str)

    policy_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        instance_port: Union[int, core.IntOut],
        load_balancer_name: Union[str, core.StringOut],
        policy_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoadBalancerBackendServerPolicy.Args(
                instance_port=instance_port,
                load_balancer_name=load_balancer_name,
                policy_names=policy_names,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        instance_port: Union[int, core.IntOut] = core.arg()

        load_balancer_name: Union[str, core.StringOut] = core.arg()

        policy_names: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )
