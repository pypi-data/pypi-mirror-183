from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_standards_subscription", namespace="aws_securityhub")
class StandardsSubscription(core.Resource):
    """
    The ARN of a resource that represents your subscription to a supported standard.
    """

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The ARN of a standard - see below.
    """
    standards_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        standards_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StandardsSubscription.Args(
                standards_arn=standards_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        standards_arn: Union[str, core.StringOut] = core.arg()
