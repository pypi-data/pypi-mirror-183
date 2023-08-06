from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_thing_principal_attachment", namespace="aws_iot")
class ThingPrincipalAttachment(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    principal: Union[str, core.StringOut] = core.attr(str)

    thing: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal: Union[str, core.StringOut],
        thing: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ThingPrincipalAttachment.Args(
                principal=principal,
                thing=thing,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        principal: Union[str, core.StringOut] = core.arg()

        thing: Union[str, core.StringOut] = core.arg()
