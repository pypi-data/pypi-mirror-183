from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PosixUser(core.Schema):

    gid: Union[int, core.IntOut] = core.attr(int)

    secondary_gids: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.attr(
        int, default=None, kind=core.Kind.array
    )

    uid: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        gid: Union[int, core.IntOut],
        uid: Union[int, core.IntOut],
        secondary_gids: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = None,
    ):
        super().__init__(
            args=PosixUser.Args(
                gid=gid,
                uid=uid,
                secondary_gids=secondary_gids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        gid: Union[int, core.IntOut] = core.arg()

        secondary_gids: Optional[Union[List[int], core.ArrayOut[core.IntOut]]] = core.arg(
            default=None
        )

        uid: Union[int, core.IntOut] = core.arg()


@core.schema
class CreationInfo(core.Schema):

    owner_gid: Union[int, core.IntOut] = core.attr(int)

    owner_uid: Union[int, core.IntOut] = core.attr(int)

    permissions: Union[str, core.StringOut] = core.attr(str)

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

    creation_info: Optional[CreationInfo] = core.attr(CreationInfo, default=None, computed=True)

    path: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        creation_info: Optional[CreationInfo] = None,
        path: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=RootDirectory.Args(
                creation_info=creation_info,
                path=path,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_info: Optional[CreationInfo] = core.arg(default=None)

        path: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_efs_access_point", namespace="aws_efs")
class AccessPoint(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    posix_user: Optional[PosixUser] = core.attr(PosixUser, default=None)

    root_directory: Optional[RootDirectory] = core.attr(RootDirectory, default=None, computed=True)

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
        file_system_id: Union[str, core.StringOut],
        posix_user: Optional[PosixUser] = None,
        root_directory: Optional[RootDirectory] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=AccessPoint.Args(
                file_system_id=file_system_id,
                posix_user=posix_user,
                root_directory=root_directory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        file_system_id: Union[str, core.StringOut] = core.arg()

        posix_user: Optional[PosixUser] = core.arg(default=None)

        root_directory: Optional[RootDirectory] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
