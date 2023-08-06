from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_subnet_cidr_reservation", namespace="aws_vpc")
class Ec2SubnetCidrReservation(core.Resource):

    cidr_block: Union[str, core.StringOut] = core.attr(str)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    reservation_type: Union[str, core.StringOut] = core.attr(str)

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cidr_block: Union[str, core.StringOut],
        reservation_type: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Ec2SubnetCidrReservation.Args(
                cidr_block=cidr_block,
                reservation_type=reservation_type,
                subnet_id=subnet_id,
                description=description,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cidr_block: Union[str, core.StringOut] = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        reservation_type: Union[str, core.StringOut] = core.arg()

        subnet_id: Union[str, core.StringOut] = core.arg()
