from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_thing_group_membership", namespace="aws_iot")
class ThingGroupMembership(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    override_dynamic_group: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    thing_group_name: Union[str, core.StringOut] = core.attr(str)

    thing_name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        thing_group_name: Union[str, core.StringOut],
        thing_name: Union[str, core.StringOut],
        override_dynamic_group: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingGroupMembership.Args(
                thing_group_name=thing_group_name,
                thing_name=thing_name,
                override_dynamic_group=override_dynamic_group,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        override_dynamic_group: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        thing_group_name: Union[str, core.StringOut] = core.arg()

        thing_name: Union[str, core.StringOut] = core.arg()
