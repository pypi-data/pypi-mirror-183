from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_index: Union[int, core.IntOut] = core.attr(int, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attachment_id: Union[str, core.StringOut],
        device_index: Union[int, core.IntOut],
        instance_id: Union[str, core.StringOut],
        instance_owner_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attachment.Args(
                attachment_id=attachment_id,
                device_index=device_index,
                instance_id=instance_id,
                instance_owner_id=instance_owner_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: Union[str, core.StringOut] = core.arg()

        device_index: Union[int, core.IntOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        instance_owner_id: Union[str, core.StringOut] = core.arg()


@core.schema
class Filter(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str)

    values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        values: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=Filter.Args(
                name=name,
                values=values,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


@core.schema
class Association(core.Schema):

    allocation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    carrier_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        allocation_id: Union[str, core.StringOut],
        association_id: Union[str, core.StringOut],
        carrier_ip: Union[str, core.StringOut],
        customer_owned_ip: Union[str, core.StringOut],
        ip_owner_id: Union[str, core.StringOut],
        public_dns_name: Union[str, core.StringOut],
        public_ip: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Association.Args(
                allocation_id=allocation_id,
                association_id=association_id,
                carrier_ip=carrier_ip,
                customer_owned_ip=customer_owned_ip,
                ip_owner_id=ip_owner_id,
                public_dns_name=public_dns_name,
                public_ip=public_ip,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_id: Union[str, core.StringOut] = core.arg()

        association_id: Union[str, core.StringOut] = core.arg()

        carrier_ip: Union[str, core.StringOut] = core.arg()

        customer_owned_ip: Union[str, core.StringOut] = core.arg()

        ip_owner_id: Union[str, core.StringOut] = core.arg()

        public_dns_name: Union[str, core.StringOut] = core.arg()

        public_ip: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_network_interface", namespace="aws_vpc")
class DsNetworkInterface(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    association: Union[List[Association], core.ArrayOut[Association]] = core.attr(
        Association, computed=True, kind=core.Kind.array
    )

    attachment: Union[List[Attachment], core.ArrayOut[Attachment]] = core.attr(
        Attachment, computed=True, kind=core.Kind.array
    )

    availability_zone: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.attr(
        Filter, default=None, kind=core.Kind.array
    )

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    interface_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    mac_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ips: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    requester_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = None,
        id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsNetworkInterface.Args(
                filter=filter,
                id=id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        filter: Optional[Union[List[Filter], core.ArrayOut[Filter]]] = core.arg(default=None)

        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
