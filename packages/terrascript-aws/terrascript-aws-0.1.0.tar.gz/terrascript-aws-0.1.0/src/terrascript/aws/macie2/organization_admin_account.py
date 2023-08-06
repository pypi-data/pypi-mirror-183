from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_macie2_organization_admin_account", namespace="aws_macie2")
class OrganizationAdminAccount(core.Resource):

    admin_account_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        admin_account_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationAdminAccount.Args(
                admin_account_id=admin_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_account_id: Union[str, core.StringOut] = core.arg()
