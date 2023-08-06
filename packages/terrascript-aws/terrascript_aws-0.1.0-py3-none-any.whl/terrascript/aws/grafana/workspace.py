from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_grafana_workspace", namespace="aws_grafana")
class Workspace(core.Resource):

    account_access_type: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    authentication_providers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    data_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    endpoint: Union[str, core.StringOut] = core.attr(str, computed=True)

    grafana_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    notification_destinations: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    organization_role_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    organizational_units: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    permission_type: Union[str, core.StringOut] = core.attr(str)

    role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    saml_configuration_status: Union[str, core.StringOut] = core.attr(str, computed=True)

    stack_set_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        account_access_type: Union[str, core.StringOut],
        authentication_providers: Union[List[str], core.ArrayOut[core.StringOut]],
        permission_type: Union[str, core.StringOut],
        data_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        notification_destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        organization_role_name: Optional[Union[str, core.StringOut]] = None,
        organizational_units: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        role_arn: Optional[Union[str, core.StringOut]] = None,
        stack_set_name: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workspace.Args(
                account_access_type=account_access_type,
                authentication_providers=authentication_providers,
                permission_type=permission_type,
                data_sources=data_sources,
                description=description,
                name=name,
                notification_destinations=notification_destinations,
                organization_role_name=organization_role_name,
                organizational_units=organizational_units,
                role_arn=role_arn,
                stack_set_name=stack_set_name,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        account_access_type: Union[str, core.StringOut] = core.arg()

        authentication_providers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        data_sources: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        notification_destinations: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        organization_role_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizational_units: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        permission_type: Union[str, core.StringOut] = core.arg()

        role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        stack_set_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
