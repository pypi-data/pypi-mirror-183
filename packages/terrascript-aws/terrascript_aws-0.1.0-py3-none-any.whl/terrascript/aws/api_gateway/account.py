from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ThrottleSettings(core.Schema):

    burst_limit: Union[int, core.IntOut] = core.attr(int, computed=True)

    rate_limit: Union[float, core.FloatOut] = core.attr(float, computed=True)

    def __init__(
        self,
        *,
        burst_limit: Union[int, core.IntOut],
        rate_limit: Union[float, core.FloatOut],
    ):
        super().__init__(
            args=ThrottleSettings.Args(
                burst_limit=burst_limit,
                rate_limit=rate_limit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        burst_limit: Union[int, core.IntOut] = core.arg()

        rate_limit: Union[float, core.FloatOut] = core.arg()


@core.resource(type="aws_api_gateway_account", namespace="aws_api_gateway")
class Account(core.Resource):

    cloudwatch_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    throttle_settings: Union[List[ThrottleSettings], core.ArrayOut[ThrottleSettings]] = core.attr(
        ThrottleSettings, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        cloudwatch_role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Account.Args(
                cloudwatch_role_arn=cloudwatch_role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
