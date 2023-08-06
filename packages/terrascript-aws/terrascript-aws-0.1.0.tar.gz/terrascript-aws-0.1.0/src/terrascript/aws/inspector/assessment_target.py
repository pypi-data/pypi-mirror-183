from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_inspector_assessment_target", namespace="aws_inspector")
class AssessmentTarget(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    resource_group_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        resource_group_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AssessmentTarget.Args(
                name=name,
                resource_group_arn=resource_group_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        name: Union[str, core.StringOut] = core.arg()

        resource_group_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
