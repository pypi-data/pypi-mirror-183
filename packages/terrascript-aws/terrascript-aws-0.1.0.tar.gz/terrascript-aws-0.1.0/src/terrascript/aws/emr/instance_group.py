from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class EbsConfig(core.Schema):

    iops: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    size: Union[int, core.IntOut] = core.attr(int)

    type: Union[str, core.StringOut] = core.attr(str)

    volumes_per_instance: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        size: Union[int, core.IntOut],
        type: Union[str, core.StringOut],
        iops: Optional[Union[int, core.IntOut]] = None,
        volumes_per_instance: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EbsConfig.Args(
                size=size,
                type=type,
                iops=iops,
                volumes_per_instance=volumes_per_instance,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iops: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        size: Union[int, core.IntOut] = core.arg()

        type: Union[str, core.StringOut] = core.arg()

        volumes_per_instance: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_emr_instance_group", namespace="aws_emr")
class InstanceGroup(core.Resource):

    autoscaling_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    bid_price: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    cluster_id: Union[str, core.StringOut] = core.attr(str)

    configurations_json: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = core.attr(
        EbsConfig, default=None, computed=True, kind=core.Kind.array
    )

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_count: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    running_instance_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        cluster_id: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        autoscaling_policy: Optional[Union[str, core.StringOut]] = None,
        bid_price: Optional[Union[str, core.StringOut]] = None,
        configurations_json: Optional[Union[str, core.StringOut]] = None,
        ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = None,
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        instance_count: Optional[Union[int, core.IntOut]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=InstanceGroup.Args(
                cluster_id=cluster_id,
                instance_type=instance_type,
                autoscaling_policy=autoscaling_policy,
                bid_price=bid_price,
                configurations_json=configurations_json,
                ebs_config=ebs_config,
                ebs_optimized=ebs_optimized,
                instance_count=instance_count,
                name=name,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        autoscaling_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        bid_price: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cluster_id: Union[str, core.StringOut] = core.arg()

        configurations_json: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ebs_config: Optional[Union[List[EbsConfig], core.ArrayOut[EbsConfig]]] = core.arg(
            default=None
        )

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_count: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)
