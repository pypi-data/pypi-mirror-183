from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class VpcSettings(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

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


@core.schema
class ConnectSettings(core.Schema):

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    connect_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    customer_dns_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    customer_username: Union[str, core.StringOut] = core.attr(str)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str)

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


@core.resource(type="aws_directory_service_directory", namespace="aws_ds")
class DirectoryServiceDirectory(core.Resource):

    access_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    alias: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    connect_settings: Optional[ConnectSettings] = core.attr(ConnectSettings, default=None)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    dns_ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    edition: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    enable_sso: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    password: Union[str, core.StringOut] = core.attr(str)

    security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    short_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    size: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_settings: Optional[VpcSettings] = core.attr(VpcSettings, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        alias: Optional[Union[str, core.StringOut]] = None,
        connect_settings: Optional[ConnectSettings] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = None,
        edition: Optional[Union[str, core.StringOut]] = None,
        enable_sso: Optional[Union[bool, core.BoolOut]] = None,
        short_name: Optional[Union[str, core.StringOut]] = None,
        size: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        type: Optional[Union[str, core.StringOut]] = None,
        vpc_settings: Optional[VpcSettings] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceDirectory.Args(
                name=name,
                password=password,
                alias=alias,
                connect_settings=connect_settings,
                description=description,
                desired_number_of_domain_controllers=desired_number_of_domain_controllers,
                edition=edition,
                enable_sso=enable_sso,
                short_name=short_name,
                size=size,
                tags=tags,
                tags_all=tags_all,
                type=type,
                vpc_settings=vpc_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        alias: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        connect_settings: Optional[ConnectSettings] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        desired_number_of_domain_controllers: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        edition: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_sso: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        password: Union[str, core.StringOut] = core.arg()

        short_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        size: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_settings: Optional[VpcSettings] = core.arg(default=None)
