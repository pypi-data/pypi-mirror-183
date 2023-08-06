from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Attachment(core.Schema):

    attachment_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_index: Union[int, core.IntOut] = core.attr(int)

    instance: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        attachment_id: Union[str, core.StringOut],
        device_index: Union[int, core.IntOut],
        instance: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Attachment.Args(
                attachment_id=attachment_id,
                device_index=device_index,
                instance=instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attachment_id: Union[str, core.StringOut] = core.arg()

        device_index: Union[int, core.IntOut] = core.arg()

        instance: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_network_interface", namespace="aws_vpc")
class NetworkInterface(core.Resource):
    """
    ARN of the network interface.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Configuration block to define the attachment of the ENI. See [Attachment](#attachment) be
    low for more details!
    """
    attachment: Optional[Union[List[Attachment], core.ArrayOut[Attachment]]] = core.attr(
        Attachment, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Description for the network interface.
    """
    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    """
    ID of the network interface.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Optional) Type of network interface to create. Set to `efa` for Elastic Fabric Adapter. Changing `i
    nterface_type` will cause the resource to be destroyed and re-created.
    """
    interface_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    (Optional) Number of IPv4 prefixes that AWS automatically assigns to the network interface.
    """
    ipv4_prefix_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) One or more IPv4 prefixes assigned to the network interface.
    """
    ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Number of IPv6 addresses to assign to a network interface. You can't use this option if s
    pecifying specific `ipv6_addresses`. If your subnet has the AssignIpv6AddressOnCreation attribute se
    t to `true`, you can specify `0` to override this setting.
    """
    ipv6_address_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) List of private IPs to assign to the ENI in sequential order.
    """
    ipv6_address_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    ipv6_address_list_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    (Optional) One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet. Addres
    ses are assigned without regard to order. You can't use this option if you're specifying `ipv6_addre
    ss_count`.
    """
    ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Number of IPv6 prefixes that AWS automatically assigns to the network interface.
    """
    ipv6_prefix_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) One or more IPv6 prefixes assigned to the network interface.
    """
    ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    MAC address of the network interface.
    """
    mac_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    outpost_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    AWS account ID of the owner of the network interface.
    """
    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Private DNS name of the network interface (IPv4).
    """
    private_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    (Optional) List of private IPs to assign to the ENI in sequential order. Requires setting `private_i
    p_list_enabled` to `true`.
    """
    private_ip_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Whether `private_ip_list` is allowed and controls the IPs to assign to the ENI and `priva
    te_ips` and `private_ips_count` become read-only. Default false.
    """
    private_ip_list_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    (Optional) List of private IPs to assign to the ENI without regard to order.
    """
    private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Number of secondary private IPs to assign to the ENI. The total number of private IPs wil
    l be 1 + `private_ips_count`, as a primary private IP will be assiged to an ENI by default.
    """
    private_ips_count: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    """
    (Optional) List of security group IDs to assign to the ENI.
    """
    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    """
    (Optional) Whether to enable source destination checking for the ENI. Default true.
    """
    source_dest_check: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    """
    (Required) Subnet ID to create the ENI in.
    """
    subnet_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Map of tags to assign to the resource. If configured with a provider [`default_tags` conf
    iguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-conf
    iguration-block) present, tags with matching keys will overwrite those defined at the provider-level
    .
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    """
    Map of tags assigned to the resource, including those inherited from the provider [`default_tags` co
    nfiguration block](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#default_tags-co
    nfiguration-block).
    """
    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        subnet_id: Union[str, core.StringOut],
        attachment: Optional[Union[List[Attachment], core.ArrayOut[Attachment]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        interface_type: Optional[Union[str, core.StringOut]] = None,
        ipv4_prefix_count: Optional[Union[int, core.IntOut]] = None,
        ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv6_address_count: Optional[Union[int, core.IntOut]] = None,
        ipv6_address_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv6_address_list_enabled: Optional[Union[bool, core.BoolOut]] = None,
        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        ipv6_prefix_count: Optional[Union[int, core.IntOut]] = None,
        ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        private_ip: Optional[Union[str, core.StringOut]] = None,
        private_ip_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        private_ip_list_enabled: Optional[Union[bool, core.BoolOut]] = None,
        private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        private_ips_count: Optional[Union[int, core.IntOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        source_dest_check: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NetworkInterface.Args(
                subnet_id=subnet_id,
                attachment=attachment,
                description=description,
                interface_type=interface_type,
                ipv4_prefix_count=ipv4_prefix_count,
                ipv4_prefixes=ipv4_prefixes,
                ipv6_address_count=ipv6_address_count,
                ipv6_address_list=ipv6_address_list,
                ipv6_address_list_enabled=ipv6_address_list_enabled,
                ipv6_addresses=ipv6_addresses,
                ipv6_prefix_count=ipv6_prefix_count,
                ipv6_prefixes=ipv6_prefixes,
                private_ip=private_ip,
                private_ip_list=private_ip_list,
                private_ip_list_enabled=private_ip_list_enabled,
                private_ips=private_ips,
                private_ips_count=private_ips_count,
                security_groups=security_groups,
                source_dest_check=source_dest_check,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        attachment: Optional[Union[List[Attachment], core.ArrayOut[Attachment]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        interface_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv4_prefix_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv4_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv6_address_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_address_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv6_address_list_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        ipv6_addresses: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipv6_prefix_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ipv6_prefixes: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        private_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        private_ip_list: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        private_ip_list_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        private_ips: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        private_ips_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        source_dest_check: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        subnet_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
