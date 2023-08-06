from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ConnectSettings(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connect_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_username: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        connect_ips: Union[List[str], core.ArrayOut[core.StringOut]],
        customer_dns_ips: Union[List[str], core.ArrayOut[core.StringOut]],
        customer_username: Union[str, core.StringOut],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ConnectSettings.Args(
                availability_zones=availability_zones,
                connect_ips=connect_ips,
                customer_dns_ips=customer_dns_ips,
                customer_username=customer_username,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        connect_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        customer_dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        customer_username: Union[str, core.StringOut] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.schema
class RadiusSettings(core.Schema):

    authentication_protocol: Union[str, core.StringOut] = core.attr(str, computed=True)

    display_label: Union[str, core.StringOut] = core.attr(str, computed=True)

    radius_port: Union[int, core.IntOut] = core.attr(int, computed=True)

    radius_retries: Union[int, core.IntOut] = core.attr(int, computed=True)

    radius_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    radius_timeout: Union[int, core.IntOut] = core.attr(int, computed=True)

    use_same_username: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        authentication_protocol: Union[str, core.StringOut],
        display_label: Union[str, core.StringOut],
        radius_port: Union[int, core.IntOut],
        radius_retries: Union[int, core.IntOut],
        radius_servers: Union[List[str], core.ArrayOut[core.StringOut]],
        radius_timeout: Union[int, core.IntOut],
        use_same_username: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=RadiusSettings.Args(
                authentication_protocol=authentication_protocol,
                display_label=display_label,
                radius_port=radius_port,
                radius_retries=radius_retries,
                radius_servers=radius_servers,
                radius_timeout=radius_timeout,
                use_same_username=use_same_username,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        authentication_protocol: Union[str, core.StringOut] = core.arg()

        display_label: Union[str, core.StringOut] = core.arg()

        radius_port: Union[int, core.IntOut] = core.arg()

        radius_retries: Union[int, core.IntOut] = core.arg()

        radius_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        radius_timeout: Union[int, core.IntOut] = core.arg()

        use_same_username: Union[bool, core.BoolOut] = core.arg()


@core.schema
class VpcSettings(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]],
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        vpc_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=VpcSettings.Args(
                availability_zones=availability_zones,
                subnet_ids=subnet_ids,
                vpc_id=vpc_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        vpc_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_directory_service_directory", namespace="aws_ds")
class DsDirectoryServiceDirectory(core.Data):

    access_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    connect_settings: Union[List[ConnectSettings], core.ArrayOut[ConnectSettings]] = core.attr(
        ConnectSettings, computed=True, kind=core.Kind.array
    )

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_id: Union[str, core.StringOut] = core.attr(str)

    dns_ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    edition: Union[str, core.StringOut] = core.attr(str, computed=True)

    enable_sso: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    radius_settings: Union[List[RadiusSettings], core.ArrayOut[RadiusSettings]] = core.attr(
        RadiusSettings, computed=True, kind=core.Kind.array
    )

    security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    short_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    size: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str, computed=True)

    vpc_settings: Union[List[VpcSettings], core.ArrayOut[VpcSettings]] = core.attr(
        VpcSettings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDirectoryServiceDirectory.Args(
                directory_id=directory_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
