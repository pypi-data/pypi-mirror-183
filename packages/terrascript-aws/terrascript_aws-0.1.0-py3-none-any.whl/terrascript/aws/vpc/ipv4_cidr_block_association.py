from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_ipv4_cidr_block_association", namespace="aws_vpc")
class Ipv4CidrBlockAssociation(core.Resource):

    cidr_block: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipv4_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ipv4_netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    vpc_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        vpc_id: Union[str, core.StringOut],
        cidr_block: Optional[Union[str, core.StringOut]] = None,
        ipv4_ipam_pool_id: Optional[Union[str, core.StringOut]] = None,
        ipv4_netmask_length: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ipv4CidrBlockAssociation.Args(
                vpc_id=vpc_id,
                cidr_block=cidr_block,
                ipv4_ipam_pool_id=ipv4_ipam_pool_id,
                ipv4_netmask_length=ipv4_netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_block: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv4_ipam_pool_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ipv4_netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        vpc_id: Union[str, core.StringOut] = core.arg()
