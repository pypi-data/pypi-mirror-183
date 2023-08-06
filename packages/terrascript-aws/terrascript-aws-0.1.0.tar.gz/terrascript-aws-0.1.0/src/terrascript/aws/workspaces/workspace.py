from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class WorkspaceProperties(core.Schema):

    compute_type_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    root_volume_size_gib: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    running_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    running_mode_auto_stop_timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    user_volume_size_gib: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        compute_type_name: Optional[Union[str, core.StringOut]] = None,
        root_volume_size_gib: Optional[Union[int, core.IntOut]] = None,
        running_mode: Optional[Union[str, core.StringOut]] = None,
        running_mode_auto_stop_timeout_in_minutes: Optional[Union[int, core.IntOut]] = None,
        user_volume_size_gib: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=WorkspaceProperties.Args(
                compute_type_name=compute_type_name,
                root_volume_size_gib=root_volume_size_gib,
                running_mode=running_mode,
                running_mode_auto_stop_timeout_in_minutes=running_mode_auto_stop_timeout_in_minutes,
                user_volume_size_gib=user_volume_size_gib,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_type_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        root_volume_size_gib: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        running_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        running_mode_auto_stop_timeout_in_minutes: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        user_volume_size_gib: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_workspaces_workspace", namespace="aws_workspaces")
class Workspace(core.Resource):

    bundle_id: Union[str, core.StringOut] = core.attr(str)

    computer_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: Union[str, core.StringOut] = core.attr(str)

    user_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None
    )

    volume_encryption_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    workspace_properties: Optional[WorkspaceProperties] = core.attr(
        WorkspaceProperties, default=None, computed=True
    )

    def __init__(
        self,
        resource_name: str,
        *,
        bundle_id: Union[str, core.StringOut],
        directory_id: Union[str, core.StringOut],
        user_name: Union[str, core.StringOut],
        root_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = None,
        volume_encryption_key: Optional[Union[str, core.StringOut]] = None,
        workspace_properties: Optional[WorkspaceProperties] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Workspace.Args(
                bundle_id=bundle_id,
                directory_id=directory_id,
                user_name=user_name,
                root_volume_encryption_enabled=root_volume_encryption_enabled,
                tags=tags,
                tags_all=tags_all,
                user_volume_encryption_enabled=user_volume_encryption_enabled,
                volume_encryption_key=volume_encryption_key,
                workspace_properties=workspace_properties,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        bundle_id: Union[str, core.StringOut] = core.arg()

        directory_id: Union[str, core.StringOut] = core.arg()

        root_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user_name: Union[str, core.StringOut] = core.arg()

        user_volume_encryption_enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        volume_encryption_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workspace_properties: Optional[WorkspaceProperties] = core.arg(default=None)
