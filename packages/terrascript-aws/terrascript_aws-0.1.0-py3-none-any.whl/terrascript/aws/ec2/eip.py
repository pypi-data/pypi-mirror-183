from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_eip", namespace="aws_ec2")
class Eip(core.Resource):

    address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    allocation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    associate_with_private_ip: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    association_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    carrier_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    domain: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    network_border_group: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    network_interface: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    private_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    private_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_dns: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ip: Union[str, core.StringOut] = core.attr(str, computed=True)

    public_ipv4_pool: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        address: Optional[Union[str, core.StringOut]] = None,
        associate_with_private_ip: Optional[Union[str, core.StringOut]] = None,
        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = None,
        instance: Optional[Union[str, core.StringOut]] = None,
        network_border_group: Optional[Union[str, core.StringOut]] = None,
        network_interface: Optional[Union[str, core.StringOut]] = None,
        public_ipv4_pool: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Eip.Args(
                address=address,
                associate_with_private_ip=associate_with_private_ip,
                customer_owned_ipv4_pool=customer_owned_ipv4_pool,
                instance=instance,
                network_border_group=network_border_group,
                network_interface=network_interface,
                public_ipv4_pool=public_ipv4_pool,
                tags=tags,
                tags_all=tags_all,
                vpc=vpc,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        associate_with_private_ip: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        customer_owned_ipv4_pool: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_border_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        network_interface: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        public_ipv4_pool: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
