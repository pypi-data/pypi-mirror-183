from typing import List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_efs_mount_target", namespace="aws_efs")
class MountTarget(core.Resource):

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    mount_target_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        file_system_id: Union[str, core.StringOut],
        subnet_id: Union[str, core.StringOut],
        ip_address: Optional[Union[str, core.StringOut]] = None,
        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MountTarget.Args(
                file_system_id=file_system_id,
                subnet_id=subnet_id,
                ip_address=ip_address,
                security_groups=security_groups,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        file_system_id: Union[str, core.StringOut] = core.arg()

        ip_address: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        security_groups: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_id: Union[str, core.StringOut] = core.arg()
