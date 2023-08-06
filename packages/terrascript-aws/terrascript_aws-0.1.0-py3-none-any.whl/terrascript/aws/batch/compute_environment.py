from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class LaunchTemplate(core.Schema):

    launch_template_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    launch_template_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    version: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        launch_template_id: Optional[Union[str, core.StringOut]] = None,
        launch_template_name: Optional[Union[str, core.StringOut]] = None,
        version: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=LaunchTemplate.Args(
                launch_template_id=launch_template_id,
                launch_template_name=launch_template_name,
                version=version,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        launch_template_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        launch_template_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        version: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Ec2Configuration(core.Schema):

    image_id_override: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    image_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        image_id_override: Optional[Union[str, core.StringOut]] = None,
        image_type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Ec2Configuration.Args(
                image_id_override=image_id_override,
                image_type=image_type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        image_id_override: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ComputeResources(core.Schema):

    allocation_strategy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bid_percentage: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    desired_vcpus: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    ec2_configuration: Optional[Ec2Configuration] = core.attr(
        Ec2Configuration, default=None, computed=True
    )

    ec2_key_pair: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    image_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_type: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    launch_template: Optional[LaunchTemplate] = core.attr(LaunchTemplate, default=None)

    max_vcpus: Union[int, core.IntOut] = core.attr(int)

    min_vcpus: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    spot_iam_fleet_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        max_vcpus: Union[int, core.IntOut],
        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]],
        subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        type: Union[str, core.StringOut],
        allocation_strategy: Optional[Union[str, core.StringOut]] = None,
        bid_percentage: Optional[Union[int, core.IntOut]] = None,
        desired_vcpus: Optional[Union[int, core.IntOut]] = None,
        ec2_configuration: Optional[Ec2Configuration] = None,
        ec2_key_pair: Optional[Union[str, core.StringOut]] = None,
        image_id: Optional[Union[str, core.StringOut]] = None,
        instance_role: Optional[Union[str, core.StringOut]] = None,
        instance_type: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        launch_template: Optional[LaunchTemplate] = None,
        min_vcpus: Optional[Union[int, core.IntOut]] = None,
        spot_iam_fleet_role: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            args=ComputeResources.Args(
                max_vcpus=max_vcpus,
                security_group_ids=security_group_ids,
                subnets=subnets,
                type=type,
                allocation_strategy=allocation_strategy,
                bid_percentage=bid_percentage,
                desired_vcpus=desired_vcpus,
                ec2_configuration=ec2_configuration,
                ec2_key_pair=ec2_key_pair,
                image_id=image_id,
                instance_role=instance_role,
                instance_type=instance_type,
                launch_template=launch_template,
                min_vcpus=min_vcpus,
                spot_iam_fleet_role=spot_iam_fleet_role,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        allocation_strategy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bid_percentage: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        desired_vcpus: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        ec2_configuration: Optional[Ec2Configuration] = core.arg(default=None)

        ec2_key_pair: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        image_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_type: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        launch_template: Optional[LaunchTemplate] = core.arg(default=None)

        max_vcpus: Union[int, core.IntOut] = core.arg()

        min_vcpus: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        security_group_ids: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        spot_iam_fleet_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        type: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_batch_compute_environment", namespace="aws_batch")
class ComputeEnvironment(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compute_environment_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    compute_environment_name_prefix: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    compute_resources: Optional[ComputeResources] = core.attr(ComputeResources, default=None)

    ecs_cluster_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_role: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    state: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    type: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        type: Union[str, core.StringOut],
        compute_environment_name: Optional[Union[str, core.StringOut]] = None,
        compute_environment_name_prefix: Optional[Union[str, core.StringOut]] = None,
        compute_resources: Optional[ComputeResources] = None,
        service_role: Optional[Union[str, core.StringOut]] = None,
        state: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ComputeEnvironment.Args(
                type=type,
                compute_environment_name=compute_environment_name,
                compute_environment_name_prefix=compute_environment_name_prefix,
                compute_resources=compute_resources,
                service_role=service_role,
                state=state,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_environment_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        compute_environment_name_prefix: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        compute_resources: Optional[ComputeResources] = core.arg(default=None)

        service_role: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        type: Union[str, core.StringOut] = core.arg()
