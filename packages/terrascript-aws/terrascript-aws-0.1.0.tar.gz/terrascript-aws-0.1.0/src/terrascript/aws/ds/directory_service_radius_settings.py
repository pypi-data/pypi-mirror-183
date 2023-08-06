from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_directory_service_radius_settings", namespace="aws_ds")
class DirectoryServiceRadiusSettings(core.Resource):

    authentication_protocol: Union[str, core.StringOut] = core.attr(str)

    directory_id: Union[str, core.StringOut] = core.attr(str)

    display_label: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    radius_port: Union[int, core.IntOut] = core.attr(int)

    radius_retries: Union[int, core.IntOut] = core.attr(int)

    radius_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    radius_timeout: Union[int, core.IntOut] = core.attr(int)

    shared_secret: Union[str, core.StringOut] = core.attr(str)

    use_same_username: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        authentication_protocol: Union[str, core.StringOut],
        directory_id: Union[str, core.StringOut],
        display_label: Union[str, core.StringOut],
        radius_port: Union[int, core.IntOut],
        radius_retries: Union[int, core.IntOut],
        radius_servers: Union[List[str], core.ArrayOut[core.StringOut]],
        radius_timeout: Union[int, core.IntOut],
        shared_secret: Union[str, core.StringOut],
        use_same_username: Optional[Union[bool, core.BoolOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DirectoryServiceRadiusSettings.Args(
                authentication_protocol=authentication_protocol,
                directory_id=directory_id,
                display_label=display_label,
                radius_port=radius_port,
                radius_retries=radius_retries,
                radius_servers=radius_servers,
                radius_timeout=radius_timeout,
                shared_secret=shared_secret,
                use_same_username=use_same_username,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        authentication_protocol: Union[str, core.StringOut] = core.arg()

        directory_id: Union[str, core.StringOut] = core.arg()

        display_label: Union[str, core.StringOut] = core.arg()

        radius_port: Union[int, core.IntOut] = core.arg()

        radius_retries: Union[int, core.IntOut] = core.arg()

        radius_servers: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        radius_timeout: Union[int, core.IntOut] = core.arg()

        shared_secret: Union[str, core.StringOut] = core.arg()

        use_same_username: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)
