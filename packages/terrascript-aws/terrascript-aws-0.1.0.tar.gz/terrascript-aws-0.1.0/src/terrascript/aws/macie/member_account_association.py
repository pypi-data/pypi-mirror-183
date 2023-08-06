from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_macie_member_account_association", namespace="aws_macie")
class MemberAccountAssociation(core.Resource):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    member_account_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        member_account_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MemberAccountAssociation.Args(
                member_account_id=member_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        member_account_id: Union[str, core.StringOut] = core.arg()
