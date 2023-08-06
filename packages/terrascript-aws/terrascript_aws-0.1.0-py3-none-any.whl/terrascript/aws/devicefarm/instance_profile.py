from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_devicefarm_instance_profile", namespace="aws_devicefarm")
class InstanceProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    exclude_app_packages_from_cleanup: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    package_cleanup: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    reboot_after_use: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

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
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        exclude_app_packages_from_cleanup: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
        package_cleanup: Optional[Union[bool, core.BoolOut]] = None,
        reboot_after_use: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceProfile.Args(
                name=name,
                description=description,
                exclude_app_packages_from_cleanup=exclude_app_packages_from_cleanup,
                package_cleanup=package_cleanup,
                reboot_after_use=reboot_after_use,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        exclude_app_packages_from_cleanup: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        package_cleanup: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        reboot_after_use: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
