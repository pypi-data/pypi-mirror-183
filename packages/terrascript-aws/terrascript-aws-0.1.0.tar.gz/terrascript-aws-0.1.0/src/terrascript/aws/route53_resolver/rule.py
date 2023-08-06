from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class TargetIp(core.Schema):

    ip: Union[str, core.StringOut] = core.attr(str)

    port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        ip: Union[str, core.StringOut],
        port: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=TargetIp.Args(
                ip=ip,
                port=port,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ip: Union[str, core.StringOut] = core.arg()

        port: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_route53_resolver_rule", namespace="aws_route53_resolver")
class Rule(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    rule_type: Union[str, core.StringOut] = core.attr(str)

    share_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_ip: Optional[Union[List[TargetIp], core.ArrayOut[TargetIp]]] = core.attr(
        TargetIp, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        domain_name: Union[str, core.StringOut],
        rule_type: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        target_ip: Optional[Union[List[TargetIp], core.ArrayOut[TargetIp]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Rule.Args(
                domain_name=domain_name,
                rule_type=rule_type,
                name=name,
                resolver_endpoint_id=resolver_endpoint_id,
                tags=tags,
                tags_all=tags_all,
                target_ip=target_ip,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domain_name: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resolver_endpoint_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        rule_type: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_ip: Optional[Union[List[TargetIp], core.ArrayOut[TargetIp]]] = core.arg(default=None)
