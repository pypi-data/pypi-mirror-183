from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class ComputeEnvironmentOrder(core.Schema):

    compute_environment: Union[str, core.StringOut] = core.attr(str, computed=True)

    order: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        compute_environment: Union[str, core.StringOut],
        order: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ComputeEnvironmentOrder.Args(
                compute_environment=compute_environment,
                order=order,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        compute_environment: Union[str, core.StringOut] = core.arg()

        order: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_batch_job_queue", namespace="aws_batch")
class DsJobQueue(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compute_environment_order: Union[
        List[ComputeEnvironmentOrder], core.ArrayOut[ComputeEnvironmentOrder]
    ] = core.attr(ComputeEnvironmentOrder, computed=True, kind=core.Kind.array)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    priority: Union[int, core.IntOut] = core.attr(int, computed=True)

    scheduling_policy_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    state: Union[str, core.StringOut] = core.attr(str, computed=True)

    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    status_reason: Union[str, core.StringOut] = core.attr(str, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsJobQueue.Args(
                name=name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
