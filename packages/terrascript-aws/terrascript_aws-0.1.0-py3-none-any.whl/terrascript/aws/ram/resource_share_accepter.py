from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ram_resource_share_accepter", namespace="aws_ram")
class ResourceShareAccepter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The ARN of the resource share invitation.
    """
    invitation_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The account ID of the receiver account which accepts the invitation.
    """
    receiver_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    A list of the resource ARNs shared via the resource share.
    """
    resources: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    """
    The account ID of the sender account which submits the invitation.
    """
    sender_account_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The ARN of the resource share.
    """
    share_arn: Union[str, core.StringOut] = core.attr(str)

    """
    The ID of the resource share as displayed in the console.
    """
    share_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The name of the resource share.
    """
    share_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The status of the resource share (ACTIVE, PENDING, FAILED, DELETING, DELETED).
    """
    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        share_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ResourceShareAccepter.Args(
                share_arn=share_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        share_arn: Union[str, core.StringOut] = core.arg()
