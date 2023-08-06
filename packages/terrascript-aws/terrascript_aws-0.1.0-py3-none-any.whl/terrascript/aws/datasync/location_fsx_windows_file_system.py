from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_datasync_location_fsx_windows_file_system", namespace="aws_datasync")
class LocationFsxWindowsFileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    domain: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    fsx_filesystem_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    password: Union[str, core.StringOut] = core.attr(str)

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

    user: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        fsx_filesystem_arn: Union[str, core.StringOut],
        password: Union[str, core.StringOut],
        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]],
        user: Union[str, core.StringOut],
        domain: Optional[Union[str, core.StringOut]] = None,
        subdirectory: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationFsxWindowsFileSystem.Args(
                fsx_filesystem_arn=fsx_filesystem_arn,
                password=password,
                security_group_arns=security_group_arns,
                user=user,
                domain=domain,
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
        domain: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        fsx_filesystem_arn: Union[str, core.StringOut] = core.arg()

        password: Union[str, core.StringOut] = core.arg()

        security_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        subdirectory: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        user: Union[str, core.StringOut] = core.arg()
