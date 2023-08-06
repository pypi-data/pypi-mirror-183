from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Egress(core.Schema):

    cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_port: Union[int, core.IntOut] = core.attr(int)

    ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    protocol: Union[str, core.StringOut] = core.attr(str)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, alias="self")

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        to_port: Union[int, core.IntOut],
        cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Egress.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                security_groups=security_groups,
                self_=self_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        from_port: Union[int, core.IntOut] = core.arg()

        ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        protocol: Union[str, core.StringOut] = core.arg()

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        self_: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        to_port: Union[int, core.IntOut] = core.arg()


@core.schema
class Ingress(core.Schema):

    cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_port: Union[int, core.IntOut] = core.attr(int)

    ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    protocol: Union[str, core.StringOut] = core.attr(str)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    self_: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, alias="self")

    to_port: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        to_port: Union[int, core.IntOut],
        cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Ingress.Args(
                from_port=from_port,
                protocol=protocol,
                to_port=to_port,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                security_groups=security_groups,
                self_=self_,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        from_port: Union[int, core.IntOut] = core.arg()

        ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        protocol: Union[str, core.StringOut] = core.arg()

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        self_: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        to_port: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_security_group", namespace="aws_vpc")
class SecurityGroup(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = core.attr(
        Egress, default=None, computed=True, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = core.attr(
        Ingress, default=None, computed=True, kind=core.Kind.array
    )

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    revoke_rules_on_delete: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        description: Optional[Union[str, core.StringOut]] = None,
        egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = None,
        ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        revoke_rules_on_delete: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityGroup.Args(
                description=description,
                egress=egress,
                ingress=ingress,
                name=name,
                name_prefix=name_prefix,
                revoke_rules_on_delete=revoke_rules_on_delete,
                tags=tags,
                tags_all=tags_all,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        egress: Optional[Union[List[Egress], core.ArrayOut[Egress]]] = core.arg(default=None)

        ingress: Optional[Union[List[Ingress], core.ArrayOut[Ingress]]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        revoke_rules_on_delete: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
