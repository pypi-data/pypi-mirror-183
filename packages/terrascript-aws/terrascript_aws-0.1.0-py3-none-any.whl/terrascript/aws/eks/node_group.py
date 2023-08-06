from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class RemoteAccess(core.Schema):

    ec2_ssh_key: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_security_group_ids: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        ec2_ssh_key: Optional[Union[str, core.StringOut]] = None,
        source_security_group_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=RemoteAccess.Args(
                ec2_ssh_key=ec2_ssh_key,
                source_security_group_ids=source_security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_ssh_key: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_security_group_ids: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class LaunchTemplate(core.Schema):

    id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    version: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        version: Union[str, core.StringOut],
        id: Optional[Union[str, core.StringOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                version=version,
                id=id,
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Union[str, core.StringOut] = core.arg()


@core.schema
class Taint(core.Schema):

    effect: Union[str, core.StringOut] = core.attr(str)

    key: Union[str, core.StringOut] = core.attr(str)

    value: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        effect: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Taint.Args(
                effect=effect,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effect: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class AutoscalingGroups(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=AutoscalingGroups.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()


@core.schema
class Resources(core.Schema):

    autoscaling_groups: Union[
        List[AutoscalingGroups], core.ArrayOut[AutoscalingGroups]
    ] = core.attr(AutoscalingGroups, computed=True, kind=core.Kind.array)

    remote_access_security_group_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        autoscaling_groups: Union[List[AutoscalingGroups], core.ArrayOut[AutoscalingGroups]],
        remote_access_security_group_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Resources.Args(
                autoscaling_groups=autoscaling_groups,
                remote_access_security_group_id=remote_access_security_group_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        autoscaling_groups: Union[
            List[AutoscalingGroups], core.ArrayOut[AutoscalingGroups]
        ] = core.arg()

        remote_access_security_group_id: Union[str, core.StringOut] = core.arg()


@core.schema
class UpdateConfig(core.Schema):

    max_unavailable: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    max_unavailable_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        max_unavailable: Optional[Union[int, core.IntOut]] = None,
        max_unavailable_percentage: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=UpdateConfig.Args(
                max_unavailable=max_unavailable,
                max_unavailable_percentage=max_unavailable_percentage,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        max_unavailable: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        max_unavailable_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ScalingConfig(core.Schema):

    desired_size: Union[int, core.IntOut] = core.attr(int)

    max_size: Union[int, core.IntOut] = core.attr(int)

    min_size: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        desired_size: Union[int, core.IntOut],
        max_size: Union[int, core.IntOut],
        min_size: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ScalingConfig.Args(
                desired_size=desired_size,
                max_size=max_size,
                min_size=min_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        desired_size: Union[int, core.IntOut] = core.arg()

        max_size: Union[int, core.IntOut] = core.arg()

        min_size: Union[int, core.IntOut] = core.arg()


@core.resource(type="aws_eks_node_group", namespace="aws_eks")
class NodeGroup(core.Resource):

    ami_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    capacity_type: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    disk_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    force_update_version: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.array
    )

    labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    launch_template: Optional[LaunchTemplate] = core.attr(LaunchTemplate, default=None)

    node_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    node_group_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    node_role_arn: Union[str, core.StringOut] = core.attr(str)

    release_version: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    remote_access: Optional[RemoteAccess] = core.attr(RemoteAccess, default=None)

    resources: Union[List[Resources], core.ArrayOut[Resources]] = core.attr(
        Resources, computed=True, kind=core.Kind.array
    )

    scaling_config: ScalingConfig = core.attr(ScalingConfig)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    taint: Optional[Union[List[Taint], core.ArrayOut[Taint]]] = core.attr(
        Taint, default=None, kind=core.Kind.array
    )

    update_config: Optional[UpdateConfig] = core.attr(UpdateConfig, default=None, computed=True)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        node_role_arn: Union[str, core.StringOut],
        scaling_config: ScalingConfig,
        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        ami_type: Optional[Union[str, core.StringOut]] = None,
        capacity_type: Optional[Union[str, core.StringOut]] = None,
        disk_size: Optional[Union[int, core.IntOut]] = None,
        force_update_version: Optional[Union[bool, core.BoolOut]] = None,
        instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        launch_template: Optional[LaunchTemplate] = None,
        node_group_name: Optional[Union[str, core.StringOut]] = None,
        node_group_name_prefix: Optional[Union[str, core.StringOut]] = None,
        release_version: Optional[Union[str, core.StringOut]] = None,
        remote_access: Optional[RemoteAccess] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        taint: Optional[Union[List[Taint], core.ArrayOut[Taint]]] = None,
        update_config: Optional[UpdateConfig] = None,
        version: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=NodeGroup.Args(
                cluster_name=cluster_name,
                node_role_arn=node_role_arn,
                scaling_config=scaling_config,
                subnet_ids=subnet_ids,
                ami_type=ami_type,
                capacity_type=capacity_type,
                disk_size=disk_size,
                force_update_version=force_update_version,
                instance_types=instance_types,
                labels=labels,
                launch_template=launch_template,
                node_group_name=node_group_name,
                node_group_name_prefix=node_group_name_prefix,
                release_version=release_version,
                remote_access=remote_access,
                tags=tags,
                tags_all=tags_all,
                taint=taint,
                update_config=update_config,
                version=version,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        ami_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        capacity_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_name: Union[str, core.StringOut] = core.arg()

        disk_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        force_update_version: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_types: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        labels: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        launch_template: Optional[LaunchTemplate] = core.arg(default=None)

        node_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_group_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_role_arn: Union[str, core.StringOut] = core.arg()

        release_version: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        remote_access: Optional[RemoteAccess] = core.arg(default=None)

        scaling_config: ScalingConfig = core.arg()

        subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        taint: Optional[Union[List[Taint], core.ArrayOut[Taint]]] = core.arg(default=None)

        update_config: Optional[UpdateConfig] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)
