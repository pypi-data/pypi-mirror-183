from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_lb_cookie_stickiness_policy", namespace="aws_elb_classic")
class LbCookieStickinessPolicy(core.Resource):

    cookie_expiration_period: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lb_port: Union[int, core.IntOut] = core.attr(int)

    load_balancer: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        lb_port: Union[int, core.IntOut],
        load_balancer: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        cookie_expiration_period: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbCookieStickinessPolicy.Args(
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                cookie_expiration_period=cookie_expiration_period,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cookie_expiration_period: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        lb_port: Union[int, core.IntOut] = core.arg()

        load_balancer: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
