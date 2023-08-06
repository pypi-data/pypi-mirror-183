from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LifecyclePolicy(core.Schema):

    transition_to_ia: Union[str, core.StringOut] = core.attr(str, computed=True)

    transition_to_primary_storage_class: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        transition_to_ia: Union[str, core.StringOut],
        transition_to_primary_storage_class: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LifecyclePolicy.Args(
                transition_to_ia=transition_to_ia,
                transition_to_primary_storage_class=transition_to_primary_storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        transition_to_ia: Union[str, core.StringOut] = core.arg()

        transition_to_primary_storage_class: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_efs_file_system", namespace="aws_efs")
class DsFileSystem(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    creation_token: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Union[bool, core.BoolOut] = core.attr(bool, computed=True)

    file_system_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    lifecycle_policy: Union[List[LifecyclePolicy], core.ArrayOut[LifecyclePolicy]] = core.attr(
        LifecyclePolicy, computed=True, kind=core.Kind.array
    )

    performance_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    provisioned_throughput_in_mibps: Union[float, core.FloatOut] = core.attr(float, computed=True)

    size_in_bytes: Union[int, core.IntOut] = core.attr(int, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_mode: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        creation_token: Optional[Union[str, core.StringOut]] = None,
        file_system_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsFileSystem.Args(
                creation_token=creation_token,
                file_system_id=file_system_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        creation_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        file_system_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
