from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_network_interface_attachment", namespace="aws_vpc")
class NetworkInterfaceAttachment(core.Resource):

    attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_index: Union[int, core.IntOut] = core.attr(int)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    network_interface_id: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        device_index: Union[int, core.IntOut],
        instance_id: Union[str, core.StringOut],
        network_interface_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterfaceAttachment.Args(
                device_index=device_index,
                instance_id=instance_id,
                network_interface_id=network_interface_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device_index: Union[int, core.IntOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        network_interface_id: Union[str, core.StringOut] = core.arg()
