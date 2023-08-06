from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Ingress(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_port: Union[int, core.IntOut] = core.attr(int)

    icmp_code: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    icmp_type: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Union[str, core.StringOut] = core.attr(str)

    rule_no: Union[int, core.IntOut] = core.attr(int)

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        rule_no: Union[int, core.IntOut],
        to_port: Union[int, core.IntOut],
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        icmp_code: Optional[Union[int, core.IntOut]] = None,
        icmp_type: Optional[Union[int, core.IntOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Ingress.Args(
                action=action,
                from_port=from_port,
                protocol=protocol,
                rule_no=rule_no,
                to_port=to_port,
                cidr_block=cidr_block,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        from_port: Union[int, core.IntOut] = core.arg()

        icmp_code: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        icmp_type: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Union[str, core.StringOut] = core.arg()

        rule_no: Union[int, core.IntOut] = core.arg()

        to_port: Union[int, core.IntOut] = core.arg()


@core.schema
class Egress(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_port: Union[int, core.IntOut] = core.attr(int)

    icmp_code: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    icmp_type: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    protocol: Union[str, core.StringOut] = core.attr(str)

    rule_no: Union[int, core.IntOut] = core.attr(int)

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        rule_no: Union[int, core.IntOut],
        to_port: Union[int, core.IntOut],
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        icmp_code: Optional[Union[int, core.IntOut]] = None,
        icmp_type: Optional[Union[int, core.IntOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Egress.Args(
                action=action,
                from_port=from_port,
                protocol=protocol,
                rule_no=rule_no,
                to_port=to_port,
                cidr_block=cidr_block,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        from_port: Union[int, core.IntOut] = core.arg()

        icmp_code: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        icmp_type: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        protocol: Union[str, core.StringOut] = core.arg()

        rule_no: Union[int, core.IntOut] = core.arg()

        to_port: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_default_network_acl", namespace="aws_vpc")
class DefaultNetworkAcl(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_network_acl_id: Union[str, core.StringOut] = core.attr(str)

    egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = core.attr(
        Egress, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = core.attr(
        Ingress, default=None, kind=core.Kind.array
    )

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        default_network_acl_id: Union[str, core.StringOut],
        egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = None,
        ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DefaultNetworkAcl.Args(
                default_network_acl_id=default_network_acl_id,
                egress=egress,
                ingress=ingress,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_network_acl_id: Union[str, core.StringOut] = core.arg()

        egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = core.arg(default=None)

        ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = core.arg(default=None)

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
