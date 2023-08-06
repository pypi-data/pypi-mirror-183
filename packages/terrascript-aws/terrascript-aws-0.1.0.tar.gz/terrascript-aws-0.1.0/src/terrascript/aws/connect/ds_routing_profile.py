from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class QueueConfigs(core.Schema):

    channel: Union[str, core.StringOut] = core.attr(str, computed=True)

    delay: Union[int, core.IntOut] = core.attr(int, computed=True)

    priority: Union[int, core.IntOut] = core.attr(int, computed=True)

    queue_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    queue_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    queue_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        channel: Union[str, core.StringOut],
        delay: Union[int, core.IntOut],
        priority: Union[int, core.IntOut],
        queue_arn: Union[str, core.StringOut],
        queue_id: Union[str, core.StringOut],
        queue_name: Union[str, core.StringOut],
    ):
        super().__init__(
            args=QueueConfigs.Args(
                channel=channel,
                delay=delay,
                priority=priority,
                queue_arn=queue_arn,
                queue_id=queue_id,
                queue_name=queue_name,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel: Union[str, core.StringOut] = core.arg()

        delay: Union[int, core.IntOut] = core.arg()

        priority: Union[int, core.IntOut] = core.arg()

        queue_arn: Union[str, core.StringOut] = core.arg()

        queue_id: Union[str, core.StringOut] = core.arg()

        queue_name: Union[str, core.StringOut] = core.arg()


@core.schema
class MediaConcurrencies(core.Schema):

    channel: Union[str, core.StringOut] = core.attr(str, computed=True)

    concurrency: Union[int, core.IntOut] = core.attr(int, computed=True)

    def __init__(
        self,
        *,
        channel: Union[str, core.StringOut],
        concurrency: Union[int, core.IntOut],
    ):
        super().__init__(
            args=MediaConcurrencies.Args(
                channel=channel,
                concurrency=concurrency,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        channel: Union[str, core.StringOut] = core.arg()

        concurrency: Union[int, core.IntOut] = core.arg()


@core.data(type="aws_connect_routing_profile", namespace="aws_connect")
class DsRoutingProfile(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_outbound_queue_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    media_concurrencies: Union[
        List[MediaConcurrencies], core.ArrayOut[MediaConcurrencies]
    ] = core.attr(MediaConcurrencies, computed=True, kind=core.Kind.array)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    queue_configs: Union[List[QueueConfigs], core.ArrayOut[QueueConfigs]] = core.attr(
        QueueConfigs, computed=True, kind=core.Kind.array
    )

    routing_profile_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        routing_profile_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsRoutingProfile.Args(
                instance_id=instance_id,
                name=name,
                routing_profile_id=routing_profile_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        routing_profile_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
