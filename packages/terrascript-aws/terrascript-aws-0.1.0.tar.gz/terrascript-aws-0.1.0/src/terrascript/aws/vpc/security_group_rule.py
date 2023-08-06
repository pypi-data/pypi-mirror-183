from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_security_group_rule", namespace="aws_vpc")
class SecurityGroupRule(core.Resource):

    cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    from_port: Union[int, core.IntOut] = core.attr(int)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    protocol: Union[str, core.StringOut] = core.attr(str)

    security_group_id: Union[str, core.StringOut] = core.attr(str)

    self_: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, alias="self")

    source_security_group_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    to_port: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        from_port: Union[int, core.IntOut],
        protocol: Union[str, core.StringOut],
        security_group_id: Union[str, core.StringOut],
        to_port: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        ipv6_cidr_blocks: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        prefix_list_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_: Optional[Union[bool, core.BoolOut]] = None,
        source_security_group_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=SecurityGroupRule.Args(
                from_port=from_port,
                protocol=protocol,
                security_group_id=security_group_id,
                to_port=to_port,
                type=type,
                cidr_blocks=cidr_blocks,
                description=description,
                ipv6_cidr_blocks=ipv6_cidr_blocks,
                prefix_list_ids=prefix_list_ids,
                self_=self_,
                source_security_group_id=source_security_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
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

        security_group_id: Union[str, core.StringOut] = core.arg()

        self_: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        source_security_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        to_port: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()
