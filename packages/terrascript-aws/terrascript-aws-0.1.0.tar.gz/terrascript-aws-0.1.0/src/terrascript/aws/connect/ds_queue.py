from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OutboundCallerConfig(core.Schema):

    outbound_caller_id_name: Union[str, core.StringOut] = core.attr(str, computed=True)

    outbound_caller_id_number_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    outbound_flow_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        outbound_caller_id_name: Union[str, core.StringOut],
        outbound_caller_id_number_id: Union[str, core.StringOut],
        outbound_flow_id: Union[str, core.StringOut],
    ):
        super().__init__(
            args=OutboundCallerConfig.Args(
                outbound_caller_id_name=outbound_caller_id_name,
                outbound_caller_id_number_id=outbound_caller_id_number_id,
                outbound_flow_id=outbound_flow_id,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        outbound_caller_id_name: Union[str, core.StringOut] = core.arg()

        outbound_caller_id_number_id: Union[str, core.StringOut] = core.arg()

        outbound_flow_id: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_connect_queue", namespace="aws_connect")
class DsQueue(core.Data):
    """
    The Amazon Resource Name (ARN) of the Queue.
    """

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Specifies the description of the Queue.
    """
    description: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    Specifies the identifier of the Hours of Operation.
    """
    hours_of_operation_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    The identifier of the hosting Amazon Connect Instance and identifier of the Queue separated by a col
    on (`:`).
    """
    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    (Required) Reference to the hosting Amazon Connect Instance
    """
    instance_id: Union[str, core.StringOut] = core.attr(str)

    """
    Specifies the maximum number of contacts that can be in the queue before it is considered full. Mini
    mum value of 0.
    """
    max_contacts: Union[int, core.IntOut] = core.attr(int, computed=True)

    """
    (Optional) Returns information on a specific Queue by name
    """
    name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    A block that defines the outbound caller ID name, number, and outbound whisper flow. The Outbound Ca
    ller Config block is documented below.
    """
    outbound_caller_config: Union[
        List[OutboundCallerConfig], core.ArrayOut[OutboundCallerConfig]
    ] = core.attr(OutboundCallerConfig, computed=True, kind=core.Kind.array)

    """
    (Optional) Returns information on a specific Queue by Queue id
    """
    queue_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    """
    Specifies the description of the Queue. Values are `ENABLED` or `DISABLED`.
    """
    status: Union[str, core.StringOut] = core.attr(str, computed=True)

    """
    A map of tags assigned to the Queue.
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
        queue_id: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsQueue.Args(
                instance_id=instance_id,
                name=name,
                queue_id=queue_id,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        instance_id: Union[str, core.StringOut] = core.arg()

        name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        queue_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
