from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_ipv6_cidr_block_association", namespace="aws_vpc")
class Ipv6CidrBlockAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    ipv6_ipam_pool_id: Union[str, core.StringOut] = core.attr(str)

    ipv6_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        ipv6_ipam_pool_id: Union[str, core.StringOut],
        vpc_id: Union[str, core.StringOut],
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = None,
        ipv6_netmask_length: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipv6CidrBlockAssociation.Args(
                ipv6_ipam_pool_id=ipv6_ipam_pool_id,
                vpc_id=vpc_id,
                ipv6_cidr_block=ipv6_cidr_block,
                ipv6_netmask_length=ipv6_netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ipv6_cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv6_ipam_pool_id: Union[str, core.StringOut] = core.arg()

        ipv6_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        vpc_id: Union[str, core.StringOut] = core.arg()
