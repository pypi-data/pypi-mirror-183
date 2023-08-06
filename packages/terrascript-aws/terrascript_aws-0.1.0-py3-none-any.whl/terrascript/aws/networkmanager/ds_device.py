from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AwsLocation(core.Schema):

    subnet_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        subnet_arn: Union[str, core.StringOut],
        zone: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AwsLocation.Args(
                subnet_arn=subnet_arn,
                zone=zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_arn: Union[str, core.StringOut] = core.arg()

        zone: Union[str, core.StringOut] = core.arg()


@core.schema
class Location(core.Schema):

    address: Union[str, core.StringOut] = core.attr(str, computed=True)

    latitude: Union[str, core.StringOut] = core.attr(str, computed=True)

    longitude: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        address: Union[str, core.StringOut],
        latitude: Union[str, core.StringOut],
        longitude: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Location.Args(
                address=address,
                latitude=latitude,
                longitude=longitude,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        address: Union[str, core.StringOut] = core.arg()

        latitude: Union[str, core.StringOut] = core.arg()

        longitude: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_networkmanager_device", namespace="aws_networkmanager")
class DsDevice(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_location: Union[List[AwsLocation], core.ArrayOut[AwsLocation]] = core.attr(
        AwsLocation, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_id: Union[str, core.StringOut] = core.attr(str)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[List[Location], core.ArrayOut[Location]] = core.attr(
        Location, computed=True, kind=core.Kind.array
    )

    model: Union[str, core.StringOut] = core.attr(str, computed=True)

    serial_number: Union[str, core.StringOut] = core.attr(str, computed=True)

    site_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    vendor: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        device_id: Union[str, core.StringOut],
        global_network_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDevice.Args(
                device_id=device_id,
                global_network_id=global_network_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_id: Union[str, core.StringOut] = core.arg()

        global_network_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
