from typing import Dict, List, Optional, Union

import terrascript.core as core


@core.schema
class NodeExporter(core.Schema):

    enabled_in_broker: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled_in_broker: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=NodeExporter.Args(
                enabled_in_broker=enabled_in_broker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled_in_broker: Union[bool, core.BoolOut] = core.arg()


@core.schema
class JmxExporter(core.Schema):

    enabled_in_broker: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled_in_broker: Union[bool, core.BoolOut],
    ):
        super().__init__(
            args=JmxExporter.Args(
                enabled_in_broker=enabled_in_broker,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled_in_broker: Union[bool, core.BoolOut] = core.arg()


@core.schema
class Prometheus(core.Schema):

    jmx_exporter: Optional[JmxExporter] = core.attr(JmxExporter, default=None)

    node_exporter: Optional[NodeExporter] = core.attr(NodeExporter, default=None)

    def __init__(
        self,
        *,
        jmx_exporter: Optional[JmxExporter] = None,
        node_exporter: Optional[NodeExporter] = None,
    ):
        super().__init__(
            args=Prometheus.Args(
                jmx_exporter=jmx_exporter,
                node_exporter=node_exporter,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        jmx_exporter: Optional[JmxExporter] = core.arg(default=None)

        node_exporter: Optional[NodeExporter] = core.arg(default=None)


@core.schema
class OpenMonitoring(core.Schema):

    prometheus: Prometheus = core.attr(Prometheus)

    def __init__(
        self,
        *,
        prometheus: Prometheus,
    ):
        super().__init__(
            args=OpenMonitoring.Args(
                prometheus=prometheus,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        prometheus: Prometheus = core.arg()


@core.schema
class ConfigurationInfo(core.Schema):

    arn: Union[str, core.StringOut] = core.attr(str)

    revision: Union[int, core.IntOut] = core.attr(int)

    def __init__(
        self,
        *,
        arn: Union[str, core.StringOut],
        revision: Union[int, core.IntOut],
    ):
        super().__init__(
            args=ConfigurationInfo.Args(
                arn=arn,
                revision=revision,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        arn: Union[str, core.StringOut] = core.arg()

        revision: Union[int, core.IntOut] = core.arg()


@core.schema
class CloudwatchLogs(core.Schema):

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    log_group: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        log_group: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=CloudwatchLogs.Args(
                enabled=enabled,
                log_group=log_group,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Union[bool, core.BoolOut] = core.arg()

        log_group: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class Firehose(core.Schema):

    delivery_stream: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        delivery_stream: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=Firehose.Args(
                enabled=enabled,
                delivery_stream=delivery_stream,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        delivery_stream: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()


@core.schema
class S3(core.Schema):

    bucket: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    enabled: Union[bool, core.BoolOut] = core.attr(bool)

    prefix: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    def __init__(
        self,
        *,
        enabled: Union[bool, core.BoolOut],
        bucket: Optional[Union[str, core.StringOut]] = None,
        prefix: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=S3.Args(
                enabled=enabled,
                bucket=bucket,
                prefix=prefix,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        bucket: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        enabled: Union[bool, core.BoolOut] = core.arg()

        prefix: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class BrokerLogs(core.Schema):

    cloudwatch_logs: Optional[CloudwatchLogs] = core.attr(CloudwatchLogs, default=None)

    firehose: Optional[Firehose] = core.attr(Firehose, default=None)

    s3: Optional[S3] = core.attr(S3, default=None)

    def __init__(
        self,
        *,
        cloudwatch_logs: Optional[CloudwatchLogs] = None,
        firehose: Optional[Firehose] = None,
        s3: Optional[S3] = None,
    ):
        super().__init__(
            args=BrokerLogs.Args(
                cloudwatch_logs=cloudwatch_logs,
                firehose=firehose,
                s3=s3,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        cloudwatch_logs: Optional[CloudwatchLogs] = core.arg(default=None)

        firehose: Optional[Firehose] = core.arg(default=None)

        s3: Optional[S3] = core.arg(default=None)


@core.schema
class LoggingInfo(core.Schema):

    broker_logs: BrokerLogs = core.attr(BrokerLogs)

    def __init__(
        self,
        *,
        broker_logs: BrokerLogs,
    ):
        super().__init__(
            args=LoggingInfo.Args(
                broker_logs=broker_logs,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        broker_logs: BrokerLogs = core.arg()


@core.schema
class Sasl(core.Schema):

    iam: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    scram: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        iam: Optional[Union[bool, core.BoolOut]] = None,
        scram: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=Sasl.Args(
                iam=iam,
                scram=scram,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        iam: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        scram: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class Tls(core.Schema):

    certificate_authority_arns: Optional[
        Union[List[str], core.ArrayOut[core.StringOut]]
    ] = core.attr(str, default=None, kind=core.Kind.array)

    def __init__(
        self,
        *,
        certificate_authority_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = None,
    ):
        super().__init__(
            args=Tls.Args(
                certificate_authority_arns=certificate_authority_arns,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        certificate_authority_arns: Optional[
            Union[List[str], core.ArrayOut[core.StringOut]]
        ] = core.arg(default=None)


@core.schema
class ClientAuthentication(core.Schema):

    sasl: Optional[Sasl] = core.attr(Sasl, default=None)

    tls: Optional[Tls] = core.attr(Tls, default=None)

    unauthenticated: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        sasl: Optional[Sasl] = None,
        tls: Optional[Tls] = None,
        unauthenticated: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=ClientAuthentication.Args(
                sasl=sasl,
                tls=tls,
                unauthenticated=unauthenticated,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        sasl: Optional[Sasl] = core.arg(default=None)

        tls: Optional[Tls] = core.arg(default=None)

        unauthenticated: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class ProvisionedThroughput(core.Schema):

    enabled: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    volume_throughput: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        enabled: Optional[Union[bool, core.BoolOut]] = None,
        volume_throughput: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=ProvisionedThroughput.Args(
                enabled=enabled,
                volume_throughput=volume_throughput,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        enabled: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)

        volume_throughput: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class EbsStorageInfo(core.Schema):

    provisioned_throughput: Optional[ProvisionedThroughput] = core.attr(
        ProvisionedThroughput, default=None
    )

    volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None)

    def __init__(
        self,
        *,
        provisioned_throughput: Optional[ProvisionedThroughput] = None,
        volume_size: Optional[Union[int, core.IntOut]] = None,
    ):
        super().__init__(
            args=EbsStorageInfo.Args(
                provisioned_throughput=provisioned_throughput,
                volume_size=volume_size,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        provisioned_throughput: Optional[ProvisionedThroughput] = core.arg(default=None)

        volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)


@core.schema
class StorageInfo(core.Schema):

    ebs_storage_info: Optional[EbsStorageInfo] = core.attr(EbsStorageInfo, default=None)

    def __init__(
        self,
        *,
        ebs_storage_info: Optional[EbsStorageInfo] = None,
    ):
        super().__init__(
            args=StorageInfo.Args(
                ebs_storage_info=ebs_storage_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        ebs_storage_info: Optional[EbsStorageInfo] = core.arg(default=None)


@core.schema
class PublicAccess(core.Schema):

    type: Optional[Union[str, core.StringOut]] = core.attr(str, default=None, computed=True)

    def __init__(
        self,
        *,
        type: Optional[Union[str, core.StringOut]] = None,
    ):
        super().__init__(
            args=PublicAccess.Args(
                type=type,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        type: Optional[Union[str, core.StringOut]] = core.arg(default=None)


@core.schema
class ConnectivityInfo(core.Schema):

    public_access: Optional[PublicAccess] = core.attr(PublicAccess, default=None, computed=True)

    def __init__(
        self,
        *,
        public_access: Optional[PublicAccess] = None,
    ):
        super().__init__(
            args=ConnectivityInfo.Args(
                public_access=public_access,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        public_access: Optional[PublicAccess] = core.arg(default=None)


@core.schema
class BrokerNodeGroupInfo(core.Schema):

    az_distribution: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    client_subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    connectivity_info: Optional[ConnectivityInfo] = core.attr(
        ConnectivityInfo, default=None, computed=True
    )

    ebs_volume_size: Optional[Union[int, core.IntOut]] = core.attr(int, default=None, computed=True)

    instance_type: Union[str, core.StringOut] = core.attr(str)

    security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.attr(
        str, kind=core.Kind.array
    )

    storage_info: Optional[StorageInfo] = core.attr(StorageInfo, default=None, computed=True)

    def __init__(
        self,
        *,
        client_subnets: Union[List[str], core.ArrayOut[core.StringOut]],
        instance_type: Union[str, core.StringOut],
        security_groups: Union[List[str], core.ArrayOut[core.StringOut]],
        az_distribution: Optional[Union[str, core.StringOut]] = None,
        connectivity_info: Optional[ConnectivityInfo] = None,
        ebs_volume_size: Optional[Union[int, core.IntOut]] = None,
        storage_info: Optional[StorageInfo] = None,
    ):
        super().__init__(
            args=BrokerNodeGroupInfo.Args(
                client_subnets=client_subnets,
                instance_type=instance_type,
                security_groups=security_groups,
                az_distribution=az_distribution,
                connectivity_info=connectivity_info,
                ebs_volume_size=ebs_volume_size,
                storage_info=storage_info,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        az_distribution: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        client_subnets: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        connectivity_info: Optional[ConnectivityInfo] = core.arg(default=None)

        ebs_volume_size: Optional[Union[int, core.IntOut]] = core.arg(default=None)

        instance_type: Union[str, core.StringOut] = core.arg()

        security_groups: Union[List[str], core.ArrayOut[core.StringOut]] = core.arg()

        storage_info: Optional[StorageInfo] = core.arg(default=None)


@core.schema
class EncryptionInTransit(core.Schema):

    client_broker: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    in_cluster: Optional[Union[bool, core.BoolOut]] = core.attr(bool, default=None)

    def __init__(
        self,
        *,
        client_broker: Optional[Union[str, core.StringOut]] = None,
        in_cluster: Optional[Union[bool, core.BoolOut]] = None,
    ):
        super().__init__(
            args=EncryptionInTransit.Args(
                client_broker=client_broker,
                in_cluster=in_cluster,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        client_broker: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        in_cluster: Optional[Union[bool, core.BoolOut]] = core.arg(default=None)


@core.schema
class EncryptionInfo(core.Schema):

    encryption_at_rest_kms_key_arn: Optional[Union[str, core.StringOut]] = core.attr(
        str, default=None, computed=True
    )

    encryption_in_transit: Optional[EncryptionInTransit] = core.attr(
        EncryptionInTransit, default=None
    )

    def __init__(
        self,
        *,
        encryption_at_rest_kms_key_arn: Optional[Union[str, core.StringOut]] = None,
        encryption_in_transit: Optional[EncryptionInTransit] = None,
    ):
        super().__init__(
            args=EncryptionInfo.Args(
                encryption_at_rest_kms_key_arn=encryption_at_rest_kms_key_arn,
                encryption_in_transit=encryption_in_transit,
            ),
        )

    @core.schema_args
    class Args(core.SchemaArgs):
        encryption_at_rest_kms_key_arn: Optional[Union[str, core.StringOut]] = core.arg(
            default=None
        )

        encryption_in_transit: Optional[EncryptionInTransit] = core.arg(default=None)


@core.resource(type="aws_msk_cluster", namespace="aws_managed_streaming_for_kafka")
class MskCluster(core.Resource):

    arn: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_iam: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_sasl_scram: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_public_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_sasl_iam: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_sasl_scram: Union[str, core.StringOut] = core.attr(str, computed=True)

    bootstrap_brokers_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    broker_node_group_info: BrokerNodeGroupInfo = core.attr(BrokerNodeGroupInfo)

    client_authentication: Optional[ClientAuthentication] = core.attr(
        ClientAuthentication, default=None
    )

    cluster_name: Union[str, core.StringOut] = core.attr(str)

    configuration_info: Optional[ConfigurationInfo] = core.attr(ConfigurationInfo, default=None)

    current_version: Union[str, core.StringOut] = core.attr(str, computed=True)

    encryption_info: Optional[EncryptionInfo] = core.attr(EncryptionInfo, default=None)

    enhanced_monitoring: Optional[Union[str, core.StringOut]] = core.attr(str, default=None)

    id: Union[str, core.StringOut] = core.attr(str, computed=True)

    kafka_version: Union[str, core.StringOut] = core.attr(str)

    logging_info: Optional[LoggingInfo] = core.attr(LoggingInfo, default=None)

    number_of_broker_nodes: Union[int, core.IntOut] = core.attr(int)

    open_monitoring: Optional[OpenMonitoring] = core.attr(OpenMonitoring, default=None)

    tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, kind=core.Kind.map
    )

    tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.attr(
        str, default=None, computed=True, kind=core.Kind.map
    )

    zookeeper_connect_string: Union[str, core.StringOut] = core.attr(str, computed=True)

    zookeeper_connect_string_tls: Union[str, core.StringOut] = core.attr(str, computed=True)

    def __init__(
        self,
        resource_name: str,
        *,
        broker_node_group_info: BrokerNodeGroupInfo,
        cluster_name: Union[str, core.StringOut],
        kafka_version: Union[str, core.StringOut],
        number_of_broker_nodes: Union[int, core.IntOut],
        client_authentication: Optional[ClientAuthentication] = None,
        configuration_info: Optional[ConfigurationInfo] = None,
        encryption_info: Optional[EncryptionInfo] = None,
        enhanced_monitoring: Optional[Union[str, core.StringOut]] = None,
        logging_info: Optional[LoggingInfo] = None,
        open_monitoring: Optional[OpenMonitoring] = None,
        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = None,
        depends_on: Optional[Union[List[str], core.ArrayOut[core.StringOut]]] = None,
        provider: Optional[Union[str, core.StringOut]] = None,
        lifecycle: Optional[core.Lifecycle] = None,
    ):
        super().__init__(
            name=resource_name,
            args=MskCluster.Args(
                broker_node_group_info=broker_node_group_info,
                cluster_name=cluster_name,
                kafka_version=kafka_version,
                number_of_broker_nodes=number_of_broker_nodes,
                client_authentication=client_authentication,
                configuration_info=configuration_info,
                encryption_info=encryption_info,
                enhanced_monitoring=enhanced_monitoring,
                logging_info=logging_info,
                open_monitoring=open_monitoring,
                tags=tags,
                tags_all=tags_all,
                depends_on=depends_on,
                provider=provider,
                lifecycle=lifecycle,
            ),
        )

    @core.schema_args
    class Args(core.Resource.Args):
        broker_node_group_info: BrokerNodeGroupInfo = core.arg()

        client_authentication: Optional[ClientAuthentication] = core.arg(default=None)

        cluster_name: Union[str, core.StringOut] = core.arg()

        configuration_info: Optional[ConfigurationInfo] = core.arg(default=None)

        encryption_info: Optional[EncryptionInfo] = core.arg(default=None)

        enhanced_monitoring: Optional[Union[str, core.StringOut]] = core.arg(default=None)

        kafka_version: Union[str, core.StringOut] = core.arg()

        logging_info: Optional[LoggingInfo] = core.arg(default=None)

        number_of_broker_nodes: Union[int, core.IntOut] = core.arg()

        open_monitoring: Optional[OpenMonitoring] = core.arg(default=None)

        tags: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(default=None)

        tags_all: Optional[Union[Dict[str, str], core.MapOut[core.StringOut]]] = core.arg(
            default=None
        )
