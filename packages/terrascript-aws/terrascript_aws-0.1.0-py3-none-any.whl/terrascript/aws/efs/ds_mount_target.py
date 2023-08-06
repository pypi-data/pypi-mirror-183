from typing import List, Optional, Union

import terrascript.core as core


@core.data(type="aws_efs_mount_target", namespace="aws_efs")
class DsMountTarget(core.Data):

    access_point_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    file_system_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    mount_target_dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    mount_target_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    network_interface_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    subnet_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        access_point_id: Optional[Union[str, core.StringOut]] = None,
        file_system_id: Optional[Union[str, core.StringOut]] = None,
        mount_target_id: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMountTarget.Args(
                access_point_id=access_point_id,
                file_system_id=file_system_id,
                mount_target_id=mount_target_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        access_point_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_system_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        mount_target_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
