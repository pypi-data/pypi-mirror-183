from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_securityhub_organization_configuration", namespace="aws_securityhub")
class OrganizationConfiguration(core.Resource):
    """
    (Required) Whether to automatically enable Security Hub for new accounts in the organization.
    """

    auto_enable: Union[bool, core.BoolOut] = core.attr(bool)

    """
    AWS Account ID.
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        auto_enable: Union[bool, core.BoolOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationConfiguration.Args(
                auto_enable=auto_enable,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        auto_enable: Union[bool, core.BoolOut] = core.arg()
