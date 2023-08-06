from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Taints(core.Schema):

    effect: Union[str, core.StringOut] = core.attr(str, computed=True)

    key: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        effect: Union[str, core.StringOut],
        key: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Taints.Args(
                effect=effect,
                key=key,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        effect: Union[str, core.StringOut] = core.arg()

        key: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.schema
class RemoteAccess(core.Schema):

    ec2_ssh_key: Union[str, core.StringOut] = core.attr(str, computed=True)

    source_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        ec2_ssh_key: Union[str, core.StringOut],
        source_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
    ):
        super().__init__(
            args=RemoteAccess.Args(
                ec2_ssh_key=ec2_ssh_key,
                source_security_group_ids=source_security_group_ids,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ec2_ssh_key: Union[str, core.StringOut] = core.arg()

        source_security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()


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
class ScalingConfig(core.Schema):

    desired_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    max_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    min_size: Union[int, core.IntOut] = core.attr(int, computed=True)

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


@core.data(type="aws_eks_node_group", namespace="aws_eks")
class DsNodeGroup(core.Data):

    ami_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    disk_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_types: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    labels: Union[Dict[str, str], core.MapOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.map
    )

    node_group_name: Union[str, core.StringOut] = core.attr(str)

    node_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    release_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    remote_access: Union[List[RemoteAccess], core.ArrayOut[RemoteAccess]] = core.attr(
        RemoteAccess, computed=True, kind=core.Kind.array
    )

    resources: Union[List[Resources], core.ArrayOut[Resources]] = core.attr(
        Resources, computed=True, kind=core.Kind.array
    )

    scaling_config: Union[List[ScalingConfig], core.ArrayOut[ScalingConfig]] = core.attr(
        ScalingConfig, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    subnet_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    taints: Union[List[Taints], core.ArrayOut[Taints]] = core.attr(
        Taints, computed=True, kind=core.Kind.array
    )

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        node_group_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsNodeGroup.Args(
                cluster_name=cluster_name,
                node_group_name=node_group_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: Union[str, core.StringOut] = core.arg()

        node_group_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
