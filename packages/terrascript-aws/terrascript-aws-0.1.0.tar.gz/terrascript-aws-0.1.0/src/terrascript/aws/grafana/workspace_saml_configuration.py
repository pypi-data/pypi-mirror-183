from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_grafana_workspace_saml_configuration", namespace="aws_grafana")
class WorkspaceSamlConfiguration(core.Resource):

    admin_role_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    allowed_organizations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    editor_role_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    email_assertion: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    groups_assertion: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idp_metadata_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    idp_metadata_xml: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    login_assertion: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    login_validity_duration: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    name_assertion: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    org_assertion: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    role_assertion: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    workspace_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        editor_role_values: Union[List[str], core.ArrayOut[core.StringOut]],
        workspace_id: Union[str, core.StringOut],
        admin_role_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        allowed_organizations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        email_assertion: Optional[Union[str, core.StringOut]] = None,
        groups_assertion: Optional[Union[str, core.StringOut]] = None,
        idp_metadata_url: Optional[Union[str, core.StringOut]] = None,
        idp_metadata_xml: Optional[Union[str, core.StringOut]] = None,
        login_assertion: Optional[Union[str, core.StringOut]] = None,
        login_validity_duration: Optional[Union[int, core.IntOut]] = None,
        name_assertion: Optional[Union[str, core.StringOut]] = None,
        org_assertion: Optional[Union[str, core.StringOut]] = None,
        role_assertion: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=WorkspaceSamlConfiguration.Args(
                editor_role_values=editor_role_values,
                workspace_id=workspace_id,
                admin_role_values=admin_role_values,
                allowed_organizations=allowed_organizations,
                email_assertion=email_assertion,
                groups_assertion=groups_assertion,
                idp_metadata_url=idp_metadata_url,
                idp_metadata_xml=idp_metadata_xml,
                login_assertion=login_assertion,
                login_validity_duration=login_validity_duration,
                name_assertion=name_assertion,
                org_assertion=org_assertion,
                role_assertion=role_assertion,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        admin_role_values: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        allowed_organizations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        editor_role_values: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        email_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        groups_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        idp_metadata_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        idp_metadata_xml: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        login_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        login_validity_duration: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        org_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        role_assertion: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workspace_id: Union[str, core.StringOut] = core.arg()
