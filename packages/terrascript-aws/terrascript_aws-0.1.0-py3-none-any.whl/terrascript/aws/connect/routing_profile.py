from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class QueueConfigs(core.Schema):

    channel: Union[str, core.StringOut] = core.attr(str)

    delay: Union[int, core.IntOut] = core.attr(int)

    priority: Union[int, core.IntOut] = core.attr(int)

    queue_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    queue_id: Union[str, core.StringOut] = core.attr(str)

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
class QueueConfigsAssociated(core.Schema):

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
            args=QueueConfigsAssociated.Args(
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

    channel: Union[str, core.StringOut] = core.attr(str)

    concurrency: Union[int, core.IntOut] = core.attr(int)

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


@core.resource(type="aws_connect_routing_profile", namespace="aws_connect")
class RoutingProfile(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    default_outbound_queue_id: Union[str, core.StringOut] = core.attr(str)

    description: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    media_concurrencies: Union[
        List[MediaConcurrencies], core.ArrayOut[MediaConcurrencies]
    ] = core.attr(MediaConcurrencies, kind=core.Kind.array)

    name: Union[str, core.StringOut] = core.attr(str)

    queue_configs: Optional[Union[List[QueueConfigs], core.ArrayOut[QueueConfigs]]] = core.attr(
        QueueConfigs, default=None, kind=core.Kind.array
    )

    queue_configs_associated: Union[
        List[QueueConfigsAssociated], core.ArrayOut[QueueConfigsAssociated]
    ] = core.attr(QueueConfigsAssociated, computed=True, kind=core.Kind.array)

    routing_profile_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        default_outbound_queue_id: Union[str, core.StringOut],
        description: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        media_concurrencies: Union[List[MediaConcurrencies], core.ArrayOut[MediaConcurrencies]],
        name: Union[str, core.StringOut],
        queue_configs: Optional[Union[List[QueueConfigs], core.ArrayOut[QueueConfigs]]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=RoutingProfile.Args(
                default_outbound_queue_id=default_outbound_queue_id,
                description=description,
                instance_id=instance_id,
                media_concurrencies=media_concurrencies,
                name=name,
                queue_configs=queue_configs,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        default_outbound_queue_id: Union[str, core.StringOut] = core.arg()

        description: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        media_concurrencies: Union[
            List[MediaConcurrencies], core.ArrayOut[MediaConcurrencies]
        ] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        queue_configs: Optional[Union[List[QueueConfigs], core.ArrayOut[QueueConfigs]]] = core.arg(
            default=None
        )

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
