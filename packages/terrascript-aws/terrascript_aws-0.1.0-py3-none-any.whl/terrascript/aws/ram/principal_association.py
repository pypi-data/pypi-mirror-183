from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ram_principal_association", namespace="aws_ram")
class PrincipalAssociation(core.Resource):
    """
    The Amazon Resource Name (ARN) of the Resource Share and the principal, separated by a comma.
    """

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The principal to associate with the resource share. Possible values are an AWS account ID
    , an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
    """
    principal: Union[str, core.StringOut] = core.attr(str)

    """
    (Required) The Amazon Resource Name (ARN) of the resource share.
    """
    resource_share_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        principal: Union[str, core.StringOut],
        resource_share_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=PrincipalAssociation.Args(
                principal=principal,
                resource_share_arn=resource_share_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        principal: Union[str, core.StringOut] = core.arg()

        resource_share_arn: Union[str, core.StringOut] = core.arg()
