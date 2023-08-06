from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_vpc_ipam_organization_admin_account", namespace="aws_vpc_ipam")
class OrganizationAdminAccount(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delegated_admin_account_id: Union[str, core.StringOut] = core.attr(str)

    email: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_principal: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        delegated_admin_account_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationAdminAccount.Args(
                delegated_admin_account_id=delegated_admin_account_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        delegated_admin_account_id: Union[str, core.StringOut] = core.arg()
