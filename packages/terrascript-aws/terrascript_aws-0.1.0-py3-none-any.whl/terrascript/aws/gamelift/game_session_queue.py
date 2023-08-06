from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PlayerLatencyPolicy(core.Schema):

    maximum_individual_player_latency_milliseconds: Union[int, core.IntOut] = core.attr(int)

    policy_duration_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        maximum_individual_player_latency_milliseconds: Union[int, core.IntOut],
        policy_duration_seconds: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=PlayerLatencyPolicy.Args(
                maximum_individual_player_latency_milliseconds=maximum_individual_player_latency_milliseconds,
                policy_duration_seconds=policy_duration_seconds,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        maximum_individual_player_latency_milliseconds: Union[int, core.IntOut] = core.arg()

        policy_duration_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.resource(type="aws_gamelift_game_session_queue", namespace="aws_gamelift")
class GameSessionQueue(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    notification_target: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    player_latency_policy: Optional[
        Union[List[PlayerLatencyPolicy], core.ArrayOut[PlayerLatencyPolicy]]
    ] = core.attr(PlayerLatencyPolicy, default=None, kind=core.Kind.array)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        resource_name: str,
        *,
        name: Union[str, core.StringOut],
        destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        notification_target: Optional[Union[str, core.StringOut]] = None,
        player_latency_policy: Optional[
            Union[List[PlayerLatencyPolicy], core.ArrayOut[PlayerLatencyPolicy]]
        ] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        timeout_in_seconds: Optional[Union[int, core.IntOut]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=GameSessionQueue.Args(
                name=name,
                destinations=destinations,
                notification_target=notification_target,
                player_latency_policy=player_latency_policy,
                tags=tags,
                tags_all=tags_all,
                timeout_in_seconds=timeout_in_seconds,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        destinations: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Union[str, core.StringOut] = core.arg()

        notification_target: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        player_latency_policy: Optional[
            Union[List[PlayerLatencyPolicy], core.ArrayOut[PlayerLatencyPolicy]]
        ] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )

        timeout_in_seconds: Optional[Union[int, core.IntOut]] = core.arg(default=None)
