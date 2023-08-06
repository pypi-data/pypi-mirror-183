from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class PolicyAttribute(core.Schema):

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        name: Optional[Union[str, core.StringOut]] = None,
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PolicyAttribute.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_load_balancer_policy", namespace="aws_elb_classic")
class LoadBalancerPolicy(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    load_balancer_name: Union[str, core.StringOut] = core.attr(str)

    policy_attribute: Optional[
        Union[List[PolicyAttribute], core.ArrayOut[PolicyAttribute]]
    ] = core.attr(PolicyAttribute, default=None, computed=True, kind=core.Kind.array)

    policy_name: Union[str, core.StringOut] = core.attr(str)

    policy_type_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        load_balancer_name: Union[str, core.StringOut],
        policy_name: Union[str, core.StringOut],
        policy_type_name: Union[str, core.StringOut],
        policy_attribute: Optional[
            Union[List[PolicyAttribute], core.ArrayOut[PolicyAttribute]]
        ] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoadBalancerPolicy.Args(
                load_balancer_name=load_balancer_name,
                policy_name=policy_name,
                policy_type_name=policy_type_name,
                policy_attribute=policy_attribute,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        load_balancer_name: Union[str, core.StringOut] = core.arg()

        policy_attribute: Optional[
            Union[List[PolicyAttribute], core.ArrayOut[PolicyAttribute]]
        ] = core.arg(default=None)

        policy_name: Union[str, core.StringOut] = core.arg()

        policy_type_name: Union[str, core.StringOut] = core.arg()
