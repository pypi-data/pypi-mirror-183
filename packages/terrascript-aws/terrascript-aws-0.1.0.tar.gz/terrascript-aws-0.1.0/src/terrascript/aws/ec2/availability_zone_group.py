from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_availability_zone_group", namespace="aws_ec2")
class AvailabilityZoneGroup(core.Resource):

    group_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    opt_in_status: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        group_name: Union[str, core.StringOut],
        opt_in_status: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AvailabilityZoneGroup.Args(
                group_name=group_name,
                opt_in_status=opt_in_status,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        group_name: Union[str, core.StringOut] = core.arg()

        opt_in_status: Union[str, core.StringOut] = core.arg()
