from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class MountOptions(core.Schema):

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=MountOptions.Args(
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Nfs(core.Schema):

    mount_options: MountOptions = core.attr(MountOptions)

    def __init__(
        self,
        *,
        mount_options: MountOptions,
    ):
        super().__init__(
            args=Nfs.Args(
                mount_options=mount_options,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        mount_options: MountOptions = core.arg()


@core.schema
class Protocol(core.Schema):

    nfs: Nfs = core.attr(Nfs)

    def __init__(
        self,
        *,
        nfs: Nfs,
    ):
        super().__init__(
            args=Protocol.Args(
                nfs=nfs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        nfs: Nfs = core.arg()


@core.resource(type="aws_datasync_location_fsx_openzfs_file_system", namespace="aws_datasync")
class LocationFsxOpenzfsFileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    fsx_filesystem_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    protocol: Protocol = core.attr(Protocol)

    security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    subdirectory: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    uri: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        fsx_filesystem_arn: Union[str, core.StringOut],
        protocol: Protocol,
        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        subdirectory: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationFsxOpenzfsFileSystem.Args(
                fsx_filesystem_arn=fsx_filesystem_arn,
                protocol=protocol,
                security_group_arns=security_group_arns,
                subdirectory=subdirectory,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        fsx_filesystem_arn: Union[str, core.StringOut] = core.arg()

        protocol: Protocol = core.arg()

        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subdirectory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
