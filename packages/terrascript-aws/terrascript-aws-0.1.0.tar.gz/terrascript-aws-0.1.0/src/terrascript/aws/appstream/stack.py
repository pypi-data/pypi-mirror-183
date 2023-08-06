from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class UserSettings(core.Schema):

    action: Union[str, core.StringOut] = core.attr(str)

    permission: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        action: Union[str, core.StringOut],
        permission: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserSettings.Args(
                action=action,
                permission=permission,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        action: Union[str, core.StringOut] = core.arg()

        permission: Union[str, core.StringOut] = core.arg()


@core.schema
class ApplicationSettings(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    settings_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        settings_group: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=ApplicationSettings.Args(
                enabled=enabled,
                settings_group=settings_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        settings_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class StorageConnectors(core.Schema):

    connector_type: Union[str, core.StringOut] = core.attr(str)

    domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    resource_identifier: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        connector_type: Union[str, core.StringOut],
        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        resource_identifier: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=StorageConnectors.Args(
                connector_type=connector_type,
                domains=domains,
                resource_identifier=resource_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        connector_type: Union[str, core.StringOut] = core.arg()

        domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(default=None)

        resource_identifier: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AccessEndpoints(core.Schema):

    endpoint_type: Union[str, core.StringOut] = core.attr(str)

    vpce_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        endpoint_type: Union[str, core.StringOut],
        vpce_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=AccessEndpoints.Args(
                endpoint_type=endpoint_type,
                vpce_id=vpce_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        endpoint_type: Union[str, core.StringOut] = core.arg()

        vpce_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_appstream_stack", namespace="aws_appstream")
class Stack(core.Resource):

    access_endpoints: Optional[
        Union[List[AccessEndpoints], core.ArrayOut[AccessEndpoints]]
    ] = core.attr(AccessEndpoints, default=None, computed=True, kind=core.Kind.array)

    application_settings: Optional[ApplicationSettings] = core.attr(
        ApplicationSettings, default=None, computed=True
    )

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    embed_host_domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    feedback_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    redirect_url: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    storage_connectors: Optional[
        Union[List[StorageConnectors], core.ArrayOut[StorageConnectors]]
    ] = core.attr(StorageConnectors, default=None, computed=True, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_settings: Optional[Union[List[UserSettings], core.ArrayOut[UserSettings]]] = core.attr(
        UserSettings, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        access_endpoints: Optional[
            Union[List[AccessEndpoints], core.ArrayOut[AccessEndpoints]]
        ] = None,
        application_settings: Optional[ApplicationSettings] = None,
        description: Optional[Union[str, core.StringOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        embed_host_domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        feedback_url: Optional[Union[str, core.StringOut]] = None,
        redirect_url: Optional[Union[str, core.StringOut]] = None,
        storage_connectors: Optional[
            Union[List[StorageConnectors], core.ArrayOut[StorageConnectors]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_settings: Optional[Union[List[UserSettings], core.ArrayOut[UserSettings]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Stack.Args(
                name=name,
                access_endpoints=access_endpoints,
                application_settings=application_settings,
                description=description,
                display_name=display_name,
                embed_host_domains=embed_host_domains,
                feedback_url=feedback_url,
                redirect_url=redirect_url,
                storage_connectors=storage_connectors,
                tags=tags,
                tags_all=tags_all,
                user_settings=user_settings,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_endpoints: Optional[
            Union[List[AccessEndpoints], core.ArrayOut[AccessEndpoints]]
        ] = core.arg(default=None)

        application_settings: Optional[ApplicationSettings] = core.arg(default=None)

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        embed_host_domains: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        feedback_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        redirect_url: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        storage_connectors: Optional[
            Union[List[StorageConnectors], core.ArrayOut[StorageConnectors]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_settings: Optional[Union[List[UserSettings], core.ArrayOut[UserSettings]]] = core.arg(
            default=None
        )
