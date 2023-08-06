from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class HomeDirectoryMappings(core.Schema):

    entry: Union[str, core.StringOut] = core.attr(str)

    target: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        entry: Union[str, core.StringOut],
        target: Union[str, core.StringOut],
    ):
        super().__init__(
            args=HomeDirectoryMappings.Args(
                entry=entry,
                target=target,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        entry: Union[str, core.StringOut] = core.arg()

        target: Union[str, core.StringOut] = core.arg()


@core.schema
class PosixProfile(core.Schema):

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
            args=PosixProfile.Args(
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


@core.resource(type="aws_transfer_access", namespace="aws_transfer")
class Access(core.Resource):

    external_id: Union[str, core.StringOut] = core.attr(str)

    home_directory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    home_directory_mappings: Optional[
        Union[List[HomeDirectoryMappings], core.ArrayOut[HomeDirectoryMappings]]
    ] = core.attr(HomeDirectoryMappings, default=None, kind=core.Kind.array)

    home_directory_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    posix_profile: Optional[PosixProfile] = core.attr(PosixProfile, default=None)

    role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    server_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        external_id: Union[str, core.StringOut],
        server_id: Union[str, core.StringOut],
        home_directory: Optional[Union[str, core.StringOut]] = None,
        home_directory_mappings: Optional[
            Union[List[HomeDirectoryMappings], core.ArrayOut[HomeDirectoryMappings]]
        ] = None,
        home_directory_type: Optional[Union[str, core.StringOut]] = None,
        policy: Optional[Union[str, core.StringOut]] = None,
        posix_profile: Optional[PosixProfile] = None,
        role: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Access.Args(
                external_id=external_id,
                server_id=server_id,
                home_directory=home_directory,
                home_directory_mappings=home_directory_mappings,
                home_directory_type=home_directory_type,
                policy=policy,
                posix_profile=posix_profile,
                role=role,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        external_id: Union[str, core.StringOut] = core.arg()

        home_directory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        home_directory_mappings: Optional[
            Union[List[HomeDirectoryMappings], core.ArrayOut[HomeDirectoryMappings]]
        ] = core.arg(default=None)

        home_directory_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        posix_profile: Optional[PosixProfile] = core.arg(default=None)

        role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        server_id: Union[str, core.StringOut] = core.arg()
