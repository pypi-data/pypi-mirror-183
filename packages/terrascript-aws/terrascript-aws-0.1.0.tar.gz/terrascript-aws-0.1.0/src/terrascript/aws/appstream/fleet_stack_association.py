from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_appstream_fleet_stack_association", namespace="aws_appstream")
class FleetStackAssociation(core.Resource):

    fleet_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    stack_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        fleet_name: Union[str, core.StringOut],
        stack_name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FleetStackAssociation.Args(
                fleet_name=fleet_name,
                stack_name=stack_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fleet_name: Union[str, core.StringOut] = core.arg()

        stack_name: Union[str, core.StringOut] = core.arg()
