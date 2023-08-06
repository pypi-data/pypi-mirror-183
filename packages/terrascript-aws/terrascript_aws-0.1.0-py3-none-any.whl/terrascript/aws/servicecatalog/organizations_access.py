from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_servicecatalog_organizations_access", namespace="aws_servicecatalog")
class OrganizationsAccess(core.Resource):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        enabled: Union[bool, core.BoolOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=OrganizationsAccess.Args(
                enabled=enabled,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: Union[bool, core.BoolOut] = core.arg()
