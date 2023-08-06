from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class AwsLocation(core.Schema):

    subnet_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    zone: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        subnet_arn: Optional[Union[str, core.StringOut]] = None,
        zone: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AwsLocation.Args(
                subnet_arn=subnet_arn,
                zone=zone,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        subnet_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        zone: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Location(core.Schema):

    address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    latitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    longitude: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        address: Optional[Union[str, core.StringOut]] = None,
        latitude: Optional[Union[str, core.StringOut]] = None,
        longitude: Optional[Union[str, core.StringOut]] = None,
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
        address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        latitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        longitude: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_networkmanager_device", namespace="aws_networkmanager")
class Device(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    aws_location: Optional[AwsLocation] = core.attr(AwsLocation, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    global_network_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Optional[Location] = core.attr(Location, default=None)

    model: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    serial_number: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    site_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vendor: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        global_network_id: Union[str, core.StringOut],
        aws_location: Optional[AwsLocation] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        location: Optional[Location] = None,
        model: Optional[Union[str, core.StringOut]] = None,
        serial_number: Optional[Union[str, core.StringOut]] = None,
        site_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        vendor: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Device.Args(
                global_network_id=global_network_id,
                aws_location=aws_location,
                description=description,
                location=location,
                model=model,
                serial_number=serial_number,
                site_id=site_id,
                tags=tags,
                tags_all=tags_all,
                type=type,
                vendor=vendor,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        aws_location: Optional[AwsLocation] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        global_network_id: Union[str, core.StringOut] = core.arg()

        location: Optional[Location] = core.arg(default=None)

        model: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        serial_number: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        site_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vendor: Optional[Union[str, core.StringOut]] = core.arg(default=None)
