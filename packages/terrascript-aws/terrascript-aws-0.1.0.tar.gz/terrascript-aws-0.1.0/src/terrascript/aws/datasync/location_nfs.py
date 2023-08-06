from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OnPremConfig(core.Schema):

    agent_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        agent_arns: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=OnPremConfig.Args(
                agent_arns=agent_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        agent_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


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


@core.resource(type="aws_datasync_location_nfs", namespace="aws_datasync")
class LocationNfs(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    mount_options: Optional[MountOptions] = core.attr(MountOptions, default=None)

    on_prem_config: OnPremConfig = core.attr(OnPremConfig)

    server_hostname: Union[str, core.StringOut] = core.attr(str)

    subdirectory: Union[str, core.StringOut] = core.attr(str)

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
        on_prem_config: OnPremConfig,
        server_hostname: Union[str, core.StringOut],
        subdirectory: Union[str, core.StringOut],
        mount_options: Optional[MountOptions] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=LocationNfs.Args(
                on_prem_config=on_prem_config,
                server_hostname=server_hostname,
                subdirectory=subdirectory,
                mount_options=mount_options,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        mount_options: Optional[MountOptions] = core.arg(default=None)

        on_prem_config: OnPremConfig = core.arg()

        server_hostname: Union[str, core.StringOut] = core.arg()

        subdirectory: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
