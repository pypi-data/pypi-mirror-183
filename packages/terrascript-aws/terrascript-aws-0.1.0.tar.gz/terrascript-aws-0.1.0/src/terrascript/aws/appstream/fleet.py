from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DomainJoinInfo(core.Schema):

    directory_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    def __init__(
        self,
        *,
        directory_name: Optional[Union[str, core.StringOut]] = None,
        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=DomainJoinInfo.Args(
                directory_name=directory_name,
                organizational_unit_distinguished_name=organizational_unit_distinguished_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        directory_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        organizational_unit_distinguished_name: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )


@core.schema
class VpcConfig(core.Schema):

    security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=VpcConfig.Args(
                security_group_ids=security_group_ids,
                subnet_ids=subnet_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        subnet_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )


@core.schema
class ComputeCapacity(core.Schema):

    available: Union[int, core.IntOut] = core.attr(int, computed=True)

    desired_instances: Union[int, core.IntOut] = core.attr(int)

    in_use: Union[int, core.IntOut] = core.attr(int, computed=True)

    running: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        available: Union[int, core.IntOut],
        desired_instances: Union[int, core.IntOut],
        in_use: Union[int, core.IntOut],
        running: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ComputeCapacity.Args(
                available=available,
                desired_instances=desired_instances,
                in_use=in_use,
                running=running,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        available: Union[int, core.IntOut] = core.arg()

        desired_instances: Union[int, core.IntOut] = core.arg()

        in_use: Union[int, core.IntOut] = core.arg()

        running: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_appstream_fleet", namespace="aws_appstream")
class Fleet(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compute_capacity: ComputeCapacity = core.attr(ComputeCapacity)

    created_time: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    display_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    domain_join_info: Optional[DomainJoinInfo] = core.attr(
        DomainJoinInfo, default=None, computed=True
    )

    enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = core.attr(
        bool, default=None, computed=True
    )

    fleet_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    idle_disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None
    )

    image_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    image_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    max_user_duration_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(
        int, default=None, computed=True
    )

    name: Union[str, core.StringOut] = core.attr(str)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    stream_view: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    vpc_config: Optional[VpcConfig] = core.attr(VpcConfig, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        compute_capacity: ComputeCapacity,
        instance_type: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
        display_name: Optional[Union[str, core.StringOut]] = None,
        domain_join_info: Optional[DomainJoinInfo] = None,
        enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = None,
        fleet_type: Optional[Union[str, core.StringOut]] = None,
        iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        idle_disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
        image_arn: Optional[Union[str, core.StringOut]] = None,
        image_name: Optional[Union[str, core.StringOut]] = None,
        max_user_duration_in_seconds: Optional[Union[int, core.IntOut]] = None,
        stream_view: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        vpc_config: Optional[VpcConfig] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Fleet.Args(
                compute_capacity=compute_capacity,
                instance_type=instance_type,
                name=name,
                description=description,
                disconnect_timeout_in_seconds=disconnect_timeout_in_seconds,
                display_name=display_name,
                domain_join_info=domain_join_info,
                enable_default_internet_access=enable_default_internet_access,
                fleet_type=fleet_type,
                iam_role_arn=iam_role_arn,
                idle_disconnect_timeout_in_seconds=idle_disconnect_timeout_in_seconds,
                image_arn=image_arn,
                image_name=image_name,
                max_user_duration_in_seconds=max_user_duration_in_seconds,
                stream_view=stream_view,
                tags=tags,
                tags_all=tags_all,
                vpc_config=vpc_config,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_capacity: ComputeCapacity = core.arg()

        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        display_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        domain_join_info: Optional[DomainJoinInfo] = core.arg(default=None)

        enable_default_internet_access: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        fleet_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        idle_disconnect_timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(
            default=None
        )

        image_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        max_user_duration_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        stream_view: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        vpc_config: Optional[VpcConfig] = core.arg(default=None)
