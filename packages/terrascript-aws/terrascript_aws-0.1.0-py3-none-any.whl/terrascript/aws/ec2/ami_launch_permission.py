from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ami_launch_permission", namespace="aws_ec2")
class AmiLaunchPermission(core.Resource):

    account_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    image_id: Union[str, core.StringOut] = core.attr(str)

    organization_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organizational_unit_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        image_id: Union[str, core.StringOut],
        account_id: Optional[Union[str, core.StringOut]] = None,
        group: Optional[Union[str, core.StringOut]] = None,
        organization_arn: Optional[Union[str, core.StringOut]] = None,
        organizational_unit_arn: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AmiLaunchPermission.Args(
                image_id=image_id,
                account_id=account_id,
                group=group,
                organization_arn=organization_arn,
                organizational_unit_arn=organizational_unit_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        group: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_id: Union[str, core.StringOut] = core.arg()

        organization_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizational_unit_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)
