from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_ec2_capacity_reservation", namespace="aws_ec2")
class CapacityReservation(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    availability_zone: Union[str, core.StringOut] = core.attr(str)

    ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    end_date: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    end_date_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    ephemeral_storage: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_count: Union[int, core.IntOut] = core.attr(int)

    instance_match_criteria: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    instance_platform: Union[str, core.StringOut] = core.attr(str)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    outpost_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    owner_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    tenancy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        availability_zone: Union[str, core.StringOut],
        instance_count: Union[int, core.IntOut],
        instance_platform: Union[str, core.StringOut],
        instance_type: Union[str, core.StringOut],
        ebs_optimized: Optional[Union[bool, core.BoolOut]] = None,
        end_date: Optional[Union[str, core.StringOut]] = None,
        end_date_type: Optional[Union[str, core.StringOut]] = None,
        ephemeral_storage: Optional[Union[bool, core.BoolOut]] = None,
        instance_match_criteria: Optional[Union[str, core.StringOut]] = None,
        outpost_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tenancy: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=CapacityReservation.Args(
                availability_zone=availability_zone,
                instance_count=instance_count,
                instance_platform=instance_platform,
                instance_type=instance_type,
                ebs_optimized=ebs_optimized,
                end_date=end_date,
                end_date_type=end_date_type,
                ephemeral_storage=ephemeral_storage,
                instance_match_criteria=instance_match_criteria,
                outpost_arn=outpost_arn,
                tags=tags,
                tags_all=tags_all,
                tenancy=tenancy,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        availability_zone: Union[str, core.StringOut] = core.arg()

        ebs_optimized: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        end_date: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        end_date_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        ephemeral_storage: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        instance_count: Union[int, core.IntOut] = core.arg()

        instance_match_criteria: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_platform: Union[str, core.StringOut] = core.arg()

        instance_type: Union[str, core.StringOut] = core.arg()

        outpost_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        tenancy: Optional[Union[str, core.StringOut]] = core.arg(default=None)
