from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_client_vpn_authorization_rule", namespace="aws_vpn")
class Ec2ClientVpnAuthorizationRule(core.Resource):

    access_group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    authorize_all_groups: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    client_vpn_endpoint_id: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_network_cidr: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        client_vpn_endpoint_id: Union[str, core.StringOut],
        target_network_cidr: Union[str, core.StringOut],
        access_group_id: Optional[Union[str, core.StringOut]] = None,
        authorize_all_groups: Optional[Union[bool, core.BoolOut]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2ClientVpnAuthorizationRule.Args(
                client_vpn_endpoint_id=client_vpn_endpoint_id,
                target_network_cidr=target_network_cidr,
                access_group_id=access_group_id,
                authorize_all_groups=authorize_all_groups,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        authorize_all_groups: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        client_vpn_endpoint_id: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_network_cidr: Union[str, core.StringOut] = core.arg()
