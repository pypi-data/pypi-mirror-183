from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_cloudwatch_log_subscription_filter", namespace="aws_cloudwatch")
class LogSubscriptionFilter(core.Resource):

    destination_arn: Union[str, core.StringOut] = core.attr(str)

    distribution: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    filter_pattern: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_group_name: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_arn: Union[str, core.StringOut],
        filter_pattern: Union[str, core.StringOut],
        log_group_name: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        distribution: Optional[Union[str, core.StringOut]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LogSubscriptionFilter.Args(
                destination_arn=destination_arn,
                filter_pattern=filter_pattern,
                log_group_name=log_group_name,
                name=name,
                distribution=distribution,
                role_arn=role_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_arn: Union[str, core.StringOut] = core.arg()

        distribution: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        filter_pattern: Union[str, core.StringOut] = core.arg()

        log_group_name: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
