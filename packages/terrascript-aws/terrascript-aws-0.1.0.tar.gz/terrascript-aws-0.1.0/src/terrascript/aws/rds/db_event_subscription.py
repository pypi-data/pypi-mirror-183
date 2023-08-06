from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.resource(type="aws_db_event_subscription", namespace="aws_rds")
class DbEventSubscription(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    customer_aws_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    event_categories: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    name_prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    sns_topic: Union[str, core.StringOut] = core.attr(str)

    source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    source_type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

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
        sns_topic: Union[str, core.StringOut],
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        event_categories: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        name: Optional[Union[str, core.StringOut]] = None,
        name_prefix: Optional[Union[str, core.StringOut]] = None,
        source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        source_type: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=DbEventSubscription.Args(
                sns_topic=sns_topic,
                enabled=enabled,
                event_categories=event_categories,
                name=name,
                name_prefix=name_prefix,
                source_ids=source_ids,
                source_type=source_type,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        event_categories: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name_prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        sns_topic: Union[str, core.StringOut] = core.arg()

        source_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        source_type: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
