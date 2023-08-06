from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_action_target", namespace="aws_securityhub")
class ActionTarget(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    identifier: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        description: Union[str, core.StringOut],
        identifier: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ActionTarget.Args(
                description=description,
                identifier=identifier,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Union[str, core.StringOut] = core.arg()

        identifier: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
