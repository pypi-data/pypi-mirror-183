from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class WorkspaceProperties(core.Schema):

    compute_type_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_volume_size_gib: Union[int, core.IntOut] = core.attr(int, computed=True)

    running_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    running_mode_auto_stop_timeout_in_minutes: Union[int, core.IntOut] = core.attr(
        int, computed=True
    )

    user_volume_size_gib: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        compute_type_name: Union[str, core.StringOut],
        root_volume_size_gib: Union[int, core.IntOut],
        running_mode: Union[str, core.StringOut],
        running_mode_auto_stop_timeout_in_minutes: Union[int, core.IntOut],
        user_volume_size_gib: Union[int, core.IntOut],
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
        compute_type_name: Union[str, core.StringOut] = core.arg()

        root_volume_size_gib: Union[int, core.IntOut] = core.arg()

        running_mode: Union[str, core.StringOut] = core.arg()

        running_mode_auto_stop_timeout_in_minutes: Union[int, core.IntOut] = core.arg()

        user_volume_size_gib: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_workspaces_workspace", namespace="aws_workspaces")
class DsWorkspace(core.Data):

    bundle_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    computer_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    directory_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    root_volume_encryption_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    user_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    user_volume_encryption_enabled: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    volume_encryption_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    workspace_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    workspace_properties: Union[
        List[WorkspaceProperties], core.ArrayOut[WorkspaceProperties]
    ] = core.attr(WorkspaceProperties, computed=True, kind=core.Kind.array)

    def __init__(
        self,
        data_name: str,
        *,
        directory_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        user_name: Optional[Union[str, core.StringOut]] = None,
        workspace_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsWorkspace.Args(
                directory_id=directory_id,
                tags=tags,
                user_name=user_name,
                workspace_id=workspace_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        user_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        workspace_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
