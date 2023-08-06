from typing import List, Union

import terrascript.core as core


@core.schema
class LaunchTemplate(core.Schema):

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    version: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        version: Union[str, core.StringOut],
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                id=id,
                name=name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        version: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_autoscaling_group", namespace="aws_autoscaling")
class DsGroup(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zones: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    default_cooldown: Union[int, core.IntOut] = core.attr(int, computed=True)

    desired_capacity: Union[int, core.IntOut] = core.attr(int, computed=True)

    enabled_metrics: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    health_check_grace_period: Union[int, core.IntOut] = core.attr(int, computed=True)

    health_check_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_configuration: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_template: Union[List[LaunchTemplate], core.ArrayOut[LaunchTemplate]] = core.attr(
        LaunchTemplate, computed=True, kind=core.Kind.array
    )

    load_balancers: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    max_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    min_size: Union[int, core.IntOut] = core.attr(int, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    new_instances_protected_from_scale_in: Union[bool, core.BoolOut] = core.attr(
        bool, computed=True
    )

    placement_group: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_linked_role_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    target_group_arns: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    termination_policies: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    vpc_zone_identifier: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsGroup.Args(
                name=name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()
