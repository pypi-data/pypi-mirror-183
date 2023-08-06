from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_network_interface_sg_attachment", namespace="aws_vpc")
class NetworkInterfaceSgAttachment(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    security_group_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        network_interface_id: Union[str, core.StringOut],
        security_group_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterfaceSgAttachment.Args(
                network_interface_id=network_interface_id,
                security_group_id=security_group_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        network_interface_id: Union[str, core.StringOut] = core.arg()

        security_group_id: Union[str, core.StringOut] = core.arg()
