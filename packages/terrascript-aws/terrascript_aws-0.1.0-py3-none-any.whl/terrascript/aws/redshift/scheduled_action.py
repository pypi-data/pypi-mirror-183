from typing import List, Optional, Union

import terrascript.core as core


@core.schema
class ResizeCluster(core.Schema):

    classic: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    cluster_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    node_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    number_of_nodes: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        cluster_identifier: Union[str, core.StringOut],
        classic: Optional[Union[bool, core.BoolOut]] = None,
        cluster_type: Optional[Union[str, core.StringOut]] = None,
        node_type: Optional[Union[str, core.StringOut]] = None,
        number_of_nodes: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ResizeCluster.Args(
                cluster_identifier=cluster_identifier,
                classic=classic,
                cluster_type=cluster_type,
                node_type=node_type,
                number_of_nodes=number_of_nodes,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        classic: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        cluster_identifier: Union[str, core.StringOut] = core.arg()

        cluster_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        node_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        number_of_nodes: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class ResumeCluster(core.Schema):

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cluster_identifier: Union[str, core.StringOut],
    ):
        super().__init__(
            args=ResumeCluster.Args(
                cluster_identifier=cluster_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: Union[str, core.StringOut] = core.arg()


@core.schema
class PauseCluster(core.Schema):

    cluster_identifier: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        cluster_identifier: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PauseCluster.Args(
                cluster_identifier=cluster_identifier,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_identifier: Union[str, core.StringOut] = core.arg()


@core.schema
class TargetAction(core.Schema):

    pause_cluster: Optional[PauseCluster] = core.attr(PauseCluster, default=None)

    resize_cluster: Optional[ResizeCluster] = core.attr(ResizeCluster, default=None)

    resume_cluster: Optional[ResumeCluster] = core.attr(ResumeCluster, default=None)

    def __init__(
        self,
        *,
        pause_cluster: Optional[PauseCluster] = None,
        resize_cluster: Optional[ResizeCluster] = None,
        resume_cluster: Optional[ResumeCluster] = None,
    ):
        super().__init__(
            args=TargetAction.Args(
                pause_cluster=pause_cluster,
                resize_cluster=resize_cluster,
                resume_cluster=resume_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        pause_cluster: Optional[PauseCluster] = core.arg(default=None)

        resize_cluster: Optional[ResizeCluster] = core.arg(default=None)

        resume_cluster: Optional[ResumeCluster] = core.arg(default=None)


@core.resource(type="aws_redshift_scheduled_action", namespace="aws_redshift")
class ScheduledAction(core.Resource):

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enable: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    end_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    iam_role: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    schedule: Union[str, core.StringOut] = core.attr(str)

    start_time: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    target_action: TargetAction = core.attr(TargetAction)

    def __init__(
        self,
        resource_name: str,
        *,
        iam_role: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        schedule: Union[str, core.StringOut],
        target_action: TargetAction,
        description: Optional[Union[str, core.StringOut]] = None,
        enable: Optional[Union[bool, core.BoolOut]] = None,
        end_time: Optional[Union[str, core.StringOut]] = None,
        start_time: Optional[Union[str, core.StringOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=ScheduledAction.Args(
                iam_role=iam_role,
                name=name,
                schedule=schedule,
                target_action=target_action,
                description=description,
                enable=enable,
                end_time=end_time,
                start_time=start_time,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enable: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        end_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        iam_role: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        schedule: Union[str, core.StringOut] = core.arg()

        start_time: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        target_action: TargetAction = core.arg()
