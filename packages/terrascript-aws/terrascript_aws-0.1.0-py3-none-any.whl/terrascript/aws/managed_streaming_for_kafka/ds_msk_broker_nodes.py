from typing import List, Union

import terrascript.core as core


@core.schema
class NodeInfoList(core.Schema):

    attached_eni_id: Union[str, core.StringOut] = core.attr(str, computed=True)

    broker_id: Union[float, core.FloatOut] = core.attr(float, computed=True)

    client_subnet: Union[str, core.StringOut] = core.attr(str, computed=True)

    client_vpc_ip_address: Union[str, core.StringOut] = core.attr(str, computed=True)

    endpoints: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, computed=True, kind=core.Kind.array
    )

    node_arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        *,
        attached_eni_id: Union[str, core.StringOut],
        broker_id: Union[float, core.FloatOut],
        client_subnet: Union[str, core.StringOut],
        client_vpc_ip_address: Union[str, core.StringOut],
        endpoints: Union[List[str], core.ArrayOut[core.StringOut]],
        node_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            args=NodeInfoList.Args(
                attached_eni_id=attached_eni_id,
                broker_id=broker_id,
                client_subnet=client_subnet,
                client_vpc_ip_address=client_vpc_ip_address,
                endpoints=endpoints,
                node_arn=node_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        attached_eni_id: Union[str, core.StringOut] = core.arg()

        broker_id: Union[float, core.FloatOut] = core.arg()

        client_subnet: Union[str, core.StringOut] = core.arg()

        client_vpc_ip_address: Union[str, core.StringOut] = core.arg()

        endpoints: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        node_arn: Union[str, core.StringOut] = core.arg()


@core.data(type="aws_msk_broker_nodes", namespace="aws_managed_streaming_for_kafka")
class DsMskBrokerNodes(core.Data):

    cluster_arn: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    node_info_list: Union[List[NodeInfoList], core.ArrayOut[NodeInfoList]] = core.attr(
        NodeInfoList, computed=True, kind=core.Kind.array
    )

    def __init__(
        self,
        data_name: str,
        *,
        cluster_arn: Union[str, core.StringOut],
    ):
        super().__init__(
            name=data_name,
            args=DsMskBrokerNodes.Args(
                cluster_arn=cluster_arn,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_arn: Union[str, core.StringOut] = core.arg()
