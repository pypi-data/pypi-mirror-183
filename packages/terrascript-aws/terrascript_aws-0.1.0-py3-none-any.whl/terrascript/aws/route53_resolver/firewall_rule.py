from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_rule", namespace="aws_route53_resolver")
class FirewallRule(core.Resource):
    """
    (Required) The action that DNS Firewall should take on a DNS query when it matches one of the domain
    s in the rule's domain list. Valid values: `ALLOW`, `BLOCK`, `ALERT`.
    """

    action: Union[str, core.StringOut] = core.attr(str)

    """
    (Required if `block_response` is `OVERRIDE`) The DNS record's type. This determines the format of th
    e record value that you provided in BlockOverrideDomain. Value values: `CNAME`.
    """
    block_override_dns_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required if `block_response` is `OVERRIDE`) The custom DNS record to send back in response to the q
    uery.
    """
    block_override_domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required if `block_response` is `OVERRIDE`) The recommended amount of time, in seconds, for the DNS
    resolver or web browser to cache the provided override record. Minimum value of 0. Maximum value of
    604800.
    """
    block_override_ttl: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    """
    (Required if `action` is `BLOCK`) The way that you want DNS Firewall to block the request. Valid val
    ues: `NODATA`, `NXDOMAIN`, `OVERRIDE`.
    """
    block_response: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    (Required) The ID of the domain list that you want to use in the rule.
    """
    firewall_domain_list_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The unique identifier of the firewall rule group where you want to create the rule.
    """
    firewall_rule_group_id: Union[str, core.StringOut] = core.attr(str)

    """
    The ID of the rule.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) A name that lets you identify the rule, to manage and use it.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The setting that determines the processing order of the rule in the rule group. DNS Firew
    all processes the rules in a rule group by order of priority, starting from the lowest setting.
    """
    priority: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        action: Union[str, core.StringOut],
        firewall_domain_list_id: Union[str, core.StringOut],
        firewall_rule_group_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        block_override_dns_type: Optional[Union[str, core.StringOut]] = None,
        block_override_domain: Optional[Union[str, core.StringOut]] = None,
        block_override_ttl: Optional[Union[int, core.IntOut]] = None,
        block_response: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallRule.Args(
                action=action,
                firewall_domain_list_id=firewall_domain_list_id,
                firewall_rule_group_id=firewall_rule_group_id,
                name=name,
                priority=priority,
                block_override_dns_type=block_override_dns_type,
                block_override_domain=block_override_domain,
                block_override_ttl=block_override_ttl,
                block_response=block_response,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        action: Union[str, core.StringOut] = core.arg()

        block_override_dns_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        block_override_domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        block_override_ttl: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        block_response: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        firewall_domain_list_id: Union[str, core.StringOut] = core.arg()

        firewall_rule_group_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()
