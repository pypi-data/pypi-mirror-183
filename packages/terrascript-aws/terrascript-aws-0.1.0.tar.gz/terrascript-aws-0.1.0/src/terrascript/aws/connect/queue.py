from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class OutboundCallerConfig(core.Schema):

    outbound_caller_id_name: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    outbound_caller_id_number_id: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None
    )

    outbound_flow_id: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        outbound_caller_id_name: Optional[Union[str, core.StringOut]] = None,
        outbound_caller_id_number_id: Optional[Union[str, core.StringOut]] = None,
        outbound_flow_id: Optional[Union[str, core.StringOut]] = None,
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
        outbound_caller_id_name: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outbound_caller_id_number_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        outbound_flow_id: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.resource(type="aws_connect_queue", namespace="aws_connect")
class Queue(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    description: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    hours_of_operation_id: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    instance_id: Union[str, core.StringOut] = core.attr(str)

    max_contacts: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    name: Union[str, core.StringOut] = core.attr(str)

    outbound_caller_config: Optional[OutboundCallerConfig] = core.attr(
        OutboundCallerConfig, default=None
    )

    queue_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    quick_connect_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.array
    )

    quick_connect_ids_associated: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    status: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

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
        hours_of_operation_id: Union[str, core.StringOut],
        instance_id: Union[str, core.StringOut],
        name: Union[str, core.StringOut],
        description: Optional[Union[str, core.StringOut]] = None,
        max_contacts: Optional[Union[int, core.IntOut]] = None,
        outbound_caller_config: Optional[OutboundCallerConfig] = None,
        quick_connect_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        status: Optional[Union[str, core.StringOut]] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=Queue.Args(
                hours_of_operation_id=hours_of_operation_id,
                instance_id=instance_id,
                name=name,
                description=description,
                max_contacts=max_contacts,
                outbound_caller_config=outbound_caller_config,
                quick_connect_ids=quick_connect_ids,
                status=status,
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

        hours_of_operation_id: Union[str, core.StringOut] = core.arg()

        instance_id: Union[str, core.StringOut] = core.arg()

        max_contacts: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        name: Union[str, core.StringOut] = core.arg()

        outbound_caller_config: Optional[OutboundCallerConfig] = core.arg(default=None)

        quick_connect_ids: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = core.arg(
            default=None
        )

        status: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
