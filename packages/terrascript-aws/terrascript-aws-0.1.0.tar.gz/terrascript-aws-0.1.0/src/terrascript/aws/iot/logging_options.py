from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_iot_logging_options", namespace="aws_iot")
class LoggingOptions(core.Resource):

    default_log_level: Union[str, core.StringOut] = core.attr(str)

    disable_all_logs: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    role_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        default_log_level: Union[str, core.StringOut],
        role_arn: Union[str, core.StringOut],
        disable_all_logs: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LoggingOptions.Args(
                default_log_level=default_log_level,
                role_arn=role_arn,
                disable_all_logs=disable_all_logs,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_log_level: Union[str, core.StringOut] = core.arg()

        disable_all_logs: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        role_arn: Union[str, core.StringOut] = core.arg()
