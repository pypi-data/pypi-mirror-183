from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dx_hosted_connection", namespace="aws_direct_connect")
class DxHostedConnection(core.Resource):

    aws_device: Union[str, core.StringOut] = core.attr(str, computed=True)

    bandwidth: Union[str, core.StringOut] = core.attr(str)

    connection_id: Union[str, core.StringOut] = core.attr(str)

    has_logical_redundancy: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    jumbo_frame_capable: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    lag_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    loa_issue_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    owner_account_id: Union[str, core.StringOut] = core.attr(str)

    partner_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    provider_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    region: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    vlan: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        resource_name: str,
        *,
        bandwidth: Union[str, core.StringOut],
        connection_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        owner_account_id: Union[str, core.StringOut],
        vlan: Union[int, core.IntOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DxHostedConnection.Args(
                bandwidth=bandwidth,
                connection_id=connection_id,
                name=name,
                owner_account_id=owner_account_id,
                vlan=vlan,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bandwidth: Union[str, core.StringOut] = core.arg()

        connection_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        owner_account_id: Union[str, core.StringOut] = core.arg()

        vlan: Union[int, core.IntOut] = core.arg()
