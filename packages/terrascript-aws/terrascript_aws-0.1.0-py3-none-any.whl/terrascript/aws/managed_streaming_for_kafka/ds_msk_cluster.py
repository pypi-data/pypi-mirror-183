from typing import Dict, Optional, Union

import terrascript.core as core


@core.data(type="aws_msk_cluster", namespace="aws_managed_streaming_for_kafka")
class DsMskCluster(core.Data):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_iam: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_scram: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_sasl_iam: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_sasl_scram: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kafka_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    number_of_broker_nodes: Union[int, core.IntOut] = core.attr(int, computed=True)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zookeeper_connect_string: Union[str, core.StringOut] = core.attr(str, computed=True)

    zookeeper_connect_string_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        data_name: str,
        *,
        cluster_name: Union[str, core.StringOut],
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
    ):
        super().__init__(
            name=data_name,
            args=DsMskCluster.Args(
                cluster_name=cluster_name,
                tags=tags,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cluster_name: Union[str, core.StringOut] = core.arg()

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)
