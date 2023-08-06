from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_route53_resolver_firewall_rule_group_association", namespace="aws_route53_resolver"
)
class FirewallRuleGroupAssociation(core.Resource):
    """
    The ARN (Amazon Resource Name) of the firewall rule group association.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The unique identifier of the firewall rule group.
    """
    firewall_rule_group_id: Union[str, core.StringOut] = core.attr(str)

    """
    The identifier for the association.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) If enabled, this setting disallows modification or removal of the association, to help pr
    event against accidentally altering DNS firewall protections. Valid values: `ENABLED`, `DISABLED`.
    """
    mutation_protection: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Required) A name that lets you identify the rule group association, to manage and use it.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The setting that determines the processing order of the rule group among the rule groups
    that you associate with the specified VPC. DNS Firewall filters VPC traffic starting from the rule g
    roup with the lowest numeric priority setting.
    """
    priority: Union[int, core.IntOut] = core.attr(int)

    """
    (Optional) Key-value map of resource tags. If configured with a provider [`default_tags` configurati
    on block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-configurati
    on-block) present, tags with matching keys will overwrite those defined at the provider-level.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    A map of tags assigned to the resource, including those inherited from the provider [`default_tags`
    configuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-
    configuration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    """
    (Required) The unique identifier of the VPC that you want to associate with the rule group.
    """
    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        firewall_rule_group_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        vpc_id: Union[str, core.StringOut],
        mutation_protection: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallRuleGroupAssociation.Args(
                firewall_rule_group_id=firewall_rule_group_id,
                name=name,
                priority=priority,
                vpc_id=vpc_id,
                mutation_protection=mutation_protection,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_rule_group_id: Union[str, core.StringOut] = core.arg()

        mutation_protection: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_id: Union[str, core.StringOut] = core.arg()
