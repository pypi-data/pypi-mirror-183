from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_organizations_delegated_administrator", namespace="aws_organizations")
class DelegatedAdministrator(core.Resource):

    account_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    delegation_enabled_date: Union[str, core.StringOut] = core.attr(str, computed=True)

    email: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_method: Union[str, core.StringOut] = core.attr(str, computed=True)

    joined_timestamp: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_principal: Union[str, core.StringOut] = core.attr(str)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        account_id: Union[str, core.StringOut],
        service_principal: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DelegatedAdministrator.Args(
                account_id=account_id,
                service_principal=service_principal,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_id: Union[str, core.StringOut] = core.arg()

        service_principal: Union[str, core.StringOut] = core.arg()
