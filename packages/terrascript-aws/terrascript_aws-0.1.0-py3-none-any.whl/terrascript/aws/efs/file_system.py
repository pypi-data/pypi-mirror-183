from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class SizeInBytes(core.Schema):

    value: Union[int, core.IntOut] = core.attr(int, computed=True)

    value_in_ia: Union[int, core.IntOut] = core.attr(int, computed=True)

    value_in_standard: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        value: Union[int, core.IntOut],
        value_in_ia: Union[int, core.IntOut],
        value_in_standard: Union[int, core.IntOut],
    ):
        super().__init__(
            args=SizeInBytes.Args(
                value=value,
                value_in_ia=value_in_ia,
                value_in_standard=value_in_standard,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        value: Union[int, core.IntOut] = core.arg()

        value_in_ia: Union[int, core.IntOut] = core.arg()

        value_in_standard: Union[int, core.IntOut] = core.arg()


@core.schema
class LifecyclePolicy(core.Schema):

    transition_to_ia: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transition_to_primary_storage_class: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    def __init__(
        self,
        *,
        transition_to_ia: Optional[Union[str, core.StringOut]] = None,
        transition_to_primary_storage_class: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LifecyclePolicy.Args(
                transition_to_ia=transition_to_ia,
                transition_to_primary_storage_class=transition_to_primary_storage_class,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        transition_to_ia: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transition_to_primary_storage_class: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.resource(type="aws_efs_file_system", namespace="aws_efs")
class FileSystem(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    creation_token: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    dns_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    encrypted: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kms_key_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    lifecycle_policy: Optional[
        Union[List[LifecyclePolicy], core.ArrayOut[LifecyclePolicy]]
    ] = core.attr(LifecyclePolicy, default=None, kind=core.Kind.array)

    number_of_mount_targets: Union[int, core.IntOut] = core.attr(int, computed=True)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    performance_mode: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    provisioned_throughput_in_mibps: Optional[Union[float, core.FloatOut]] = core.attr(
        float, default=None
    )

    size_in_bytes: Union[List[SizeInBytes], core.ArrayOut[SizeInBytes]] = core.attr(
        SizeInBytes, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    throughput_mode: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone_name: Optional[Union[str, core.StringOut]] = None,
        creation_token: Optional[Union[str, core.StringOut]] = None,
        encrypted: Optional[Union[bool, core.BoolOut]] = None,
        kms_key_id: Optional[Union[str, core.StringOut]] = None,
        lifecycle_policy: Optional[
            Union[List[LifecyclePolicy], core.ArrayOut[LifecyclePolicy]]
        ] = None,
        performance_mode: Optional[Union[str, core.StringOut]] = None,
        provisioned_throughput_in_mibps: Optional[Union[float, core.FloatOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        throughput_mode: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FileSystem.Args(
                availability_zone_name=availability_zone_name,
                creation_token=creation_token,
                encrypted=encrypted,
                kms_key_id=kms_key_id,
                lifecycle_policy=lifecycle_policy,
                performance_mode=performance_mode,
                provisioned_throughput_in_mibps=provisioned_throughput_in_mibps,
                tags=tags,
                tags_all=tags_all,
                throughput_mode=throughput_mode,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        creation_token: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        encrypted: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        kms_key_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        lifecycle_policy: Optional[
            Union[List[LifecyclePolicy], core.ArrayOut[LifecyclePolicy]]
        ] = core.arg(default=None)

        performance_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        provisioned_throughput_in_mibps: Optional[Union[float, core.FloatOut]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        throughput_mode: Optional[Union[str, core.StringOut]] = core.arg(default=None)
