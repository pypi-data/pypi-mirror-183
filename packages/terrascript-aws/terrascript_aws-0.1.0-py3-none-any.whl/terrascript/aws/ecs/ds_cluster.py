from typing import List, Union

import terrascript.core as core


@core.schema
class Setting(core.Schema):

    name: Union[str, core.StringOut] = core.attr(str, computed=True)

    value: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        name: Union[str, core.StringOut],
        value: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Setting.Args(
                name=name,
                value=value,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        value: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_ecs_cluster", namespace="aws_ecs")
class DsCluster(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    pending_tasks_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    registered_container_instances_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    running_tasks_count: Union[int, core.IntOut] = core.attr(int, computed=True)

    setting: Union[List[Setting], core.ArrayOut[Setting]] = core.attr(
        Setting, computed=True, kind=core.Kind.array
    )

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsCluster.Args(
                cluster_name=cluster_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: Union[str, core.StringOut] = core.arg()
