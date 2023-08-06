from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PosixUser(core.Schema):

    gid: Union[int, core.IntOut] = core.attr(int, computed=True)

    secondary_gids: Union[List[int], core.ArrayOut[core.IntOut]] = core.attr(
        int, computed=True, kind=core.Kind.array
    )

    uid: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        gid: Union[int, core.IntOut],
        secondary_gids: Union[List[int], core.ArrayOut[core.IntOut]],
        uid: Union[int, core.IntOut],
    ):
        super().__init__(
            args=PosixUser.Args(
                gid=gid,
                secondary_gids=secondary_gids,
                uid=uid,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gid: Union[int, core.IntOut] = core.arg()

        secondary_gids: Union[List[int], core.ArrayOut[core.IntOut]] = core.arg()

        uid: Union[int, core.IntOut] = core.arg()


@core.schema
class CreationInfo(core.Schema):

    owner_gid: Union[int, core.IntOut] = core.attr(int, computed=True)

    owner_uid: Union[int, core.IntOut] = core.attr(int, computed=True)

    permissions: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        owner_gid: Union[int, core.IntOut],
        owner_uid: Union[int, core.IntOut],
        permissions: Union[str, core.StringOut],
    ):
        super().__init__(
            args=CreationInfo.Args(
                owner_gid=owner_gid,
                owner_uid=owner_uid,
                permissions=permissions,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        owner_gid: Union[int, core.IntOut] = core.arg()

        owner_uid: Union[int, core.IntOut] = core.arg()

        permissions: Union[str, core.StringOut] = core.arg()


@core.schema
class RootDirectory(core.Schema):

    creation_info: Union[List[CreationInfo], core.ArrayOut[CreationInfo]] = core.attr(
        CreationInfo, computed=True, kind=core.Kind.array
    )

    path: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        creation_info: Union[List[CreationInfo], core.ArrayOut[CreationInfo]],
        path: Union[str, core.StringOut],
    ):
        super().__init__(
            args=RootDirectory.Args(
                creation_info=creation_info,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_info: Union[List[CreationInfo], core.ArrayOut[CreationInfo]] = core.arg()

        path: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_efs_access_point", namespace="aws_efs")
class DsAccessPoint(core.Data):

    access_point_id: Union[str, core.StringOut] = core.attr(str)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    posix_user: Union[List[PosixUser], core.ArrayOut[PosixUser]] = core.attr(
        PosixUser, computed=True, kind=core.Kind.array
    )

    root_directory: Union[List[RootDirectory], core.ArrayOut[RootDirectory]] = core.attr(
        RootDirectory, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        access_point_id: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsAccessPoint.Args(
                access_point_id=access_point_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
