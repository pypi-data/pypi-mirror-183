from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class WorkspaceCreationProperties(core.Schema):

    custom_security_group_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    default_ou: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable_internet_access: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    enable_maintenance_mode: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    user_enabled_as_local_administrator: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    def __init__(
        self,
        *,
        custom_security_group_id: Optional[Union[str, core.StringOut]] = None,
        default_ou: Optional[Union[str, core.StringOut]] = None,
        enable_internet_access: Optional[Union[bool, core.BoolOut]] = None,
        enable_maintenance_mode: Optional[Union[bool, core.BoolOut]] = None,
        user_enabled_as_local_administrator: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=WorkspaceCreationProperties.Args(
                custom_security_group_id=custom_security_group_id,
                default_ou=default_ou,
                enable_internet_access=enable_internet_access,
                enable_maintenance_mode=enable_maintenance_mode,
                user_enabled_as_local_administrator=user_enabled_as_local_administrator,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        custom_security_group_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        default_ou: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable_internet_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        enable_maintenance_mode: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        user_enabled_as_local_administrator: Optional[Union[bool, core.BoolOut]] = core.arg(
            default=None
        )


@core.schema
class SelfServicePermissions(core.Schema):

    change_compute_type: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    increase_volume_size: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    rebuild_workspace: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    restart_workspace: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    switch_running_mode: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        change_compute_type: Optional[Union[bool, core.BoolOut]] = None,
        increase_volume_size: Optional[Union[bool, core.BoolOut]] = None,
        rebuild_workspace: Optional[Union[bool, core.BoolOut]] = None,
        restart_workspace: Optional[Union[bool, core.BoolOut]] = None,
        switch_running_mode: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=SelfServicePermissions.Args(
                change_compute_type=change_compute_type,
                increase_volume_size=increase_volume_size,
                rebuild_workspace=rebuild_workspace,
                restart_workspace=restart_workspace,
                switch_running_mode=switch_running_mode,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        change_compute_type: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        increase_volume_size: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        rebuild_workspace: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        restart_workspace: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        switch_running_mode: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class WorkspaceAccessProperties(core.Schema):

    device_type_android: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_chromeos: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_ios: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_linux: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_osx: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_web: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_windows: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    device_type_zeroclient: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        device_type_android: Optional[Union[str, core.StringOut]] = None,
        device_type_chromeos: Optional[Union[str, core.StringOut]] = None,
        device_type_ios: Optional[Union[str, core.StringOut]] = None,
        device_type_linux: Optional[Union[str, core.StringOut]] = None,
        device_type_osx: Optional[Union[str, core.StringOut]] = None,
        device_type_web: Optional[Union[str, core.StringOut]] = None,
        device_type_windows: Optional[Union[str, core.StringOut]] = None,
        device_type_zeroclient: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=WorkspaceAccessProperties.Args(
                device_type_android=device_type_android,
                device_type_chromeos=device_type_chromeos,
                device_type_ios=device_type_ios,
                device_type_linux=device_type_linux,
                device_type_osx=device_type_osx,
                device_type_web=device_type_web,
                device_type_windows=device_type_windows,
                device_type_zeroclient=device_type_zeroclient,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        device_type_android: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_chromeos: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_ios: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_linux: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_osx: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_web: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_windows: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        device_type_zeroclient: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_workspaces_directory", namespace="aws_workspaces")
class Directory(core.Resource):

    alias: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_user_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_id: Union[str, core.StringOut] = core.attr(str)

    directory_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_ip_addresses: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    iam_role_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    registration_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    self_service_permissions: Optional[SelfServicePermissions] = core.attr(
        SelfServicePermissions, default=None, computed=True
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    workspace_access_properties: Optional[WorkspaceAccessProperties] = core.attr(
        WorkspaceAccessProperties, default=None, computed=True
    )

    workspace_creation_properties: Optional[WorkspaceCreationProperties] = core.attr(
        WorkspaceCreationProperties, default=None, computed=True
    )

    workspace_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        ip_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        self_service_permissions: Optional[SelfServicePermissions] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        workspace_access_properties: Optional[WorkspaceAccessProperties] = None,
        workspace_creation_properties: Optional[WorkspaceCreationProperties] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Directory.Args(
                directory_id=directory_id,
                ip_group_ids=ip_group_ids,
                self_service_permissions=self_service_permissions,
                subnet_ids=subnet_ids,
                tags=tags,
                tags_all=tags_all,
                workspace_access_properties=workspace_access_properties,
                workspace_creation_properties=workspace_creation_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        directory_id: Union[str, core.StringOut] = core.arg()

        ip_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        self_service_permissions: Optional[SelfServicePermissions] = core.arg(default=None)

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        workspace_access_properties: Optional[WorkspaceAccessProperties] = core.arg(default=None)

        workspace_creation_properties: Optional[WorkspaceCreationProperties] = core.arg(
            default=None
        )
