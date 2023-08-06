from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_route53_query_log", namespace="aws_route53")
class QueryLog(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cloudwatch_log_group_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    zone_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        cloudwatch_log_group_arn: Union[str, core.StringOut],
        zone_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=QueryLog.Args(
                cloudwatch_log_group_arn=cloudwatch_log_group_arn,
                zone_id=zone_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cloudwatch_log_group_arn: Union[str, core.StringOut] = core.arg()

        zone_id: Union[str, core.StringOut] = core.arg()
