from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_ecs_service", namespace="aws_ecs")
class DsService(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_arn: Union[str, core.StringOut] = core.attr(str)

    desired_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    launch_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    scheduling_strategy: Union[str, core.StringOut] = core.attr(str, computed=True)

    service_name: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    task_definition: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_arn: Union[str, core.StringOut],
        service_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsService.Args(
                cluster_arn=cluster_arn,
                service_name=service_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_arn: Union[str, core.StringOut] = core.arg()

        service_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
