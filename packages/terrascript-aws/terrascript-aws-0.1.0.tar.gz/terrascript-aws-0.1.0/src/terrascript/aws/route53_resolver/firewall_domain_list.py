from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_domain_list", namespace="aws_route53_resolver")
class FirewallDomainList(core.Resource):
    """
    The ARN (Amazon Resource Name) of the domain list.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) A array of domains for the firewall domain list.
    """
    domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    """
    The ID of the domain list.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) A name that lets you identify the domain list, to manage and use it.
    """
    name: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) A map of tags to assign to the resource. f configured with a provider [`default_tags` con
    figuration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-con
    figuration-block) present, tags with matching keys will overwrite those defined at the provider-leve
    l.
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

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallDomainList.Args(
                name=name,
                domains=domains,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
