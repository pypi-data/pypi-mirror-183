from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_destination_policy", namespace="aws_cloudwatch")
class LogDestinationPolicy(core.Resource):

    access_policy: Union[str, core.StringOut] = core.attr(str)

    destination_name: Union[str, core.StringOut] = core.attr(str)

    force_update: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        access_policy: Union[str, core.StringOut],
        destination_name: Union[str, core.StringOut],
        force_update: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogDestinationPolicy.Args(
                access_policy=access_policy,
                destination_name=destination_name,
                force_update=force_update,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: Union[str, core.StringOut] = core.arg()

        destination_name: Union[str, core.StringOut] = core.arg()

        force_update: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
