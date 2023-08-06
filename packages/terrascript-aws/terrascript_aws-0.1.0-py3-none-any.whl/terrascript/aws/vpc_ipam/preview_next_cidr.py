from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_ipam_preview_next_cidr", namespace="aws_vpc_ipam")
class PreviewNextCidr(core.Resource):

    cidr: Union[str, core.StringOut] = core.attr(str, computed=True)

    disallowed_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ipam_pool_id: Union[str, core.StringOut] = core.attr(str)

    netmask_length: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        ipam_pool_id: Union[str, core.StringOut],
        disallowed_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        netmask_length: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PreviewNextCidr.Args(
                ipam_pool_id=ipam_pool_id,
                disallowed_cidrs=disallowed_cidrs,
                netmask_length=netmask_length,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        disallowed_cidrs: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        ipam_pool_id: Union[str, core.StringOut] = core.arg()

        netmask_length: Optional[Union[int, core.IntOut]] = core.arg(default=None)
