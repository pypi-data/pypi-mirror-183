from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_standards_control", namespace="aws_securityhub")
class StandardsControl(core.Resource):

    control_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    control_status: Union[str, core.StringOut] = core.attr(str)

    control_status_updated_at: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    disabled_reason: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    The standard control ARN.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    related_requirements: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    remediation_url: Union[str, core.StringOut] = core.attr(str, computed=True)

    severity_rating: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The standards control ARN.
    """
    standards_control_arn: Union[str, core.StringOut] = core.attr(str)

    title: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        control_status: Union[str, core.StringOut],
        standards_control_arn: Union[str, core.StringOut],
        disabled_reason: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=StandardsControl.Args(
                control_status=control_status,
                standards_control_arn=standards_control_arn,
                disabled_reason=disabled_reason,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        control_status: Union[str, core.StringOut] = core.arg()

        disabled_reason: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        standards_control_arn: Union[str, core.StringOut] = core.arg()
