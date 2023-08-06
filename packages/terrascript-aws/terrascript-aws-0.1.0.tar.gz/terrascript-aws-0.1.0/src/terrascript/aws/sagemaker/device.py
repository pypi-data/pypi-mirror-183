from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class DeviceBlk(core.Schema):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_name: Union[str, core.StringOut] = core.attr(str)

    iot_thing_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        iot_thing_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DeviceBlk.Args(
                device_name=device_name,
                description=description,
                iot_thing_name=iot_thing_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_name: Union[str, core.StringOut] = core.arg()

        iot_thing_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_sagemaker_device", namespace="aws_sagemaker")
class Device(core.Resource):

    agent_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    device: DeviceBlk = core.attr(DeviceBlk)

    device_fleet_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        device: DeviceBlk,
        device_fleet_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Device.Args(
                device=device,
                device_fleet_name=device_fleet_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        device: DeviceBlk = core.arg()

        device_fleet_name: Union[str, core.StringOut] = core.arg()
