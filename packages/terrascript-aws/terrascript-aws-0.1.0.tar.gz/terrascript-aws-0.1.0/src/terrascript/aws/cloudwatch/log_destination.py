from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_destination", namespace="aws_cloudwatch")
class LogDestination(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    target_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        target_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogDestination.Args(
                name=name,
                role_arn=role_arn,
                target_arn=target_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        role_arn: Union[str, core.StringOut] = core.arg()

        target_arn: Union[str, core.StringOut] = core.arg()
