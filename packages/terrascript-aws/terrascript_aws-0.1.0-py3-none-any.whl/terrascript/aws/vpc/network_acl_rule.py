from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_network_acl_rule", namespace="aws_vpc")
class NetworkAclRule(core.Resource):

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    egress: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    from_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    icmp_code: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    icmp_type: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    network_acl_id: Union[str, core.StringOut] = core.attr(str)

    protocol: Union[str, core.StringOut] = core.attr(str)

    rule_action: Union[str, core.StringOut] = core.attr(str)

    rule_number: Union[int, core.IntOut] = core.attr(int)

    to_port: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        network_acl_id: Union[str, core.StringOut],
        protocol: Union[str, core.StringOut],
        rule_action: Union[str, core.StringOut],
        rule_number: Union[int, core.IntOut],
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        egress: Optional[Union[bool, core.BoolOut]] = None,
        from_port: Optional[Union[int, core.IntOut]] = None,
        icmp_code: Optional[Union[int, core.IntOut]] = None,
        icmp_type: Optional[Union[int, core.IntOut]] = None,
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        to_port: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkAclRule.Args(
                network_acl_id=network_acl_id,
                protocol=protocol,
                rule_action=rule_action,
                rule_number=rule_number,
                cidr_block=cidr_block,
                egress=egress,
                from_port=from_port,
                icmp_code=icmp_code,
                icmp_type=icmp_type,
                ipv6_cidr_block=ipv6_cidr_block,
                to_port=to_port,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        egress: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        from_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        icmp_code: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        icmp_type: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_acl_id: Union[str, core.StringOut] = core.arg()

        protocol: Union[str, core.StringOut] = core.arg()

        rule_action: Union[str, core.StringOut] = core.arg()

        rule_number: Union[int, core.IntOut] = core.arg()

        to_port: Optional[Union[int, core.IntOut]] = core.arg(default=None)
