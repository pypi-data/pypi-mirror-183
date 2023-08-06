from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_batch_job_queue", namespace="aws_batch")
class JobQueue(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    compute_environments: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    priority: Union[int, core.IntOut] = core.attr(int)

    scheduling_policy_arn: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    state: Union[str, core.StringOut] = core.attr(str)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        resource_name: str,
        *,
        compute_environments: Union[List[str], core.ArrayOut[core.StringOut]],
        name: Union[str, core.StringOut],
        priority: Union[int, core.IntOut],
        state: Union[str, core.StringOut],
        scheduling_policy_arn: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=JobQueue.Args(
                compute_environments=compute_environments,
                name=name,
                priority=priority,
                state=state,
                scheduling_policy_arn=scheduling_policy_arn,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        compute_environments: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        scheduling_policy_arn: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        state: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
