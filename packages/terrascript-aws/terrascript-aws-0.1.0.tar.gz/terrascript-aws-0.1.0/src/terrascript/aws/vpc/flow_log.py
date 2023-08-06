from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class DestinationOptions(core.Schema):

    file_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hive_compatible_partitions: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    per_hour_partition: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        file_format: Optional[Union[str, core.StringOut]] = None,
        hive_compatible_partitions: Optional[Union[bool, core.BoolOut]] = None,
        per_hour_partition: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=DestinationOptions.Args(
                file_format=file_format,
                hive_compatible_partitions=hive_compatible_partitions,
                per_hour_partition=per_hour_partition,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        file_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        hive_compatible_partitions: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        per_hour_partition: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.resource(type="aws_flow_log", namespace="aws_vpc")
class FlowLog(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    destination_options: Optional[DestinationOptions] = core.attr(DestinationOptions, default=None)

    eni_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_role_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    log_destination: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    log_destination_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    log_format: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    log_group_name: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    max_aggregation_interval: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    subnet_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    traffic_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    transit_gateway_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    vpc_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        destination_options: Optional[DestinationOptions] = None,
        eni_id: Optional[Union[str, core.StringOut]] = None,
        iam_role_arn: Optional[Union[str, core.StringOut]] = None,
        log_destination: Optional[Union[str, core.StringOut]] = None,
        log_destination_type: Optional[Union[str, core.StringOut]] = None,
        log_format: Optional[Union[str, core.StringOut]] = None,
        log_group_name: Optional[Union[str, core.StringOut]] = None,
        max_aggregation_interval: Optional[Union[int, core.IntOut]] = None,
        subnet_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        traffic_type: Optional[Union[str, core.StringOut]] = None,
        transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = None,
        transit_gateway_id: Optional[Union[str, core.StringOut]] = None,
        vpc_id: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=FlowLog.Args(
                destination_options=destination_options,
                eni_id=eni_id,
                iam_role_arn=iam_role_arn,
                log_destination=log_destination,
                log_destination_type=log_destination_type,
                log_format=log_format,
                log_group_name=log_group_name,
                max_aggregation_interval=max_aggregation_interval,
                subnet_id=subnet_id,
                tags=tags,
                tags_all=tags_all,
                traffic_type=traffic_type,
                transit_gateway_attachment_id=transit_gateway_attachment_id,
                transit_gateway_id=transit_gateway_id,
                vpc_id=vpc_id,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destination_options: Optional[DestinationOptions] = core.arg(default=None)

        eni_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_destination: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_destination_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_format: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        log_group_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        max_aggregation_interval: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        subnet_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        traffic_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_gateway_attachment_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        transit_gateway_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        vpc_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)
