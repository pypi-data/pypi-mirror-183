from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class Notification(core.Schema):

    events: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(str, kind=core.Kind.array)

    sns_topic: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        events: Union[List[str], core.ArrayOut[core.StringOut]],
        sns_topic: Union[str, core.StringOut],
    ):
        super().__init__(
            args=Notification.Args(
                events=events,
                sns_topic=sns_topic,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        events: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        sns_topic: Union[str, core.StringOut] = core.arg()


@core.resource(type="aws_glacier_vault", namespace="aws_glacier")
class Vault(core.Resource):

    access_policy: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    location: Union[str, core.StringOut] = core.attr(str, computed=True)

    name: Union[str, core.StringOut] = core.attr(str)

    notification: Optional[Notification] = core.attr(Notification, default=None)

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
        name: Union[str, core.StringOut],
        access_policy: Optional[Union[str, core.StringOut]] = None,
        notification: Optional[Notification] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Vault.Args(
                name=name,
                access_policy=access_policy,
                notification=notification,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        access_policy: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        notification: Optional[Notification] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
