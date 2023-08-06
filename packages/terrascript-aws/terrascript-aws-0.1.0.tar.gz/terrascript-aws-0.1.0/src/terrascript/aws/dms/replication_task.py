from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_dms_replication_task", namespace="aws_dms")
class ReplicationTask(core.Resource):

    cdc_start_position: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    cdc_start_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    migration_type: Union[str, core.StringOut] = core.attr(str)

    replication_instance_arn: Union[str, core.StringOut] = core.attr(str)

    replication_task_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    replication_task_id: Union[str, core.StringOut] = core.attr(str)

    replication_task_settings: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    source_endpoint_arn: Union[str, core.StringOut] = core.attr(str)

    start_replication_task: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    table_mappings: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    target_endpoint_arn: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        resource_name: str,
        *,
        migration_type: Union[str, core.StringOut],
        replication_instance_arn: Union[str, core.StringOut],
        replication_task_id: Union[str, core.StringOut],
        source_endpoint_arn: Union[str, core.StringOut],
        table_mappings: Union[str, core.StringOut],
        target_endpoint_arn: Union[str, core.StringOut],
        cdc_start_position: Optional[Union[str, core.StringOut]] = None,
        cdc_start_time: Optional[Union[str, core.StringOut]] = None,
        replication_task_settings: Optional[Union[str, core.StringOut]] = None,
        start_replication_task: Optional[Union[bool, core.BoolOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ReplicationTask.Args(
                migration_type=migration_type,
                replication_instance_arn=replication_instance_arn,
                replication_task_id=replication_task_id,
                source_endpoint_arn=source_endpoint_arn,
                table_mappings=table_mappings,
                target_endpoint_arn=target_endpoint_arn,
                cdc_start_position=cdc_start_position,
                cdc_start_time=cdc_start_time,
                replication_task_settings=replication_task_settings,
                start_replication_task=start_replication_task,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        cdc_start_position: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        cdc_start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        migration_type: Union[str, core.StringOut] = core.arg()

        replication_instance_arn: Union[str, core.StringOut] = core.arg()

        replication_task_id: Union[str, core.StringOut] = core.arg()

        replication_task_settings: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        source_endpoint_arn: Union[str, core.StringOut] = core.arg()

        start_replication_task: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        table_mappings: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        target_endpoint_arn: Union[str, core.StringOut] = core.arg()
