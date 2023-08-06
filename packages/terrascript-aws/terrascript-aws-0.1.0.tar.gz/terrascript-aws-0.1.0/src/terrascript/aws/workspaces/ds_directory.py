from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class WorkspaceAccessProperties(core.Schema):

    device_type_android: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_chromeos: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_ios: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_linux: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_osx: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_web: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_windows: Union[str, core.StringOut] = core.attr(str, computed=True)

    device_type_zeroclient: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        device_type_android: Union[str, core.StringOut],
        device_type_chromeos: Union[str, core.StringOut],
        device_type_ios: Union[str, core.StringOut],
        device_type_linux: Union[str, core.StringOut],
        device_type_osx: Union[str, core.StringOut],
        device_type_web: Union[str, core.StringOut],
        device_type_windows: Union[str, core.StringOut],
        device_type_zeroclient: Union[str, core.StringOut],
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
        device_type_android: Union[str, core.StringOut] = core.arg()

        device_type_chromeos: Union[str, core.StringOut] = core.arg()

        device_type_ios: Union[str, core.StringOut] = core.arg()

        device_type_linux: Union[str, core.StringOut] = core.arg()

        device_type_osx: Union[str, core.StringOut] = core.arg()

        device_type_web: Union[str, core.StringOut] = core.arg()

        device_type_windows: Union[str, core.StringOut] = core.arg()

        device_type_zeroclient: Union[str, core.StringOut] = core.arg()


@core.schema
class WorkspaceCreationProperties(core.Schema):

    custom_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_ou: Union[str, core.StringOut] = core.attr(str, computed=True)

    enable_internet_access: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    enable_maintenance_mode: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    user_enabled_as_local_administrator: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        custom_security_group_id: Union[str, core.StringOut],
        default_ou: Union[str, core.StringOut],
        enable_internet_access: Union[bool, core.BoolOut],
        enable_maintenance_mode: Union[bool, core.BoolOut],
        user_enabled_as_local_administrator: Union[bool, core.BoolOut],
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
        custom_security_group_id: Union[str, core.StringOut] = core.arg()

        default_ou: Union[str, core.StringOut] = core.arg()

        enable_internet_access: Union[bool, core.BoolOut] = core.arg()

        enable_maintenance_mode: Union[bool, core.BoolOut] = core.arg()

        user_enabled_as_local_administrator: Union[bool, core.BoolOut] = core.arg()


@core.schema
class SelfServicePermissions(core.Schema):

    change_compute_type: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    increase_volume_size: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    rebuild_workspace: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    restart_workspace: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    switch_running_mode: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    def __init__(
        self,
        *,
        change_compute_type: Union[bool, core.BoolOut],
        increase_volume_size: Union[bool, core.BoolOut],
        rebuild_workspace: Union[bool, core.BoolOut],
        restart_workspace: Union[bool, core.BoolOut],
        switch_running_mode: Union[bool, core.BoolOut],
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
        change_compute_type: Union[bool, core.BoolOut] = core.arg()

        increase_volume_size: Union[bool, core.BoolOut] = core.arg()

        rebuild_workspace: Union[bool, core.BoolOut] = core.arg()

        restart_workspace: Union[bool, core.BoolOut] = core.arg()

        switch_running_mode: Union[bool, core.BoolOut] = core.arg()


@core.data(type="aws_workspaces_directory", namespace="aws_workspaces")
class DsDirectory(core.Data):

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

    ip_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    registration_code: Union[str, core.StringOut] = core.attr(str, computed=True)

    self_service_permissions: Union[
        List[SelfServicePermissions], core.ArrayOut[SelfServicePermissions]
    ] = core.attr(SelfServicePermissions, computed=True, kind=core.Kind.array)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    workspace_access_properties: Union[
        List[WorkspaceAccessProperties], core.ArrayOut[WorkspaceAccessProperties]
    ] = core.attr(WorkspaceAccessProperties, computed=True, kind=core.Kind.array)

    workspace_creation_properties: Union[
        List[WorkspaceCreationProperties], core.ArrayOut[WorkspaceCreationProperties]
    ] = core.attr(WorkspaceCreationProperties, computed=True, kind=core.Kind.array)

    workspace_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsDirectory.Args(
                directory_id=directory_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
