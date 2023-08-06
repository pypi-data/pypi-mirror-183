from typing import List, Optional, Union

import terrascript.core as core


@core.resource(
    type="aws_worklink_website_certificate_authority_association", namespace="aws_worklink"
)
class WebsiteCertificateAuthorityAssociation(core.Resource):

    certificate: Union[str, core.StringOut] = core.attr(str)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fleet_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    website_ca_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        certificate: Union[str, core.StringOut],
        fleet_arn: Union[str, core.StringOut],
        display_name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WebsiteCertificateAuthorityAssociation.Args(
                certificate=certificate,
                fleet_arn=fleet_arn,
                display_name=display_name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        certificate: Union[str, core.StringOut] = core.arg()

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fleet_arn: Union[str, core.StringOut] = core.arg()
