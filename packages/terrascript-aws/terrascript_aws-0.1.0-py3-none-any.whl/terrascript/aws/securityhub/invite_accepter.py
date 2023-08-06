from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_invite_accepter", namespace="aws_securityhub")
class InviteAccepter(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The ID of the invitation.
    """
    invitation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) The account ID of the master Security Hub account whose invitation you're accepting.
    """
    master_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        master_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InviteAccepter.Args(
                master_id=master_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        master_id: Union[str, core.StringOut] = core.arg()
