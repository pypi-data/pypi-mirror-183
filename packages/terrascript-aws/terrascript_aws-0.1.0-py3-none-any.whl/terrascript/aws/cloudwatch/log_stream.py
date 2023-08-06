from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_stream", namespace="aws_cloudwatch")
class LogStream(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        log_group_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogStream.Args(
                log_group_name=log_group_name,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        log_group_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()
