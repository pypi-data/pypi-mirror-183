from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class PhoneConfig(core.Schema):

    phone_number: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class QueueConfig(core.Schema):

    contact_flow_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    queue_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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

    contact_flow_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_id: Union[str, core.StringOut] = core.attr(str, computed=True)

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
class QuickConnectConfig(core.Schema):

    phone_config: Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]] = core.attr(
        PhoneConfig, computed=True, kind=core.Kind.array
    )

    queue_config: Union[List[QueueConfig], core.ArrayOut[QueueConfig]] = core.attr(
        QueueConfig, computed=True, kind=core.Kind.array
    )

    quick_connect_type: Union[str, core.StringOut] = core.attr(str, computed=True)

    user_config: Union[List[UserConfig], core.ArrayOut[UserConfig]] = core.attr(
        UserConfig, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        *,
        phone_config: Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]],
        queue_config: Union[List[QueueConfig], core.ArrayOut[QueueConfig]],
        quick_connect_type: Union[str, core.StringOut],
        user_config: Union[List[UserConfig], core.ArrayOut[UserConfig]],
    ):
        super().__init__(
            args=QuickConnectConfig.Args(
                phone_config=phone_config,
                queue_config=queue_config,
                quick_connect_type=quick_connect_type,
                user_config=user_config,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        phone_config: Union[List[PhoneConfig], core.ArrayOut[PhoneConfig]] = core.arg()

        queue_config: Union[List[QueueConfig], core.ArrayOut[QueueConfig]] = core.arg()

        quick_connect_type: Union[str, core.StringOut] = core.arg()

        user_config: Union[List[UserConfig], core.ArrayOut[UserConfig]] = core.arg()


@core.data(type="aws_connect_quick_connect", namespace="aws_connect")
class DsQuickConnect(core.Data):
    """
    The Amazon Resource Name (ARN) of the Quick Connect.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Specifies the description of the Quick Connect.
    """
    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Quick Connect separated
    by a colon (`:`).
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: Union[str, core.StringOut] = core.attr(str)

    """
    (Optional) Returns information on a specific Quick Connect by name
    """
    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    A block that defines the configuration information for the Quick Connect: `quick_connect_type` and o
    ne of `phone_config`, `queue_config`, `user_config` . The Quick Connect Config block is documented b
    elow.
    """
    quick_connect_config: Union[
        List[QuickConnectConfig], core.ArrayOut[QuickConnectConfig]
    ] = core.attr(QuickConnectConfig, computed=True, kind=core.Kind.array)

    """
    (Optional) Returns information on a specific Quick Connect by Quick Connect id
    """
    quick_connect_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    """
    A map of tags to assign to the Quick Connect.
    """
    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    def __init__(
        self,
        data_name: str,
        *,
        instance_id: Union[str, core.StringOut],
        name: Optional[Union[str, core.StringOut]] = None,
        quick_connect_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQuickConnect.Args(
                instance_id=instance_id,
                name=name,
                quick_connect_id=quick_connect_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        quick_connect_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
