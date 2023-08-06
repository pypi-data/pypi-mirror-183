from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_detective_invitation_accepter", namespace="aws_detective")
class InvitationAccepter(core.Resource):

    graph_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        graph_arn: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InvitationAccepter.Args(
                graph_arn=graph_arn,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        graph_arn: Union[str, core.StringOut] = core.arg()
