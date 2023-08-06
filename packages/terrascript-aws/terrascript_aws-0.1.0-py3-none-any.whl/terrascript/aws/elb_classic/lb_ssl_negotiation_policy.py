from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class Attribute(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    value: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attribute.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_lb_ssl_negotiation_policy", namespace="aws_elb_classic")
class LbSslNegotiationPolicy(core.Resource):

    attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.attr(
        Attribute, default=None, kind=core.Kind.array
    )

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
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LbSslNegotiationPolicy.Args(
                lb_port=lb_port,
                load_balancer=load_balancer,
                name=name,
                attribute=attribute,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attribute: Optional[Union[List[Attribute], core.ArrayOut[Attribute]]] = core.arg(
            default=None
        )

        lb_port: Union[int, core.IntOut] = core.arg()

        load_balancer: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
