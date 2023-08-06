from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_grafana_license_association", namespace="aws_grafana")
class LicenseAssociation(core.Resource):

    free_trial_expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_expiration: Union[str, core.StringOut] = core.attr(str, computed=True)

    license_type: Union[str, core.StringOut] = core.attr(str)

    workspace_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        license_type: Union[str, core.StringOut],
        workspace_id: Union[str, core.StringOut],
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LicenseAssociation.Args(
                license_type=license_type,
                workspace_id=workspace_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        license_type: Union[str, core.StringOut] = core.arg()

        workspace_id: Union[str, core.StringOut] = core.arg()
