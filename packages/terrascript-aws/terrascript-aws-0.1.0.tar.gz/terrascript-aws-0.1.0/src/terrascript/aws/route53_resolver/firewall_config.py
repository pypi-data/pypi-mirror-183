from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_resolver_firewall_config", namespace="aws_route53_resolver")
class FirewallConfig(core.Resource):
    """
    (Required) Determines how Route 53 Resolver handles queries during failures, for example when all tr
    affic that is sent to DNS Firewall fails to receive a reply. By default, fail open is disabled, whic
    h means the failure mode is closed. This approach favors security over availability. DNS Firewall bl
    ocks queries that it is unable to evaluate properly. If you enable this option, the failure mode is
    open. This approach favors availability over security. DNS Firewall allows queries to proceed if it
    is unable to properly evaluate them. Valid values: `ENABLED`, `DISABLED`.
    """

    firewall_fail_open: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    The ID of the firewall configuration.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The AWS account ID of the owner of the VPC that this firewall configuration applies to.
    """
    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The ID of the VPC that the configuration is for.
    """
    resource_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        resource_id: Union[str, core.StringOut],
        firewall_fail_open: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FirewallConfig.Args(
                resource_id=resource_id,
                firewall_fail_open=firewall_fail_open,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        firewall_fail_open: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        resource_id: Union[str, core.StringOut] = core.arg()
