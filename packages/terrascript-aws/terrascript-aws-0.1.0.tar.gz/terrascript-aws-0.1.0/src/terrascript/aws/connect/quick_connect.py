from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class QueueConfig(core.Schema):

    contact_flow_id: Union[str, core.StringOut] = core.attr(str)

    queue_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        contact_flow_id: Union[str, core.StringOut],
        queue_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=QueueConfig.Args(
                contact_flow_id=contact_flow_id,
                queue_id=queue_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_id: Union[str, core.StringOut] = core.arg()

        queue_id: Union[str, core.StringOut] = core.arg()


@core.schema
class UserConfig(core.Schema):

    contact_flow_id: Union[str, core.StringOut] = core.attr(str)

    user_id: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        contact_flow_id: Union[str, core.StringOut],
        user_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=UserConfig.Args(
                contact_flow_id=contact_flow_id,
                user_id=user_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        contact_flow_id: Union[str, core.StringOut] = core.arg()

        user_id: Union[str, core.StringOut] = core.arg()


@core.schema
class PhoneConfig(core.Schema):

    phone_number: Union[str, core.StringOut] = core.attr(str)

    def __init__(
        self,
        *,
        phone_number: Union[str, core.StringOut],
    ):
        super().__init__(
            args=PhoneConfig.Args(
                phone_number=phone_number,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_number: Union[str, core.StringOut] = core.arg()


@core.schema
class QuickConnectConfig(core.Schema):

    phone_config: Optional[Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]]] = core.attr(
        PhoneConfig, default=None, kind=core.Kind.array
    )

    queue_config: Optional[Union[List[QueueConfig], core.ArrayOut[QueueConfig]]] = core.attr(
        QueueConfig, default=None, kind=core.Kind.array
    )

    quick_connect_type: Union[str, core.StringOut] = core.attr(str)

    user_config: Optional[Union[List[UserConfig], core.ArrayOut[UserConfig]]] = core.attr(
        UserConfig, default=None, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        quick_connect_type: Union[str, core.StringOut],
        phone_config: Optional[Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]]] = None,
        queue_config: Optional[Union[List[QueueConfig], core.ArrayOut[QueueConfig]]] = None,
        user_config: Optional[Union[List[UserConfig], core.ArrayOut[UserConfig]]] = None,
    ):
        super().__init__(
            args=QuickConnectConfig.Args(
                quick_connect_type=quick_connect_type,
                phone_config=phone_config,
                queue_config=queue_config,
                user_config=user_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_config: Optional[Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]]] = core.arg(
            default=None
        )

        queue_config: Optional[Union[List[QueueConfig], core.ArrayOut[QueueConfig]]] = core.arg(
            default=None
        )

        quick_connect_type: Union[str, core.StringOut] = core.arg()

        user_config: Optional[Union[List[UserConfig], core.ArrayOut[UserConfig]]] = core.arg(
            default=None
        )


@core.resource(type="aws_connect_quick_connect", namespace="aws_connect")
class QuickConnect(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    name: Union[str, core.StringOut] = core.attr(str)

    quick_connect_config: QuickConnectConfig = core.attr(QuickConnectConfig)

    quick_connect_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        quick_connect_config: QuickConnectConfig,
        description: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=QuickConnect.Args(
                instance_id=instance_id,
                name=name,
                quick_connect_config=quick_connect_config,
                description=description,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        description: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        instance_id: Union[str, core.StringOut] = core.arg()

        name: Union[str, core.StringOut] = core.arg()

        quick_connect_config: QuickConnectConfig = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
